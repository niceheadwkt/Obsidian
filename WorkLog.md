# 工作筆記

**更新日期**：2026-09-20

## 上次做到哪
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

## 相關筆記與腳本連結
- [[AI/raw/2026-09-20T174500+0800-SogaType語音輸入操作踩坑與排錯實戰全紀錄]]
- [[AI/raw/NoType 專案深度分析與演進建議書]]
- [[AI/raw/如何看四大工具的目錄連結（NTFS Junction）]]
- [[AI/raw/CROSS_AGENT_SKILLS_SHARING_PLAN]]
- [[AI/scripts/bootstrap-skills.ps1]]

## 下一步
- 深入研究 NoType 專案架構，評估實作台灣專用詞庫與兩岸用語對照（雙層過濾機制）。
- SogaType 操作注意事項：若需在管理員權限終端機輸入，需以系統管理員權限啟動 SogaType，或以 `Ctrl + V` 手動貼上剪貼簿。
- 於公司 NB 執行 `chezmoi update` 驗證全域設定與腳本同步狀態。

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
