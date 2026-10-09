# 工作筆記

**更新日期**：2026-10-09

## 上次做到哪
- **2026-10-09 RQ11510012 風險評估系統優化：規劃設計 v0.3 與待確認清單**：
  - 查程式：EAJJRE00N【新增】按鈕無任何管制（一律顯示、只檢核部門與說明必填、評估代碼未檢核）；EAJJRE20N【預估評估】管制整理（畫面 `isCanExecuteHrisk()`＋建立人＋狀態；後端 `doEstimate()` 只檢查建立人與日期，未再呼叫 `isCanExecuteHrisk()`）。
  - 評估 R4「新版複製時就執行預估評估」違反「第一階段須簽核完成」規則，且 `doConfirm()` 會把 RE04 重設成 `10` 卡死按鈕；改採**方案 B：延到風險評估核准（`eajcRE00CRN.agree()` 變 E）時才自動移轉＋預估評估**，衍生問題 B1～B13 寫入規劃文件 3.4.5。
  - `TBEAWORKDOCEX.field7` 確定 10 碼：追蹤列改為 field1 放關聯文號、field7 放移轉日，CP 前綴用途更正為防止主鍵撞號，srlNo 補 4 碼。
  - 正式機唯讀查詢（3.4.7）：高風險列 2,031 筆，`getWorkDocNumber()` 跨序號錯號 0 筆（bug 未觸發，仍建議修正）；flow1Code 有尾端空白（如 `03 `），不可 trim；同版次多文號 397 組皆為 2026/03 前舊流程資料，2026/04 起 0 組，「舊文號」定義為最新版次 WorkDocID 最大者（與最新B表 `HR_LATEST` 一致）。
  - 產出給申請人蔡侑儒的待確認清單（Q13 執行時間點、Q14 舊文號鎖住、Q11 預估完工日過期）：[[AI/ERP/RQ11510012_待確認事項_Q11_Q13_Q14]] 與同名 .docx（本機 Word 由 HTML 轉檔；公司網路擋 npm，`docx` 套件裝不了）。
  - 踩坑：erp_web_client 查詢逾時後命令中心分頁會失聯（`NO_SQL_FIELD`），需重新整理分頁；含相關子查詢的 SQL 易逾時，拆成單表查詢較穩。Claude Docs 連線失敗（ECONNREFUSED）。
- **2026-10-08 Wiki Ingest 四筆**（commit `82e3f31`、`895728c`、`4c1fe93`，皆已推送）：
  - `SRC-254` Gemini 3 全能使用手冊影片：原始剪藏與檔名轉繁體（OpenCC s2twp），逐字稿依影片 12 個章節時間戳分段；新增 [[AI/wiki/Gemini 全能使用手冊與 Google 生態工作流]]，更新 `AI 工具與框架概覽`、`三大 AI 付費版選用與效能橫向對比`。
  - `SRC-255` Gemini 私人對話「2026 銀髮經濟認知地圖」：經 CDP 9222 已登入 Chrome 擷取（Gemini 對話內容為隱藏 DOM，需用 textContent 才抓得到）；新增 [[AI/wiki/2026 銀髮經濟認知地圖與樂齡數位課程商機]]。
  - `SRC-256` AVA-GPT 內部對話「AVA_ERP MCP 工具建立標準流程」：新增 [[AI/wiki/AVA_ERP MCP 工具建立標準流程]]，標註 AVA-GPT 兩處錯誤（MCP 誤稱 Model-Controller-Policy、工具定義應由 MCP 伺服器宣告），補七步驟流程與 FastMCP 示意範例。AVA_ERP 四個會議室工具當天為強制禁用。
  - `SRC-257` 根目錄筆記〈目前 2026 年最主流的 AI 發展趨勢〉移入 `raw/`，新增 [[AI/wiki/AI 工具應用內容趨勢與選題地圖]]（10 個選題對照本庫素材與知識缺口）。
  - 根目錄 `未命名.md`（手動貼上的 AVA-GPT 標準流程段落，內容已收進 SRC-256）已刪除。
  - 踩坑：AVA-GPT 須在 CDP 9222 的同一個 Chrome 登入；載入時會轉址，讀取要容錯等待。
