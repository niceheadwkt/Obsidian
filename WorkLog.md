# 工作筆記

**更新日期**：2026-09-22

## 上次做到哪
- **ZP `zpjcDailyTriggerWorkNotice`　`{maxPosNo:08}` 模板展開修復（測試、驗證、清理全部完成）**：
  - 詳見 [[AI/ERP/zpjcDailyTriggerWorkNotice_工作筆記]] 與 [D:/CHSBrowser_erp/erpHome/yl.ear/erp.war/zp/zpjcDailyTriggerWorkNotice_TBZP0053_測試報告.md](file:///D:/CHSBrowser_erp/erpHome/yl.ear/erp.war/zp/zpjcDailyTriggerWorkNotice_TBZP0053_測試報告.md)。
  - 測試機驗證通過後，清理 17 筆測試簽核單/工作通知與 48+6 筆 TBDW11 殘留、13 筆 TBZP0053 測試資料。
  - 依同一份修復邏輯，協助重設 3 筆正式機匯入用測試資料（`TBZP0053_v1.txt`：初始值重設、cron 限今日執行），並排除 DSIMPORT 匯入工具的欄位切分 bug（字串區隔字元需改用 `%`）。
- **EA `(EAJJLICENSEBAT)` 證照整批新增版次作業　操作手冊建置**：
  - 讀 [eajjLicenseBat.jsp](file:///D:/CHSBrowser_erp/erpHome/yl.ear/erp.war/ea/jsp/eajjLicenseBat.jsp)／[eajjLicenseBatM1.jsp](file:///D:/CHSBrowser_erp/erpHome/yl.ear/erp.war/ea/jsp/eajjLicenseBatM1.jsp)／[eajcLicenseBat.java](file:///D:/CHSBrowser_erp/erpHome/yl.ear/erp.war/ea/src/com/chsteel/ea/eajcLicenseBat.java)／[eajcLicense.java](file:///D:/CHSBrowser_erp/erpHome/yl.ear/erp.war/ea/src/com/chsteel/ea/eajcLicense.java) 原始碼，整理成使用者操作角度的 md＋PDF 手冊。
  - PDF 產製踩坑：Chrome headless `--print-to-pdf` 對特定中文字型有已知 bug，會把常用字（如「手」）誤對應成康熙部首碼（U+2F80~U+2FDF 區段），改用 reportlab 內嵌微軟正黑體字型重新產生，逐頁掃描確認無部首誤植字元。
  - 手冊補上正式機實際畫面截圖，並將證書號碼／專責人員／證照名稱／證照原始號碼等個資欄位事後遮蔽處理。
- **Obsidian 筆記庫跨電腦分岐合併**：解掉 `WorkLog.md`／`AI/wiki/log.md`／`AI/wiki/index.md`／一篇 `AI/raw/` 逐字稿共 4 個檔案的真實 Git 合併衝突（兩台電腦各自獨立新增的內容，非格式問題），保留雙方各自獨有內容後推送成功。

## 相關筆記與腳本連結
- [[AI/ERP/zpjcDailyTriggerWorkNotice_工作筆記]]
- [[AI/raw/2026-09-20T174500+0800-SogaType語音輸入操作踩坑與排錯實戰全紀錄]]
- [[AI/raw/NoType 專案深度分析與演進建議書]]

## 下一步
- ZP：正式機那 3 筆測試資料實際匯入、觸發驗證後，記得清理正式機產生的簽核單／工作通知殘留（比照測試機作法，勿用裸 SQL）。
- EA：`EAJJLICENSEBAT` 操作手冊如需交付其他同仁，確認遮蔽後的截圖與內容是否符合需求。
- SogaType／NoType 相關待辦沿用 [[AI/raw/2026-09-20T174500+0800-SogaType語音輸入操作踩坑與排錯實戰全紀錄]] 內容，尚未進一步跟進。

---

## [歷史紀錄 2026-09-20] SogaType 語音輸入除錯與 NoType 專案分析

- **SogaType 語音輸入操作踩坑與 Windows 底層除錯全紀錄**：
  - 診斷出 ASUS ROG Zephyrus G14 內建麥克風陣列在 Windows CoreAudio 處於 `0x2`（`DEVICE_STATE_DISABLED`）狀態，致 WinMM `waveInGetNumDevs() == 0`，引發 SogaType `NAudio BadDeviceId` 崩潰。
  - 運用 Windows 未公開 COM 介面 `IPolicyConfig::SetEndpointVisibility` 成功將端點復原為 Active（`0x1`），WinMM 順利收音 32,000 bytes。
  - 釐清實體鍵盤 F8 受 ASUS Hotkey 控制為調高亮度（需按 `Fn + F8`）及 `Ctrl + Space` 與輸入法切換相撞失焦之問題。
  - 查明 SogaType 識別成功卻無法在終端機自動貼上文字的根因：Windows UIPI（使用者介面權限隔離）——以管理員身分執行的 Windows Terminal 阻擋了一般權限 SogaType 發送的 `keybd_event(Ctrl + V)`。
  - 完成完整踩坑實戰技術文件：[AI/raw/2026-09-20T174500+0800-SogaType語音輸入操作踩坑與排錯實戰全紀錄.md](file:///C:/Users/niceh/我的雲端硬碟/Obsidian/AI/raw/2026-09-20T174500+0800-SogaType語音輸入操作踩坑與排錯實戰全紀錄.md)。
- **NoType 專案深入分析與架構演進建議書**：
  - 針對 `C:\aiTest\NoType` 進行全專案架構分析，比對 SogaType 優缺點。
  - 完成建議書 [AI/raw/NoType 專案深度分析與演進建議書.md](file:///C:/Users/niceh/我的雲端硬碟/Obsidian/AI/raw/NoType%20專案深度分析與演進建議書.md) 並同步備份於 [C:/aiTest/NoType/IMPROVEMENT_PROPOSAL.md](file:///C:/aiTest/NoType/IMPROVEMENT_PROPOSAL.md)。
  - 制定台灣客製化詞庫策略（Whisper Prompt 注入 + LLM 系統提示詞雙層過濾機制；前期使用輕量 JSON / `store.js`，後期採用純 JS Trie 字典樹，避免破壞跨平台純 Node 架構）。
- **四大 AI Agent 技能共享與 NTFS Junction 架構整定（家用 NB 實裝完成）**：
  - 於本機建立中央真相來源 `~/.agents/skills/`，集中管理 7 個核心自訂技能。
  - 落地新機一鍵冷啟動萬能腳本至 [AI/scripts/bootstrap-skills.ps1](file:///C:/Users/niceh/我的雲端硬碟/Obsidian/AI/scripts/bootstrap-skills.ps1)。

### 當時的下一步（供對照）
- 深入研究 NoType 專案架構，評估實作台灣專用詞庫與兩岸用語對照（雙層過濾機制）。
- SogaType 操作注意事項：若需在管理員權限終端機輸入，需以系統管理員權限啟動 SogaType，或以 `Ctrl + V` 手動貼上剪貼簿。
- 於公司 NB 執行 `chezmoi update` 驗證全域設定與腳本同步狀態。

---

## [歷史紀錄 2026-09-17] 跨電腦與跨 Agent 全域規範同步體系建立／工安稽查單號 1150504015

- **Wiki 第二十一批 Ingest 完成**：匯入 `SRC-235`（AI Agent 教學應用：放大你的專業能力，輕鬆生成段考試卷），更新 `[[Wordwall 與教育科技的 AI Agent 自動化實務]]` 頁面新增「多 Agent 段考出題自動化實戰」章節，並同步 `index.md`、`log.md`。
- **多 Agent 全域規範與跨電腦同步體系建立 (chezmoi & GitHub)**：
  - 將 Antigravity、Claude Code、Codex 三大工具的全域規範統一（包含開工、收工、Edge-TTS 語音播報、語音輸入錯字校正）。
  - 使用 `chezmoi` 範本（`{{ .chezmoi.homeDir }}`）管理三方規則與 PowerShell Profile，相容公司電腦與家裡筆電（NB）。
  - 將變更全數推送到 GitHub `niceheadwkt/dotfiles`，家裡 NB 只需執行 `chezmoi update` 即可完成同步。
  - 完成《AI Agent 基本功 EP06 跨 Agent、跨電腦協作同一個專案》重點精華摘要，已整理追加至 `chezmoi.md` 與對應原始文獻中。
- **工安稽查單號 1150504015 誤植資料刪除案 (RQ11508035)**：
  - 完成 `HGJJG01` 全系統關聯資料表探索與異動申請表 ODT 產出。

### 相關筆記連結（當時）
- [[chezmoi]]
- [[AI/wiki/AI Agent 實戰與 MCP 伺服器整合]]
- [[HGJJG01_稽查單號_1150504015_資料關聯與刪除計畫]]

### 下一步（當時，供對照）
- 回到家裡筆電執行 `chezmoi update` 驗證三方 AI CLI / IDE 規則是否順暢生效。
- 待工安稽查單號 1150504015 ODT 申請表內部簽核後，於維護時段至正式機執行備份與刪除。

> 註：以上為 2026-09-17 在另一台電腦上的工作紀錄，因兩邊分別新建 `WorkLog.md` 未即時同步而分岐，2026-09-22 合併時保留於此作為歷史紀錄，最新狀態請見本檔最上方「上次做到哪」。

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
