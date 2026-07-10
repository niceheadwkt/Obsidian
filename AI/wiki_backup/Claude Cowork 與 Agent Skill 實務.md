---
type: concept
tags: [Claude, ClaudeCowork, AgentSkills, AI工作流, Excel自動化]
sources: [
  "[[raw/2026-06-15T152529+0800-Claude桌面版三大模式：Chat、Cowork、Code差在哪？.md]]",
  "[[raw/2026-06-15T154818+0800-Claude Cowork是什麼？Cowork教學：簡報、報帳、整理雲端硬碟5個超實用場景.md]]",
  "[[raw/2026-06-15T154838+0800-同事都在用AI做事？Claude Cowork完整教學，教你一步步打造AI Agent超強工作流.md]]",
  "[[raw/2026-06-15T154903+0800-丟掉提示詞吧！Cowork實戰技巧：建立核心資料夾、把背景知識寫成.md檔，4步驟操作一次學.md]]",
  "[[raw/2026-06-15T154950+0800-Claude Cowork實測：20分鐘產出100頁PPT！也可以修改.md]]",
  "[[raw/2026-06-15T155042+0800-如何用Claude Cowork做Excel？教學：一段提示詞從零生成700條公式.md]]",
  "[[raw/2026-06-15T155155+0800-Agent Skills懶人包｜Agent Skills格式、範例，跟GPT或Gem有什麼差異？.md]]",
  "[[raw/2026-06-15T155211+0800-Agent skill 是什麼？Agent skill教學，6步驟打造你的第一個Skill.md]]",
  "[[raw/2026-06-15T155239+0800-Claude Skills是什麼、怎麼用？新手零基礎入門教學，不用每次重貼提示詞.md]]",
  "[[raw/2026-06-15T155546+0800-實測｜我用Skill把AI訓練成專屬助理，報帳、資料整理都超快！.md]]",
  "[[raw/2026-06-15T155632+0800-X上爆紅的26個Skill！賈伯斯、卡帕西的思維都能「蒸餾」、還能算命，完整清單一次收.md]]",
  "[[raw/2026-06-15T155655+0800-不會Claude Code也能上手！用Projects打造AI工作流，5步驟養成長期記憶助理.md]]",
  "[[raw/2026-06-15T154424+0800-Claude地圖｜Cowork、Claude Code是什麼？初階者從哪開始學？進階技巧有哪些？.md]]"
]
created: 2026-06-15
updated: 2026-06-15
---

# Claude Cowork 與 Agent Skill 實務

**Claude Cowork 與 Agent Skill 實務** 探討了 Anthropic 旗下大模型在自動化代理協作（Cowork）與客製化技能擴充（Agent Skills）領域的應用。本篇旨在引導使用者擺脫單一的問答模式，透過建立無提示詞專案架構、自動化辦公流程及客製化 Skills，建立高自主性的 AI Agent 協作工作流。

---

## 1. Claude Desktop 三大工作模式解析

官方桌面應用程式 (Claude Desktop App) 整合了三種完全不同定位的交互模式：

1.  **Claude Chat (常規對話)**：
    *   **定位**：一對一問答。適合簡單寫作、代碼單點解釋、臨時資訊查詢。
2.  **Claude Cowork (自主代理協作)**：
    *   **定位**：具備 Agent 自主規劃能力。能夠讀取您指定的整個專案資料夾，並透過背景排程自主拆解任務、執行文件處理、建立多步驟工作流，且支援 API 與 Connectors 連線（如 Gmail）。
3.  **Claude Code (終端開發 CLI)**：
    *   **定位**：終端機原生 Agent。直接在 CLI 環境中讀寫代碼、編譯、執行本地測試、修復 Bug 並自動撰寫 Git 提交。

*(關於初學者的學習地圖與進階技巧大綱，請參見 [[raw/2026-06-15T154424+0800-Claude地圖｜Cowork、Claude Code是什麼？初階者從哪開始學？進階技巧有哪些？.md|Claude 學習地圖與進階技巧指南]])*

---

## 2. Claude Cowork 實戰與「免提示詞」工作流

傳統在使用 AI 處理大型任務時，每次開啟新對話都需要貼上成堆的 System Prompts 或規則指引，既繁瑣又容易使上下文混亂。

