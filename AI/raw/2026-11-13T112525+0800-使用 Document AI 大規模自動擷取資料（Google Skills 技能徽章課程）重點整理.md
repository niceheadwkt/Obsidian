# 使用 Document AI 大規模自動擷取資料：重點整理

> 來源：Google Skills 課程頁（course_templates/674）
> 課程連結：https://www.skills.google/course_templates/674?locale=zh_TW
> 英文原名：Automate Data Capture at Scale with Document AI
> 類型：Course（技能徽章課程）　難度：Introductory（入門）　頁面標示時長：30 分鐘
> 整理依據：2026-11-13 以已登入的瀏覽器讀取課程頁與各實驗室說明頁（未實際啟動實驗室）
> 說明：第二個實驗室「透過 Document AI API 使用 Python 處理文件」的頁面顯示「目前無法使用」（中英文版都一樣），只能取得課程卡片上的簡介。標示「（補充）」的段落是整理者加的說明，不是課程原文。

**目錄**
- [課程概要](#課程概要)
- [課程大綱](#課程大綱)
- [實驗室一：建立及測試 Document AI 處理器（GSP924）](#實驗室一建立及測試-document-ai-處理器gsp924)
- [實驗室二：透過 Document AI API 使用 Python 處理文件](#實驗室二透過-document-ai-api-使用-python-處理文件)
- [實驗室三：使用 Document AI 建構完整資料擷取管道（GSP927）](#實驗室三使用-document-ai-建構完整資料擷取管道gsp927)
- [挑戰實驗室：使用 Document AI 大規模自動擷取資料（GSP367）](#挑戰實驗室使用-document-ai-大規模自動擷取資料gsp367)
- [重點觀念整理](#重點觀念整理)
- [應用聯想（補充）](#應用聯想補充)

---

## 課程概要

- 完成課程即可取得入門級**技能徽章（Skill badge）**。課程教你用 Document AI 擷取、處理和提取文件中的資料。
- 技能徽章透過實作實驗室和挑戰評量，驗證你對特定產品的實務能力。
- **可以直接挑戰**：有把握的話，不用修完整門課，直接做挑戰實驗室就能拿徽章（頁面上的「Start challenge」）。進度會保留，但完成百分比可能改變。
- 所有實驗室都在真正的 Google Cloud 環境操作，會發給臨時的學員帳號。
  - 實驗室計時，開始後不能暫停，中途結束要從頭來。
  - 建議用無痕視窗開啟，避免和個人 Google 帳號衝突、產生額外費用。
  - 同一時間只能進行一個實驗室。

## 課程大綱

| 順序 | 活動 | 代號 | 必修 | 內容摘要 |
|---|---|---|---|---|
| 1 | 建立及測試 Document AI 處理器 | GSP924 | | 用 Document AI API 建立和使用文件處理器 |
| 2 | 透過 Document AI API 使用 Python 處理文件 | （頁面無法使用） | | 用 Python 建立一般表單處理器、文件 OCR 處理器，並發出同步和非同步呼叫 |
| 3 | 使用 Document AI 建構完整資料擷取管道 | GSP927 | | 搭配 Cloud Functions（Cloud Run 函式）和 Pub/Sub 建立完整的文件處理管道 |
| 4 | 使用 Document AI 大規模自動擷取資料：挑戰實驗室 | GSP367 | **Required** | 沒有逐步說明，限時自行完成整條管道 |
| — | 技能徽章 | | | 完成所有必修活動後頒發 |

依課程設計，**只有挑戰實驗室是必修**，前三個是練習用的實驗室。

---

## 實驗室一：建立及測試 Document AI 處理器（GSP924）

**學習目標**
- 用 Google Cloud 控制台建立和測試 Document AI 處理器。
- 用指令列（curl）測試處理器。
- 用 Python 發出 Document AI 同步 API 呼叫。

**使用的處理器**：一般表單處理器（Form Parser）
- 可以處理任何類型的文件，擷取所有可辨識的文字。
- 支援多種語言，能處理印刷、手寫、任意方向的文字。
- 能看懂表單元素之間的關係，從有文字標籤的欄位擷取**鍵/值組合**（例如 Date → 2026/11/13）。

**操作步驟**
1. **啟用 API**：導覽選單 >「API 和服務」>「程式庫」，搜尋「Cloud Document AI API」後啟用。
2. **建立處理器**：Document AI >「總覽」>「探索處理器」> 選 Form Parser，名稱 `form-parser`，區域選 US。建立後記下**處理器 ID**。
3. **在控制台測試**：下載範例表單 `form.pdf`（手寫的健康資料登記表），按「上傳測試文件」。
   - 左側列出擷取到的鍵/值資料。
   - 右側用藍框標出每筆資料在原文件的位置，方便比對。
4. **設定 VM 環境**：SSH 連到 VM `document-ai-dev`。
   - 用環境變數存放處理器 ID 和專案 ID。
   - 建立服務帳戶，授予「Document AI API 使用者」角色，產生 `key.json`。
   - 把 `GOOGLE_APPLICATION_CREDENTIALS` 指向這個憑證檔。
5. **用 curl 同步處理**：把表單轉成 Base64，包成 JSON 要求送到同步端點，結果存成 `output.json`。
   - 可以用 `jq` 取出原始文字（`document.text`）和表單欄位。
   - 表單欄位用 `textAnchor.startIndex`／`endIndex` 對回 `document.text` 裡的文字。
6. **用 Python 用戶端程式庫**：執行 `synchronous_doc_ai.py`。
   - 程式先用 `project_id`、`location`、`processor_id` 組出處理器名稱，再把文件和 `mime_type` 一起送出同步呼叫。
   - 輸出分兩段：第一段是整份原始文字，Date、Name 這些欄位會混在一起；第二段是依表單結構整理過的「欄位名稱 → 值」，還附上**可信度分數**。

**重點**：同步端點一次處理一份文件；要一次處理大量文件，改用**非同步 API**。

---

## 實驗室二：透過 Document AI API 使用 Python 處理文件

> 這個實驗室頁面目前顯示「Sorry, … is currently unavailable」，以下只有課程卡片上的簡介。

- 用 Document AI API 搭配 Python 建立各種處理器，包括**一般表單處理器**和**文件 OCR 處理器**。
- 用 Python 對 API 發出**同步**和**非同步**呼叫。

---

## 實驗室三：使用 Document AI 建構完整資料擷取管道（GSP927）

**情境**：文件上傳到 Cloud Storage 後自動分析。抓出來的表單資料寫進 BigQuery；有地址的話，再用 Geocoding API 補上經緯度。

**管道架構（九步）**
1. 把含地址的表單上傳到 Cloud Storage。
2. 上傳事件觸發 Cloud Run 函式 `process-invoices`。
3. 函式呼叫 Document AI 處理表單。
4. Document AI 產生的 JSON 存回 Cloud Storage。
5. 函式把表單資料寫進 BigQuery。
6. 函式把地址送到 Pub/Sub 主題。
7. Pub/Sub 訊息觸發第二個函式 `geocode-addresses`。
8. 這個函式呼叫 Geocoding API。
9. 地理編碼結果寫進 BigQuery。

**操作步驟**
1. **啟用 API 並建立 API 金鑰**：啟用 Document AI、Cloud Run functions、Cloud Build、Geocoding API。建立 API 金鑰，並限制只能用在 Geocoding API。
2. **下載實驗室原始碼**到 Cloud Shell，內容包括函式程式碼和 BigQuery 資料表結構定義。
3. **建立表單處理器**：用 Form Parser 建立，名稱 `form-processor`，區域 US。記下 ID 和區域。
4. **建立資源**
   - 建立三個 Cloud Storage bucket：輸入、輸出、封存。
   - 建立 BigQuery 資料集 `invoice_parser_results` 和三個資料表，例如 `doc_ai_extracted_entities`、`geocode_details`。
   - 建立 Pub/Sub 主題。
5. **部署兩個 Cloud Run 函式**：先授權 Cloud Storage 服務代理。
6. **設定環境變數**
   - `process-invoices`：`GCP_PROJECT`、`PROCESSOR_ID`、`PARSER_LOCATION`（必須小寫的 `us` 或 `eu`）。
   - `geocode-addresses`：`API_key`。
   - 執行階段變數和 `.env.yaml` 兩邊都要設定。
7. **測試**：上傳範例表單，到函式的「記錄」看到最後以 `LoadJob` 結束，就代表跑完了。再到 BigQuery 預覽兩個資料表。

**`process-invoices` 的內部函式**
- `write_to_bq`：把字典寫進 BigQuery。呼叫前要先確認結構定義正確。
- `get_text`：用文字錨點把欄位名稱和值對回掃描出的文字，認出供應商、地址這類欄位。
- `process_invoice`：用**非同步** Document AI API 處理，流程如下。
  1. 建立非同步處理要求。
  2. 取出預先定義的欄位。
  3. 發布 Pub/Sub 訊息。
  4. 寫進 BigQuery。
  5. 刪除中繼輸出檔。
  6. 把原檔複製到封存 bucket。
  7. 刪除已處理的輸入檔。

**只會擷取的欄位**：`input_file_name`、`address`、`supplier`、`invoice_number`、`purchase_order`、`date`、`due_date`、`subtotal`、`tax`、`total`

**課程提醒**
- 這個範例用 Cloud Run 函式做簡易管道，**不建議用在正式環境**，因為 Document AI 呼叫可能超過函式的逾時上限。比較完整的無伺服器做法建議改用 **Cloud Tasks**。
- 一般表單處理器只抓得到「有標籤」的欄位。比較複雜的文件，可以改用 Document AI 的**專用剖析器**，例如應付憑據（發票）剖析器，沒有標籤也能認出地址和供應商。

---

## 挑戰實驗室：使用 Document AI 大規模自動擷取資料（GSP367）

**情境**：你是大型基礎架構管理公司的資料工程師，和財務部門合作。公司要處理的文件越來越多，每份都要人工驗證和授權，成本很高，所以要用 Google Cloud 把文件的收集、分類和驗證自動化。

**規則**
- 沒有逐步說明，要自己運用前面實驗室學到的技巧。
- 自動評分系統會檢查每項任務有沒有正確完成。
- 必須在時限內完成全部任務才能滿分。

**任務**

| 工作 | 內容 | 要點 |
|---|---|---|
| 1 | 啟用 Cloud Document AI API，複製實驗室原始碼 | 原始碼放在遠端 Cloud Storage bucket |
| 2 | 建立表單處理器 | 選「一般」區的 Form Parser，區域選美國。處理器名稱由實驗室指定。記下 PROCESSOR ID；處理器區域就是 PARSER LOCATION |
| 3 | 建立 Cloud Storage 和 BigQuery 資源 | 三個 bucket：輸入帳單、處理後資料、封存帳單。都用標準儲存空間級別，並啟用統一 bucket 層級存取權。BigQuery 建資料集 `invoice_parser_results`（美國），再用 `doc_ai_extracted_entities.json` 結構定義建資料表 `doc_ai_extracted_entities` |
| 4 | 部署 Cloud Run 函式 `process-invoices` | 觸發條件設為「檔案上傳到輸入 bucket」。先把「Artifact Registry 讀取者」角色指派給 Compute Engine 服務帳戶。環境變數 `PROCESSOR_ID`、`PARSER_LOCATION`（小寫）、`PROJECT_ID` 要改成正確的值 |
| 5 | 端對端測試 | 把 `~/document-ai-challenge/invoices` 裡的帳單上傳到輸入 bucket，看記錄直到最後顯示「OK」，再確認資料有寫進 BigQuery |

**課程提到的指令**
- 建 bucket：`gcloud storage buckets create`，搭配 `--default-storage-class`、`--location`、`--uniform-bucket-level-access`。
- 建資料集：`bq mk -d --location=...`。
- 建資料表：`bq mk --table`，並指定結構定義檔。

**排錯提醒**
- 部署時出現權限錯誤，等兩、三分鐘再重跑。
- 過程中可能出現一些錯誤（特別是逾時），不影響文件處理。
- 如果 BigQuery 沒有資料，到 Cloud Run 控制台的「變數與密鑰」分頁，確認處理器 ID 和位置正確，位置要小寫。
- 活動清單不會自動重新整理，要手動按。

---

## 重點觀念整理

| 觀念 | 說明 |
|---|---|
| 處理器（Processor） | Document AI 的處理單位。建立時選類型和區域，產生處理器 ID，呼叫 API 時用「專案 + 區域 + 處理器 ID」指定 |
| 一般表單處理器（Form Parser） | 擷取全部文字和有標籤欄位的鍵/值組合，每個值附可信度分數 |
| 文件 OCR 處理器 | 純文字辨識（實驗室二） |
| 專用剖析器 | 例如應付憑據剖析器，懂特定文件的版面，沒有標籤也能抓出欄位 |
| 同步 vs. 非同步 | 同步：一次一份，結果直接回傳。非同步：大量文件，結果寫到 Cloud Storage |
| 文字錨點（textAnchor） | 欄位用 `startIndex`／`endIndex` 對回 `document.text`，取出欄位名稱和值 |
| 事件驅動管道 | Cloud Storage 上傳觸發函式 → Document AI → BigQuery；用 Pub/Sub 串接後續加值處理（地理編碼） |
| 三個 bucket 分工 | 輸入（待處理）→ 輸出（Document AI 中繼結果）→ 封存（處理完的原檔），處理完就刪除輸入檔 |
| 常見錯誤 | 位置參數要小寫、IAM 權限要等幾分鐘才生效、環境變數執行階段和 `.env.yaml` 都要設定 |

---

## 應用聯想（補充）

以下是整理者的延伸想法，不是課程內容：
- 這條管道的模式是「上傳 → 擷取欄位 → 寫進資料表 → 觸發後續處理」，和 [[n8n]] 課程裡「RSS → Gemini → LINE」的工作流程是同一種思路：事件觸發、逐站處理、串接 API。
- ERP 情境可以參考的方向：紙本或 PDF 的發票、報支單據、證照影本等，先用 Form Parser 或專用剖析器抽出欄位（發票號碼、日期、金額、供應商），寫進中介表，再交給既有系統比對或匯入。正式導入時，要照課程提醒改用 Cloud Tasks 之類可靠的排程，也要評估資料出境和個資問題。
