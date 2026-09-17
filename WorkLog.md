# 工作筆記

**更新日期**：2026-09-17

## 上次做到哪
- **Wiki 第二十一批 Ingest 完成**：匯入 `SRC-235`（AI Agent 教學應用：放大你的專業能力，輕鬆生成段考試卷），更新 `[[Wordwall 與教育科技的 AI Agent 自動化實務]]` 頁面新增「多 Agent 段考出題自動化實戰」章節，並同步 `index.md`、`log.md`。
- **多 Agent 全域規範與跨電腦同步體系建立 (chezmoi & GitHub)**：
  - 將 Antigravity、Claude Code、Codex 三大工具的全域規範統一（包含開工、收工、Edge-TTS 語音播報、語音輸入錯字校正）。
  - 使用 `chezmoi` 範本（`{{ .chezmoi.homeDir }}`）管理三方規則與 PowerShell Profile，相容公司電腦與家裡筆電（NB）。
  - 將變更全數推送到 GitHub `niceheadwkt/dotfiles`，家裡 NB 只需執行 `chezmoi update` 即可完成同步。
  - 完成《AI Agent 基本功 EP06 跨 Agent、跨電腦協作同一個專案》重點精華摘要，已整理追加至 `chezmoi.md` 與對應原始文獻中。
- **工安稽查單號 1150504015 誤植資料刪除案 (RQ11508035)**：
  - 完成 `HGJJG01` 全系統關聯資料表探索與異動申請表 ODT 產出。

## 相關筆記連結
- [[chezmoi]]
- [[AI/wiki/AI Agent 實戰與 MCP 伺服器整合]]
- [[HGJJG01_稽查單號_1150504015_資料關聯與刪除計畫]]

## 下一步
- 回到家裡筆電執行 `chezmoi update` 驗證三方 AI CLI / IDE 規則是否順暢生效。
- 待工安稽查單號 1150504015 ODT 申請表內部簽核後，於維護時段至正式機執行備份與刪除。

---

## 資料摘要：AI Agent 教學應用－放大你的專業能力，輕鬆生成段考試卷

**更新日期**：2026-09-17
**來源**：`[[AI/raw/2026-09-17T082024+0800-AI Agent 教學應用：放大你的專業能力_輕鬆生成段考試卷.md]]`（三師爸直播影片逐字稿，2026-09-07 發布）

### 核心主題
以數學段考出題為例，示範如何用 AI Agent（而非傳統生成式 AI）取代出題過程中繁瑣的文書工作，把省下的時間留給真正的專業（審題），並同場橫向比較 OpenCode（免費 Muse Spark 1.3 Free）、AntiGravity（Gemini 3.8 Flash）、Codex（Astra）三款 Agent 的生成品質。

### 出題兩大痛點與解法
- **方程式編輯器**：改用 Word 的 `OMML` 格式，讓 Agent 直接生成正確排版的數學方程式；網頁版則對應使用 `MathML`。
- **幾何圖形繪製**：改由 Agent 用 Python 現場計算、繪圖後直接插入 Word（Codex 甚至可輸出 SVG 向量圖），不再需要學 GGB、MyViewBoard 等繪圖工具。

### 操作流程（可複製的 SOP）
1. 準備教材：下載書商（如康軒）備課用書 PDF（課本＋習作），以及一份自己出過的舊段考試卷（作為格式範本）。
2. 讓 Agent 讀取教材與舊卷，建立「檔案索引」與「考卷格式規格」兩份 Markdown，供專案內所有 Agent 共用。
3. 與 Agent 討論並確認考卷規格：以 Bloom 認知層次（記憶／理解／應用／分析）控制難度分布、方程式用 OMML、幾何圖形用 Python 繪製。
4. 請最聰明的模型（示範中為 Astra）產出一份完整「出題提示詞」，供三個 Agent 共同使用。
5. 三個 Agent 平行生成 Word 三件套：題目卷、答案卷、教師解答，並自動輸出命題雙向細目表。
6. 人力只需專注在最後的審題與細修，省下「從 0 到 1」的出題耗時。

### 三家 Agent 實測比較
- **AntiGravity**：速度最快、非選題品質最佳（評為完成度最高，約 80 分水準）。
- **Codex（Astra）**：圖形最精準、可直接輸出 SVG 向量圖，適合需要 AI 生圖（情境圖、地理／歷史圖片）的科目；作者已將主力 Agent 從 Claude Code 轉為 Codex。
- **OpenCode（Muse Spark 1.3 Free）**：免費模型（Meta），仍有 100 萬上下文與多模態能力，出圖與排版效果令人驚艷，代價是對話紀錄會被用於訓練。

### 額外分享：Math Review Deck 技能
作者將「國中數學全六冊互動視覺化複習網頁」框架整理成一個公開 GitHub 技能（Math Review Deck）：左側概念、右側圖形，支援滑桿互動、內建畫筆／雷射筆／橡皮擦等課堂教具，方程式以 MathML 正確顯示，可魔改套用至其他科目。

### 核心觀點
AI Agent 是「放大你專業能力的工具」，而非取代專業；使用者必須帶著自己的教學專業去對話（而非空泛提問），才能換得真正有價值的產出（Garbage in, garbage out）。
