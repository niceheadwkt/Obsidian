在 AI Agent 與寫碼工具（如 Claude Code, Cursor, Copilot CLI, Gemini CLI 等）的生態系中，**Superpowers**（由 _Jesse Vincent / obra_ 開源）是一個非常熱門且革命性的 Agent 技能與軟體開發方法論套件（Agentic Skills Framework）。

與 Ponytail 主打「極簡與少寫程式碼」不同，**Superpowers 的核心是「極致的紀律與工程規範」**。

它解決了 AI 寫碼常見的缺點——**衝動直接寫 Code、沒有規劃、瞎猜 Bug、寫完不驗證**。安裝 Superpowers 後，AI Agent 會被強制注入一套成熟的軟體工程 SOP，讓 AI 不再自由發揮，而是像經驗豐富的資深架構師與 QA 一樣嚴謹作業。

## 核心工作流：自動觸發的開發五部曲

Superpowers 將開發流程拆解為可組合的 Skill，並由 Router 自動引導 AI 走完以下流程：

1. **頭腦風暴（`brainstorming`）：** 在寫任何程式碼之前啟動。與使用者反覆問答釐清需求、評估替代方案，並產出架構設計文件。
    
2. **隔離工作區（`using-git-worktrees`）：** 自動開立獨立的 Git Worktree 空間與分支，確保開發與測試環境乾淨。
    
3. **編寫計畫（`writing-plans`）：** 將設計拆解為「2~5 分鐘可完成」的極小 Task，每個 Task 包含明確的檔案路徑、精確程式碼與驗證步驟。
    
4. **測試驅動開發（`test-driven-development`）：** 強制執行 **RED-GREEN-REFACTOR**。必須先寫出會失敗的測試（Red）、寫最少程式碼讓測試通過（Green）、最後重構。**完全禁止不寫測試就直接改 Code**。
    
5. **完成前驗證（`verification-before-completion`）：** 拒絕 AI 口頭宣稱「已修復」。必須由 AI 親自執行全新測試或腳本，提出過關數據與證據才能結案。
    

## 核心 Skill 模組分類

|**模組名稱**|**代表 Skill**|**運作邏輯 / 解決痛點**|
|---|---|---|
|**規劃與架構**|`brainstorming`<br><br>  <br><br>`writing-plans`|避免 AI 理解錯誤就亂寫；先把龐大需求切成無痛小任務。|
|**系統化除錯**|`systematic-debugging`|分為 4 階段追蹤。**禁止 AI 憑空瞎猜**，必須重現 Bug、追蹤根因（Root Cause）並驗證。|
|**執行與分工**|`subagent-driven-development`<br><br>  <br><br>`dispatching-parallel-agents`|調度子 Agent（Subagents）並行執行任務，並安排兩階段 Review（規格與品質）。|
|**程式碼審查**|`requesting-code-review`<br><br>  <br><br>`receiving-code-review`|著重安全性、效能、可讀性與測試覆蓋率的自動化 Code Review。|

## 主要優勢

- **提升 Agent 自主性：** Agent 可以連續自主工作數小時，嚴格按照 Plan 執行，不會半途偏離方向或忘記上下文。
    
- **高品質程式碼：** 透過強制 TDD 與嚴格驗證，大幅減少 AI 產出「看似正確實則有漏洞」的幻覺程式碼。
    
- **團隊標準化：** 為團隊內使用 AI Coding 助理建立統一的工作流規範。
    

## 安裝方式

Superpowers 支援多種 AI 工具，可以透過對應 Marketplace 進行安裝：

- **Claude Code:**
    
    Plaintext
    
    ```
    /plugin marketplace add obra/superpowers-marketplace
    /plugin install superpowers@superpowers-marketplace
    ```
    
- **GitHub Copilot CLI:**
    
    Bash
    
    ```
    copilot plugin marketplace add obra/superpowers-marketplace
    copilot plugin install superpowers@superpowers-marketplace
    ```
    
- **Devin CLI / Droid / Grok / Kimi Code / Codex:**
    
    支援透過各自的 Plugin Manager 或官方 Marketplace 搜尋 `superpowers` 進行一鍵安裝。