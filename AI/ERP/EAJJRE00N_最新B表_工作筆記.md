# EAJJRE00N 最新B表匯出 工作筆記

## 上次做到哪 (2026-09-24)
- **需求**：(EAJJRE00N) 風險評估作業的匯出選單新增【最新B表】選項（`exportType=L`），SQL 依 [[最新B表匯出_MPW1]]。
- **程式與 CVS 版次**（都已提交，本機內容和 CVS 一致）：
  | 物件 | 版次 | 內容 |
  |---|---|---|
  | [eajcRERpt.java](file:///D:/CHSBrowser_erp/erpHome/yl.ear/erp.war/ea/src/com/chsteel/ea/bp/eajcRERpt.java) | 1.15 | 新增 `exportLatestB()`（with CTE）；風險評估編號改用 `trim(char(srlNo))` 去掉尾端空白 |
  | [eajcExportCSV.java](file:///D:/CHSBrowser_erp/erpHome/yl.ear/erp.war/ea/src/com/chsteel/ea/util/eajcExportCSV.java) | 1.5 | 新增 `exportByQuerySql()`（用 dejcQueryDAO）；抽出 `writeCSV()`；最新B表的欄位值加 CSV 引號跳脫 |
  | [eajjRE00MainN.jsp](file:///D:/CHSBrowser_erp/erpHome/yl.ear/erp.war/ea/jsp/eajjRE00MainN.jsp) | 1.28 | 下拉新增 `L=最新B表`；選取時顯示「關聯文件編號」說明（RA-/HR-/HC-/RO-） |
- **業務規則確認**：最新版維持 `REPORTID='0002'`（風險與機會評估維護階段），不改用 isCrntVer。`RANK` 為 NULL 時用 `coalesce` 處理；`tbeaWorkDocEX` 先用 LATEST_RA 縮小範圍再 GROUP BY。
- **測試結果**：
  - 正式機 dsjjsql 驗證 MPW1（單號 26S01MPW1261891331）：取到第 05 版 26S01MPW1262390800，共 125 筆，124 筆 RA、1 筆 HC。
  - 測試機匯出 M421：修正前的舊檔 `tmp-L-20260924150015L.csv` 有 7 列因欄位內含半形逗號而錯位，修正後的新檔 `tmp-L-20260924153726L.csv` 共 118 筆，全部 16 欄正確，資料內容和舊檔一致。
- **DAJJU1 上線申請**：測試機畫面已填好 eajcRERpt 1.15、eajjRE00MainN 1.28、eajcExportCSV 1.5 和上線說明，**尚未送出**（需求單號未填）。
- **新技能**：建立 `~/.claude/skills/erp-cvs`（Python pserver 工具，密碼以 DPAPI 加密存在 `~/.erp_cvs.dpapi`），說「cvs commit」就能提交；每月改密碼後會跳出 setpw 視窗重新輸入。

## 踩坑記錄
- **zafcDAO 不接受 with 語法**：`zafcDAO.query()` 只允許 `SELECT` 開頭的 SQL，with 會丟 `Sql is not Select`。`doExport` 把例外吞掉後回傳空字串，前端開啟 `/erp/`，結果跳到**登入頁**。解法：改用 `dejcQueryDAO.getDatas()`（同模組 `eajcRERptCRN` 已用它跑 with）。
- **CSV 欄位內含半形逗號會錯位**：原本 `exportBySql` 不做跳脫。這次只對最新B表加引號；A/B/H 等既有匯出沒動，因為 CSV 可能會再匯入，要先確認匯入端的解析方式。
- 既有的 `csvEscape()` 有缺陷：只有雙引號沒有逗號時，不會加外層引號。
- 只看檔案修改時間判斷「未提交」會誤報，要實際和 CVS 內容比對（erp-cvs 的 `status`）。

## 下一步
- 確認需求單號後送出 DAJJU1 上線申請，上線後在正式機匯出最新B表驗證。
- （可選）前端 `setExptFile()`：匯出失敗時改為跳訊息，不要開 `/erp/`，A/B/H 匯出也有同樣問題。
- （可選）評估 A/B/H 既有匯出是否也要做 CSV 跳脫：先確認 `doImport` 的 CSV 解析方式。
- （可選）建議使用者輸入時統一用全形逗號，符合畫面上匯入說明的規定。
