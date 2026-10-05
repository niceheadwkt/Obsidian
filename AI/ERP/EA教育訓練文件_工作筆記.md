# EA 系統新進人員教育訓練文件 工作筆記

## 上次做到哪 (2026-10-02)
- **需求**：製作給新進員工的 EA（安環績效管理系統）教育訓練文件，格式 HTML。
- **最終版定案方向**（使用者指示）：
  - 不放資訊窗口選單資料表與權限機制（屬 DS 系統，非 EA）。
  - 章節依資訊窗口 EA 選單分類編排，每支作業說明「用途、主要功能、管制與限制、不妥之處／建議調整」。
- **輸出成果**：[EA系統新進人員教育訓練.html](file:///D:/CHSBrowser_erp/erpHome/yl.ear/erp.war/ea/EA系統新進人員教育訓練.html)（UTF-8，單檔，尚未提交 CVS、未發布）
  - 11 章、89 支作業；附錄 A 自動通知與排程、附錄 B 待改善事項 441 項（可搜尋篩選）、附錄 C 選單上看不到的 27 個舊節點。
- **資料來源**：
  - 正式機（erp-prod-web-executor，唯讀）：TBDSDF／TBDSMF 遞迴查 `AIEA` 選單樹、TBDSAF／TBDSA1 權限、TBDFJOB（SYSID='EA'）排程、TBZP100A 資料字典、TBEADOCTYPE／TBEADOCSTATUS。
  - 程式碼：7 個子代理分組讀 JSP／Controller（cp950），結果 JSON 在 session scratchpad（res_*.json）。
- **重要發現**：
  - `EABATCHLAWSOVER`（法規查核追蹤）DF 實際設定為**每週一 02:40**，但說明與需求單 RQ11306027 寫每週二；Outlook 查無林孜容要求改時間的信。2026/5/18（週一）使用者確有收到通知。
  - `EABATCHLAWSFULLOVER` cron `0 30 2 ? 2-6 3 *` ＝ 2～6 月每週二 02:30，與 2025/8/19 林孜容需求一致。
  - 7 個 EA DF 工作未設執行失敗通知群組（只有 3 個新工作設 EASYSMGR）。
  - 高優先待改善：證照整批清單頁可執行任意 SQL（eajjLicenseBatM1.jsp）、證照列印 whereStr 串接 SQL、多數強制刪除／修改權限只在前端、eaStructs.xml 多個 action 指向不存在方法、環保許可新版本 IndexOutOfBounds、事故 IsAgreeEnd 條件錯誤（eajcUtil.java:2776）。
  - 舊 `EA功能規格手冊.md`（AI 產生）有多處錯誤：通報 10～40 分類、證照 30/60/90 天、CDSDoc 非 CEMS 等。

## 下一步
- 與 M9 確認 `EABATCHLAWSOVER` 應為週一或週二；若改週二可用 cron `0 40 2 ? * 3 *`。
- 依附錄 B 優先項目評估開需求單修正（建議先在測試機逐項驗證，目前僅為讀碼結論）。
- 確認附錄 C 的舊節點是否移除或改掛目錄。
- 決定教材是否發布分享連結（教材不提交 CVS）。
