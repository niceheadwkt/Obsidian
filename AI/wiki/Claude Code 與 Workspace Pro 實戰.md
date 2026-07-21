---
type: concept
tags: [ClaudeCode, Workspace-Mode, 一桌三櫃, 軟體架構, 專案管理, Prompt-Library]
sources:
  - "[[raw/2026-07-08T160415+0800-Claude Code提示詞懶人包！52組指令一次整理，工程師、PM、設計師都適用.md]]"
  - "[[raw/2026-07-20T150840+0800-Claude基本功EP10新手從零開始你的專案-使用Claude code來寫教學應用程式_從小白到高手的進階分水嶺：掌握專案管理的「一桌三櫃」法.md]]"
  - "[[raw/Claude_Workspace_Mode_使用說明.md]]"
  - "[[raw/Claude_Workspace_Pro_設計指南.md]]"
  - "[[raw/Software_Architect_v1.0_繁體中文.md]]"
  - "[[raw/Software Architect Workspace Pro v2.0製作方式.md]]"
created: 2026-07-20
updated: 2026-07-20
---

# Claude Code 與 Workspace Pro 實戰

本頁面聚焦於 Anthropic 終端代理 **Claude Code CLI** 的進階應用，以及在大型專案開發中如何藉由模組化架構（**Software Architect Workspace Pro**）來建置專案上下文，實施正確的「一桌三櫃」專案管理。

---

## 1. Claude Code 52 組官方提示詞懶人包

Anthropic 官方 Prompt Library 收錄了 52 組針對 Claude Code CLI 的精準指令，按軟體生命週期的 5 大階段分類：

1.  **Discover (探索代碼庫)**：
    *   *語法結構*：`定位 X 的實作`、`解釋 X 的依賴與調用鏈`、`找出代碼庫中可能存在性能漏洞的區塊`。
2.  **Design (設計與原型)**：
    *   *語法結構*：`設計一個新模組 X 的架構並產出設計文件`、`提議對 X 模組進行重構的幾種可行性方案`。
3.  **Build (實作、測試與重構)**：
    *   *語法結構*：`替 X 函數補齊邊界測試 (Unit Tests)`、`優化 X 算法的空間複雜度`、`執行程式碼審查 (Code Review) 並提供修改清單`。
4.  **Ship (Git 與版本發佈)**：
    *   *語法結構*：`撰寫本次 Git Commit Message`、`分析兩個分支間的差異並產生 Release Note`。
5.  **Operate (除錯與運維)**：
    *   *語法結構*：`分析生產環境之日誌 (Logs) 並抓出錯誤根源`、`實施資料遷移 (Migration) 自動化腳本`。

---

## 2. 專案管理的「一桌三櫃」升級版 (EP10)

當 AI Agent 處理大型專案時，經常會因為上下文過於混亂而開始「胡言亂語」。正確的**一桌三櫃 (One Table Three Cabinets) 專案管理法**是解決此痛點的核心。

### 2.1 什麼是一桌三櫃？
*   **一桌（工作桌）**：即 `Google Drive 工作桌`（本地同步資料夾），放置當前正在修改、測試的程式碼與主要專案文件。
*   **三櫃（記憶庫分流）**：
    1.  **檔案櫃 (File Cabinet)**：專案備檔與版本控制。
    2.  **規則櫃 (Rule Cabinet)**：如 `.agents/` 或 `CLAUDE.md`，定義 AI 的工作底線。
    3.  **暫存櫃 (Temp Cabinet)**：放置本次會話的 log 與臨時測試腳本，隨時可 compact 丟棄。

### 2.2 EP10 實戰精華 (初始化班級工具工作模式)
在 EP10 實戰中，三師爸示範了開發一個教學應用程式。當專案進入中後期，應上傳專用的初始化說明書檔案（如 `07-初始化班級工具工作模式.md`），使 Agent 自動加載「架構地圖、命名規範與代碼限制」，保持長期記憶不偏離軌道。

---

## 3. Claude Workspace Pro (GPT-5.5) 設計與實務

**Workspace Mode (工作區模式)** 將整個長對話視為「同一個專案」，而非多次獨立問答。這能維持大語言模型在大型專案中的上下文一致性。

### 3.1 核心運作理念
1.  **專案狀態 (Project State)**：每次對話前，模型應在內部更新：當前 Goal、Context、已作出的 Decisions、Roadmap 路線圖、待辦 TODO 與已知風險。
2.  **增量修改 (Incremental Editing)**：禁止每次都重寫全文，預設只輸出 Diff 修改區塊，大省 Token。
3.  **先分析再修改**：要求模型在動手寫程式碼前，必須先分析代碼影響力、依賴關係與潛在破壞性，待使用者確認後再修改。

### 3.2 Software Architect Workspace Pro v2.0 架構
為將「軟體架構師說明書」完全檔案化與版本控制，建議在專案中建置以下目錄結構：

```text
Software-Architect-Workspace-Pro/
├── docs/                     # 1. 架構文件 (唯讀原則)
│   ├── 01_設計理念.md         # DDD 與 Clean Architecture
│   ├── 02_工作流程.md         # Git 與 AI Agent 協作規範
│   └── 06_技術決策(ADR).md    # 記錄技術架構決定
├── prompts/                  # 2. AI 角色指令封裝
│   ├── SystemPrompt.md       # 系統大腦設定
│   ├── CodeArchitect.md      # 代碼架構師
│   └── Reviewer.md           # 審核者指令
├── workspace/                # 3. 專案狀態 (隨時更新)
│   ├── Workspace_State.md    # 專案當前狀態與進度
│   ├── TODO.md               # 待辦清單
│   └── Glossary.md           # 命名術語詞彙表
└── templates/                # 4. 範本格式
    └── Bug_Template.md       # 提 Bug 標準格式
```

### 3.3 技術決策紀錄 (ADR, Architecture Decision Records)
任何架構變更（如資料庫更換、通訊協定變更）皆必須寫入 `docs/06_技術決策(ADR).md`。這使後續加入協作的 AI Agent 能瞬間理解專案底層脈絡，避免給出相左的技術方案。

---

## 4. 延伸閱讀與交叉連結
*   關於如何跨電腦同步一桌三櫃專案資料夾與 chezmoi 技能，請參閱：`[[AI Agent 實戰與 MCP 伺服器整合#2. 跨裝置與多 Agent 專案協作架構]]`。
*   關於 Claude Token 的節流技巧，請參閱：`[[Claude 系統優化與 Token 節省指南]]`。
