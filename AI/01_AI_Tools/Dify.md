---
tags:
- AI工具
- Claude
- Dify
- Docker
- Ollama
- RAG
- Slack
- 智能體
- 知識庫
---
Dify 是一個開源的 LLM（大語言模型）應用開發平台（Orchestration Platform）。它的核心理念是讓開發者（甚至是完全不會寫程式的業務人員）能夠簡單、快速地將各種大語言模型（如 ChatGPT、Claude、Gemini 等）轉化為具備實際功能的企業級 AI 應用。

如果用一句話來形容：**Dify 是 AI 時代的 Low-Code（低代碼）/ No-Code（無代碼）開發看板與工作流引擎。**

以下為您梳理 Dify 的核心功能、核心概念以及它為什麼受歡迎：

## 核心功能與優勢

### 1. 豐富的應用類型

Dify 支援建立多種型態的 AI 應用：

- **Chatbot（聊天機器人）：** 類似自訂版的 ChatGPT，可以設定 Role-play、語氣與特定任務。
    
- **Agent（智能體）：** 具備「思考」與「工具調用」能力。AI 可以根據使用者的問題，主動決定何時去搜尋網頁、計算數學或調用外部 API。
    
- **Workflow（工作流）：** 這是 Dify 最強大的功能之一。允許使用者用**拖拉黏貼圖形介面（Canvas）**，將 Prompt、LLM、程式碼節點（Python/Node.js）、條件分支（If/Else）和外部 API 串聯成複雜的自動化流程。
    

### 2. RAG（檢索增強生成）與知識庫管理

- **內建知識庫（Knowledge Base）：** 支援上傳 PDF、Word、TXT 或同步 Notion、網頁。
    
- **自動文本處理：** Dify 會自動幫你做文本切片（Chunking）與向量化（Embedding），不需要自己架設向量資料庫（Vector DB），就能輕鬆讓 AI 根據你的私有文件回答問題。
    

### 3. 模型中立（Model Agnostic）

- Dify 支援市面上幾乎所有主流的 LLM API（包括 OpenAI、Anthropic Claude、Google Gemini、DeepSeek，以及透過 Ollama 本地部署的開源模型 Llama 等）。
    
- 你可以在同一個工作流中，前端用便宜的模型做分類，後端核心邏輯換成強大的模型，切換模型只需要下拉選單即可完成。
    

### 4. 後端即服務（Backend as a Service）

- 當你在 Dify 介面設計好一個 AI 應用後，它會**自動生成標準的 API 接口**與一個**可直接分享的 WebApp 網頁**。
    
- 前端開發者可以直接調用 Dify API，完全不需要花時間去寫管理對話歷史（Session）、計算 Token、整合 Embedding 的後端程式碼。
    

## Dify 與類似工具（如 LangChain）的差異

許多人會拿 Dify 與 **LangChain** 或 **Flowise** 做比較：

|**特性**|**LangChain**|**Flowise / Langflow**|**Dify**|
|---|---|---|---|
|**定位**|開發者程式庫 (SDK)|可視化 LLM 連接工具|**企業級 AI 應用平台**|
|**使用門檻**|高（需純程式碼開發）|中（圖形化，但偏向底層邏輯）|**低（商務與開發者皆適用）**|
|**知識庫([[RAG]])**|需自行寫程式串接資料庫|需手動串接各個組件|**內建一鍵導入與最佳化**|
|**生產環境準備**|需自行處理高併發與維運|較適合原型設計|**內建完整的 API、日誌監控與用戶管理**|

## 常見的應用場景

1. **企業內部知識庫：** 將公司的規章制度、產品規格書、HR 手冊餵給 Dify，打造內部 IT/HR 客服。
    
2. **自動化報告生成：** 設定定時任務，讓 AI 自動抓取科技新聞、進行摘要，並排版發送到 [[Slack]] 或郵件。
    
3. **多步驟 AI 代理：** 建立一個能幫忙寫程式的 Agent，第一步生成程式碼，第二步調用 Python 節點執行測試，第三步根據報錯自動修復。
    

## 部署方式

Dify 提供了兩種主要的使用方式：

- **Cloud 版本：** 直接在 Dify 官網註冊帳號，內建免費額度，綁定自己的 Model API Key 就能使用。
    
- **Community 版本（開源）：** 支援透過 **Docker Compose** 一鍵本地部署（Self-hosted），對於重視資安、資料不願外流的企業非常友善。