### 🛠️ 「免提示詞」(No-Prompt) 實戰四步驟
透過以下工作流，可以讓 Cowork 專案自動索引上下文，實現「丟掉 Prompt」的高效運作：
1.  **建立核心資料夾**：在電腦中建立專案專屬目錄。
2.  **撰寫背景說明書**：將專案的背景知識、命名風格指南、API 串接文檔或簡報大綱，分別撰寫成數個獨立的 Markdown（`.md`）檔案置於該資料夾下。
3.  **啟動專案關聯**：在 Claude 桌面版的 Cowork 中建立新專案，並指向該資料夾。
4.  **自然語言引導**：此時直接使用白話文對話。Claude 會自動在後台索引並讀取這些 Markdown 檔案作為背景，無須您手動貼上任何提示詞。

### 📈 超強商務應用場景
*   **20分鐘產出百頁 PPT**：在 Cowork 專案中關聯大綱與簡報 Spec 檔，AI 能在 20 分鐘內自主分析、排版並輸出多達 100 頁的簡報 Markdown 大綱與佈局。
*   **自動報帳與檔案整理**：讓 Cowork 自動掃描發票資料夾，辨識 CSV 數據並歸類整理至指定雲端目錄。
*   **Excel 巢狀公式自動生成**：
    > **實戰 Prompt**：「請幫我分析這張銷售數據表，並從零生成適用於 A2 到 A700 欄位的高難度巢狀 VLOOKUP 與 IF 判斷公式。請直接在 Excel 的 API 環境中完成寫入與測試，確保無 `#VALUE!` 錯誤。」

---

## 3. Agent Skills 核心技術：打造專屬 AI 助理

### ❓ 什麼是 Agent Skill？
**Agent Skill** 是 Anthropic 專門為 AI 代理設計的「技能擴充模組」。它將一組特定任務的指令、所需的工具（Tools）與代碼執行權限打包在一起，使 AI 可以像人類一樣「學會」新技能。

### ⚖️ 與 GPTs / Gems 的本質差異
*   **GPTs / Gems**：本質上是「靜態的 System Prompt 包裹」，AI 僅在對話框內依據提示詞變更語氣或調用固定的 web search 插件，無法觸及本地環境。
*   **Agent Skills**：具備**本地自主執行力**。一個 Skill 可以包含本地 Python 腳本、API 密鑰調用與 terminal 命令執行權限，使 AI 在 CLI 或 Cowork 中能真正讀寫本地檔案並調用外部系統進行自動化操作。

### 🛠️ 6 步驟打造您的第一個自訂 Skill
1.  **明確技能任務**：定義 Skill 要解決的特定痛點（例如：一鍵將代碼打包並壓縮）。
2.  **設計 Skill 指令**：編寫引導 AI 執行的 Prompt 規則。
3.  **宣告工具調用**：定義該 Skill 需要調用哪些本地編譯器、指令或 API。
4.  **建立設定檔**：在本地配置目錄（如 `.claudecode/skills/`）下建立 Skill 定義文件。
5.  **終端機註冊**：於 Claude Code CLI 中載入並完成技能註冊。
6.  **高頻調用測試**：此後，您只需在終端機輸入「執行【技能名稱】」，AI 便會自主完成整套工作流，無須每次重新貼指令。

### 🌟 X (Twitter) 爆紅的 26 個 Skill 盤點
在開發者社群中，有許多被熱烈討論的 Skill，例如：
*   **賈伯斯/卡帕西思維蒸餾**：讓 AI 模擬大師的直覺進行產品美學或代碼結構審查。
*   **自動代碼審核 (Auto Code Reviewer)**：自動掃描 Git Diff 並指出潛在的記憶體洩漏與邏輯 Bug。
*   **自動週報生成器**：自動讀取本週 Git Commits 歷史，一鍵生成繁體中文的工作週報。

---

## 4. 免程式碼 Projects 工作流

若您是非技術背景的商務或行銷人員，可善用 claude.ai 網頁版的 **Projects** 功能，以 5 步驟養成長期記憶助理：

1.  **建立 Project**：在網頁端點選 Projects 建立專案。
2.  **上傳核心背景 (Project Knowledge)**：上傳公司產品規格書、風格指南或常用郵件範本。
3.  **配置全局 Instructions**：在 Project 設定中寫入全域提示詞（例如：「請永遠使用繁體中文，且排版需符合行銷團隊的簡約風格」）。
4.  **開展對話與更新**：在專案內開啟不同的對談。若產品規格有更新，隨時在 Project Knowledge 中替換檔案，確保**單一事實來源**。
5.  **接續記憶**：每次開新 Session，Claude 都會自動繼承 Project 內的所有知識檔案，擁有長期的專案記憶，不會因為對話清除而「失憶」。

*(可交叉參考：[[AI 第二大腦與 Claude Cowork 自動化]])*
