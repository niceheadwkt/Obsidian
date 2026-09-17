> [!NOTE]
>  (輸入：/agy-customizations)

 
Google Antigravity 客製化系統 (Customization System) 指南！

  透過客製化系統，您可以將 Antigravity 從通用的 AI 助理轉化為熟悉您專案架構、開發規範與自動化流程的專屬結對工程師 (Pair Programmer)。
  ──────
  ### 一、五大客製化類型速查表

  依據您的需求目標，挑選合適的客製化方式：
   客製化類型                       | 設定檔案 / 目錄                      | 生效範圍                        | 核心用途與適用情境
  ----------------------------------|--------------------------------------|---------------------------------|------------------------------------------------------------------------------------------------
   規則 (Rules)                     | GEMINI.mdAGENTS.md.agents/rules/*.md | 目錄層級繼承 / 上下文注入       | • 強制規範編碼風格、命名原則• 限制敏感 API 或特定目錄操作• 設定專案架構與全域規範
   技能 (Skills)                    | skills/<名稱>/SKILL.md               | 按需載入 (On-Demand)            | • 傳授多步驟標準作業程序 (SOP)• 特定除錯、分析或建置流程• 平時不佔用 Context，觸發時才載入
   外掛 (Plugins)                   | plugins/<名稱>/plugin.json           | 模組化打包 (Bundle)             | • 將相關的技能、規則與 MCP 設定打包成單一套件• 方便團隊跨專案共享與版本控管
   鉤子 (Hooks)                     | hooks.json                           | 生命週期事件觸發                | • 在 Agent 生命週期特定時間點執行自訂腳本• 例如：工具呼叫前檢查、檔案寫入後自動 Linter
   MCP 伺服器                       | mcp_config.json                      | 外部工具整合                    | • 透過 Model Context Protocol 串接外部服務• 例如：內部 API、資料庫直連、Obsidian、Google Tasks
  ──────
  ### 二、檔案配置目錄與載入優先級

  Antigravity 會自動遍歷並掛載您的客製化設定：

  #### 1. 探索路徑 (Discovery Locations)

  • 專案工作區 (Project-Specific)：
      • 路徑：專案根目錄下的 .agents/、.agent/、GEMINI.md 或 AGENTS.md。
      • 適用：團隊協作、隨 Git 版本庫進行版本控制。
  • 全域設定 (Machine-Local)：
      • 路徑：~/.gemini/config/（Windows 位於 C:/Users/<使用者>/.gemini/config/）。
      • 適用：跨所有專案通用的個人習慣、預設規則與常用 MCP。


  #### 2. 載入優先順序 (Priority Order)

  當名稱或規則發生衝突時，載入優先級由高至低如下：

  1. 🥇 工作區專案自訂（從目前工作目錄向上查找到 Git 根目錄）
  2. 🥈 工作區宣告檔（專案內的 skills.json、plugins.json）
  3. 🥉 全域使用者設定（~/.gemini/config/）
  4. 🎖️ 系統內建客製化（Built-in，隨應用程式內建）
  5. 🏅 全域宣告檔（全域 JSON 註冊項目）
  ──────
  ### 三、關鍵運作機制

  │ Tip
  │ 漸進式揭露 (Progressive Disclosure)
  │ 為了節省 Context 視窗並維持回答精準度，技能 (Skills) 與設定為條件觸發的規則不會預先載入全文，系統僅向模型注入其名稱與簡述。只有當對話觸發相關任務或您手動啟用時，詳細步驟與資源才會被動態讀取。
  ──────
  ### 🛠️ 您接下來想進行哪項設定？

  請告訴我您的需求，我可以立即為您生成範本或實作：

  6. 建立專案規範：為目前專案建立 GEMINI.md 規則檔（規範語言、架構風格、Git Commit 流程等）。
  7. 新增客製技能 (Skill)：建立新的 SKILL.md（編寫多步驟自動化或特定分析 SOP）。
  8. 擴充外部工具 (MCP)：在 mcp_config.json 中配置新的 MCP 伺服器整合。
  9. 生命週期自動化 (Hooks)：設定工具執行前/後的自訂執行腳本。