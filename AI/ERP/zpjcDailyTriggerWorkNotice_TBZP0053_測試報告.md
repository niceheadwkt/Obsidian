# zpjcDailyTriggerWorkNotice／TBZP0053 測試機驗證報告

- 測試日期：2026/09/21
- 測試機：test.chsteel.com.tw
- 程式檔：[zpjcDailyTriggerWorkNotice.java](file:///D:/CHSBrowser_erp/erpHome/yl.ear/erp.war/zp/src/com/chsteel/zp/busi/zpjcDailyTriggerWorkNotice.java)
- 測試資料表：`DB.TBZP0053`（`SYSTEMID='ZP'`、`APPID='ZPJCDAILYTRIGGERWORKNOTICE'`）
- 對照文件：[zpjcDailyTriggerWorkNotice_analysis_report.md](file:///D:/CHSBrowser_erp/erpHome/yl.ear/erp.war/zp/zpjcDailyTriggerWorkNotice_analysis_report.md)
- log 來源：`ZPJCDAILYTRIGGERWORKNOTICE_ERP01.log`（手動觸發 DF 排程後匯出）

---

## 一、本次調整內容

### 1. 2026/09/15 版（`CLASS_VERSION v1.21`）既有修復

| 項目 | 修復前 | 修復後 |
|---|---|---|
| `eSign` 空字串判斷 | 只檢查 `has("eSign")`，未檢查是否為空字串；`"".split(";")` 產生長度 1 的固定陣列，誤走簽核流程並在 `personnel_list.add(...)` 時因 `Arrays.asList()` 不可變丟出 `UnsupportedOperationException`（訊息顯示為 `null`） | 改為 `has() && !trim後為空` 才視為有值，並一律以 `new ArrayList<>(...)` 包裝確保可變 |
| `cron` 小時欄位 | 寫死 `"4,5,6"`，排程只在凌晨 4:00~6:00 觸發時段內才會真正處理業務邏輯，異常錯過窗口即整天漏發 | 改為 `"*"`，只要日／月／星期條件仍符合，任何時間觸發都會處理 |

### 2. 本次測試中新發現並修復：`{maxPosNo:01}` 寫死問題

測試 `TEST_ESIGN_TEMPLATE`／`TEST_URL_APPROVAL`（`eSign:"{maxPosNo:08}"`）時發現，程式判斷「是否為模板」與呼叫展開 API 的參數都寫死比對字串 `"{maxPosNo:01}"`，導致非 `01` 的模板值（如 `08`）完全不會展開成主管清單，而是把整串字面文字當成「簽核人工號」直接送進簽核流程（不拋例外，但簽核對象是錯的）。

[zpjcDailyTriggerWorkNotice.java](file:///D:/CHSBrowser_erp/erpHome/yl.ear/erp.war/zp/src/com/chsteel/zp/busi/zpjcDailyTriggerWorkNotice.java) 第 167-168 行修復：

```java
// 修改前
if (sir_list.size() == 1 && "{maxPosNo:01}".equals(sir_list.get(0))) {
    List list_tmp = zpjcESignAPI.getESingAuthListByTemplate(dsCom_new, "{maxPosNo:01}");

// 修改後
if (sir_list.size() == 1 && sir_list.get(0).indexOf("{") != -1) {
    List list_tmp = zpjcESignAPI.getESingAuthListByTemplate(dsCom_new, sir_list.get(0));
```

判斷邏輯改成跟 [zpjcESignAPI.getESingAuthListByTemplate](file:///D:/CHSBrowser_erp/erpHome/yl.ear/erp.war/zp/src/com/chsteel/zp/esign/zpjcESignAPI.java) 內部自己認定模板的方式一致（`template.indexOf("{")==-1` 才視為字面工號清單），並把實際設定的字串動態傳入展開，不再限定只支援 `{maxPosNo:01}`。此 API 本身已支援 `{maxPosNo:NN}`、`{upper}`、`{deptNo:NN}`、`{userId}` 等多種模板語法。

**狀態：已修復、已 `erp_verify.py` 確認 Big5 編碼合法，等待系統 reload 後重新驗證。**

---

## 二、TBZP0053 資料結構

| 欄位 | 型態限制 | 說明 |
|---|---|---|
| `systemId` | VARCHAR(10) | 固定 `'ZP'` |
| `appId` | VARCHAR(50) | 固定 `'ZPJCDAILYTRIGGERWORKNOTICE'` |
| `keyId` | VARCHAR(50)，與 `systemId`＋`appId` 組成 PK | 每列一組獨立排程設定 |
| `content` | VARCHAR(3000) | JSON：`title`／`cron`／`detail[]`／`runMsg`／`runComplete`／`lastRunDate` |

正式機參考基準（`keyId='每季外部人員異動調查'`）：

```json
{
  "cron": "* * * 16 SEP ? *",
  "runMsg": "成功",
  "lastRunDate": "20260921",
  "detail": [
    {
      "eSign": "", "enable": "Y", "followUpEmp": "26622",
      "uniKey": "每季外部人員異動調查", "lastRunDate": "20260916",
      "runMsg": "成功", "runComplete": "Y",
      "reESignEmp": "", "mainFile": "", "applyEmp": "26622", "mainUrl": ""
    }
  ],
  "runComplete": "Y",
  "title": "每季外部人員異動調查"
}
```

該筆正式機資料本來就使用 `eSign` 空字串，等於已在正式機踩著本次修復的情境運作，是本次回歸測試的重點參照對象。

---

## 三、測試資料設計（13 筆，測試機 `TBZP0053`）

| keyId | 測試角度 |
|---|---|
| `TEST_BASELINE_NORMAL` | 回歸測試：比照正式機真實案例（`eSign` 空字串） |
| `TEST_CRON_NOMATCH` | cron 日期不符（沿用正式機原始 cron `16 SEP`，驗證僅時分秒被強制 `*`） |
| `TEST_ESIGN_NONE` | 不帶 `eSign` 欄位 |
| `TEST_ESIGN_BLANK` | `eSign` 為空白字元 |
| `TEST_ESIGN_SINGLE` | `eSign` 為單一工號（`25963`，非模板） |
| `TEST_ESIGN_TEMPLATE` | `eSign` 為 `{maxPosNo:08}` 模板 |
| `TEST_ESIGN_MULTI` | `eSign` 多工號（`26622;25963`） |
| `TEST_NO_FOLLOWUP` | 缺 `followUpEmp`（必填檢核） |
| `TEST_DUP_UNIKEY` | 同筆 `detail[]` 內 `uniKey` 重複 |
| `TEST_APPLYEMP_NOTEXIST` | `applyEmp` 不存在 DU01（`99999999`） |
| `TEST_ENABLE_N` | `enable="N"` 與未帶 `enable` 兩種情境 |
| `TEST_SKIP_TODAY` | 今日已執行過的防重跑 |
| `TEST_URL_APPROVAL` | `eSign` 模板 + `mainUrl` 分支 |

`applyEmp`／`followUpEmp` 皆為 `26622`（正式機已驗證存在），多人簽核情境第二工號用 `25963`。13 筆已於測試機用 SQL 命令中心（`dsjjsql.jsp`，CDP 連線登入分頁）逐筆 `INSERT` 寫入並以 `SELECT` 回查驗證內容無誤（中文標題、`{maxPosNo:08}`、`mainUrl` 皆正確保存）。

---

## 四、手動觸發執行結果（log 分析）

於測試機 `DFJJJOBTIMERMAIN` 手動觸發一次，13 筆依 `keyId` 字母序全數處理。

| keyId | 結果 | 依據 |
|---|---|---|
| `TEST_APPLYEMP_NOTEXIST` | ✓ 正確拋例外 | `applyEmp:99999999資料不存在DU01`（`:129`） |
| `TEST_BASELINE_NORMAL` | ✓ **修復核心驗證通過** | eSign 空字串，未再拋出舊版 `null`／`AbstractList.add` 例外，直接派工成功 |
| `TEST_CRON_NOMATCH` | ✓ 正確跳過 | `不符合cron:* * * 16 SEP ? * 不予執行` |
| `TEST_DUP_UNIKEY` | ✓ 正確擋下第 2 筆 | 第 1 筆 `DUP_TEST` 正常派工成功，第 2 筆同 `uniKey` 觸發「不可重複」（`:106`） |
| `TEST_ENABLE_N`（兩筆） | ✓ 皆正確跳過 | `enable:N 不予執行`，無後續派送 |
| `TEST_ESIGN_BLANK` | ✓ 修復驗證通過 | `eSign:" "` trim 後視為空，直接派工成功 |
| `TEST_ESIGN_NONE` | ✓ 修復驗證通過 | 不帶 `eSign`，同上 |
| `TEST_ESIGN_SINGLE` | ✓ **原始 bug 情境復現且已修復** | `eSign:"25963"` 單一元素不可變清單型態，`fileApproval` 正常無例外 |
| `TEST_ESIGN_MULTI` | ✓ 修復驗證通過 | `eSign:"26622;25963"` 多人清單，`personnel_list.add(0,...)` 正常執行 |
| `TEST_NO_FOLLOWUP` | ✓ 正確拋例外 | `沒有設定followUpEmp欄位`（`:188`） |
| `TEST_SKIP_TODAY` | ✓ 正確擋下重複執行 | `20260921 已執行過，不予執行` |
| `TEST_ESIGN_TEMPLATE` | ⚠ 發現問題 | `eSign:"{maxPosNo:08}"` 未拋例外，但 ESignVO `before/after` 的 `topApprove` 維持空白（同類正常案例會從空白變 `"08"`），證實模板未被展開，簽核對象錯誤 |
| `TEST_URL_APPROVAL` | ⚠ 發現問題 | 同上（`{maxPosNo:08}` 未展開），但 `mainUrl` 分支本身正確觸發 `urlApproval` |

---

## 五、TBZP0053 回寫內容比對

觸發後重新 `SELECT` 回查各筆 `content`，`runComplete`／`runMsg`／`lastRunDate` 與 log 完全吻合：

| keyId | 頂層 runComplete/runMsg | detail[] runComplete/runMsg |
|---|---|---|
| `TEST_APPLYEMP_NOTEXIST` | Y／成功 | N／`applyEmp:99999999資料不存在DU01` |
| `TEST_BASELINE_NORMAL` | Y／成功 | Y／成功 |
| `TEST_CRON_NOMATCH` | 空／空（未變動，僅 lastRunDate 更新為 20260921） | 空／空（未變動） |
| `TEST_DUP_UNIKEY` | Y／成功 | 第1筆：Y／成功；第2筆：N／不可重覆 |
| `TEST_ENABLE_N` | Y／成功 | 兩筆皆 N／空（從未真正執行） |
| `TEST_ESIGN_BLANK` | Y／成功 | Y／成功 |
| `TEST_ESIGN_MULTI` | Y／成功 | Y／成功 |
| `TEST_ESIGN_NONE` | Y／成功 | Y／成功 |
| `TEST_ESIGN_SINGLE` | Y／成功 | Y／成功 |
| `TEST_NO_FOLLOWUP` | Y／成功 | N／沒有設定followUpEmp資料 |
| `TEST_SKIP_TODAY` | Y／成功 | Y／成功（沿用預設值，本次未重跑，防重複機制生效） |
| `TEST_ESIGN_TEMPLATE` | Y／成功 ⚠ | Y／成功 ⚠（記錄成功，但實際簽核清單錯誤，詳見下方說明） |
| `TEST_URL_APPROVAL` | Y／成功 ⚠ | Y／成功 ⚠（同上） |

> `TBZP0053.content` 不會記錄實際簽核清單內容，因此 `TEST_ESIGN_TEMPLATE`／`TEST_URL_APPROVAL` 顯示的「成功」只代表程式沒有拋例外，**不代表主管清單正確**；此二筆為修復前那次觸發所留下的結果。

---

## 六、待辦事項

1. **確認 `{maxPosNo:01}` 寫死修復已 reload 生效**（系統管理端操作）。
2. 將 `TEST_ESIGN_TEMPLATE`／`TEST_URL_APPROVAL` 的 `content.detail[].runComplete` 重設為 `"N"`（或 `lastRunDate` 改為非今日），使其可於今日重新被觸發。
3. 重新手動觸發一次，改看 log 中 ESignVO `before/after` 的 `topApprove` 欄位是否從空白正確展開為有值，驗證 `{maxPosNo:08}` 模板修復是否生效。
4. 全部驗證通過後，清除測試資料：
   ```sql
   DELETE FROM db.tbzp0053
   WHERE systemId='ZP' AND appId='ZPJCDAILYTRIGGERWORKNOTICE' AND keyId LIKE 'TEST_%';
   ```
   同時確認測試過程中產生的簽核單／工作通知（`followUpEmp=26622`、`eSign` 涉及 `25963`）是否需要同步作廢，避免殘留待辦。