- **ZPJJB01 10/08 登打完成**（已查 `DB.TBZP0050` 確認，合計 3.0 HR，系統別留空）：
  - 001　1300–1430（1.5）AVA_ERP MCP工具建立流程研究
  - 002　1430–1600（1.5）AI知識庫匯入及git同步假修改自動清除
  - 開新分頁用 `/erp/zp/do?_pageId=zpjjb0101Edit` 時員工欄位為空，需先填 26788 再送出。
- **2026-10-08 跨電腦同步造成的 git 假修改：自動清除**（commit `6f68a8c`、`8971e02`，已推送）：
  - 現象：在家裡 NB（鏡像模式）commit 後，公司 ADM-189（串流模式）的 `git status` 會把內容未變的檔案標成 `M`（`.git` index 經雲端硬碟同步、時間戳記不符，`core.autocrlf=true`）。
  - 新增 SessionStart hook：`.claude/settings.json` → `.claude/hooks/clean-phantom-modified.sh`，啟動時從 `git status` 取 ` M` 檔案、忽略換行比對，內容相同者 `git add` 刷新；加入後若與 HEAD 仍有差異則撤回。已用測試 repo 驗證 autocrlf 開關兩種情況。
  - 新增 `.gitattributes`（`*.sh text eol=lf`），避免腳本被轉成 CRLF 導致 bash 失敗。
  - 專案記憶 `git-phantom-modified-drive-sync` 記錄判斷方式，並授權對話中途遇到時直接自動處理。
- **2026-10-08 刪除 `AI/ERP/RQ11506072_特檢申報到職年資管制_計畫書.md`**（使用者指示；該檔未曾納入 git，如需救回只能從雲端硬碟垃圾桶找）。
- **2026-10-07 Wiki Ingest：a16z 第七版生成式 AI 應用榜**：新增 [[AI/wiki/a16z 第七版生成式 AI 應用榜與變現趨勢]]（六大洞察、4.5% 訂閱率與前 1% 重度用戶經濟、29 家隱形贏家、Agent 平台選邊、變現轉向廣告與抽成）；同步更新 `Claude`、`三大 AI 付費版選用與效能橫向對比`、`生成式 AI 企業應用與成本經濟學`，index 新增 `SRC-253`、log 追加 ingest 紀錄。原始剪藏後半段混入無關業配文（星城），未納入。
- **2026-10-07 Wiki 健康檢查**：修正 wiki 37 處斷鏈（多為 `[[sources/…]]` 實際在 `raw/`），wiki 內已無斷鏈；raw／sources 的 179 個為剪藏作者鏈結（唯讀，不修改）。無孤立頁面，frontmatter 完整。詳見 [[AI/wiki/log]] 2026-10-07 lint 紀錄。
- **2026-10-07 根目錄歸檔整理**：根目錄由 49 個檔案整理到剩 7 個（AGENTS／CLAUDE／README／WorkLog／package*.json／檔案清冊.base）。圖片 20 張移到 `AI/sources/images/`、PDF 2 份移到新建的 `AI/sources/assets/`；17 篇筆記依主題歸入 `AI/sources/01_AI_Tools`、`03_AI_Concepts`、`05_Tech_Development`、`06_Networking_Systems`、`07_Daily_Notes`；`chezmoi.md` 移到 `AI/`；`未命名.md` 改名為 `AI/fastmarkets-daily-v2/Fastmarkets_問題修復摘要.md`；刪除空白的 `2026-07-28.md` 與 2 個內容完全相同且無引用的重複檔。Obsidian 附件資料夾設為 `AI/sources/images`。搬移前後斷鏈數皆為 217（既有問題，搬移未新增）。
- **2026-10-07 ZPJJB01 九月補登完成**：依 Obsidian、chezmoi、Outlook 信件、TBDW11 待辦線索，補登 09/01、04、07、14、16、17、18 共 7 筆（各 0800–1500、6.0 HR），每筆送出後查 `DB.TBZP0050` 確認。九月現為 25 筆、105.0 HR，平日全數有紀錄（09/25 中秋節、09/28 教師節放假）。另將 10/06 序號 001 的報告內容改為 HGJJB05 結案結果。
- **ZPJJB01 10/07 登打完成**（已查 `DB.TBZP0050` 確認）：001　0800–0900（1.0）ZP：ZPJJB01九月工作記錄補登及待辦事項盤點結案。10/06 維持只有 001（2.0 HR），其餘時段不補登。
- **2026-10-07 待辦盤點結案**：EAJJRE00N（已上線，無需求單）、HGJJG01 刪除案（使用者已刪除）、ZP 正式機測試資料（交由 26622 自行處理）、HGJJB02（移交 27159 劉明峰）、MT／EA／HG 教材（不發布）、EAJJLICENSEBAT 手冊（已 Email 給 M9）、SogaType（結案；NoType 列為構想）、環境整理（公司電腦 ADM-189 已 `chezmoi update` 拉下 3 個 commit 並套用）。
- **2026-10-06 家裡 NB 技能中央倉庫同步修復**：
  - 原因：`~/.agents/skills` 是 09/18 複製的普通資料夾，不是 git clone，所以 10/02 之後新增的 `erp-cvs`、`erp-dajju1`、`find-skills`、`pdf` 都沒有同步過來。
  - 已原地轉為 `niceheadwkt/erp-skills` 的 git checkout，重跑 `setup-junctions.ps1`，四個工具都已載入 11 個技能；`~/erp_web_client.py` 同步為 repo 版；`sanshiba-voice` 加入本機 `.git/info/exclude`。
  - 刪除 Google Drive 上的技能散落副本（根目錄四個與 `claude_erp_rule`），細節見 [[AI/raw/CROSS_AGENT_SKILLS_SHARING_PLAN]]。
