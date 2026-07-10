---
type: concept
tags: [AIAgent, AntiGravity, 專案管理, 權限設定, Token優化]
sources: [
  "[[raw/2026-06-24T214648+0800-AntiGravity 基本功 EP04一鍵將 Gems 全面升級成 Skill 的終極指南_懶人包大放送.md]]",
  "[[raw/2026-06-25T134848+0800-AI Agent基本功EP01用Agent來學習Agent_一個 GitHub repo，複製我的整套 AI 工作流到你的 Agent.md]]",
  "[[raw/2026-06-25T210734+0800-AI Agent 基本功 EP02：學習 Agent 必懂的核心觀念與初始化設定.md]]",
  "[[raw/2026-06-26T190950+0800-AntiGravity 基本功 EP01Claude Code 與 Codex 的強敵？Google AntiGravity 2.0 實測評價.md]]"
]
created: 2026-06-26
updated: 2026-06-26
---

# AI Agent 與 AntiGravity 2.0 基礎入門

**AI Agent 與 AntiGravity 2.0 基礎入門** 旨在系統化梳理從「雲端生成式 AI（對話式 AI）」轉向「本地端 AI Agent（代理人）」的核心轉變，打通權限設定、記憶初始化與 Token 節約的底層邏輯，並介紹 Google 新一代終端機代理工具 **AntiGravity 2.0** 的實測實務與舊有 Gems 一鍵升級至 Skills 的工作流。

---

## 1. 生成式 AI 與 AI Agent 的本質差異

理解 AI Agent 的第一步，是釐清它與傳統聊天機器人（如網頁版 ChatGPT, Gemini）的根本差別：

*   **雲端生成式 AI (Generative AI)**：所有的輸入與對話運算皆在雲端伺服器完成。AI 主要是個「補全機器」，它只能針對您提供的提示詞（Prompt）輸出回答，不具備與您本地電腦環境直接互動的物理能力。
*   **本地端 AI Agent (智慧代理)**：雖然其推理「大腦」依然在雲端，但其「手腳」被賦予了本地電腦的執行權限。Agent 能夠在您的工作目錄中自動讀寫檔案、呼叫工具、執行終端機命令、除錯並直接進行版本控制（如 Git 提交），是一個具備**自主性**與**執行力**的工作夥伴。

---

## 2. Agent 初始化設定與記憶系統

要讓 Agent 高效運作且不發生混難，必須建立規範性的專案初始化機制：

### 📁 專案資料夾與 Git 設定
1.  **資料夾出發**：AI Agent 的所有工作都基於一個本地的專案資料夾。
2.  **Git 初始化**：在專案開工前，必須執行 `git init`，讓 Agent 能夠透過 Git 追蹤每次的程式碼變更與版本倒帶。
3.  **防禦性 `.gitignore`**：配置排除清單，防止 Agent 在掃描專案時讀入大量無關的快取、依賴檔（如 `node_modules/`）或經常變動的 IDE 配置文件（如 `.obsidian/workspace.json`，參見 [[Git GUI 與 GitHub 雙向同步實務]]），這能大幅降低 Token 的無效消耗。

