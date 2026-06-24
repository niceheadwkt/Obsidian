---
type: concept
tags: [Antigravity, AI-Agent, 記憶系統, MCP, IDE]
sources: [
  "[[sources/2026-06-17T143022+0800-99%的人沒用好Antigravity：22個核心概念一次講透，從記憶系統到MCP協議全解析【2026最新保姆實操】.md]]",
  "[[raw/2026-06-20T143229+0800-N8N要被取代了？用Google Antigravity 10分钟聊出智能获客引擎：0代码搭建全自动金融机构抓取+同步工作流【新型n8n实战】.md]]"
]
created: 2026-06-18
updated: 2026-06-23
---

# Antigravity 核心概念與五層記憶系統

本頁面整理並分析了 Google Antigravity IDE 代理程式（AI Agent）的核心運作機制，內容提煉自 [[sources/2026-06-17T143022+0800-99%的人沒用好Antigravity：22個核心概念一次講透，從記憶系統到MCP協議全解析【2026最新保姆實操】.md|Automate with Bonnie 的 22 個核心概念解析]]，並引入最新 [[raw/2026-06-20T143229+0800-N8N要被取代了？用Google Antigravity 10分钟聊出智能获客引擎：0代码搭建全自动金融机构抓取+同步工作流【新型n8n实战】.md|Antigravity 自動化實戰與 n8n 終極對比]]。

---

## 1. Antigravity 的本質與 IDE 介面

Antigravity 與一般的聊天機器人（如網頁版 ChatGPT）有本質上的不同。它是一個「擁有手腳、穿著鋼鐵裝」的 **AI Agent**，具有讀取檔案、自主運行測試、操作瀏覽器以及在本地儲存檔案的能力。

### 核心介面與工作管理
- **規劃模式 (Planning Mode)**：在面對複雜任務時（如重大架構修改、深度研究），Agent 會先制定 `implementation_plan.md`，經使用者審查批准後才進入執行模式，並透過 `task.md` 追蹤任務進度。
- **Agent 管理器 (Agent Manager)**：用於管理多個正在背景執行的任務與 Subagents，確保同時進行多個專案時不會混亂。
- **工作區 (Workspace)**：Agent 綁定的本地工作目錄，限制 Agent 的檔案讀寫範圍，確保安全性。
- **審查驅動開發 (RDD, Review-Driven Development)**：在每一步關鍵變更後，由 Agent 自動或提示使用者進行審查，以確保代碼質量並將錯誤率降到最低。

---

## 2. 工具操作與安全性限制

### 自主操作能力
- **多模態截圖輸入**：Agent 可以對目前的螢幕或特定視窗進行截圖，並將其作為多模態輸入來感知 UI 狀態。
- **內置瀏覽器自主操作**：Agent 可啟動無頭或有頭瀏覽器，自動進行點擊、填寫表單、抓取網頁數據等複雜的瀏覽器自動化任務。

### 安全與權限控制
- **權限設置 (Permissions Control)**：Antigravity 擁有一套細粒度的安全機制。當 Agent 嘗試執行敏感操作（如執行終端命令、讀寫工作區外的檔案或發起外部網路請求）時，會暫停並向使用者申請權限。
- **安全自動運行**：使用者可以對信任的命令或工具配置白名單，使其在無需反覆彈出提示的情況下自動執行，在效率與安全之間取得平衡。

---

## 3. 全局行為規範引導

Agent 的行為受到兩個核心規則文件的約束：
1. **`agent.md`**（或 `.cursorrules` 等）：存放於工作區根目錄，專門為該專案量身打造的 Agent 開發與行為規範。
2. **全局用戶規則 (Global User Rules)**：位於 IDE 的全局設定中，定義 Agent 對於所有專案通用的回覆風格、程式碼偏好與行為邊界。

---

## 4. 五層記憶系統（為什麼 Agent 會遺忘？）

Antigravity 設計了精細的五層記憶結構，用以在長對話中保持上下文，並避免因 Token 暴漲而導致的「遺忘」或「決策偏差」：

