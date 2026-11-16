---
type: source-summary
tags: [Document-AI, Google-Cloud, GCP, OCR, Form-Parser, Cloud-Run, Pub-Sub, BigQuery, Cloud-Storage, 文件擷取, 技能徽章, 線上課程]
sources: ["[[AI/raw/2026-11-13T112525+0800-使用 Document AI 大規模自動擷取資料（Google Skills 技能徽章課程）重點整理.md|使用 Document AI 大規模自動擷取資料（Google Skills 技能徽章課程）重點整理]]"]
created: 2026-11-16
updated: 2026-11-16
---

# Document AI 大規模資料擷取：課程總結

本頁整理 Google Skills 的入門級技能徽章課程〈使用 Document AI 大規模自動擷取資料〉（Automate Data Capture at Scale with Document AI，course_templates/674）。課程教你用 Google Cloud **Document AI** 擷取文件中的欄位，再串成「上傳 → 擷取 → 寫入資料表」的自動化管道。可以和 [[GCP 雲端排程與現代化數據工程實戰]] 的 BigQuery 資料工程一起看。

> [!NOTE]
> 整理時只讀了課程頁和各實驗室的說明頁，沒有實際啟動實驗室。實驗室二的頁面顯示「目前無法使用」，只取得課程卡片上的簡介。

---

## 1. 課程結構

| 順序 | 活動 | 代號 | 必修 | 內容 |
|---|---|---|---|---|
| 1 | 建立及測試 Document AI 處理器 | GSP924 | | 在控制台、curl、Python 測試 Form Parser |
| 2 | 透過 Document AI API 使用 Python 處理文件 | （頁面無法使用） | | 一般表單處理器、文件 OCR 處理器，同步與非同步呼叫 |
| 3 | 使用 Document AI 建構完整資料擷取管道 | GSP927 | | Cloud Run 函式＋Pub/Sub＋BigQuery＋Geocoding |
| 4 | 挑戰實驗室 | GSP367 | **必修** | 沒有逐步說明，限時完成整條管道 |

- **只有挑戰實驗室是必修**。有把握的話可以直接挑戰，不用修完前三個練習。
- 實驗室在真正的 Google Cloud 環境操作，會發臨時帳號。計時開始後不能暫停，建議用無痕視窗，同一時間只能做一個實驗室。

---

## 2. 核心觀念

| 觀念 | 說明 |
|---|---|
| 處理器（Processor） | Document AI 的處理單位。建立時選類型和區域，呼叫時用「專案＋區域＋處理器 ID」指定 |
| 一般表單處理器（Form Parser） | 擷取全部文字，以及有標籤欄位的**鍵/值組合**（例如 Date → 2026/11/13）。支援手寫、多語言、任意方向，每個值附**可信度分數** |
| 文件 OCR 處理器 | 純文字辨識 |
| 專用剖析器 | 例如應付憑據（發票）剖析器，懂特定版面，沒有標籤也能抓出供應商、地址 |
| 同步／非同步 | 同步一次處理一份、結果直接回傳；非同步可以大量處理，結果寫到 Cloud Storage |
| 文字錨點（textAnchor） | 欄位用 `startIndex`／`endIndex` 對回 `document.text`，取出欄位名稱和值 |

---

## 3. 實驗室一：建立與測試處理器（GSP924）

1. 啟用 Cloud Document AI API，建立 Form Parser（區域 US），記下處理器 ID。
2. 在控制台上傳範例表單：左側列出鍵/值，右側用藍框標出每個值在原文件的位置。
3. 在 VM 上建立服務帳戶（角色「Document AI API 使用者」），並把 `GOOGLE_APPLICATION_CREDENTIALS` 指向 `key.json`。
4. **curl**：把檔案轉成 Base64 送到同步端點，用 `jq` 取出 `document.text` 和表單欄位。
5. **Python 用戶端程式庫**：輸出分兩段，一段是原始全文，一段是「欄位名稱 → 值＋可信度」。