### 🧠 全域記憶 vs. 專案記憶
*   **全域記憶 (Global Memory)**：記錄您個人跨專案的共用偏好，如個人背景、常用品牌語氣等（參見 [[Claude 高階提示詞與應用場景#情境工程]]）。
*   **專案記憶 (Project Memory)**：在專案根目錄下建立的 `agent.md` 或 `CLAUDE.md`。它作為該專案的專屬操作說明書，記錄了專案的建置指令、測試指令與代碼規範，是引導 Agent 在該目錄下工作的唯一事實來源。

---

## 3. 權限管理與 Bypass 設定 (1-5 級)

Agent 在本地電腦執行指令時，需要取得安全授權。一般 Agent 工具提供五個級別 of 權限設定：

| 授權級別 | 說明 | 適用場景 |
| :--- | :--- | :--- |
| **1-3 級：嚴格/限制模式** | 執行任何檔案讀寫、指令或 MCP 串接前，都必須由使用者手動點擊「允許」或輸入確認。 | 剛接觸 Agent 的新手，或是執行高風險系統級命令時。 |
| **4 級：半自動模式** | 僅針對破壞性指令（如刪除檔案、大範圍覆寫）進行詢問，其餘常規讀寫自動放行。 | 日常開發的推薦模式，兼顧效率與基本安全。 |
| **5 級：Bypass 授權模式** | 授權全開，Bypass 所有權限詢問。Agent 會流暢地自主修改檔案並完成工作，不再反覆中斷對話。 | 已經具備成熟 Git 版本控制（隨時可倒帶）的專案，能將協作效率拉到極致。 |

> [!WARNING]
> 開啟 **Bypass 模式** 雖然效率最高，但 Agent 如果出現幻覺，可能會誤改或刪除重要代碼。務必確保專案已進行 Git 初始化，以便在 Agent 失控時能一鍵回滾（如 `/rewind` 倒帶）。

---

## 4. 上下文窗口與 Token 經濟學

AI 在對話中會隨著對話變長而「越聊越笨」（注意力失焦），且會急遽消耗 Token 額度。掌握以下觀念可有效節流：

1.  **歷史累積負擔**：每次發送新訊息時，Agent 都會將「前文歷史 + 所有載入代碼 + 新 Prompt」打包發送。對話越長，每次交互的 Token 計費便呈指數型上升。
2.  **壓縮對話 (Compaction)**：當某個子任務完成或代碼 Bug 被修復時，適時使用 `/compact` 指令（或在 AntiGravity/Claude Code 中清空對話），只保留關鍵邏輯，釋放上下文空間。
3.  **多對話分工**：不要在同一個對話 Session 中塞入不同的任務。開新對話來處理新功能，利用「小步快跑」維持 Agent 的高精準度（參見 [[Claude 系統優化與 Token 節省指南]]）。

---

## 5. Google AntiGravity 2.0 實測與實務

**AntiGravity 2.0** 是 Google 推出的本地終端機 AI 代理工具，與 Claude Code、Codex 等並列為新一代智慧終端工具。

### ⚙️ 串接與一鍵懶人包安裝
AntiGravity 2.0 支援透過 MCP 協議與 [[Git GUI 與 GitHub 雙向同步實務|GitHub]]、Obsidian 知識庫、Firebase 及 Google [[NotebookLM 綜合指南|NotebookLM]] 進行深度對接。
*   **一鍵懶人包套件**：三師爸打包了全自動環境部署套件 `antigravity-lazy-pack`，使用者只需將此 GitHub Repo 網址：
    `https://github.com/mathruffian-dot/antigravity-lazy-pack`
    直接餵給您的 AntiGravity 2.0 Agent，它便會自動在本地拉取配置、建立環境依賴並完成所有工具的串接設定。

---

## 6. Gems 升級為 Skills 的工作流

在 Google 生態系中，早期的 **Gems（專屬寶石助手）** 已逐漸落伍，因為它本質上仍是一次性問答的對話指令，無法驅動複雜的工作流。而 **Skills（Agent 技能組）** 才是 Agent 時代的標配。

### 🔄 升級套件 `gem-to-agent-kit`
使用者可以透過三師爸提供的開源轉換工具組，一鍵將 Google Drive 上的舊 Gems 升級為進階版的超級 Skills。
*   **工具庫網址**：`https://github.com/mathruffian-dot/gem-to-agent-kit`
*   **工作流步驟**：
    1.  將該 Repo 指向您的工作目錄。
    2.  啟動 AntiGravity 2.0，Agent 將自動讀取、分類並批次合併雲端硬碟中的舊 Gems。
    3.  將其編譯為符合 Agent 規範的 Skill 腳本。

### 🎨 實務示範：跨工具工作流 (Nano Banana Pro)
轉換後的 Skills 可支援複雜的跨工具連動。例如：給出一個故事大綱，Skill 自動呼叫生圖工具 **Nano Banana Pro**（會扣除對應生圖額度）生成三頁一致性角色的語音漫畫網頁，將文字、圖像與語音無縫融合成一個可執行的 HTML 工件。