| 記憶層級 | 名稱 | 作用與原理 |
| :---: | :--- | :--- |
| 第一層 | **上下文窗口 (Context Window)** | 當前對話中最直接、即時的緩衝區。受限於 LLM 的最大 Input Token 限制。 |
| 第二層 | **對話歷史記錄 (Conversation History)** | 保留對話的順序脈絡。當對話過長時，系統會自動進行摘要壓縮（Compaction），這也是有時 Agent 會忘記細節的主因。 |
| 第三層 | **知識項 (Knowledge Items, KI)** | 儲存在專案 `.gemini/` 或特定目錄下的結構化知識快照，包含 metadata 與 artifacts。Agent 會在工作開始前優先檢索相關的 KIs，以避免重複勞動。 |
| 第四層 | **記憶轉移 (Memory Transfer)** | 允許使用者一鍵將其他工具（如 ChatGPT、Gemini）中的個人偏好與歷史對話背景匯入至 Antigravity 中。 |
| 第五層 | **長期記憶助理 (Long-Term Memory Assistant)** | 跨會話的持久化記憶載體。配合 `Projects` 功能，Agent 可以自動記住使用者的長期開發習慣、指令風格與系統配置。 |

---

## 5. 模型多樣性與 MCP 協議

### 多模型支持
Antigravity 原生支援 Gemini，但使用者也可以隨時切換至 Claude、OpenAI 等大模型。此外，可以在 IDE 中直接安裝 [[Claude]] 相關的 CLI 工具（如 Claude Code）或整合 CodeX 橋接本地與雲端推理服務。

### 連接萬物的 MCP 協議
- **MCP 協議 (Model Context Protocol)**：由 Anthropic 提出的統一標準，用於將外部資料源和工具（如 Notion、Airtable、GitHub、YouTube 等）以 API 或 MCP Server 的形式接入 AI Agent。
- **技能與工作流 (Skills & Workflows)**：技能（Skills）是打包好的外部工具或 SOP 腳本（例如 edge TTS、remotion 影片生成等）。將技能放入指定目錄後，Agent 即可手動或自動調用，實現更為複雜的個人自動化工作流。

---

## 6. AI 自動化工作流之範式轉移：n8n 與 Antigravity 終極對比
依據 [[raw/2026-06-20T143229+0800-N8N要被取代了？用Google Antigravity 10分钟聊出智能获客引擎：0代码搭建全自动金融机构抓取+同步工作流【新型n8n实战】.md|Automate with Bonnie 的 Antigravity 實戰分析]]，2026 年自動化領域正在經歷一場從「手動連線」到「Vibe Coding」的範式轉移：

### ▍ n8n / Make 的侷限
*   **痛點**：節點成百上千、邏輯分支極其複雜、除錯過程繁瑣。一旦外部網站結構微調或 API 變更，常導致整個流程崩潰且難以修復。

### ▍ Antigravity 帶來的變革 (Vibe Coding)
*   **意圖導向 (Vibe Coding)**：使用者只需以自然語言描述終端意圖，Agent 即能自主進行邏輯推演、撰寫 Python/Node 腳本，甚至能控制無頭瀏覽器模擬真實人類操作。
*   **自我修復能力 (Self-annealing)**：當工作流在背景執行出錯或遭到目標網站阻擋時，Agent 能自我捕捉錯誤日誌，即時改寫代碼或重新規劃路徑，無須人工干預。

### ▍ 實戰應用：DOE 框架引導與智能獲客引擎
在自動化工作流中，可以使用 **DOE 框架** 作為給 Agent 的行為約束，實現高度穩定的業務執行：
*   **D (Directive, 指令)**：清晰定義 Agent 的目標任務與輸入格式（如：`.env`、`credentials.json` 與 Google Sheet 位置）。
*   **O (Observation, 觀察)**：要求 Agent 對抓取的資料進行高頻狀態確認，檢查格式與遺漏。
*   **E (Experiment, 實驗)**：Agent 自主進行 API 測試、模擬瀏覽與數據富化。
*   **業務場景落地（自動化金融獲客）**：
    1.  **GMB 數據抓取**：Agent 自主分析並抓取 Google 地圖上特定地區（如多倫多）金融機構的原始名冊。
    2.  **深度數據富化**：Agent 啟動瀏覽器深入各金融機構官網，自動提取官方 Email 與 LinkedIn、Twitter 等社群帳號。
    3.  **AI 智慧評分**：利用 LLM 分析機構網站內容，自動對其潛在價值進行 1-5 分的評分。
    4.  **個性化冷啟動郵件生成**：AI 自動檢測其官網 SEO 漏洞，隨機生成極具吸引力的專屬開發信開頭。
    5.  **持久化同步**：自動將所有富化後的資料寫入雲端 Google Sheets。

---

## 關聯概念與頁面
- **知識庫規範**：[運作規範](../schema.md)
- **專案管理工作流**：`[[Claude 專案管理一桌三櫃工作流]]`
- **影片工程自動化**：`[[Antigravity 與 Remotion 影片生成實務]]`
