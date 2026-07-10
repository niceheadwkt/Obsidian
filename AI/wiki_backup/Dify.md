---
type: entity
tags: [AI工具, Dify, LowCode, NoCode, RAG, 工作流, Docker]
sources: ["[[sources/01_AI_Tools/Dify.md]]"]
created: 2026-06-18
updated: 2026-06-18
---

# Dify (開源企業級低代碼 AI 應用平台)

**Dify** 是一個開源的大語言模型（LLM）應用開發平台（Orchestration Platform）。它的核心理念是讓開發者與業務人員能夠快速、無縫地將各種大語言模型（如 ChatGPT、[[Claude]]、Gemini、DeepSeek 等）轉化為具備實際功能、符合生產環境要求的企業級 AI 應用。

如果用一句話來形容：**Dify 是 AI 時代的 Low-Code（低代碼）/ No-Code（無代碼）開發看板與工作流引擎。**

---

## 1. 核心功能與技術優勢

### 豐富的應用型態
Dify 支援建立多種不同的 AI 應用，滿足從輕量聊天到複雜業務流程的需求：
- **聊天機器人 (Chatbot)**：類似自訂版的 ChatGPT，可配置角色設定（Role-play）、人設語氣與特定上下文任務。
- **智能體 (Agent)**：具備「思考」與「工具調用」能力。AI 可以根據使用者的提問，自主決定何時進行網頁搜尋、執行程式碼計算或調用外部 API（基於 ReAct 或 Function Calling 框架）。
- **工作流 (Workflow)**：這是 Dify 最強大的核心功能之一。允許使用者使用**可視化圖形介面（Canvas）**，以拖拉黏貼的方式將 Prompt 提示詞、LLM 模型、程式碼節點（Python/Node.js）、條件分支（If/Else）和外部 API 串聯成複雜的自動化商務流程。

### 內建 RAG 與知識庫管理
- **一鍵導入**：支援上傳 PDF、Word、TXT 等文件，或直接同步 Notion、抓取網頁內容。
- **自動化處理**：Dify 自動在背景完成文本分段（Chunking）、向量化（Embedding）與清理，使用者無需手動架設與維護複雜的向量資料庫（Vector DB），即可輕鬆讓 AI 根據私有知識庫進行精確的檢索與問答（[[RAG 與 DeepSearch 概念綜述|檢索增強生成]]）。

### 模型中立 (Model Agnostic)
- **廣泛兼容**：支援市面上所有主流雲端模型 API，同時支援透過 [[Ollama]] 本地部署的開源模型（如 Qwen、Llama 等）。
- **混合呼叫**：允許在同一個工作流中混合使用不同的模型（例如：前端先用便宜的模型做意圖分類，後端核心步驟再調用強大的 Claude 模型進行推理），切換模型只需透過下拉選單即可完成。

### 後端即服務 (BaaS, Backend as a Service)
- **自動生成 API**：在 Canvas 上設計完成後，Dify 會自動生成符合標準的 API 接口以及可直接分享的 WebApp 網頁。
- **簡化開發**：前端開發人員可直接調用 API，省去處理對話歷史管理（Session）、Token 計算、向量檢索等繁瑣後端程式開發。

---

## 2. 業界主流工具橫向對比

在選擇 AI 應用編排工具時，Dify 與 LangChain 及 Flowise 存在以下定位差異：

| **特性** | **LangChain** | **Flowise / Langflow** | **Dify** |
| :--- | :--- | :--- | :--- |
| **技術定位** | 開發者程式庫 (SDK) | 可視化 LLM 連接工具 | **企業級 AI 應用平台** |
| **使用門檻** | 高（需純程式碼撰寫） | 中（圖形化，但偏向底層連線） | **低（商務人員與工程師皆適用）** |
| **知識庫 (RAG)** | 需自行編寫程式碼串接數據庫 | 需手動串接各個 Embedding 與 DB 組件 | **內建一鍵導入與檢索最佳化** |
| **生產環境整備** | 需自行處理並發、日誌與維運 | 較適合概念驗證 (PoC) 原型設計 | **內建完整 API、日誌監控與用戶管理** |

---

## 3. 常見應用場景與實務

1. **企業內部智慧客服**：將公司的規章制度、產品規格書、HR 手冊整包餵給 Dify 知識庫，打造 24 小時不間斷的內部 IT 與 HR 問答助理。
2. **自動化行銷與新聞日報**：設定定時任務，讓 AI 工作流自動抓取科技新聞、進行篩選摘要，並將排版好的日報自動發送至 [[sources/05_Tech_Development/Slack.md|Slack]] 或 Gmail。
3. **多步驟 AI 代碼偵錯 Agent**：建立一個能幫忙寫程式的 Agent，第一步生成程式碼，第二步調用本地 Python 節點執行測試，第三步若報錯則自動讀取錯誤日誌進行自我修正。

---

## 4. 部署方案

- **Dify Cloud**：直接在 Dify 官網註冊，內建免費額度，只需綁定自己的 Model API Key 即可快速上手。
- **Dify Community (開源版)**：支援透過 **Docker Compose** 一鍵本地部署（Self-hosted），對於重視隱私安全、數據不允許外流的企業提供完善的私有化保障。
