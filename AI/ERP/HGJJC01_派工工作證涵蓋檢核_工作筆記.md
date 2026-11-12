# HGJJC01 派工工作證涵蓋檢核（缺最後一天未擋下）工作筆記

## 上次做到哪 (2026-11-11)
- **緣由**：吳星輝副課長 11/11 10:58 來信「115年度內部控制自行評估工作底稿(作業層級)」，11/30（一）下班前交。使用者指定以 HG 系統為主。
- **內控自評工作底稿**：沿用 114 年度自己交的格式（編號 G447-1、種類 O,F），控制點選 (HGJJC01) 承攬商派工申請作業「派工期間須有已核准工作證」。正式機全查 115 年 10 月已核准派工單 196 張、810 人次，皆有工作證；51 人次由多張證接續涵蓋。
  - 檔案：`C:/Users/ch26788/AppData/Local/Temp/claude/0dc289264e089a1c/c0fca6c9-067a-49e8-a1c0-431657f5285b/scratchpad/icsa/內部控制自行評估工作底稿(作業層級)_G447-1_翁國烔_20261111.odt`（暫存區，送出前建議另存）。
  - Outlook 回覆吳星輝草稿已存（附上述 ODT、「名片」簽名），**尚未寄出**。
  - 待確認：測試程序第 1 項的模擬輸入未實際操作；編號是否沿用 G447-1；種類是否補遵循類。
- **發現問題**：派工單 2026061707（3 人，10/12～10/13）所持臨時證 2026030715 只到 10/12（10/02 就是這個效期，非事後改短），卻可存檔。
  - 原因：`ha/tool/hajcCutDays.CoverPeriodTime()` 第 89～92 行兩個 `if` 連續對 `endPoint` 加 1；工作證迄日剛好是派工迄日前一天時，最後一天被誤判為已涵蓋。
  - 115 年全年已核准派工 8,319 人次，派工迄日無證涵蓋 17 人次（6 張單），其中 15 人次符合此模式；另 2 人次原因未查。
  - `hajcCutDays` 另有 HA 薪資 7 支程式共用，不改共用工具。
  - 分析文件：`D:/CHSBrowser_erp/erpHome/yl.ear/erp.war/hg/HGJJC01_派工工作證涵蓋檢核邊界問題分析.md`。
- **程式修正（CVS）**：`hgjcc01StaffEntity.java` **1.11**（`checkValidDate()` 收集已核准工作證；新增 `checkJobDateECovered()` 檢核派工迄日當天須有工作證涵蓋，訊息沿用「[,日期~日期，未申請工作證無法申請允許入廠]」）。本機無 JDK，未本機編譯。
- **上線**：測試機 DAJJU1 已填（類別 30 系統Bug、無需求單、「補檢核派工迄日須有工作證涵蓋」）。使用者表示**預計 2026/11/11 16:17 上正式機生效**。
- **ZPJJB01 11/11**：002（1330–1530 內控自評）、003（1530–1700 問題分析）、004（1700–1730 程式修正）已登打（HG，無需求單），已查 `DB.TBZP0050` 確認；001 為使用者自行登打。

## 2026-11-12 上線確認
- `DB.TBDAU1` 申請 `20261111_153556`（26788，hg，類別 30）狀態 **A**，CHS01 於 11/11 16:20 核准；**實際生效 115/11/11 23:42**（非原預計 16:17）。`TBDAU3` 1 支 `hgjcc01StaffEntity`。
- 正式機查 11/11 起異動派工單（APPLYTYPE 06）：B02 29 張 81 人次、B01 1 張 4 人次，最後異動日均為 11/11（生效前存檔），11/12 上午尚無新派工；85 人次派工迄日皆有 B02 工作證涵蓋，缺口 0。
- 查詢注意：工作證效期要用 `TBHG202.VALIDDATES／VALIDDATEE`，不可用 `TBHG201.VALIDDATEE` 過濾（會誤報）。
- 驗證查詢（缺口應為 0）：
  ```sql
  WITH C AS (SELECT P.IDNO, P.VALIDDATES, P.VALIDDATEE FROM DB.TBHG201 G JOIN DB.TBHG202 P ON P.APPLYID=G.APPLYID
    WHERE G.APPLYTYPE IN ('02','03') AND G.STATUS='B02' AND P.VALIDDATEE>='20261101' AND (G.APPLYTYPE='03' OR P.CARDID<>''))
  SELECT COUNT(*) AS GAP FROM DB.TBHG201 H JOIN DB.TBHG204 D ON D.APPLYID=H.APPLYID
  WHERE H.APPLYTYPE='06' AND (H.UPDATEDATE>='20261112' OR D.UPDATEDATE>='20261112')
    AND NOT EXISTS (SELECT 1 FROM C WHERE C.IDNO=D.IDNO AND C.VALIDDATES<=D.JOBDATEE AND C.VALIDDATEE>=D.JOBDATEE)
  ```

## 下一步
- **11/13 開工時**：用上方驗證查詢檢查 11/12 起（生效後）異動的派工單，先看筆數，再確認缺口為 0；資料累積幾天皆為 0 即作為修正有效佐證。
- ~~內控自評底稿改結論後寄出~~：已寄給新系統負責人，由對方自行決定後續（2026-11-12 使用者告知），不再追蹤。
- 若補開需求單：ZPJJB01 11/11 003、004 補需求編號。
- 歷史 15 人次是否需追蹤、另 2 人次原因待決定。
