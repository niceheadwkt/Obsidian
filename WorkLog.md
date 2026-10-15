# 工作筆記

**更新日期**：2026-10-15（收工）

## 上次做到哪
- **2026-10-15 工作日誌整理匯入晤談內容檔 TBHBM22B（已匯入，使用者確認）**：
  - 來源：`DB.TBZP0050` 本人（26788）`YYYYMMDD` 20260101～20260831、`APPLYNO` 有值，共 85 筆、274.0 HR、47 張需求單 → `D:/temp/tbzp0050_26788_202601_202608_APPLYNO.csv`（dsimport 原表格式；文字欄用 `HEX()` 取原始 Big5 位元組，避免命令中心 CSV 遇多行 MEMO 錯欄）。
  - 目標：`TBHBM22B`（晤談內容(專業及主管)檔，PK `APPLYID, EMPNO, NUM`），本期 `APPLYID=1788912444167`。比照同仁 26358 格式：一張需求單一筆，ITEM＝「需求單號＋名稱」(≤50 bytes，標題取自 `DB.TBZM100.APPLYTITLE` 並縮短)、TARGET＝「工時X小時」、DESC＝民國日期區間＋摘要(≤300 bytes)。
  - 使用者要求刪除工時 <2.5 小時者（27 筆、31 HR），最後 20 筆、243 HR → `D:/temp/tbhbm22b_26788_1788912444167.csv`，**使用者已自行匯入**。
  - ZPJJB01 10/15 001　0730–1030（3.0）EA RQ11510012：匯出銹字轉碼修正、測試機匯入驗證及異動申請表；002　1030–1200（1.5）HB（無需求單）：工作日誌整理匯入晤談內容檔，已查 `DB.TBZP0050` 確認。
