---
type: entity
tags: [AI工具, Claude, VSCode, CLI, Anthropic]
sources: [
  "[[sources/01_AI_Tools/Claude 操作模式與功能介紹.md]]",
  "[[sources/01_AI_Tools/claude 如何加入vs code中.md]]",
  "[[sources/01_AI_Tools/AI CLI 工具比較與選擇.md]]",
  "[[raw/2026-06-15T152121+0800-Claude是什麼？claude ai教學：38篇Cowork、Skills、省Token秘訣全打包.md]]"
]
created: 2026-06-11
updated: 2026-06-11
---

# Claude (Anthropic AI 家族)

**Claude** 是由 Anthropic 開發的先進大型語言模型系列，在程式碼開發、複雜邏輯推理及自然語言理解方面表現卓越。

---

## 1. 介面與操作模式 (Interface Modes)

Claude 的使用介面可依您的工作場景進行選擇：

### 網頁協作版 (claude.ai)
- **專案模式 (Projects)**：Pro 與 Team 用戶專屬。可上傳特定代碼庫、風格指南等背景知識，使 Claude 的回答具備精確的專案上下文。
- **協作預覽 (Artifacts)**：當 Claude 生成網頁（HTML/React）、SVG 向量圖或程式碼時，會在右側彈出獨立視窗提供即時預覽與編輯，無須頻繁複製代碼。
- **分析工具 (Analysis Tool)**：後台整合 JavaScript 執行環境，可動態計算複雜數學或處理 CSV 數據。

### 行動 App 與 桌面應用程式
- **行動 App (iOS/Android)**：強調即時擷取，支援語音輸入與透過相機拍照 (Vision) 進行錯誤訊息辨識。
- **桌面 App (macOS/Windows)**：支援全域快捷鍵喚醒、內建螢幕截圖直接輸入分析。

### 技術開發與 API
- **API Console (Workbench)**：供開發者測試參數（Temperature 等）、調用不同模型版本（Opus, Sonnet, Haiku）。
- **Model Context Protocol (MCP)**：開放式協議，讓 Claude 可以安全地讀取本地數據源（如本地資料庫、[[sources/05_Tech_Development/Slack.md|Slack]]、Google Drive）。

---

## 2. 整合進 VS Code 開發環境

在 VS Code 編輯器中，您可以透過以下兩款主流擴充套件來整合 Claude (需要於 [Anthropic Console](https://console.anthropic.com/) 申請 API Key)：

### 方式 A：使用 Continue 擴充功能 (側邊欄助手)
- **特點**：適合日常對話、程式碼解釋與自動補全。
- **配置步驟**：
  1. 安裝 Continue 插件。
  2. 點擊側邊欄 Continue 圖標，打開底部齒輪設定檔 `config.json`。
  3. 在 `models` 區塊加入以下 JSON 配置：
     ```json
     {
       "title": "Claude 3.5 Sonnet",
       "provider": "anthropic",
       "model": "claude-3-5-sonnet-latest",
       "apiKey": "您的_API_KEY"
     }
     ```

### 方式 B：使用 Cline 擴充功能 (自主開發 Agent)
- **特點**：具備強大 Agent 自主能力，可要求其自動讀寫本地檔案、執行終端機指令及分析整個專案結構。
- **配置步驟**：安裝後點擊 Cline 圖標，在 API Provider 選擇 `Anthropic`，貼上 API Key 並選擇 `claude-3-5-sonnet-latest`。

---

## 3. Claude Code (命令行 CLI 工具)

**Claude Code** 是 Anthropic 官方推出的終端機 Agent 工具。

### 核心功能
- **自主執行**：可以直接在您的終端機環境中讀取本地代碼、執行編譯指令、自動執行測試、修復 Bug 並直接撰寫 Git commit 提交。
- **運作機制**：其「推理」大腦運行在雲端（資料傳輸全程加密，API 與商業版資料不納入訓練），而「執行手腳」則在您的本地電腦執行。
- **安裝與登入**：
  - Windows PowerShell (管理員權限)：
    ```powershell
    irm https://claude.ai/install.ps1 | iex
    claude auth login
    ```

---

## 4. 模型版本對比

- **Claude 3.5 Sonnet**：最推薦的黃金平衡版本，推理速度快，代碼能力最強。
- **Claude 3 Opus**：最強推理，適合邏輯極度複雜之任務，但速度慢、成本高。
- **Claude 3 Haiku**：極速輕量，適用於翻譯、簡單歸類與低延遲對話。

---

## 5. 辦公自動化與橫向對比

- **辦公軟體整合**：Claude 可以透過官方外掛直接整合至 Microsoft Excel 與 Microsoft Word，協助進行自動化數據處理與文件修訂，詳見 [[Claude 辦公自動化 (Excel & Word)]]。
- **主流模型評估**：關於 Claude 與 ChatGPT、Gemini 在付費版功能與代理執行力上的橫向對比，請參閱 [[三大 AI 付費版選用與效能橫向對比]]。
- **系統化學習資源**：針對 Claude 的入門與高階教學，包含 38 篇 Cowork、Skills 與省 Token 的實踐秘訣，請參閱 [[raw/2026-06-15T152121+0800-Claude是什麼？claude ai教學：38篇Cowork、Skills、省Token秘訣全打包.md|Claude 38篇精華教學打包]]。

