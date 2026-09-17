# Fastmarkets V2 安裝與設定流程

本文件說明 **Fastmarkets V2** 專案的安裝、設定與初始資料庫建立流程。

---

## 流程圖

```mermaid
flowchart TD
    Start(["開始安裝與設定"]) --> Step1["步驟 1：安裝 Python 套件<br><code>pip install -e .</code>"]

    Step1 --> Step2["步驟 2：設定環境變數<br>建立 <code>.env</code> 檔案"]
    
    subgraph EnvConfig ["💡 .env 必要設定項"]
        direction TB
        E1["AVA_BASE_URL=https://demoava.icsc.com.tw"]
        E2["AVA_API_KEY=你的 API Key"]
        E3["AVA_EXPERT_ID=你的 Expert ID"]
    end
    Step2 -.-> EnvConfig

    Step2 --> Step3["步驟 3：初始化資料庫結構<br><code>fastmarkets-v2 db init</code><br><i>(建立 data/fastmarkets.db 與資料表)</i>"]

    Step3 --> Step4["步驟 4：匯入指標定義資料<br><code>fastmarkets-v2 seed-indicators &lt;路徑&gt;/indicators_current.md</code>"]

    Step4 --> Step5["步驟 5：放置 PDF 並匯入資料<br>放置 PDF 至 <code>raw/</code> 目錄<br>執行 <code>fastmarkets-v2 ingest</code>"]

    Step5 --> Ready{"系統準備就緒"}

    Ready -->|啟動 Web 儀表板| Serve["<code>fastmarkets-v2 serve</code><br>開啟 http://127.0.0.1:8000"]
    Ready -->|產出 HTML 週報| Report["<code>fastmarkets-v2 report</code><br>產出自包含週報 HTML"]

    classDef default fill:#f9f9f9,stroke:#333,stroke-width:1px;
    classDef step fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef ready fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef action fill:#fff3e0,stroke:#e65100,stroke-width:1.5px;
    classDef note fill:#fafafa,stroke:#9e9e9e,stroke-dasharray: 5 5;

    class Step1,Step2,Step3,Step4,Step5 step;
    class Ready ready;
    class Serve,Report action;
    class EnvConfig note;
```

---

## 詳細步驟說明

### 步驟 1：安裝 Python 套件
在專案根目錄下以開發模式安裝套件與相依函式庫：
```bash
pip install -e .
```

### 步驟 2：建立並設定 `.env`
在專案根目錄下建立 `.env` 檔案，並填入 Ava API 連線資訊：
```env
AVA_BASE_URL=https://demoava.icsc.com.tw
AVA_API_KEY=你的 API Key
AVA_EXPERT_ID=你的 Expert ID
```

### 步驟 3：初始化 SQLite 資料庫
建立 `data/fastmarkets.db` 以及所需資料表（`indicator`, `price_weekly`, `summary`）：
```bash
fastmarkets-v2 db init
```

### 步驟 4：匯入指標定義
將各鋼鐵產品規格與指標定義匯入資料庫：
```bash
fastmarkets-v2 seed-indicators path/to/indicators_current.md
```

### 步驟 5：匯入 PDF 原始報告
將 Fastmarkets Daily PDF 報告檔案放置於 `raw/` 資料夾，接著執行自動掃描與批次匯入：
```bash
# 批次匯入所有尚未處理的 PDF
fastmarkets-v2 ingest

# 或匯入指定檔案
fastmarkets-v2 ingest --file raw/20260708.pdf
```

---

## 常用操作指令速查

| 指令 | 說明 | 備註 |
| :--- | :--- | :--- |
| `fastmarkets-v2 serve` | 啟動 Web 儀表板 | 預設監聽 `http://127.0.0.1:8000` |
| `fastmarkets-v2 report` | 產出最近週三的 HTML 週報 | 預設存至 `output/YYYY/MM/` |
| `fastmarkets-v2 db stats` | 查詢資料庫目前紀錄統計 | 顯示指標數、價格筆數、摘要篇數 |
