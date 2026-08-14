---
type: concept
tags: [AI-Agent, 基礎入門, MCP, 專案管理, RDQ, 跨電腦同步]
sources: 
  - "[[sources/2026-07-28T064848+0800-AI Agent基本功EP01用Agent來學習Agent_一個 GitHub repo，複製我的整套 AI 工作流到你的 Agent.md]]"
  - "[[sources/2026-07-28T070734+0800-AI Agent 基本功 EP02：學習 Agent 必懂的核心觀念與初始化設定.md]]"
  - "[[sources/2026-07-28T081508+0800-AI Agent 基本功 EP03：一句話讓 AI 幫你讀檔、寫程式、上網、做出成品.md]]"
  - "[[sources/2026-07-28T081524+0800-AI Agent 基本功 EP04：連接外部工具，MCP 與連接器一張地圖講清楚.md]]"
  - "[[sources/2026-07-28T082604+0800-AI Agent基本功 EP05三層一次講清楚 搞定 技能全域專案.md]]"
  - "[[sources/2026-07-28T083320+0800-AI Agent 基本功 EP06 跨 Agent、跨電腦協作同一個專案，設定觀念一次到位.md]]"
  - "[[sources/2026-07-28T084017+0800-AI Agent 基本功EP07需求探索四象限法，釐清專案需求的最後一塊拼圖.md]]"
created: 2026-08-07
updated: 2026-08-07
---

# AI Agent 基本功系列實踐指南 (EP01-EP07)

本指南根據三師爸 [[Claude 基本功與個人 AI 工作流實戰|三師爸 (Sense Bar)]] 的「AI Agent 基本功」EP01 至 EP07 系列教學整理，旨在幫助開發者與非技術人員打通 AI Agent 的核心觀念與本地環境配置，不分工具（如 Claude Code, Codex, OpenCode, AntiGravity 等）均能一體適用。

## EP01：用 Agent 來學習 Agent 與知識庫複製
- **雲端 AI 與本地 Agent 的差異**：
  - **生成式 AI**（如 ChatGPT Web）：僅能接收 Prompt 並在雲端生成文字，無法直接與使用者的本地系統互動。
  - **AI Agent**（如 AntiGravity）：具有執行命令、讀寫檔案、呼叫工具等「手腳」，可以直接在使用者電腦上產出成品。
- **快速複製工作流**：
  - 透過 GitHub 倉庫 [sensebar-agent-knowledge-vault-builder](https://github.com/mathruffian-dot/sensebar-agent-knowledge-vault-builder) 可以一鍵複製整套 AI 知識庫建置與 Ingest 工作流。

## EP02：核心觀念與初始化設定
- **權限控制 (Permissions)**：
  - 分為半自動模式（需要使用者每次確認執行指令，適合新手）與 Bypass 模式（AI 自動執行指令，適合老手與受信任指令）。
- **初始化與記憶**：
  - 專案初始化的首要步驟是 `git init`，讓 Git 追蹤程式碼變更。
  - 使用 `.gitignore` 排除大檔案或敏感設定檔（例如 `workspace.json`、`.env` 等）。
  - 設定專案專屬的記憶與規範規則檔案（如 `agent.md` 或 `CLAUDE.md`）。

## EP03：Agent 的四隻手腳（讀檔、寫程式、上網、產生成品）
- **讀檔與寫檔**：Agent 能在授權目錄下讀取多種格式文檔，並直接編輯或新增程式碼檔案。
- **代碼執行與上網**：藉由安全沙箱（如 `ava_sandbox`）或本地執行環境，AI 能夠編譯、調試程式碼，並使用 Playwright 等工具上網抓取即時資訊，實時調整策略。

## EP04：連接外部工具與 MCP 通道
- **連接前評估**：
  1. 是否為 Google 生態系（如 Tasks, Gmail, Classroom）？
  2. 需要簡單使用（唯讀/快照）還是完整控制（雙向同步/修改）？
- **四種連接通道**：
  - **內建連接器**：原廠寫好的原生 API。
  - **Model Context Protocol (MCP)**：開源的統一協議標準，便於將任何本地/雲端資料源轉換為 Agent 可以使用的 Tools。
  - **CLI (命令列)**：透過終端機執行第三方 CLI 工具。
  - **畫面操控**：透過模擬瀏覽器點擊與輸入。

## EP05：三層架構（技能、全域、專案）
- **技能 (Skills)**：以 Markdown 格式撰寫的使用說明書，告訴 Agent 如何呼叫內部工具與外部通道執行特定複雜任務。*注意：別人寫好的技能需依自己的本地環境進行路徑與參數微調。*
- **全域設定 (Global)**：每次對話皆會載入的通用偏好設定（如：chezmoi 或 Windows 語音朗讀）。
- **專案設定 (Project)**：僅針對當前專案資料夾生效的局部規則。

## EP06：跨裝置與跨 Agent 專案協作
- **雲端硬碟同步**：
  - 將專案建立於雲端硬碟本地端應用程式同步的目錄（如 Google Drive 的 G:\\ 槽），而非網頁版，使多台實體電腦與不同的 Agent 程式能共享同一個專案實體檔案。
- **設定檔與技能同步**：
  - 使用 `chezmoi` 管理工具在多台 PC 之間同步全域 dotfiles（如 `chezmoi.md` 指南）與 Agent Skills，確保多台機器上的 Agent 表現一致。

## EP07：需求探索四象限法 (RDQ)
- **RDQ (Requirements Discovery Quadrant)**：
  - 釐清專案需求時，人類通常只能表達「你知道你知道的」與「你知道你不知道的」前兩個象限。
  - 後半部的「你不知道你知道的」與「你不知道你不知道的」需要依靠 Agent 透過引導式問答（例如「用 RDQ 問我」，AI 引導最多 3 個追問）來挖掘，從而避免最終產出與期望不符。

---

## 延伸實務應用專題
- **無 API 平台自動化 (EP04 延伸)**：針對無官方 API/MCP 的平台（如 Wordwall、LoiLoNote），採用 Playwright 封裝為 CLI，實現三級自動出題。詳見 `[[Wordwall 與教育科技的 AI Agent 自動化實務]]`。
- **雲端排程與 GAS 閉環**：結合雲端 24/7 常駐 Agent 與本地 `clasp` 部署。詳見 `[[Google Spark 與 GAS 雲端自動化實務]]`。
- **跨平台 Agent 新版實踐**：跨模型與平價高智力架構。詳見 `[[OpenCode 新版架構與模型最佳搭配指南]]`。