- **2026-10-15 RQ11510012 資料庫異動申請表**：
  - 10/14 正式機 5 支 CSV／匯入修正上線成功（使用者確認）。
  - **0b 正式機匯出 B 表逐欄比對**（`tmp-B-20261015083828B.csv`，`26S01M462262081511`）：1,371 筆×15 欄，與正式機同一 SQL 結果比對，逗號不錯位、無雙引號／換行問題；底層位元組除「銹」外完全相同（列 803 的 `&#189;` 是資料庫原本就存的字面文字、列 1188 的造字 `FC57` 原樣保留）。**發現：資料庫「銹」存 `F9D7`，Java MS950 匯出成 `C8CA`（Windows 造字區）**，共 8 處，Java 匯入可還原，但 Excel 可能顯示不正確，使用者 Excel、Notepad++ 確認「銹」顯示方框。
  - **原因**（本機 zulu JDK 8 實測）：DB2 JDBC 以 IBM-950 把 Big5 `F9D6～F9FE`（碁銹裏墻恒粧嫺＋34 個框線）讀成造字區 `U+F813～U+F83B`，Java MS950 再寫成 `C8C9～C8F1`（Windows 造字區）；反向 IBM-950 也無法編碼標準字 `U+92B9`。
  - **修正 `eajcExportCSV`（CVS 1.7→1.8，10/15 10:00 提交；測試機 DAJJU1 已上線，類別 30、RQ11510012）**：新增 `toStdChar()`（匯出 `writeCSV`、`exportByLine` 轉回標準字）、`toDbChar()`（`readCSV` 讀入後轉回造字區碼）；標準字以 MS950 解 `F9D6～F9FE` 動態取得，原始碼不放擴充字。`-encoding big5` 編譯通過；測試 41 字往返、MS950／UTF-8 BOM 匯入、1.7 舊檔（`C8CA`）匯入皆還原；以實際檔模擬新版輸出：「銹」8 處變 `F9D7`、`C8CA` 0 處。公司造字 `FC57`（列 1188）不在此範圍，維持原樣。
  - **測試機匯入驗證**：匯入單 `26S01M462262881018`，1,371 筆與來源 `26S01M462262081511` 以 flow0Code／flow1Code／srlNo 對應、11 個內容欄位全部相同；含「銹」6 筆皆存為 `F9D7`、無 `C8CA`；1.8 匯出檔 Excel 顯示「銹」正常（使用者確認）。**正式機 DAJJU1 已送審上線，使用者匯出 B 表確認「銹」正確（10/15）**。
  - **R1～R5 未完成部分一起修改（big5／Java 8 編譯通過；**CVS 已提交 10/15**：`eajcRERpt` 1.19、`eajcRE20CRN` 1.90、`eajcRE00CRN` 1.28、`eajcRE13CRN` 1.12、`eajjRE00MainN.jsp` 1.30、`eajjRE13MainN.jsp` 1.17、`eaStructs.xml` 1.167；連同 `eajcRE03DAO` 1.12、`eajcRE03VO` 1.5 共 9 支，**測試機 DAJJU1 已上線成功（10/15）**，待測 R1～R5）**：
    - R1 `eajcRE00CRN.checkVerCtl()`：系統參數 EA0013 `REVerCtlDate`（未設定不管控）起，新增時同部門前一版（WorkDoc.timeStamp 最新，Y/S 一起）須 0002/E；附件 P1 已明確「前一版」、生效日例 2026/12/01，Q1、Q8 視為已確定。**上線前須在 TBDE23 新增參數**（測試機已新增 `yl／EA0013／REVerCtlDate／20261015`，10/15；正式機上線時再新增，日期依申請人，例 20261201）。
    - R2／R3 `eajcRE00CRN.doCopyLatest()`（flag `CL`，`eaStructs.xml` 已加）＋`eajjRE00MainN.jsp`「新版複製」按鈕；`eajcRERpt` 最新B表 SQL 抽成 `getLatestBSql(forCopy)`，另加 `queryLatestBForCopy()`、`getLatestRaFormNo()`；RE03 寫 refType／refDocNo。正式機唯讀驗證：M462 1,371 筆全 RA；MPW1 125 筆（HC 1、RA 124）。
    - R4 `eajcRE20CRN`：`doEstimate()` 寫入動作抽成 static `estimate()`；`getWorkDocNumber()` 修正（只取長度＝鍵＋3 碼、不吃錯誤）；新增 `transferHC()`（核准 0001/E 時於 `eajcRE00CRN.agree()` 呼叫，savepoint 逐筆、跳過不擋核准，複製 RE043 改核准日、memo 註記移轉與逾期）；`isCanExecuteHrisk()` 加 B2 鎖定（`getTransferredFormNo()`，測試機驗證 SQL）。待確認 Q2、Q3、Q11、Q13、Q14 先依規劃文件建議實作。
    - R5 `eajcRE13CRN.update()` 原等級 1、2 拋錯；`eajjRE13MainN.jsp` 停用該列勾選框＋紅字說明（只停用勾選框，避免欄位錯位）。
    - 未做：B7 待辦訊息、B10 核准前提示、B 表顯示原始依據（Q10）、R1 前端提示、排程 B13、舊 `eajcRE00CR`。
    - 上線條件：需 RE03 DAO 1.12／VO 1.5 與 DDL（測試機已 ALTER；正式機須先執行 DDL）→ 屬第二次上線。
  - ZPJJB01 10/15 004　1430–1630（2.0）RQ11510012版次管控、新版複製、高風險移轉及機會評估卡控，系統別 EA、需求編號 RQ11510012，已查 `DB.TBZP0050` 確認，10/15 合計 8.0 HR（主題上限 60 bytes，原擬 66 bytes 被擋後縮短）。
  - ZPJJB01 10/15 003　1300–1430（1.5）RQ11510012風險評估最新A表匯出及流程圖匯入開發上線，系統別 EA、需求編號 RQ11510012，已查 `DB.TBZP0050` 確認（001 0730–1030 3.0、002 1030–1200 1.5 HB 為先前已登，目前合計 6.0 HR）。
  - **第二階段開工：最新A表匯出＋流程圖匯入（big5 編譯通過；**CVS 已提交 10/15**：`eajcExportCSV` 1.9、`eajcRERpt` 1.18、`eajcRE00CRN` 1.27、`eajjRE00MainN.jsp` 1.29；待測試機 DAJJU1 上線測試）**：
    - `eajcRERpt`：新增匯出類型 `M`＝最新A表 `exportLatestA()`（格式同 A 表，可直接以 A 表匯入）；`LATEST_RA` 抽成共用 `getLatestRaSql()`（最新B表同用）；流程圖匯出名稱以 `csvQuote` 包覆（含逗號才能匯入）。正式機唯讀跑最新A表 SQL：`26S01M462262081511` 12 筆＝該單 RE02 筆數。
    - `eajcExportCSV`：`csvQuote()` 改 public（`eajcRERpt` 依賴，**兩支須一起上線**）。
    - `eajcRE00CRN`：`doImport()` 匯入類型 `F` 走新 `doImportFlow()`：表單已有任何 RE01 就拒絕（使用者決定）；每列第1欄製程「代碼_名稱」、其後作業「製程-作業_名稱」；檢查格式、製程代碼一致、代碼≤3碼、名稱≤100 bytes、重複；srl 依檔案順序 1、2、3…。
    - `eajjRE00MainN.jsp`：匯入下拉加 `F=流程圖`、匯出加 `M=最新A表`＋說明、匯入說明第 3 點（流程圖 → A表 → B表）。
    - **測試機驗證（10/15）**：先清空 `26S01M462262881018` 的 RE01／02／03（5／12／1,371 筆，表頭保留；命令中心 `recordLimit` 填筆數可一次刪），再依序匯入：流程圖 16 筆（代碼、類別、名稱與來源 `26S01M462262081511` 全同，srl 依序編號）、A 表 12 筆（以 `tmp-A-…A.csv`，非最新A表）、B 表 1,371 筆，逐欄與來源相同，「銹」6 筆為 `F9D7`。誤匯入來源單時「鍵值已存在」整批回復，無資料異動。待測：最新A表（M）匯出、重複匯入流程圖應被擋。
    - **正式機 DAJJU1 已送審，預計 10/15 14:17 上線**（4 支：`eajcExportCSV` 1.9、`eajcRERpt` 1.18、`eajcRE00CRN` 1.27、`eajjRE00MainN.jsp` 1.29）。上線後驗證：最新A表匯出（12 筆、`tmp-M-`）、流程圖匯出／重複匯入被擋。
    - 環境考量（EAJJEA00N）流程匯入：使用者決定等風險評估測試後再比照。
  - 正式機 `eajjRE00CopyListN`、`eajjEA00CopyListN` 經 CDP 抓頁面確認已是新版（bootstrap 已載入、form1 包住分頁列），使用者實測換頁正常。
  - 依 RQ11501028 的 TBHG202 範例產出 `D:/0.翁國烔_中鴻專案/RQ115/RQ11510012(風險評估系統優化(115107與A3翁國烔工程師溝通))/20261015-ERP資料庫異動作業表格-修改表格TBEARE03.odt`（勾表格修改＋Index Key 建立；一、ALTER 加 refType／refDocNo／hcTransDate；二、CREATE INDEX `IXEARE03_REF`；回退 SQL 未放），**使用者已確認 OK**。內嵌欄位表的舊預覽圖已移除，由 LibreOffice 開啟時重畫。
