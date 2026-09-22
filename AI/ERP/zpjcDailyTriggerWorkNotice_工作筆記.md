# zpjcDailyTriggerWorkNotice 工作筆記

## 上次做到哪 (2026-09-22)
- **程式**：[zpjcDailyTriggerWorkNotice.java](file:///D:/CHSBrowser_erp/erpHome/yl.ear/erp.war/zp/src/com/chsteel/zp/busi/zpjcDailyTriggerWorkNotice.java)（每日觸發工作通知排程，設定存於 `DB.TBZP0053`）。
- **測試機建了 13 筆 `TBZP0053` 測試資料**（`keyId` 前綴 `TEST_`），涵蓋 eSign 空字串/單一/多工號/模板、無效工號、uniKey 重複、enable 停用、防重複執行、mainUrl 分支等角度，並手動觸發 DF 排程驗證，結果與比對整理於 [zpjcDailyTriggerWorkNotice_TBZP0053_測試報告.md](file:///D:/CHSBrowser_erp/erpHome/yl.ear/erp.war/zp/zpjcDailyTriggerWorkNotice_TBZP0053_測試報告.md)。
- **發現並修復 `{maxPosNo:01}` 模板展開機制的兩層問題**：
  1. 判斷模板與展開 API 呼叫都寫死比對 `"{maxPosNo:01}"`，非 01 的層級（如 08）不會展開。
  2. `sir_list` 只有在申請人自己出現在展開清單裡（`index != -1`）才會被賦值，但正常情況下申請人本來就會被 `getAuthList()` 過濾掉，導致模板展開實質上從未生效；且原 `subList(0, index)` 方向錯誤（取到較低階，應取較高階）。
  - 已修正並用 `erp_verify.py` 確認 Big5 編碼合法，已於 Eclipse Team Commit 到 CVS。
- **✅ 修復已重新部署並驗證通過**：重新手動觸發排程後，比對 `ZPJCDAILYTRIGGERWORKNOTICE_ERP01.log`，`TEST_ESIGN_TEMPLATE`／`TEST_URL_APPROVAL` 兩筆的 `getESingAuthListByTemplate` 均正確觸發（`before.template={maxPosNo:08}`），ESignVO `topApprove` 由空白正確展開為 `"08"`；其餘 11 筆測資行為與第一輪測試一致，無例外、無退化。驗證明細已補進測試報告第七節。

- **✅ 測試殘留已全部清理**：17 筆 `db.tbzpESign` 測試簽核單/工作通知已作廢（`status=99`），連帶的 TBDW11 待處理代辦與系統提示通知共 54 筆全數刪除（第一輪 48 筆＋事後補漏 6 筆）；`TBZP0053` 的 13 筆 `TEST_%` 測試資料也已刪除。複查皆為 0 筆殘留。`25963` 全程未受影響。
- 執行方式：SQL 命令中心單一語句有 10 筆異動上限，改寫 Python 腳本透過既有 CDP 連線分批（≤10 筆／批）送出 SQL 完成，未走 DF 批次排程。
- **踩坑記錄**：測試機 DF 排程實際是**每小時觸發一次**，不是只有兩次手動觸發；`TEST_APPLYEMP_NOTEXIST`／`TEST_DUP_UNIKEY`／`TEST_NO_FOLLOWUP` 這 3 筆必定失敗的測資不受「當日已執行」防重複機制擋下，每小時都會重新產生失敗通知，第一輪清理只鎖定 2 個已知時間窗因而漏掉 05:00／06:00 各 3 筆。之後用 SELECT 不限定時間窗、只用 `USERID+WORKITEMSTATE='01'` 廣查才抓到全部殘留。

## 下一步
- `zpjcDailyTriggerWorkNotice` 這次修復（`{maxPosNo:08}` 模板展開）已測試、驗證、清理完畢，暫無待辦。
