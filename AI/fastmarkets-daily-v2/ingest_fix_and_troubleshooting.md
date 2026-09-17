# Fastmarkets V2 系統修復與 Ingest 執行問題診斷報告

**產出時間**：2026-09-04  
**專案路徑**：`C:/aiTest/fastmarkets-daily-v2`

---

## 壹、程式碼修改內容彙整

本次處理針對程式崩潰與測試錯誤進行了核心修復，共修改 **4 個檔案**，所有單元測試（25 項）已全數通過。

### 1. [`pipeline.py`](file:///C:/aiTest/fastmarkets-daily-v2/src/fastmarkets_v2/pipeline.py)
* **原始錯誤**：
  ```python
  AttributeError: 'ChunkedIteratorResult' object has no attribute 'scalar_subquery'
  ```
* **問題原因**：
  在計算價格週變動率（WoW）取得前一週價格時，原程式將 `session.execute(...)` 包裹在子查詢外層，使得呼叫 `scalar_subquery()` 的對象變成 SQLAlchemy 的查詢結果物件，引發例外。
* **修改前後對比**：
  ```python
  # === 修改前 ===
  prev_prices: dict[str, float] = {}
  for row in session.execute(
      select(PriceWeekly.code, PriceWeekly.price_mt).where(
          PriceWeekly.week_date == session.execute(
              select(PriceWeekly.week_date)
              .where(PriceWeekly.week_date < week_date)
              .order_by(PriceWeekly.week_date.desc())
              .limit(1)
          ).scalar_subquery()
      )
  ).all():
      prev_prices[row[0]] = row[1]

  # === 修改後 ===
  prev_prices: dict[str, float] = {}
  prev_week_subq = (
      select(PriceWeekly.week_date)
      .where(PriceWeekly.week_date < week_date)
      .order_by(PriceWeekly.week_date.desc())
      .limit(1)
      .scalar_subquery()
  )
  for row in session.execute(
      select(PriceWeekly.code, PriceWeekly.price_mt).where(
          PriceWeekly.week_date == prev_week_subq
      )
  ).all():
      prev_prices[row[0]] = row[1]
  ```

---

### 2. [`app.py`](file:///C:/aiTest/fastmarkets-daily-v2/src/fastmarkets_v2/app.py)
* **原始錯誤**：
  ```python
  TypeError: unhashable type: 'dict'
  ```
* **問題原因**：
  新版 Starlette / FastAPI 規範中，`TemplateResponse` 的第一個參數已改為 `request: Request`。原寫法第一個位置傳遞檔名字串、第二個位置傳遞字典，導致底層 Jinja2 快取機制將 context 字典誤當成快取 Key。
* **修改方式**：改用標準關鍵字引數傳遞：
  ```python
  return templates.TemplateResponse(
      request=request,
      name="dashboard.html",
      context={
          "request": request,
          "latest_date": latest_date,
          # ...其餘參數...
      }
  )
  ```

---

### 3. [`routers/prices.py`](file:///C:/aiTest/fastmarkets-daily-v2/src/fastmarkets_v2/routers/prices.py)
* **修改說明**：
  將 `/prices` 與 `/prices/{code}` 兩處視圖中的 `TemplateResponse` 呼叫統一調整為現代簽名：
  - `request=request`
  - `name="prices.html"` / `name="price_detail.html"`
  - `context={ ... }`

---

### 4. [`routers/summaries.py`](file:///C:/aiTest/fastmarkets-daily-v2/src/fastmarkets_v2/routers/summaries.py)
* **修改說明**：
  將 `/summaries` 與 `/summaries/{summary_id}` 兩處視圖中的 `TemplateResponse` 呼叫統一調整為：
  - `request=request`
  - `name="summaries.html"` / `name="summary_detail.html"`
  - `context={ ... }`

---

## 貳、執行 `uv run fastmarkets-v2 ingest` 出現的問題

在執行指令後，終端機回報：
```text
完成: 1 檔, 新聞 0 篇, 價格 0 筆, 失敗 5 篇
```

### 問題根因分析

1. **PDF 解析正常**：
   - 待匯入檔案為 `raw/modal2/CHS_C5...1150527.pdf`。
   - 程式成功解析並切分出 **5 篇** 待摘要的新聞文本（該 PDF 無價格表格）。
2. **Ava GPT 遠端伺服器報錯**：
   - 本地 [`ava_client.py`](file:///C:/aiTest/fastmarkets-daily-v2/src/fastmarkets_v2/ava_client.py) 向 Ava 伺服器端點發出摘要請求：
     - **專家 ID**：`28999566-b676-4449-aa41-0077857ace8a`
   - Ava 伺服器回傳狀態碼 500，錯誤內文為：
     ```json
     {
       "error": "Upstream service error: No API key was provided. Please pass a valid API key. Learn how to create an API key at https://ai.google.dev/gemini-api/docs/api-key."
     }
     ```
3. **結論**：
   - **本地端**：[`.env`](file:///C:/aiTest/fastmarkets-daily-v2/.env) 的 `AVA_API_KEY` 認證完全正常，Web Gateway 有正確放行。
   - **遠端伺服器**：Ava 平台內部該專家所串接的上游 **Google Gemini 模型未配置有效的 API Key**，導致後端模型推論失敗。本地程式依容錯機制寫入資料庫（`parse_failed = True`），因此呈現「失敗 5 篇」。

---

## 參、目前應如何解決

針對上述 Ava 後端金鑰問題，建議依照您的權限選擇以下方案：

### 方案 A：修正 Ava 平台後端設定（推薦根治）
* **操作**：登入 Ava GPT 系統後台管理介面。
* **項目**：檢查專家 `28999566-b676-4449-aa41-0077857ace8a` 所綁定的模型渠道（Gemini 服務），重新填入一組有效的 Google Gemini API Key。

### 方案 B：切換為其他正常的 Ava 專家 ID
* 若 Ava 平台內有其他可正常回答的專家 ID（例如未綁定失效 Gemini Key 的其他角色）：
  1. 開啟 [`.env`](file:///C:/aiTest/fastmarkets-daily-v2/.env)。
  2. 將 `AVA_EXPERT_ID` 修改為新的專家 UUID：
     ```ini
     AVA_EXPERT_ID=新的_EXPERT_ID
     ```

### 方案 C：修復後重新匯入已失敗的新聞
當 Ava 平台恢復正常後，因為該 5 筆紀錄在資料庫已被標記為 `parse_failed = True`，為重新執行摘要可執行以下步驟：

1. **清理資料庫中失敗的紀錄**：
   ```bash
   uv run python -c "from fastmarkets_v2.database import SessionLocal; from fastmarkets_v2.models import Summary; s=SessionLocal(); s.query(Summary).filter(Summary.parse_failed==True).delete(); s.commit(); print('已清理失敗紀錄')"
   ```
2. **重新執行匯入**：
   ```bash
   uv run fastmarkets-v2 ingest
   ```