- **2026-10-14 RQ11510012：RE03 加欄位、CSV 匯出匯入修正、環境考量匯入修正，正式機預計 16:17 上線**：
  - **RE03 加欄位（第二段基礎，暫不上線）**：`eajcRE03.dao` 加 refType(2)／refDocNo(40)／hcTransDate(8)（CVS 1.2→1.3）；新增 `ea/dao/sql/db.tbeaRE03_RQ11510012.sql`（ALTER、索引 `ixeaRE03_ref`、回退 DDL，**新檔，需在 Eclipse 做 Team → Add＋Commit，是否已做未確認**）；測試機 ALTER＋索引已由使用者執行並查證。daotool 重新產生，保留手寫方法，`update()`／`getUpdatePreSql()`／`prepareUpdate()` SET 拿掉新欄位；`eajcRE03DAO` 1.11→1.12、`eajcRE03VO` 1.4→1.5（備份 `D:/temp/RQ11510012_daotool_bak/`）。**第二段上線前不可放進正式機 DAJJU1**。
  - **測試機 26S01M462262081511 的 B 表亂碼錯位**：內文含逗號未加引號、「銹」被 Java Big5 編成 `?`（MS950 才正確）。以正式機資料 MERGE 修復 1,371 筆並比對一致（命令中心每句最多異動 10 筆、不能用 `;` 送多句）。
  - **CSV 匯出匯入修正**：`eajcExportCSV` 新增共用 `readCSV`（MS950，有 UTF-8 BOM 改用 UTF-8；支援雙引號包覆的逗號、換行）、匯出一律跳脫並改 MS950 寫檔；`eajcRE00CRN` 1.26、`eajcRE10CRN` 1.21、`eajcEA00CRN` 匯入改用 `readCSV`。測試機 26S01M462262871204 匯入驗證：A 表 12、B 表 1,371 筆逐欄與來源相同（含逗號 7 筆、「銹」6 筆）。舊控制器 `eajcRE00CR`、`eajcEA00CR` 未改。
  - 測試機 RE 下拉選單空白：`DB.TBEARISKRRVERS` 缺 yl／026S01，使用者已 INSERT。
  - **環境考量匯入**：13:17「鍵值已存在」是匯入了投入產出表的匯出檔（8 欄）且類別選 A，不是 B 檔問題。B 表匯入比對發現 `eajcEA02DAO.queryByName` 用 `like '名稱%'`，「電」對到「電池」、找不到時預設第 1 筆 → 改為先全名、再前綴（取最短）、都找不到就報錯（**1.3→1.4**）；`eajcEA00CRN` 錯誤訊息只有欄數過多才提示雙引號（**1.20**）。測試機驗證：顯示「第62列有誤!處理第61項資料：找不到投入產出名稱「廢綿手套」(製程10作業05)」，B 表 0 筆。測試機目標單 `20Y01M514201291343` 的 EA03 已清空（A 表 153 筆與來源不同，不適合測成功案例）。
  - **正式機上線失敗**：伺服器以 `-encoding big5` 編譯，`eajcExportCSV` 註解含「銹、碁、裏」→ unmappable character。改註解 **1.6→1.7**，5 支以 big5 編譯全過。測試機重新申請（1.7）；正式機 5 支：`eajcExportCSV` 1.7、`eajcRE00CRN` 1.26、`eajcRE10CRN` 1.21、`eajcEA00CRN` 1.20、`eajcEA02DAO` 1.4，**預計 16:17 上線**。
  - 流程作業表沒有匯入功能：建議暫不開發，加入待確認 **Q16**（7.2 已有 Q15）；第二段加「匯入前檢查流程存在」（T-C1／T-C2、0.5 人日），已寫入 v0.4。
  - ZPJJB01 10/14 002　0830–1000（1.5）、003　1000–1200（2.0）、004　1300–1630（3.5），需求編號 RQ11510012，連 001 合計 8.0 HR，已讀回確認。
  - 工具：`erp_web_client.py` 預設固定正式機完整網址，`--test` 查測試機（私人技能 repo `~/.agents/skills` 三個檔案，收工時 commit）；statusline 設定 `~/.claude/statusline-command.sh`。
  - **chezmoi 同步 Claude Code 狀態列與佈景主題**（commit `0678818`、`f407603`、`3b47cde`，已推送）：`statusline-command.sh`、`themes/solarized-light.json` 整檔納入；`settings.json` 用 modify 範本 `dot_claude/modify_settings.json`，只合併 `statusLine`、`theme`（`custom:solarized-light`），`autoUpdatesChannel`／`skipDangerousModePermissionPrompt` 等其餘設定保留各電腦原值，沒有 settings.json 的電腦會建立只含這兩項的檔案。chezmoi repo 新增 `.gitattributes`（`*.sh text eol=lf`），避免其他電腦 checkout 成 CRLF 讓 bash 失敗。其他電腦執行 `chezmoi update` 即套用。
