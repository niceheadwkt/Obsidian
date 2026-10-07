---
type: entity
tags: [AI工具, Claude, VSCode, CLI, Anthropic]
sources: [
  "[[sources/01_AI_Tools/Claude 操作模式與功能介紹.md]]",
  "[[sources/01_AI_Tools/claude 如何加入vs code中.md]]",
  "[[sources/01_AI_Tools/AI CLI 工具比較與選擇.md]]",
  "[[raw/2026-06-15T152121+0800-Claude是什麼？claude ai教學：38篇Cowork、Skills、省Token秘訣全打包.md]]",
  "[[AI/raw/2026-08-18T194359+0800-Claude「隱形文字浮水印」是什麼？看懂背後原理、限制和影響.md|Claude「隱形文字浮水印」是什麼？看懂背後原理、限制和影響]]",
  "[[AI/raw/2026-10-07T155412+0800-全球100大AI工具榜出爐！誰流量海放全場？有哪些隱形贏家？6大洞察一次看.md|全球100大AI工具榜出爐！6大洞察一次看（數位時代）]]"
]
created: 2026-06-11
updated: 2026-10-07
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

---

## 6. 生成內容標記：Claude 文字浮水印機制

自 2026 年 8 月 2 日起，部分支援的 Claude 模型輸出文字會帶有**肉眼不可見的浮水印**，此為回應歐盟《人工智慧法案》（EU AI Act）要求服務歐盟市場的 AI 業者以機器可讀方式標記 AI 生成內容的規定，全球（含台灣）使用者的輸出皆一體適用。

### 運作原理
- 浮水印**不改變文字內容本身**，而是動了大型語言模型逐字生成時「怎麼選都對」的候選詞亂數來源：改用一套含金鑰的演算法依前文決定選字，讀者讀起來自然，但持有 Anthropic 金鑰者事後可驗出該文字出自 Claude 的機率。
- 技術源自 Google DeepMind 2024 年發表於《Nature》的 SynthID-Text；不增加 token、不影響速度與價格，浮水印中也沒有可追溯特定使用者、組織或對話的資訊。

### 偵測邊界（可能驗不出的情況）
- **短文字**、**事實密集段落**（下一個詞只有一個正確答案）、**校對／輕度編輯**（絕大多數字是人寫的）、**程式碼本體**（選擇空間小）。
- 翻譯內容則相反：譯文每個字都是 Claude 選的，通常會帶有浮水印。
- **關鍵限制**：逐字詞替換的完整重寫可使標記消失；驗出浮水印只能證明「Claude 可能參與過」，無法區分「從頭寫的」與「重度編修的」，也驗不出其他公司 AI 生成的文字。

> [!WARNING]
> 部分用戶（含 Claude Max 訂閱者）因擔心自己原創內容經 Claude 校對／翻譯後被驗出參與痕跡，在學術或客戶合約場景可能被誤判為 AI 代寫，已有用戶因此退訂。技術社群亦批評此舉是「合規劇場」（compliance theatre）：坦誠使用 AI 的人被牽連進懷疑範圍，有心規避者徹底改寫一遍即可脫身。

Claude 產生的受支援檔案類型（如 PNG、JPG、SVG）則會附加 **C2PA 內容憑證**，屬於不同機制；2026 年 8 月 2 日前推出的舊版 Claude 模型將於公告後數月內陸續補上浮水印。

---

## 7. 市場地位（a16z 第七版榜單，2026 年 8 月數據）

- **流量**：2023 年 9 月 a16z 首版榜單未進榜，如今網頁流量排第三，超越 DeepSeek 與 Perplexity；但網頁造訪量約為 ChatGPT 的六分之一，手機月活僅 ChatGPT 的十四分之一。
- **付費訂戶**：美國付費訂戶數 2026 年稍早一度超越 Gemini，8 月兩者並駕齊驅。
- **變現策略**：三巨頭中唯一表態不在 Claude 放廣告，消費端以訂閱變現且敢收高價——7.3% 付費用戶選擇月費 100 美元起的 Max 方案（Google、ChatGPT 對應方案僅 1% 出頭）；另有企業 API 收入。
- **警訊**：7 至 8 月全球桌面平均每日使用次數下滑，新增訂戶放緩、流失上升；ChatGPT 訂戶中僅 8% 同時訂閱 Claude。

詳見 [[a16z 第七版生成式 AI 應用榜與變現趨勢]]。

