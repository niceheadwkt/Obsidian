---
type: concept
tags:
  - GCP
  - Cloud-Scheduler
  - ETL
  - ELT
  - dbt
  - BigQuery
  - 數據工程
sources:
  - "[[AI/raw/GCP_AI_and_ETL_Master_Guide.md|GCP 雲端服務、AI Agent 與現代化數據工程 (ETL/ELT) 全方位實戰指南]]"
created: 2026-09-17
updated: 2026-09-17
---

# GCP 雲端排程與現代化數據工程實戰

本頁彙整 Google Cloud Platform（GCP）的雲端排程服務、傳統 ETL 與現代 ELT 架構的差異，以及以 dbt + BigQuery 為核心的現代化數據棧（Modern Data Stack）實戰。

---

## 1. Google Cloud Scheduler

**Cloud Scheduler** 是 GCP 提供的全託管式時間排程服務，等同「雲端版 Cron Job」，無需維護伺服器即可依時間規律自動發送 HTTP 請求或觸發 GCP 內部服務。

- **免費額度**：每個計費帳戶每月免費 **3 個 Job**；計費以 Job 數量計算，**不限執行次數**（例如一個 Job 每分鐘執行一次，一個月約 43,200 次，只要總 Job 數在 3 個以內仍完全免費）。
- **超額收費**：第 4 個 Job 起，每個 Job 每月 $0.10 美元，按天數比例折算。
- **常見陷阱**：Cloud Scheduler 本身免費，但它**觸發的後端服務**（Cloud Run、Cloud Functions、Pub/Sub、Compute Engine 或外部 API）若耗用算力/流量/記憶體，會依原本計費方式**另行收費**。

### Cloud Scheduler vs. Gemini Spark（與 [[Google Spark 與 GAS 雲端自動化實務]] 對照）

| 比較維度 | Cloud Scheduler | Gemini Spark |
| :--- | :--- | :--- |
| 定位 | 基礎設施層時間排程工具 | 應用層 24/7 個人 AI 代理 |
| 操作方式 | Cron 語法或 GCP 控制台 | 自然語言對話 |
| 邏輯與推理 | 無 AI，純時間觸發 | 具 LLM 思考能力，能理解語意與決策 |
| 適用目標 | 後端 API 觸發、資料庫備份 | 個人工作自動化、郵件/文件智慧搜尋 |

兩者可協同運作：Cloud Scheduler 負責硬性時間驅動（如每天凌晨 2 點跑 ETL 寫入 BigQuery），Gemini Spark 負責智慧型內容處理（如早上 8 點自動摘要 ETL 分析報告並發送團隊信箱）。

---

## 2. ETL 基礎與 ETL / ELT 架構演進

**ETL** 由三階段組成：**Extract（擷取）→ Transform（轉換）→ Load（載入）**。Transform 階段最複雜，包含數據清洗（去重、處理缺失值）、格式統一、商業邏輯計算，以及 PII（個人可識別資訊）的加密/遮蔽去識別化。

隨雲端分散式算力（BigQuery、Snowflake）普及，衍生出 **ELT**：資料先直接寫入雲端資料倉儲（保留 Raw Data），再利用倉儲本身的平行算力以 SQL 進行轉換。

| 比較項目 | ETL（傳統） | ELT（現代雲端） |
| :--- | :--- | :--- |
| 轉換位置 | 獨立 ETL 伺服器 | 目標雲端資料倉儲內部 |
| 原始資料保留 | 通常不保留 | 完整保留 |
| 開發靈活性 | 較低 | 極高（改 SQL 即可重算） |
| 資安合規性 | 極高（落庫前已遮蔽） | 需搭配欄位級存取權限控管 |
| 技術門檻 | 高（需專用工具或 Python/Java） | 低（多用標準 SQL） |

**選型建議**：地端架構、嚴格資安合規（金融/醫療 PII 規定）適合 ETL；已採用雲端原生資料倉儲、商業需求變動快速則適合 ELT。

---

## 3. 現代化數據棧：dbt + BigQuery

現代 ELT 主流組合：Extract & Load 工具（Fivetran、Airbyte）＋ 資料倉儲與算力（BigQuery）＋ Transform 管理（**dbt**）。

- **dbt（data build tool）** 只專注 Transform 階段：工程師只需寫 `SELECT` 語句，dbt 自動編譯並指揮 BigQuery 建表；透過 `{{ ref('model_name') }}` 自動解析模型依賴關係（DAG／資料血緣圖）；支援 Git 版本控制、環境隔離與 `dbt test` 資料品質自動測試。
- **金牌分層架構（Medallion Architecture）**：`raw_data`（原始層）→ `staging`（基礎清洗層，`stg_` 前綴，欄位重新命名、型態轉換）→ `intermediate`（複雜邏輯拼貼層，`int_` 前綴，可選）→ `marts`（商業報表/語意層，`fct_`/`dim_` 前綴，對接 Looker/Tableau/PowerBI）。
- **效能優化**：BigQuery 可用 `Partitioning`（分區表，依日期切塊）將查詢費用降低達 90% 以上。

---

## 4. 關鍵術語速查

- **Cron Job**：Unix/Linux 定時任務排程設定（如 `0 2 * * *` 代表每日凌晨 2 點）。
- **DAG（有向無環圖）**：表示任務執行順序與依賴關係，確保步驟 A 跑完才跑步驟 B。
- **PII（個人可識別資訊）**：姓名、身分證字號、電話等，數據工程中須高度防護的敏感資安標的。

---

## 關聯頁面
- `[[Google Spark 與 GAS 雲端自動化實務]]`
- `[[生成式 AI 企業應用與成本經濟學]]`
