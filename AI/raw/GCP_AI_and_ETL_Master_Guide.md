# GCP 雲端服務、AI Agent 與現代化數據工程 (ETL/ELT) 全方位實戰指南

---

## 📌 目錄
1. [Google Cloud Scheduler 完整解析](#1-google-cloud-scheduler-完整解析)
2. [Cloud Scheduler vs. Gemini Spark 深入對比](#2-cloud-scheduler-vs-gemini-spark-深入對比)
3. [ETL 基礎觀念與運作流程](#3-etl-基礎觀念與運作流程)
4. [ETL 與 ELT 架構演進、差異與選型指南](#4-etl-與-elt-架構演進差異與選型指南)
5. [現代化數據棧 (Modern Data Stack)：dbt + BigQuery 實戰](#5-現代化數據棧-modern-data-stack-dbt--bigquery-實戰)
6. [新手必讀：關鍵術語與技術概念總整理](#6-新手必讀關鍵術語與技術概念總整理)

---

## 1. Google Cloud Scheduler 完整解析

### 1.1 什麼是 Cloud Scheduler？
Cloud Scheduler 是 Google Cloud Platform (GCP) 提供的全託管式**時間排程服務**。它等同於「雲端版的 Cron Job」，無需維護任何實體或虛擬伺服器，就能依照預設定的時間規律，自動發送 HTTP 請求或觸發 GCP 內部服務。

### 1.2 免費額度與費用計算機制
* **免費配額**：每個 Google 帳戶（以 **Billing Account / 計費帳戶** 為單位）每月免費提供 **3 個 Job（工作）**。
* **按 Job 數量計費，不限執行次數**：
  * 免費計費單位是「Job 的數量」，而非「執行/觸發的次數」。
  * *範例*：若您設定了一個 Job 且頻率為每分鐘執行一次（一個月執行約 43,200 次），只要帳戶內總 Job 數在 3 個以內，**依舊完全免費**。
* **超過免費額度的收費**：
  * 第 4 個 Job 開始，每個 Job 的價格為 **$0.10 美元 / 月**（折合台幣約 3 元/月）。
  * 採天數按比例折算：若建立第 4 個 Job 只使用了 10 天便刪除，費用為 `$0.10 ÷ 31 × 10 ≈ $0.032 美元`。
* **⚠️ 初學者常見陷阱（關聯服務費用）**：
  * Cloud Scheduler 本身免費（3 個額度內），但它**觸發的後端服務**（如 Cloud Run、Cloud Functions、Pub/Sub、Compute Engine 或外部 API）若有使用到算力、網絡流量或記憶體，該後端服務會**依據其原本的計費方式另行收費**。

---

## 2. Cloud Scheduler vs. Gemini Spark 深入對比

初學者常混淆「自動化排程工具」與「AI 代理 (AI Agent)」，兩者位處完全不同的架構層級：

### 2.1 核心差異對比表

| 比較維度 | **Cloud Scheduler** | **Gemini Spark** |
| :--- | :--- | :--- |
| **定位與性質** | 基礎設施層級 (Infrastructure) 的時間排程工具 | 應用層/Workspace 的 24/7 個人 AI 代理 (AI Agent) |
| **主要功能** | 在指定時間發送 API 請求、觸發事件隊列 | 自動讀取、整理與處理 Gmail、Calendar、Drive 任務 |
| **操作方式** | 撰寫 Cron 語法（如 `0 8 * * *`）或設定 GCP 控制台 | 使用自然語言對話（如「每天早上 8 點整理信件並產出摘要」） |
| **邏輯與推理** | **無 AI / 無推理能力**，純粹依時間「死板觸發」 | **具備 LLM 思考能力**，能理解語意、上下文與做出決策 |
| **適用目標** | 後端 API 觸發、資料庫備份、批次檔驅動 | 個人工作自動化、會議行程協調、郵件與文件智慧搜尋 |

### 2.2 兩者如何協同運作？
* **Cloud Scheduler** 負責**硬性時間與系統層級的驅動**（如每天半夜 2 點執行資料庫 ETL，將數據寫入 BigQuery）。
* **Gemini Spark** 負責**智慧型內容處理與對人互動**（如早上 8 點自動閱讀 ETL 產出的分析報告，將內容摘要為重點訊息發送到團隊信箱）。

---

## 3. ETL 基礎觀念與運作流程

### 3.1 什麼是 ETL？
ETL 是數據工程與數據倉儲（Data Warehouse）中最基礎且核心的數據流水線架構，由三個階段組成：
1. **Extract（擷取）**
2. **Transform（轉換）**
3. **Load（載入）**

```
[多方原始數據源] ──( Extract )──> [暫存區 Staging / 記憶體]
                                         │
                                  ( Transform )
                                         ▼
[目標資料倉儲/分析系統] <──( Load )──── [乾淨結構化數據]
```

### 3.2 三大步驟詳細拆解

1. **Extract（擷取）**
   * **目的**：將散落在企業各系統的原始資料提取出來。
   * **常見資料源**：關聯式資料庫 (MySQL, PostgreSQL)、第三方 API、網站日誌 (Logs)、CSV/JSON 檔案、CRM/ERP 系統。
2. **Transform（轉換）**
   * **目的**：將雜亂無章的原始數據清理並轉換成適合商業分析的格式（最複雜的一環）。
   * **包含操作**：
     * **數據清洗**：刪除重複資料、處理缺失值 (Null Handling)。
     * **格式統一**：例如統一將日期格式轉為 `YYYY-MM-DD`，將貨幣統一折算為 USD。
     * **商業邏輯計算**：衍生計算欄位（例如透過出生年月日計算年齡分群）、數據聚合 (SUM / AVG)。
     * **資安與去識別化**：加密或遮蔽敏感個人資料 (PII)，如身份證字號、電話號碼。
3. **Load（載入）**
   * **目的**：將處理好的乾淨數據寫入目標儲存系統。
   * **目標系統**：數據倉儲 (Data Warehouse) 或商業智慧 (BI) 資料庫。

---

## 4. ETL 與 ELT 架構演進、差異與選型指南

隨著雲端分散式算力（如 Google BigQuery、Snowflake）的普及，傳統的 **ETL** 架構逐漸演進出現代化的 **ELT**。

### 4.1 核心差異：轉換 (Transform) 發生的位置與時間
* **ETL (傳統)**：資料進入資料庫**之前**，先在專用的 ETL 伺服器中做完轉換，才寫入目標資料庫。
* **ELT (現代)**：資料**直接先寫入雲端資料倉儲** (Raw Data)，後續再利用資料倉儲龐大的平行算力（使用 SQL）進行轉換。

```
ETL 流程： 資料源 ──> 專用 ETL 伺服器 (Transform) ──> 資料倉儲 (Load)
ELT 流程： 資料源 ───────────(Load Direct)─────────> 雲端資料倉儲 ──(Transform via SQL)──> 分析模型
```

### 4.2 ETL vs. ELT 詳細對比表

| 比較項目 | **ETL (傳統模式)** | **ELT (現代雲端模式)** |
| :--- | :--- | :--- |
| **轉換位置** | 獨立的 ETL 伺服器 / 記憶體 | 目標雲端資料倉儲內部 (In-Warehouse) |
| **原始資料 (Raw Data)** | 通常不保留（僅保留轉換後的結果） | 完整保留於資料倉儲/資料湖中 |
| **開發靈活性** | 較低（若要調整邏輯，需修訂 Pipeline 並重新抓取）| 極高（原始資料都在，修改 SQL 即可重新計算） |
| **載入速度** | 較慢（需等待 Transform 處理完成） | 極快（資料先寫入資料庫再說） |
| **資安與合規性** | **極高**（敏感資料落庫前就已遮蔽/去識別化） | 需要配合細緻的欄位級 (Column-level) 存取權限控管 |
| **技術維護門檻** | 高（需學習專用 ETL 工具或寫 Python/Java 流水線） | 低（大部份轉換邏輯使用標準 **SQL** 即可完成） |

### 4.3 選型決策指南
* **選擇 ETL 的情境**：
  1. 使用地端 (On-Premise) 架構，資料庫運算資源有限。
  2. 嚴格的資安與個資法規（如金融、醫療業，規定敏感個資 PII 絕不能以明文儲存在目標資料庫中）。
* **選擇 ELT 的情境**：
  1. 已採用雲端原生資料倉儲（Google BigQuery、Snowflake、Amazon Redshift）。
  2. 商業需求變動快速，分析師需要靈活地針對歷史資料重新定義分析指標與報表。

---

## 5. 現代化數據棧 (Modern Data Stack)：dbt + BigQuery 實戰

在現代 ELT 架構中，最主流的組合為：
* **Extract & Load 工具**（如 Fivetran、Airbyte）
* **資料倉儲與算力**（Google BigQuery）
* **Transform 轉換管理**（dbt - data build tool）

### 5.1 dbt (data build tool) 的角色與優勢
dbt 不負責「擷取」或「儲存」資料，它只專注於 **Transform** 階段：
* **純 SQL 開發**：工程師只需撰寫 `SELECT` 語句，dbt 會自動編譯並指揮 BigQuery 建立 Table 或 View。
* **自動依賴管理 (DAG)**：透過 `{{ ref('model_name') }}`，dbt 自動解析模型之間的前後依賴關係與資料血緣圖 (Lineage Graph)。
* **工程化最佳實踐**：支援 Git 版本控制、環境隔離 (Dev/Prod)、資料品質自動測試 (`dbt test`) 與自動化文件生成。

### 5.2 金牌分層架構 (Medallion Architecture)

在 dbt + BigQuery 架構中，通常將資料轉換分為三層：

```
BigQuery: raw_data ──> BigQuery: staging ──> BigQuery: intermediate ──> BigQuery: marts
  (原始資料層)              (基礎清洗層)           (複雜邏輯拼貼層)          (商業報表/語意層)
```

1. **Staging 層 (`stg_`)**：
   * 與原始表 1:1 對應，僅做基礎清洗：欄位重新命名（符合團隊規範）、型態轉換 (CAST)、時區統一。
2. **Intermediate 層 (`int_`)**（可選）：
   * 處理複雜的多表 Join、中間聚合或窗口函數 (Window Functions) 運算。
3. **Marts 層 (`fct_` / `dim_`)**：
   * 建立維度模型（事實表 Fact Table 與維度表 Dimension Table），對接 Looker、Tableau 或 PowerBI 等前端報表。

### 5.3 實戰程式碼範例

**步驟 1：Staging 模型 (`models/staging/stg_orders.sql`)**
```sql
SELECT
    order_id,
    customer_id,
    CAST(order_date AS DATE) AS order_date,
    status AS order_status,
    amount AS order_amount_usd
FROM {{ source('raw_shop', 'orders') }}
```

**步驟 2：Marts 模型與效能優化 (`models/marts/fct_daily_revenue.sql`)**
```sql
-- 指揮 BigQuery 建立實體表，並使用 Partitioning (分區) 降低查詢費用
{{ config(
    materialized='table',
    partition_by={
      "field": "order_date",
      "data_type": "date",
      "granularity": "day"
    }
) }}

WITH stg_orders AS (
    SELECT * FROM {{ ref('stg_orders') }} -- dbt 自動建立依賴與 DAG
)

SELECT
    order_date,
    COUNT(DISTINCT order_id) AS total_orders,
    SUM(order_amount_usd) AS total_revenue
FROM stg_orders
WHERE order_status = 'COMPLETED'
GROUP BY 1
```

---

## 6. 新手必讀：關鍵術語與技術概念總整理

以下為對談中涉及的重要技術專有名詞對照說明：

* **Cron Job**：Unix/Linux 系統中的定時任務排程設定（例如：`0 2 * * *` 代表每日凌晨 2:00 自動執行）。
* **API (Application Programming Interface)**：應用程式介面，軟體與軟體之間溝通與傳送指令的標準管道。
* **Data Warehouse (資料倉儲)**：專門為「大規模數據分析與查詢」設計的高效能資料庫（如 Google BigQuery）。
* **DAG (Directed Acyclic Graph, 有向無環圖)**：數據工程中用來表示「任務執行順序與依賴關係」的圖表，確保步驟 A 跑完才能跑步驟 B。
* **Partitioning (分區表)**：BigQuery 中的費用優化技術，將大表按日期切塊。查詢時只需掃描特定分區，可節省高達 90% 以上的查詢費用。
* **PII (Personally Identifiable Information)**：個人可識別資訊（如姓名、身分證字號、電話），在數據工程中屬於必須高度防護的敏感資安標的。