- **2026-10-14 環境考量查詢畫面顯示 SQL 修正（納入 RQ11510012）**：
  - 現象：`eajjEA00PopupN.jsp` 查詢結果最上方印出整段 SQL。原因是結果頁 `eajjEA00ListN.jsp` 第 23 行遺留除錯用 `out.print(sql)`（1.8 版，2017 年 ch25359 提交），與這次 RQ11510012 上線無關；兩支 CopyList(N) 早已註解。
  - 修正：該行註解；版次參數 `isCrntVer` 原本直接串入 SQL，改為只接受選單值（`A`／`S`／`Y`／`N`／空字串），其餘視為 `A`，防止 SQL injection。**CVS 1.8→1.9**，使用者已自行送出正式機上線，**10:17 生效**。改前備份在本次對話 scratchpad `bak/`。
  - 未處理：舊版 `eajjEA00List.jsp` 第 13 行同樣串接 `isCrntVer`；框架 `dejcGridTable.getCombineSql(request)` 是否跳脫未查。
  - DAJJCVS（`dajjCVSTag.jsp`）按 Checkout 很久才列出明細：`CK` 動作走 `da.jar` 的 `dajcCVSFuncControl.checkout()`，以 Ant `Cvs` task checkout **整個系統模組**（EA 本機約 1,900 檔、29 MB）再用 Ant `Copy` 部署，主要耗時在此；`dajcCVS` 1.19（2011）、`dajcCVSFuncControl` 1.9（2006）為 ICSC 框架，CVS 上無原始碼、本機無 JDK 無法反編譯。**使用者決定暫不處理**。
  - ZPJJB01 10/14 001　0730–0830（1.0）系統別 EA、需求編號 RQ11510012：環境考量查詢顯示SQL修正及CVS Checkout效能分析（已查 `DB.TBZP0050` 確認）。
  - 踩坑：Python 經 CDP 印出中文時，Git Bash 主控台要設 `PYTHONIOENCODING=utf-8`，否則 cp950 輸出看起來像亂碼（頁面本身正常）。
