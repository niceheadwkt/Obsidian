# EAJJLICENSEBAT（證照整批新增版次作業）工作筆記

## 上次做到哪 (2026-09-22)
- **需求**：使用者要求整理 `(EAJJLICENSEBAT) 證照整批新增版次作業` 的操作功能，做成給使用者看的 md／PDF 操作手冊。
- **程式閱讀範圍**：
  - [eajjLicenseBat.jsp](file:///D:/CHSBrowser_erp/erpHome/yl.ear/erp.war/ea/jsp/eajjLicenseBat.jsp)（查詢列：證照類別必選、專責單位模糊查詢）
  - [eajjLicenseBatM1.jsp](file:///D:/CHSBrowser_erp/erpHome/yl.ear/erp.war/ea/jsp/eajjLicenseBatM1.jsp)（清單／輔助輸入批次帶值／修改／新增版本按鈕）
  - [eajcLicenseBat.java](file:///D:/CHSBrowser_erp/erpHome/yl.ear/erp.war/ea/src/com/chsteel/ea/eajcLicenseBat.java)（controller，flag R=修改／V=新增版本）
  - [eajcLicense.java](file:///D:/CHSBrowser_erp/erpHome/yl.ear/erp.war/ea/src/com/chsteel/ea/eajcLicense.java) 的 `updateOneRow`／`newVersionOneRow`（實際業務邏輯與 6 項驗證規則）
- **輸出成果**：
  - [EAJJLICENSEBAT_證照整批新增版次作業_操作手冊.md](file:///D:/CHSBrowser_erp/erpHome/yl.ear/erp.war/ea/EAJJLICENSEBAT_證照整批新增版次作業_操作手冊.md)
  - [EAJJLICENSEBAT_證照整批新增版次作業_操作手冊.pdf](file:///D:/CHSBrowser_erp/erpHome/yl.ear/erp.war/ea/EAJJLICENSEBAT_證照整批新增版次作業_操作手冊.pdf)（3 頁，含畫面截圖）
  - [EAJJLICENSEBAT_操作畫面.png](file:///D:/CHSBrowser_erp/erpHome/yl.ear/erp.war/ea/EAJJLICENSEBAT_操作畫面.png)（正式機截圖，已遮蔽個資）
- **PDF 產製踩坑（重要，下次遇到類似需求直接參考）**：
  - 第一次用 Chrome headless `--print-to-pdf` 直接列印 HTML，抽出文字檢查發現常用字（如「手」）被誤對應成康熙部首碼（U+2E80~U+2FDF 區段），視覺上多半看得出來但字碼是錯的，遇缺部首字集的字型/閱讀器會變空白方塊。
  - 改用 `reportlab` + `pdfmetrics.registerFont(TTFont(..., subfontIndex=0))` 內嵌 `C:\Windows\Fonts\msjh.ttc`（微軟正黑體）字型直接產生 PDF，逐頁轉 PNG 用肉眼複查＋程式掃描 `\u2e80-\u2fdf` 區段確認無誤植字元。
  - Emoji（如 ⚠️）在內嵌字型裡沒有對應字形會變空白，改用純文字符號（如「【注意】」）。
- **個資處理**：畫面截圖來自正式機真實資料，證書號碼／專責人員／證照名稱（連帶embed的真實姓名）／證照原始號碼、以及登入者姓名，皆用 PIL 依精確像素座標（用取樣掃描表格分隔線位置）加灰色遮罩後才嵌入文件。

## 下一步
- 若後續要交付其他同仁使用，確認遮蔽後的截圖／內容是否符合需求，或是否需要另外補充「新增版本」實際操作結果的畫面（目前只有查詢＋清單畫面，沒有截到操作後的成功訊息畫面）。
