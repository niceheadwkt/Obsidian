# HGJJB05 送出「輸入資料錯誤」工作筆記

## 上次做到哪 (2026-10-06)
- **問題**：A32 尤柏智轉來 MPW1 潘勝賢（26446）的問題。10/05 在 HGJJB05 臨時通行證申請作業按「送出」，一直出現「輸入資料錯誤!!」，單號 2026051060／066／067 都送不出去（依據 `HGJJB05APPLY_ERP21.log`）。
- **錯誤來源**：[zpjcESignAPI.java](file:///D:/CHSBrowser_erp/erpHome/yl.ear/erp.war/zp/src/com/chsteel/zp/esign/zpjcESignAPI.java) `addESign()` 第 85 行（正式機 1.74 版；本機是 1.72 版，所以本機在第 83 行）。觸發條件是 `topApprove` 空白，而且 `approveUsers` 也是空的，也就是 `{maxPosNo:18}` 沒有抓到任何簽核主管。這不是使用者輸入錯誤。
- **呼叫鏈**：[hgjcb05Apply.java](file:///D:/CHSBrowser_erp/erpHome/yl.ear/erp.war/hg/src/com/icsc/hg/controller/hgjcb05Apply.java):436 `sent()` → `getESingAuthListByTemplate` → `getESingAuthList` → `zpjcEmpAuthLevel`／`apjcUserAuthLevel.genLevel()` → [hajcForOut.java](file:///D:/CHSBrowser_erp/erpHome/yl.ear/erp.war/ha/src/com/icsc/ha/tool/hajcForOut.java) `getSirsPostNo()`／`getSirs()` → TBHAM0＋TBHAM1，依股長(21)／課長(18,19)／處長(08,09) 往上找。
- **資料狀況**：TBHG201 單號 2026051066 的 STATUS 是 A01（承辦人尚未送出），送出交易已經 rollback。畫面顯示「主管審批中」，是因為 `sent()` 失敗後沒有重新讀取資料。
- **TBDU01 組織正常**：26446 是 MPW1 股長(21) → 課長 26451(MPW) → 處長 25582(MP) → 助理副總 23730(MA)。同部門的 26465 送出正常，原本研判是 26446 本人的 TBHAM0 資料異常。
- **後續（2026-10-06）**：HA 系統負責人表示是程式問題，已修改 HA 程式，但**沒有說明改了哪支程式、哪一段**。
  - 「改的是 `hajcForOut.getSirsPostNo()`」只是依我們分析的推測，**沒有經過確認**。
  - 使用者對 HA 系統沒有權限：CVS `/cvsroot/ha` 回應 Permission denied，看不到版本歷史；TBHAM0／TBHAM1 也是管制表。本機 erp.war 的 `hajcForOut.java` 是 2022 年 1.102 版的舊複本。
- **TBHAM0／TBHAM1 是管制表**，網頁 SQL 命令中心查詢會逾時，無法驗證。
- **發現的程式問題**（還沒修）：
  1. `hajcForOut.getSirsPostNo()` 的 catch 宣告 `new String[1][2]`，卻寫入 `[0][2]`，會陣列越界；第 843～846 行的 `sirs[1][...]` 也一樣。錯誤被 `apjcUserAuthLevel.genLevel()` 的空 catch 吃掉，log 看不出原因。
  2. `hgjcb05Apply.sent()` 失敗後，畫面狀態沒有還原；訊息也沒有說明是抓不到簽核主管。
- 已提供測試 JSP（`hajcForOut.getSirsPostNo("26446")`、`apjcUserAuthLevel.getAuthList("18")`，JSP 內要用 `_dsCom`）。
- 已經口頭向尤柏智說明，不另外回信。ZPJJB01 每日工作記錄已新增（10/06 序號 001，1000～1300，工時 2.0，計劃類別 Q0910；說明中的 A01 已註明「承辦人尚未送出」，並補充「可用 ZZR00620（簽核層級清單）來查」）。
- 另外：`apjcUserAuthLevel` 今天有人提交 1.48 版（ch25690，調整重複主管問題），跟這次的錯誤無關。

- **✅ 結案（2026-10-06）**：HA 修改上線後，潘勝賢已重新送出 2026051066，確認能正常送簽。

## 下一步
- 已結案，沒有待辦。
- 參考：HGJJB05 送出失敗時的提示訊息與畫面狀態，仍可考慮調整（HG 系統）。