- **2026-10-13 16:17 RQ11510012 第一段過渡版正式機上線（6 支）**：`eajcRE00CR` 1.12、`eajcRE00CRN` 1.25、`eajcRE03DAO` 1.11、`eajcRERpt` 1.17、`eajjRE00CopyListN`（CVS 1.6）、`eajjEA00CopyListN` 1.8。
  - 16:2x 從正式機抓兩支 JSP 頁面，**仍是舊版**（form1 在分頁列之後，RE00 沒有載入 bootstrap、換頁列為圖片），可能 JSP 尚未同步；Java 部分未從外部驗證。
- **ZPJJB01 補登 10/09、10/12、10/13 也補了報告內容、附件代號各自獨立**（10/09 001 保留使用者上傳的附件）。
- **ZPJJB01 補登 10/09、10/12、10/13 完成**（已查 `DB.TBZP0050` 確認，系統別 EA；**需求單號一律要填**，6 筆已補上 RQ11510012）：
  - 10/09　001　0800–1200（4.0）RQ11510012風險評估優化規劃設計v0.3及方案B評估；002　1300–1600（3.0）RQ11510012正式機資料查核及待確認清單製作
  - 10/12　001　0800–1200（4.0）RQ11510012追蹤資料存放評估及RE03加欄位替代方案；002　1300–1600（3.0）RQ11510012規劃設計v0.4整合及上線步驟規劃
  - 10/13　002　1030–1200（1.5）RQ11510012正式機查核及過渡版INSERT欄位清單修正；003　1300–1600（3.0）RQ11510012匯出重複及複製清單換頁修正、CVS提交（001 為原有 HG 紀錄）
  - 踩坑：Edge 的正式機登入逾時（要 OTP），改用 Chrome（`127.0.0.1:9222`）已登入的正式機分頁查詢與登打。
- **ZPJJB01 10/13 登打完成**（已查 DB.TBZP0050 確認，合計 2.0 HR，系統別 HG）：
  - 001 0830~1030 (2.0) HG：查承攬商人員E124765450派工單簽核核准歷程（產製 Markdown、排版 PDF 報告與多表關聯 SQL）。