- **2026-10-05 新進人員教育訓練教材（三份）**：
  - MT：[MT系統新進人員教育訓練.html](file:///D:/CHSBrowser_erp/erpHome/yl.ear/erp.war/mt/MT系統新進人員教育訓練.html)，詳見 [[AI/ERP/MT教育訓練文件_工作筆記]]。
  - EA：[EA系統新進人員教育訓練.html](file:///D:/CHSBrowser_erp/erpHome/yl.ear/erp.war/ea/EA系統新進人員教育訓練.html)（10/05 13:42 再修訂），詳見 [[AI/ERP/EA教育訓練文件_工作筆記]]。
  - HG：[HG門禁管理系統_新進人員教育訓練.html](file:///D:/CHSBrowser_erp/erpHome/yl.ear/erp.war/hg/HG門禁管理系統_新進人員教育訓練.html)，依選單分類逐支作業說明用途、功能、管制限制與不妥之處。
  - 三份皆未發布；教材不需提交 CVS。
- **ZPJJB01 10/05 登打完成**（已查 `DB.TBZP0050` 確認，合計 7.0 HR）：
  - 001　0900–1200（3.0）115年「防禦性駕駛交通安全訓練」（原已存在）
  - 002　1300–1600（3.0）HG：HG門禁管理系統新進人員教育訓練文件製作
  - 003　0800–0900（1.0）MT：MT系統新進人員教育訓練文件製作
  - 10/02 補登 003　1500–1600（1.0）EA：EA系統新進人員教育訓練文件製作。
  - 10/02 補登 004　1100–1200（1.0）ZP：車籍管理系統新進人員教育訓練文件製作（[車籍管理系統_新進人員教育訓練.html](file:///D:/CHSBrowser_erp/erpHome/yl.ear/erp.war/zp/車籍管理系統_新進人員教育訓練.html)），10/02 合計 7.0 HR。
- **HGJJB02 承攬商工作證申請作業：明細 cardOk（是否核准）判斷分析**：
  - 結論：畫面下拉的 cardOk 會被 `hgjcb02StaffEntity.checkValidDate()` 的規則覆寫，實際由停權期間、重複發證、人事基本資料等規則決定 isOk。
  - 產出分析文件 [[AI/ERP/HGJJB02_cardOk核准判斷分析]]（本機版放在 `hg/` 根目錄，未加入 CVS），詳見 [[AI/ERP/HGJJB02_cardOk核准判斷_工作筆記]]。
  - 發現 5 個程式問題，**尚未修改**。
- **chezmoi：停止同步 `~/.claude.json`**：
  - 這個檔案是 Claude Code 的狀態和快取檔（內含 machineID、帳號資訊、各專案上一次對話的第一句話），多台電腦同步只會反覆出現 `MM` 衝突。
  - 已執行 `chezmoi forget`，commit `756d7c3` 並推上遠端，`chezmoi status` 已經沒有差異。
- **語音回覆修復**：公司網路的 SSL 檢查會讓 `edge-tts` 指令失敗，而且仍產生 0 KB 的 mp3。改用 Python 的 `truststore.inject_into_ssl()` 再呼叫 `edge_tts`；播放要用 `powershell.exe -STA`（pwsh 7 預設 MTA，MediaPlayer 抓不到長度）。
- **ZPJJB01 每日工作記錄：登打 10/01 兩筆**（已查 `DB.TBZP0050` 確認寫入，合計 6.0 HR）：
  - 001　0800–1200（4.0）HG：HGJJB02明細cardOk核准判斷流程分析
  - 002　1300–1500（2.0）HG：HGJJB02 cardOk核准判斷分析文件整理
  - 踩坑記錄：瀏覽器開了兩個 dsjjsql.jsp 分頁時，erp_web_client 會抓到沒有載入完成的那一個，回傳 `NO_SQL_FIELD`；改挑標題含「命令中心」的分頁就正常。時間格式是 `0800`，沒有冒號。

## 相關筆記與腳本連結
- [[AI/ERP/HGJJB02_cardOk核准判斷_工作筆記]]
- [[AI/ERP/zpjcDailyTriggerWorkNotice_工作筆記]]
- [[AI/ERP/EAJJRE00N_最新B表_工作筆記]]
- [[AI/ERP/EAJJLICENSEBAT_工作筆記]]
- [[AI/ERP/RQ11510012_風險評估系統優化_規劃設計]]

## 下一步
- RQ11510012 風險評估系統優化：規劃設計文件 v0.3（方案 B）。
  1. 待確認清單 .docx 補上「提出：」姓名後寄給申請人蔡侑儒，取得 Q11、Q13、Q14 回覆（Q14 子題 A1「撤除舊文號簽核待辦」若不想增加工時可拿掉）。
  2. 其餘待確認 Q1～Q8、Q10、Q12 一併與申請人確認。
  3. 依回覆修訂規劃文件，再寫 `doCopyLatest()`、`agree()` hook、共用 `estimate()` 與 `getWorkDocNumber()` 修正的程式草稿；家中可續作項目見該文件第 8.2 節，回公司待辦見第 8.3 節。

## 以後的構想（不列入待辦）
- chezmoi 範本小瑕疵：非 weng 電腦的全域規範「例外」說明用 `{{ .chezmoi.homeDir }}`，會把 weng 路徑顯示成本機家目錄（如 `C:/Users/ch26788/`），實際應為 weng 的 `C:/Users/niceh/`；不影響運作，有空再改三份 `.tmpl`。
- NoType：依 [[AI/raw/NoType 專案深度分析與演進建議書]] 的三階段藍圖（台灣詞庫、情境感知、記憶體直傳／UIPI），有空再評估是否實作。SogaType 已於 2026-10-07 結案（四個踩坑皆已排除）。
---

## [歷史紀錄 2026-09-29] ZPJJB01 九月每日工作記錄盤點與補登

- **ZPJJB01 每日工作記錄：九月紀錄盤點與補登**：
  - 用 erp-prod-web-executor 查正式機 `DB.TBZP0050`（每日工作記錄主檔，DAO：[zpjc0050DAO.java](file:///D:/CHSBrowser_erp/erpHome/yl.ear/erp.war/zp/src/com/icsc/zp/dao/zpjc0050DAO.java)），九月原有 11 筆、34.5 HR。
  - 對照 Obsidian 筆記找出漏填，透過已登入瀏覽器（CDP）操作 [zpjjb0101Edit.jsp](file:///D:/CHSBrowser_erp/erpHome/yl.ear/erp.war/zp/jsp/zpjjb0101Edit.jsp) 畫面按「新增」補登 5 筆，每筆送出後都查表確認：
    - 09/15 001　0800–1200（4.0）：zpjcDailyTriggerWorkNotice排程null錯誤修復(v1.21)
    - 09/21 001　0800–1600（7.0）：zpjcDailyTriggerWorkNotice測試機驗證及{maxPosNo}模板修正
    - 09/23 001　0800–1600（7.0）：zpjcDailyTriggerWorkNotice修正後驗證及測試資料清理
    - 09/29 001　1000–1100（1.0）：115年9月份A3處務會議（系統別、報告內容留空，比照以往處務會議寫法）
    - 09/29 002　1300–1600（3.0）：ZPJJB01九月每日工作記錄盤點及補登
  - 補登後九月共 16 筆、56.5 HR。
  - 踩坑記錄：
    - `TBZP0050` 為 Big5 編碼，`TOPIC`（工作摘要）上限 60 bytes、`MEMO`（報告內容）上限 1000 bytes；工作摘要沒有跳脫單引號（`MEMO` 有 `encodeSqlStr`），不可含 `'`。
    - 週別、星期、工時、部門代號由 controller `zpjcb01` 自動計算，畫面只需填起訖時間。
    - erp_web_client 匯出 CSV 時，報告內容含換行的欄位沒有加引號，一筆會被拆成多列（回報 27 筆，實際 11 筆），用 Excel 開 CSV 要注意。

---

## [歷史紀錄 2026-09-22] ZP 模板展開修復／EAJJLICENSEBAT 操作手冊／筆記庫合併

- **ZP `zpjcDailyTriggerWorkNotice`　`{maxPosNo:08}` 模板展開修復（測試、驗證、清理全部完成）**：
  - 詳見 [[AI/ERP/zpjcDailyTriggerWorkNotice_工作筆記]] 與 [D:/CHSBrowser_erp/erpHome/yl.ear/erp.war/zp/zpjcDailyTriggerWorkNotice_TBZP0053_測試報告.md](file:///D:/CHSBrowser_erp/erpHome/yl.ear/erp.war/zp/zpjcDailyTriggerWorkNotice_TBZP0053_測試報告.md)。
  - 測試機驗證通過後，清理 17 筆測試簽核單/工作通知與 48+6 筆 TBDW11 殘留、13 筆 TBZP0053 測試資料。
  - 依同一份修復邏輯，協助重設 3 筆正式機匯入用測試資料（`TBZP0053_v1.txt`：初始值重設、cron 限今日執行），並排除 DSIMPORT 匯入工具的欄位切分 bug（字串區隔字元需改用 `%`）。
- **EA `(EAJJLICENSEBAT)` 證照整批新增版次作業　操作手冊建置**：
  - 讀 [eajjLicenseBat.jsp](file:///D:/CHSBrowser_erp/erpHome/yl.ear/erp.war/ea/jsp/eajjLicenseBat.jsp)／[eajjLicenseBatM1.jsp](file:///D:/CHSBrowser_erp/erpHome/yl.ear/erp.war/ea/jsp/eajjLicenseBatM1.jsp)／[eajcLicenseBat.java](file:///D:/CHSBrowser_erp/erpHome/yl.ear/erp.war/ea/src/com/chsteel/ea/eajcLicenseBat.java)／[eajcLicense.java](file:///D:/CHSBrowser_erp/erpHome/yl.ear/erp.war/ea/src/com/chsteel/ea/eajcLicense.java) 原始碼，整理成使用者操作角度的 md＋PDF 手冊。
  - PDF 產製踩坑：Chrome headless `--print-to-pdf` 對特定中文字型有已知 bug，會把常用字（如「手」）誤對應成康熙部首碼（U+2F80~U+2FDF 區段），改用 reportlab 內嵌微軟正黑體字型重新產生，逐頁掃描確認無部首誤植字元。
  - 手冊補上正式機實際畫面截圖，並將證書號碼／專責人員／證照名稱／證照原始號碼等個資欄位事後遮蔽處理。
- **Obsidian 筆記庫跨電腦分岐合併**：解掉 `WorkLog.md`／`AI/wiki/log.md`／`AI/wiki/index.md`／一篇 `AI/raw/` 逐字稿共 4 個檔案的真實 Git 合併衝突（兩台電腦各自獨立新增的內容，非格式問題），保留雙方各自獨有內容後推送成功。

### 相關筆記連結（當時）
- [[AI/ERP/zpjcDailyTriggerWorkNotice_工作筆記]]
- [[AI/raw/2026-09-20T174500+0800-SogaType語音輸入操作踩坑與排錯實戰全紀錄]]
- [[AI/raw/NoType 專案深度分析與演進建議書]]

### 下一步（當時，供對照）
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