---

## 4. 實驗室三：完整資料擷取管道（GSP927）

事件驅動的九步管道：

```text
表單上傳 Cloud Storage（輸入 bucket）
  → 觸發 Cloud Run 函式 process-invoices
  → 非同步呼叫 Document AI → JSON 存到輸出 bucket
  → 欄位寫進 BigQuery（doc_ai_extracted_entities）
  → 地址送到 Pub/Sub
  → 觸發函式 geocode-addresses → Geocoding API
  → 經緯度寫進 BigQuery（geocode_details）
處理完：刪除中繼輸出、原檔複製到封存 bucket、刪除輸入檔
```

- **三個 bucket 分工**：輸入（待處理）→ 輸出（Document AI 中繼結果）→ 封存（處理完的原檔）。
- **只擷取固定欄位**：`input_file_name`、`address`、`supplier`、`invoice_number`、`purchase_order`、`date`、`due_date`、`subtotal`、`tax`、`total`。
- `process-invoices` 的環境變數是 `GCP_PROJECT`、`PROCESSOR_ID`、`PARSER_LOCATION`；`PARSER_LOCATION` **必須是小寫**的 `us`／`eu`。執行階段變數和 `.env.yaml` 兩邊都要設定。
- Geocoding 用的 API 金鑰要限制成只能呼叫 Geocoding API。

> [!WARNING]
> 課程提醒：用 Cloud Run 函式做的簡易管道**不建議用在正式環境**，因為 Document AI 呼叫可能超過函式的逾時上限。比較完整的無伺服器做法是改用 **Cloud Tasks**。

---

## 5. 挑戰實驗室（GSP367）

- **情境**：大型基礎架構管理公司的財務部門，帳單量越來越大、人工驗證成本高，要把收集、分類、驗證自動化。
- **任務**：
  1. 啟用 API，從遠端 bucket 複製原始碼。
  2. 建立 Form Parser（美國區）。
  3. 建立三個 bucket（標準級別、統一 bucket 層級存取權），以及 BigQuery 資料集 `invoice_parser_results`、資料表 `doc_ai_extracted_entities`。
  4. 部署 `process-invoices`，觸發條件設為「上傳到輸入 bucket」。要先把「Artifact Registry 讀取者」角色指派給 Compute Engine 服務帳戶。
  5. 上傳帳單做端對端測試，看記錄到「OK」，再確認 BigQuery 有資料。
- **常用指令**：`gcloud storage buckets create --default-storage-class --location --uniform-bucket-level-access`、`bq mk -d --location=...`、`bq mk --table`。
- **排錯**：
  - 部署出現權限錯誤時，等兩、三分鐘再重跑（IAM 生效有延遲）。
  - BigQuery 沒有資料時，到 Cloud Run 的「變數與密鑰」確認處理器 ID 和位置（小寫）。
  - 活動清單要手動重新整理。

---

## 6. 應用聯想（整理者補充，非課程內容）

- 「上傳 → 擷取欄位 → 寫進資料表 → 觸發後續處理」和 [[n8n]] 的事件觸發工作流是同一種思路，參見 [[AI 工作流程自動化實作_n8n 課程總結]]。
- ERP 情境可以參考的方向：紙本或 PDF 的發票、報支單據、證照影本，先用 Form Parser 或專用剖析器抽出欄位（發票號碼、日期、金額、供應商），寫進中介表，再交給既有系統比對或匯入。正式導入時，要改用 Cloud Tasks 這類可靠的排程，也要評估資料出境和個資問題。
- 擷取出來的欄位如果還要分類（例如判斷單據類型、轉給哪個部門），可以搭配 [[Jev 與 System One 決策模型]] 這類只回傳結構化判斷的模型。

---

## 關聯頁面
- [[GCP 雲端排程與現代化數據工程實戰]]
- [[跨平台螢幕擷取與智慧辨識實務]]
- [[n8n]]
- [[Jev 與 System One 決策模型]]