- **2026-10-13 RQ11510012：決定採用 v0.4（RE03 加欄位）**：v0.3（WorkDocEX 追蹤列）不再續作，只當 DDL 被退回時的備案參考。已在 v0.4 開頭、Q-B1、第 9 節，以及 v0.3 開頭標註這個決定。
  - Q-B4 正式機查詢：`tbeaRE03` 共 1,309,777 筆、2,805 個 formNo，只有主鍵索引；B2 反查沒帶 formNo，**必須加索引** `ixeaRE03_ref (refDocNo, refType)`，和 ALTER 放同一個 SQL 檔。
  - 3.6.2 三項確認：`eajcRE03CRN` 修改是原地 update（插入序號、插入作業也都是 UPDATE），B14 不會發生；`eajcRE10CRN`／`eajcRE13CRN` 的 `SELECT *` 經 `getInstanceByName()` 依名稱取值，不受影響；依位置取值的 `getInstance(rs)` 在 `ea/` 下沒有人呼叫。
  - 新發現：`eajcRE03DAO.update()`／`updateList()` 的 VO 來自畫面，daotool 重新產生後若 SET 帶上新欄位，使用者一按修改就會清空追蹤資料，重新產生後要拿掉。已寫入 v0.4 第 3.3.3、3.6.2 節。
  - 第一段過渡版（v0.4 第 5 節步驟 1）本機已改好，**尚未測試、尚未提交 CVS**：`eajcRE03DAO.copyByFormNo()`、`eajcRE00CRN` 與 `eajcRE00CR` 的匯入 `prepareSql`，各改一行補上 16 欄清單（正式機 `SYSCAT.COLUMNS` 確認欄位順序）。改前備份在本次對話的 scratchpad `bak/`。
  - 測試機 T-B5：A 表匯入成功（41 筆）；B 表匯入失敗「第67列(MPW1-20-01-2)資料鍵值已存在」，原因是**匯出 B 表的既有 bug**：`eajcRERpt.exptByFormNos()` B 表為取狀態 join `tbeare02` 只用作業流程，A 表一個作業多列就重複（來源 114 筆匯出 539 列）。已比照最新B表改寫（以事故類型對應危害特性、每筆 RE03 只取 srlNo 最小的 RE02），測試機驗證 114 筆、鍵不重複；尚未在測試機 reload／測試。
  - **CVS 已提交（2026-10-13，T-B5 尚未測完）**：`eajcRE03DAO` 1.10→1.11、`eajcRE00CRN` 1.24→1.25、`eajcRE00CR` 1.11→1.12、`eajcRERpt` 1.15→1.16。測試機 DAJJU1 四則上線說明已填（未送出）。
  - `eajcRERpt.exptByFormNox()`（風險與機會評估匯出，`eajcRE10CRN` 呼叫）同樣修正重複，**CVS 已提交 1.16→1.17**（DAJJU1 說明已改為「修正B表及機會匯出資料重複」，畫面版本仍顯示 1.16，需重新帶入）：除了 RE02，還有 RE13 同一序號存 `'14'` 和 `'0014'` 兩筆（測試機 1,184 組；`eajcRE10CRN.addRE13()` 補零 4 碼、`eajcRE13CRN` 畫面用未補零），優先取未補零那筆。測試機驗證：MT61 單 172→171、MPW1 單 539→114。RE13 補零不一致是資料面既有問題，未處理。
  - `eajjRE00CopyListN.jsp`（複製來源清單）換頁無反應：分頁 `deGrid_setFunc()` 取最後一個 form，但 `form1` 放在 `</html>` 後且沒包住分頁欄位，`f.deGrid_pageRow` 為 undefined 而 JS 中斷。已比照 `eajjBossList.jsp` 把 form1 移進 body 包住分頁列與表格，本機已改、**未測試／未提交**。`eajjEA00CopyListN.jsp`（環境考量複製清單）同樣問題，已用同方式修正。**CVS 已提交**：`eajjRE00CopyListN.jsp` 1.4→1.5、`eajjEA00CopyListN.jsp` 1.7→1.8（畫面換頁尚未實測、尚未加入 DAJJU1）。之後測試機分頁列變成新式 bootstrap 按鈕，但 `eajjRE00CopyListN` 用 `dzjjmain.jsp` 沒載入 bootstrap，按鈕只剩空框；改用 `dzjjMainHeader`／`dzjjMainFooter`（比照 `eajjRE00CopyList`），**CVS 1.5→1.6**，提交後測試機仍是舊版，待更新後確認版面。DAJJU1 版本需改 1.6。`eajjRE00CopyList.jsp`、`eajjEA00CopyList.jsp`（舊版）暫不修。
  - 測試機查詢：Edge（`[::1]:9222`）＝正式機、Chrome（`127.0.0.1:9222`）＝測試機；`erp_web_client.py` 只會連到 Edge，查測試機要用 scratchpad 的 `erp_web_client_host.py`（`CDP_HOST=127.0.0.1 ERP_HOST=test.chsteel.com.tw`）。
- **2026-10-12 RQ11510012：規劃設計 v0.4（整合 RE03 加欄位替代方案）**：
  - 以 v0.3 為基礎，把替代方案整合成完整的另一版：[[AI/ERP/RQ11510012_風險評估系統優化_規劃設計_v0.4]]；v0.3 保留不動（開頭加註新版連結），作為 DDL 無法執行時的備案。
  - 主要變動：追蹤資料改存 `tbeaRE03` 的 `refType`／`refDocNo`／`hcTransDate`（3.3.3，含 DDL、回退、DAO 重新產生）；HC 移轉改掃 RE03；B2／B6／B8 改讀 RE03，B9 消失，新增 B14（空窗期改鍵要保留新欄位）；取號修正拿掉 `NOT LIKE 'CP%'`；新增 3.6 既有程式影響、第 5 節兩段式上線與回退；測試、待確認（分申請人／DBA 兩表）、工時（約 12 人日）一併更新。
  - 順手修正：附錄 A 的 `INSERT INTO DB.TBEARE03 WITH … SELECT` 補上 16 欄欄位清單（加欄位後原寫法會壞）；續作提示路徑由 `G:/` 改為 `C:/Users/niceh/我的雲端硬碟/`。附錄 B 整理回到 v0.3 時要恢復的項目與兩方案比較。
- **2026-10-12 RQ11510012：追蹤資料存放位置評估，產出替代方案計畫書**：
  - 比較 `tbeaWorkDocEX` 與 `tbzafrd`：`tbzafrd` 雖然欄位寬（item 50、data 100 碼、有建立人／日期），但它是全公司共用的系統組態參數表，追蹤列屬於交易資料，會持續增加、也可能被 ZAF 參數畫面誤改，**不建議使用**；兩者擇一選 `tbeaWorkDocEX`。
  - 提出更好的做法：`tbeaRE03` 加 `refType`／`refDocNo`／`hcTransDate` 三欄，與 B 表一對一，v0.3 的 CP 前綴、field5 留空、B9 孤兒追蹤列都不再需要。產出 [[AI/ERP/RQ11510012_替代方案_RE03加欄位_計畫書]]。
  - 查到的改表影響：`eajcRE03DAO.copyByFormNo()`（第 647 行）、`eajcRE00CRN.doImport()`（第 896 行）、`eajcRE00CR`（第 754 行，JSP 已無引用）三處 INSERT 沒寫欄位清單，加欄位後會壞；daotool 重新產生 DAO 會蓋掉手寫方法。建議兩段式上線（先上補欄位清單的過渡版，再 ALTER＋新功能）。
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
- [[AI/ERP/RQ11510012_替代方案_RE03加欄位_計畫書]]
- [[AI/ERP/RQ11510012_風險評估系統優化_規劃設計_v0.4]]
- [[AI/ERP/RQ11510012_2026-10-13_修改紀錄]]

## 下一步
- RQ11510012 風險評估系統優化（v0.4，R1～R5 程式已完成並上測試機，10/15）：
  1. **測試機續測**（R1 已測通過）：
     - 新版複製：目標草稿單 `25Y01MPW1262661342`（建立人 26788），預期來源 `25Y01MPW1250391703`、B 表 114 筆（RA 112／RO 1／HC 1，HC 舊文號 `25Y01MPW125039170330021001`），複製後比對 RE03 refType／refDocNo 及 RO 列覆蓋值。
     - R4：該單確認→送簽→核准到 E，確認核准訊息「高風險移轉成功 1 筆」、新高風險文號（發文者暫存、發文者＝建立人）、RE043 歷程改核准日、RE03.hcTransDate；EAJJRE20N 舊文號顯示已移轉不可異動。
     - R5：進【風險與機會評估】原等級 1、2 列勾選框停用、後端擋下。
     - 原【預估評估】（改用共用 `estimate()`）與取號修正：任一高風險項目手動預估評估一次。
     - 0c：Excel 另存 Big5／UTF-8 CSV 匯入、舊格式檔應 0 筆、`eajcRE10CRN` 機會評估匯入；重複匯入流程圖應被擋；最新A表匯出（`tmp-M-`）。
  2. 正式機上線前：依程序申請 DDL（ODT 已備：`20261015-ERP資料庫異動作業表格-修改表格TBEARE03.odt`）；上線當天先 ALTER＋索引→確認→部署 9 支（含 RE03 DAO 1.12／VO 1.5）；TBDE23 新增 `REVerCtlDate`（日期依申請人，例 20261201）。
  3. 待確認清單寄申請人蔡侑儒：Q1、Q8 已依附件確定可刪；R4 的 Q2、Q3、Q11、Q13、Q14 已先依建議實作，請申請人確認；另 Q4～Q7、Q10、Q12、Q16。
  4. 未做（視需要）：B7 核准後待辦訊息、B10 核准前提示移轉筆數、B 表顯示原始依據（Q10）、R1 前端提示、排程 B13、環境考量流程圖匯入、匯入前檢查流程存在、R6 操作手冊。
  5. 規劃文件 v0.4 補記 10/15 決定（R1 前一版＝WorkDoc.timeStamp 最新、參數 REVerCtlDate、R4 共用方法放 `eajcRE20CRN` static、transferHC 以 savepoint 逐筆）。

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
