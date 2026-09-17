# MP 採購管理系統功能規格手冊

> 版本：v1.0  
> 整理日期：2026-08-18  
> 整理範圍：`D:\CHSBrowser_erp\erpHome\yl.ear\erp.war\mp`  
> 依據來源：`config/yl/mp/mp_yl.ini`、`config/yl/mp/mp_app.ini`、`jsp`、`src/com/icsc/mp`、`dao`、`xml/dr` 目錄內容。

## 1. 系統概述

### 1.1 系統定位

MP 採購管理系統為 ERP 中的採購作業模組，主要支援 YL 公司別／廠別的採購流程。系統涵蓋從請購、採購方式決定、詢價、報價、議比價、訂購、信用狀申請、收貨、驗收、報支到付款查詢及報表列印等作業。

系統同時包含一般物料採購與特定鋼品採購作業，例如鋼胚、鋼捲相關請採購、規格維護與驗收流程。

### 1.2 使用對象

本系統主要使用對象包含：

- 請購單位：建立與維護物料請購資料。
- 採購人員：執行採購方式設定、詢價、議比價、訂單建立與訂單維護。
- 主管／簽核人員：執行簽核、核決與相關單據審閱。
- 驗收人員：處理收貨、驗收、勞務驗收、鋼胚與鋼捲驗收。
- 財會／報支人員：處理報支、發票通知、付款時程與付款查詢。
- 系統維護人員：維護基礎資料、流程設定、批次作業、報表與共用查詢。

### 1.3 系統目的

系統目的如下：

- 建立一致的採購作業流程，降低人工文件往返與資料重複輸入。
- 將採購生命週期資料集中管理，便於追蹤請購、詢價、訂購、驗收與付款狀態。
- 支援採購單據列印、簽核表、信用狀、驗收單、報支與統計報表產出。
- 提供鋼胚、鋼捲等特定物料的專用採購與驗收流程。
- 透過 DAO 與報表樣板分離資料存取與文件輸出，提升維護性。

### 1.4 系統範圍

本手冊整理的系統範圍包含：

- YL 採購作業入口設定。
- JSP 傳統 Web 畫面。
- Java 業務邏輯與控制類別。
- DAO 資料存取定義。
- 報表 XML／Jasper 樣板。
- HTML／Vue 行動或新式查詢頁面。

不包含範圍：

- ERP 整體登入、權限平台與跨系統主框架的完整規格。
- 外部系統實際介接 API 文件。
- 每一張資料表的完整欄位級資料字典。
- 每一張報表的逐欄格式規格。

## 2. 系統架構總覽

### 2.1 架構型態

本系統採用傳統 Java Web 應用架構，搭配 JSP、Java 業務類別、DAO 定義與報表樣板組成。主要架構分層如下：

| 層級 | 主要目錄／檔案 | 說明 |
| --- | --- | --- |
| 入口設定層 | `config/yl/mp/MP.ini`、`config/yl/mp/mp_yl.ini` | 定義公司別／廠別設定、功能頁面與 Java 類別對應。 |
| 前端畫面層 | `jsp`、`html` | 提供採購作業畫面、查詢頁、列印頁與輔助視窗。 |
| 控制／流程層 | `src/com/icsc/mp/controller`、`src/com/icsc/mp/flow` | 處理流程控制、簽核、單據流轉與報表控制。 |
| 業務邏輯層 | `src/com/icsc/mp/*.java` | 實作請購、詢價、報價、議價、訂單、驗收、報支等核心邏輯。 |
| 資料存取層 | `dao/*.dao`、`src/com/icsc/mp/dao` | 定義 TBMP 系列表格及相關資料存取。 |
| 報表輸出層 | `xml/dr/*.xml`、`xml/dr/*.jasper` | 定義 Jasper 報表樣板與列印輸出。 |
| 共用元件層 | `html/*.jss`、`src/com/icsc/mp/tag`、`src/com/icsc/mp/util`、`src/com/icsc/mp/sg` | 提供 JavaScript、公用標籤、選單、模糊查詢、工具方法與遠端資料選擇。 |

### 2.2 設定與入口關係

`config/yl/mp/MP.ini` 定義預設與 YL 設定檔對應：

| 設定鍵 | 設定值 | 說明 |
| --- | --- | --- |
| `default` | 空白 | 預設設定。 |
| `YL` | `mp_yl` | YL 公司別／廠別使用 `mp_yl.ini` 作為採購模組設定。 |

`config/yl/mp/mp_yl.ini` 定義主要功能入口，例如：

| 功能 | JSP 入口 | Java 類別 |
| --- | --- | --- |
| 物料請購單維護 | `jsp/mpjjYLReq.jsp`、`jsp/mpjjYLReqElec.jsp` | `com.icsc.mp.mpjcYLReqMAN`、`com.icsc.mp.mpjcYLReqValidation`、`com.icsc.mp.mpjcYLSerialNoMAN` |
| 請購單列印 | `jsp/mpjjReqP.jsp` | `com.icsc.mp.mpjcYLReqP` |
| 採購方式卡 | `jsp/mpjjYLIssue.jsp` | `com.icsc.mp.mpjcIssueP` |
| 詢價管理 | `jsp/mpjjYLRFQ.jsp` | `com.icsc.mp.mpjcYLRFQP` |
| 報價管理 | `jsp/mpjjDQuote.jsp` | `com.icsc.mp.mpjcQuoteP` |
| 議比價管理 | `jsp/mpjjYLMatch.jsp` | `com.icsc.mp.mpjcYLMatchP` |
| 訂單維護 | `jsp/mpjjYLPO.jsp` | `com.icsc.mp.mpjcPOP` |
| 信用狀申請 | `jsp/mpjjYLLCApply.jsp` | `com.icsc.mp.mpjcYLLCApplyP` |
| 收貨作業 | `jsp/mpjjConsign.jsp` | `com.icsc.mp.mpjcRcvP` |
| 驗收作業 | `jsp/mpjjYLCheckedHead.jsp`、`jsp/mpjjYLChecked2.jsp` | `com.icsc.mp.mpjcYLCheckedMAN`、`com.icsc.mp.mpjcCheckedP` |
| 報支作業 | `jsp/mpjjYLBillNew.jsp` | `com.icsc.mp.mpjcYLFC`、`com.icsc.mp.mpjcYLBillP` |
| 鋼胚請採購 | `jsp/mpjjSlabReq.jsp` | `com.icsc.mp.mpjcSlabReq` |
| 鋼捲請採購 | `jsp/mpjjCoilReq.jsp` | `com.icsc.mp.mpjcCoilReq` |
| 信用狀修狀 | `jsp/mpjjYLLCAmend.jsp` | `com.icsc.mp.mpjcYLLCAmend` |

### 2.3 主要資料與物件

系統資料存取以 `dao` 目錄下的 `tbmp*.dao` 與 `src/com/icsc/mp/dao` 內的 VO／DAO 類別為主。主要資料表可依採購流程與功能定位整理如下：

| 資料表 | VO／DAO | 功能定位 | 主要用途 | 關聯功能 |
| --- | --- | --- | --- | --- |
| `DB.TBMP10` | `mpjc10VO`／`mpjc10DAO` | 物料請購主檔 | 保存請購單表頭資料，例如公司別、請購單號、請購部門、請購日期、請購人、需求日期、預算、幣別、採購類別、請購狀態、承辦人與結案資料。 | 請購維護、電子請購、採購方式卡、詢價、訂購、請購查詢、請購列印 |
| `DB.TBMP11` | `mpjc11VO`／`mpjc11DAO` | 物料請購明細檔 | 保存請購項次、物料編號、品名、規格、數量、單位、預估單價、用途與交期等明細資料。 | 請購維護、請購項目查詢、詢價項目、報價、議比價、訂單轉入 |
| `DB.TBMP20` | `mpjc20VO`／`mpjc20DAO` | 採購方式／發詢處理主檔 | 保存採購案件、採購方式、發詢處理序號、發詢日期、開標日期、截止日期、採購依據與承辦資訊。 | 採購方式卡、詢價管理、採購案件查詢、採購流程控管 |
| `DB.TBMP21`～`DB.TBMP26` | `mpjc21VO`～`mpjc26VO`／`mpjc21DAO`～`mpjc26DAO` | 採購方式與詢價延伸明細 | 保存採購處理、供應商、發詢項目或相關補充資料，作為詢價與後續報價的延伸資料群。 | 採購方式卡、詢價單、詢價清單、供應商選擇 |
| `DB.TBMP30` | `mpjc30VO`／`mpjc30DAO` | 報價／議價資料檔 | 保存供應商報價、報價幣別、匯率、報價日期、有效期限、交期、議價單價、議價日期、報價狀態與訂單號。 | 報價管理、價格輸入、議比價管理、訂購簽核、訂單建立 |
| `DB.TBMP31` | `mpjc31VO`／`mpjc31DAO` | 報價／議價補充資料 | 保存報價作業衍生資訊，支援報價清單、議價結果或列印資料組裝。 | 報價管理、議比價簽核表、報價查詢 |
| `DB.TBMP40` | `mpjc40VO`／`mpjc40DAO` | 採購訂單主檔 | 保存訂購單表頭資料，例如訂購單號、訂購日期、採購案號、國內外別、供應商、合約、總金額、幣別、付款條件、貿易條件、信用狀號、訂單狀態與結案日期。 | 訂單維護、國內訂購單列印、國外訂購單列印、信用狀、收貨、驗收、報支 |
| `DB.TBMP41` | `mpjc41VO`／`mpjc41DAO` | 採購訂單明細檔 | 保存訂購項次、物料編號、品名、規格、訂購數量、單位、單價、交期與項次狀態等訂單明細資料。 | 訂單維護、訂單項目查詢、收貨、驗收、付款時程、訂單列印 |
| `DB.TBMP42`、`DB.TBMP42A`、`DB.TBMP42B` | `mpjc42VO`、`mpjc42aVO`、`mpjc42bVO`／`mpjc42DAO`、`mpjc42aDAO`、`mpjc42bDAO` | 訂單付款／條件延伸資料 | 保存訂單付款條件、費用、稅額或其他訂購條件延伸資料。 | 訂單維護、付款時程設定、報支、付款查詢 |
| `DB.TBMP43`、`DB.TBMP43A`、`DB.TBMP43HIS` | `mpjc43VO`、`mpjc43aVO`、`mpjc43HisVO`／`mpjc43DAO`、`mpjc43aDAO`、`mpjc43HisDAO` | 信用狀申請與異動資料 | 保存信用狀申請、修狀或歷史資料，支援國外採購信用狀流程。 | 信用狀申請、信用狀修狀、國外訂購、信用狀列印 |
| `DB.TBMP44`、`DB.TBMP44A` | `mpjc44VO`、`mpjc44aVO`／`mpjc44DAO`、`mpjc44aDAO` | 訂單變更或履約延伸資料 | 保存訂購異動、交貨或履約補充資料，支援訂單後續異動與追蹤。 | 訂單變更、合約訂單、交期管理、訂單查詢 |
| `DB.TBMP45` | `mpjc45VO`／`mpjc45DAO` | 訂單關聯／彙整資料 | 保存訂單或採購案延伸關聯資料，供查詢、彙整與特殊採購處理使用。 | 訂單維護、採購查詢、合約或特殊採購流程 |
| `DB.TBMP50` | `mpjc50VO`／`mpjc50DAO` | 收貨紀錄檔 | 保存收貨單號、訂單號、訂單項次、採購案號、發票、船運、匯率等收貨資訊。 | 收貨作業、PDA 收貨、收貨查詢、驗收作業、報支 |
| `DB.TBMP51` | `mpjc51VO`／`mpjc51DAO` | 驗收紀錄檔 | 保存驗收單號、訂單號、訂單項次、收貨單號、入庫單號、傳票號、驗收數量與驗收金額等資料。 | 一般驗收、勞務驗收、鋼胚驗收、鋼捲驗收、驗收單列印、報支 |
| `DB.TBMP51B`～`DB.TBMP51E` | `mpjc51bVO`～`mpjc51eVO`／`mpjc51bDAO`～`mpjc51eDAO` | 驗收延伸明細 | 保存不同驗收情境的補充資料，例如勞務驗收、扣款、驗收附件或特殊項目。 | 驗收暫存、勞務驗收、驗收查詢、付款資料 |
| `DB.TBMP60` | `mpjc60VO`／`mpjc60DAO` | 報支／付款主資料 | 保存報支單號、付款序號、發票號、收貨單號、驗收單號、訂購單號、信用狀申請號與報支日期等資料。 | 購案報支、發票通知書、付款查詢、付款報表 |
| `DB.TBMP60A`、`DB.TBMP60B`、`DB.TBMP60S` | `mpjc60aVO`、`mpjc60bVO`／`mpjc60aDAO`、`mpjc60bDAO` | 報支付款延伸資料 | 保存報支明細、付款補充或特殊付款狀態資料。 | 報支作業、付款查詢、財會核對 |
| `DB.TBMP61`、`DB.TBMP61A`、`DB.TBMP62` | `mpjc61VO`、`mpjc61aVO`、`mpjc62VO`／`mpjc61DAO`、`mpjc61aDAO`、`mpjc62DAO` | 付款／發票／報支延伸資料 | 保存付款、發票或報支後續處理資料，作為財會與報表查詢依據。 | 發票通知、付款時程、付款報表、報支統計 |
| `DB.TBMP80`、`DB.TBMP81` | `mpjc80VO`、`mpjc81VO`／`mpjc80DAO`、`mpjc81DAO` | 外部交易／供應商相關資料 | 保存外部交易、客戶／供應商、合約或網路採購相關資料。 | 電子交易、電子供應商、外部系統介接、供應商查詢 |
| `DB.TBMP800`、`DB.TBMP801`、`DB.TBMP802`、`DB.TBMP810`、`DB.TBMP811` | `mpjc800VO`、`mpjc801VO`、`mpjc802VO`、`mpjc810VO`、`mpjc811VO`／對應 DAO | 外部作業延伸資料 | 保存電子採購、電子檢驗、電子供應商或外部資料傳輸的延伸內容。 | 電子採購、電子檢驗、電子供應商、介接批次 |
| `DB.TBMP90`～`DB.TBMP95` | `mpjc90VO`～`mpjc95_vo`／`mpjc90DAO`～`mpjc95_dao` | 基礎設定與輔助資料 | 保存採購流程所需基礎設定、分類、代碼、對照或輔助查詢資料。 | 基礎資料維護、下拉選單、模糊查詢、共用代碼 |
| `DB.TBMPAUDIT`、`DB.TBMPAUDITITEM`、`DB.TBMPAUDITITEMSCORE` | `mpjcAuditVO`、`mpjcAuditItemVO`、`mpjcAuditItemScoreVO`／對應 DAO | 稽核資料 | 保存稽核主檔、稽核項目與評分資料。 | 稽核作業、稽核報表、供應商或採購績效檢核 |
| `DB.TBMPBOSSAGREE`、`DB.TBMPBOSSAGREESET` | `mpjcBossAgreeVO`、`mpjcBossAgreeSetVO`／`mpjcBossAgreeDAO`、`mpjcBossAgreeSetDAO` | 主管同意與簽核設定 | 保存主管同意資料與簽核設定條件。 | 主管同意、簽核流程、電子簽核表 |
| `DB.TBMPDOCFLOW`、`DB.TBMPDEPTFLOW` | `mpjcDocFlow_vo`、`mpjcDeptFlow_vo`／`mpjcDocFlow_dao`、`mpjcDeptFlow_dao` | 文件與部門流程設定 | 保存採購文件流程與部門流程設定。 | 文件流程、部門簽核、流程查詢 |
| `DB.TBMPCCVOM`、`DB.TBMPCCVOD`、`DB.TBMPCCVOSUMM`、`DB.TBMPCCVOSUMD` | `mpjcCCVOMVO`、`mpjcCCVODVO`、`mpjcCCVOSumMVO`、`mpjcCCVOSumDVO`／對應 DAO | CCVO 特殊業務資料 | 保存 CCVO 主檔、明細與彙總資料。 | CCVO 維護、CCVO 修訂、CCVO 彙總、CCVO 列印 |
| `DB.TBMPOTCO`、`DB.TBMPOTCOITEM`、`DB.TBMPOTCOSUM`、`DB.TBMPOTCOSUMITEM` | `mpjcOTCOVO`、`mpjcOTCOItemVO`、`mpjcOTCOSumVO`、`mpjcOTCOSumItemVO`／對應 DAO | OTCO 特殊業務資料 | 保存 OTCO 主檔、項目與彙總資料。 | OTCO 維護、OTCO 查詢、OTCO 彙總、OTCO 列印 |
| `DB.TBMPCPALI*` | `mpjcCPALIInspVO`、`mpjcCPALIPoVO`、`mpjcCPALIRateVO`、`mpjcCPALISumVO`／對應 DAO | CPALI 特殊業務資料 | 保存 CPALI 採購、檢驗、費率、文件與彙總資料。 | CPALI 維護、CPALI 彙總、CPALI 轉檔、進口或特殊採購流程 |
| `DB.TBMPE51*`、`DB.TBMPE61`、`DB.TBMPE62`、`DB.TBMPEGP*` | `mpjce51*_vo`、`mpjce61_vo`、`mpjce62_vo`、`mpjcegp*_vo`／對應 DAO | 電子採購／電子供應商資料 | 保存電子採購、電子供應商或電子流程相關資料。 | 電子請購、電子交易、電子供應商、外部平台介接 |
| `DB.TMPF01*`、`DB.TMPF02*` | `mpjcf01VO`、`mpjcf01dVO`、`mpjcf01ddVO`、`mpjcf02VO`／對應 DAO | 表單或流程輔助資料 | 保存表單、流程或列印相關輔助資料。 | 文件產生、流程控制、報表列印 |
| `DB.TBMPWORKDOC` | `mpjcWorkDoc_vo`／`mpjcWorkDoc_dao` | 工作文件資料 | 保存採購文件或工作單據資料。 | 文件流程、簽核、列印、附件或工作文件追蹤 |

> 備註：以上「功能定位」係依 DAO meta、VO／DAO 命名及既有功能入口整理。若需作為正式資料字典，仍需再逐一比對資料庫 schema、欄位中文說明、索引、外鍵與實際 SQL 使用情境。

### 2.4 報表與列印架構

報表樣板位於 `xml/dr`，主要支援：

- 請購單與電子簽核文件：`mpjrYLReqM.xml`、`mpjrYLReqElec.xml`、`mpjrSlabReqESign.xml`、`mpjrCoilReqESign.xml`。
- 詢價、報價、議比價：`mpjrYLQuote.xml`、`mpjrYLMatchM.xml`。
- 訂購與未結案統計：`mpjrOEPOM2.xml`、`mpjrUnClosePO.xml`、`mpjrUnClosePur.xml`、`mpjrUnPo.xml`。
- 信用狀：`mpjrYLLCApply.xml`、`mpjrYLLCApply01.xml`、`mpjrYLLCApply02.xml`。
- 驗收與付款：`mpjrCheckList.xml`、`mpjrPayQueryM.xml`、`mpjrPayRpt.xml`、`mpjrPaySQ.xml`。
- 稽核與違約：`mpjrAudit01.xml`、`mpjrAudit02.xml`、`mpjrAudit03.xml`、`mpjrViolateRpt.xml`。
- YL 統計報表：`mpjrYLBillCount.xml`、`mpjrYLRecvCount1.xml`、`mpjrYLCoilPur.xml`、`mpjrYLSlabPur.xml`。

### 2.5 新式查詢頁面

`html/app` 目錄包含 Vue／Framework7 類型的新式查詢頁面，例如：

- `mpjj01App.html`
- `mpwh002App.html`
- `mpwh003App.html`
- `mpwh004App.html`
- `mpwh005App.html`
- `mpwh006App.html`

其中 `mpwh003App.html` 為「年度扁鋼胚進耗存推移表」，透過 `/erp/zp/do` 呼叫 `zpSimpleQueryApp`，並使用 `config/yl/mp/mp_app.ini` 內的 SQL 設定取得年度選項，再以 `D0R01160`、`D0R01160A` 報表代碼查詢資料並繪製圖表。

## 3. 功能模組詳細說明

### 3.1 請購管理模組

#### 3.1.1 功能目的

提供使用單位建立、維護及送出物料請購資料，作為後續採購方式判定、詢價與訂單建立的來源。

#### 3.1.2 主要功能

- 物料請購單新增、修改、查詢與送出。
- 電子請購畫面支援。
- 請購單號產生與規則控管。
- 請購資料驗證。
- 請購單列印。
- 請購批次接辦作業。
- 請購項目查詢與合併提示。

#### 3.1.3 主要畫面與程式

| 作業 | 畫面 | Java 類別 |
| --- | --- | --- |
| 物料請購單維護 | `jsp/mpjjYLReq.jsp` | `mpjcYLReqMAN`、`mpjcYLReq`、`mpjcReq` |
| 電子請購 | `jsp/mpjjYLReqElec.jsp` | `mpjcReqElecBath`、`mpjcReqElecBatch` |
| 請購單列印 | `jsp/mpjjReqP.jsp`、`jsp/mpjjYLReqP.jsp` | `mpjcYLReqP`、`mpjcReqP` |
| 請購批次接辦 | `jsp/mpjjReqBath.jsp` | `mpjcReqBath` |
| 請購項目查詢 | `jsp/mpjjReqItemQuery.jsp` | `mpjcReqItemQuery` |

#### 3.1.4 主要輸入與輸出

- 輸入：請購部門、請購人員、物料、規格、數量、需求日期、用途、成本中心、專案號、採購類別。
- 輸出：請購單、請購明細、請購列印文件、後續採購處理資料。

#### 3.1.5 控制重點

- 請購單號需由序號管理邏輯產生。
- 請購資料需通過欄位與商業規則驗證。
- 請購狀態需可被後續採購流程追蹤。

### 3.2 採購方式卡模組

#### 3.2.1 功能目的

決定請購案件的採購方式與承辦資訊，作為詢價或直接訂購的前置作業。

#### 3.2.2 主要功能

- 採購方式卡維護。
- 採購方式卡列印。
- 採購承辦與採購條件設定。
- 指定供應商或採購處理方式。

#### 3.2.3 主要畫面與程式

| 作業 | 畫面 | Java 類別 |
| --- | --- | --- |
| 採購方式卡 | `jsp/mpjjYLIssue.jsp`、`jsp/mpjjIssue.jsp` | `mpjcIssue`、`mpjcIssueMAP` |
| 採購方式卡列印 | `jsp/mpjjYLIssueP.jsp`、`jsp/mpjjYLIssuePadd.jsp` | `mpjcIssueP` |
| 採購方式查詢 | `jsp/mpjjIssueList.jsp` | `mpjcIssue` |

#### 3.2.4 控制重點

- 採購方式應連動請購資料。
- 採購方式確認後，資料需可供詢價、報價或訂單模組引用。

### 3.3 詢價管理模組

#### 3.3.1 功能目的

依採購需求建立詢價資料，並向供應商或供應商群組發出詢價文件。

#### 3.3.2 主要功能

- 詢價單建立與維護。
- 詢價項目管理。
- 依群組列印詢價單。
- 依廠商列印詢價單。
- 詢價清單與查詢。

#### 3.3.3 主要畫面與程式

| 作業 | 畫面 | Java 類別 |
| --- | --- | --- |
| 詢價管理 | `jsp/mpjjYLRFQ.jsp`、`jsp/mpjjRFQ.jsp` | `mpjcRFQ`、`mpjcRFQMAP` |
| 詢價項目管理 | `jsp/mpjjRFQItemMan.jsp` | `mpjcRFQItemMan` |
| 詢價單列印 | `jsp/mpjjRFQP.jsp`、`jsp/mpjjYLRFQP01.jsp`、`jsp/mpjjYLRFQP02.jsp` | `mpjcYLRFQP`、`mpjcRFQP` |

#### 3.3.4 控制重點

- 詢價資料需保留與請購、供應商及採購項目的關聯。
- 列印格式需支援依群組與依廠商輸出。

### 3.4 報價管理模組

#### 3.4.1 功能目的

登錄供應商報價資料，支援後續比價與議價流程。

#### 3.4.2 主要功能

- 報價資料新增與維護。
- 報價清單查詢。
- 報價資料列印或簽核表輸出。
- 價格輸入輔助作業。

#### 3.4.3 主要畫面與程式

| 作業 | 畫面 | Java 類別 |
| --- | --- | --- |
| 報價管理 | `jsp/mpjjDQuote.jsp`、`jsp/mpjjQuote.jsp` | `mpjcQuote`、`mpjcQuoteMAP` |
| 報價清單 | `jsp/mpjjQuoteList.jsp` | `mpjcQuote` |
| 議比價簽核表 | `jsp/mpjjYLQuoteP.jsp`、`jsp/mpjjYLQuotePE.jsp`、`jsp/mpjjYLQuotePEItem.jsp` | `mpjcQuoteP`、`mpjcYLQuote` |
| 價格輸入 | `jsp/mpjjPriceInput.jsp`、`jsp/mpjjPriceInput2.jsp` | `mpjcPriceInput` |

#### 3.4.4 控制重點

- 報價需對應詢價單、供應商與採購項目。
- 報價資料需可供議比價模組比較與決議。

### 3.5 議比價管理模組

#### 3.5.1 功能目的

彙整各供應商報價，提供議比價、決標與訂購前簽核依據。

#### 3.5.2 主要功能

- 議比價資料維護。
- 供應商與報價比較。
- 訂購簽核單列印。
- 指定廠商轉訂單。

#### 3.5.3 主要畫面與程式

| 作業 | 畫面 | Java 類別 |
| --- | --- | --- |
| 議比價管理 | `jsp/mpjjYLMatch.jsp`、`jsp/mpjjMatch.jsp` | `mpjcYLMatch`、`mpjcMatch`、`mpjcMatchMAP` |
| 訂購簽核單列印 | `jsp/mpjjYLMatchP.jsp`、`jsp/mpjjMatchP.jsp` | `mpjcYLMatchP`、`mpjcMatchP` |
| 指定廠商訂單建立 | `jsp/mpjjPOSel.jsp` | `mpjcPOSel`、`mpjcPOSelMAP` |

#### 3.5.4 控制重點

- 議比價結果需能明確記錄決議供應商與決標條件。
- 通過後需可轉入訂單維護流程。

### 3.6 訂單管理模組

#### 3.6.1 功能目的

建立與維護採購訂單，管理國內外訂購單、訂單明細、付款條件與訂單異動。

#### 3.6.2 主要功能

- 訂單建立與維護。
- 國內訂購單列印。
- 國外訂購單列印。
- 訂單項目管理與查詢。
- 訂單付款時程設定。
- 訂單變更、合併、母訂單、長約與合約訂單處理。

#### 3.6.3 主要畫面與程式

| 作業 | 畫面 | Java 類別 |
| --- | --- | --- |
| 訂單維護 | `jsp/mpjjYLPO.jsp`、`jsp/mpjjPO.jsp` | `mpjcYLPO`、`mpjcPO`、`mpjcPOMAP` |
| 國內訂購單列印 | `jsp/mpjjYLPOP01.jsp` | `mpjcPOP` |
| 國外訂購單列印 | `jsp/mpjjYLPOP02.jsp` | `mpjcPOP` |
| 訂單項目管理 | `jsp/mpjjPOItemMan.jsp` | `mpjcPOItemMan` |
| 訂單項目查詢 | `jsp/mpjjPOItemQuery.jsp` | `mpjcPOItemQuery` |
| 付款時程設定 | `jsp/mpjjPayStone.jsp`、`jsp/mpjjPayStone2.jsp` | `mpjcPayStone`、`mpjcPayStoneM` |
| 訂單變更 | `jsp/mpjjPOAmd.jsp`、`jsp/mpjjCoilPOAmd.jsp` | `mpjcPO`、`mpjcCoilReq` |
| 合約訂單 | `jsp/mpjjContractPO.jsp`、`jsp/mpjjYlContractPO.jsp` | `mpjcLongContract` |

#### 3.6.4 控制重點

- 訂單資料需承接請購、詢價、報價與議比價結果。
- 訂單列印需依國內／國外格式分流。
- 付款時程需供後續報支與付款查詢使用。

### 3.7 信用狀管理模組

#### 3.7.1 功能目的

支援國外採購信用狀申請與修狀作業，並提供信用狀相關文件列印。

#### 3.7.2 主要功能

- 信用狀申請資料維護。
- 信用狀申請單列印。
- 信用狀修狀作業。
- 信用狀條款維護。
- 國外進口相關信用狀申請。

#### 3.7.3 主要畫面與程式

| 作業 | 畫面 | Java 類別 |
| --- | --- | --- |
| 信用狀申請 | `jsp/mpjjYLLCApply.jsp`、`jsp/mpjjYLLCApplyD.jsp` | `mpjcLCApply`、`mpjcLCApplyMAP`、`mpjcYLLCApply` |
| 信用狀申請列印 | `jsp/mpjjLCApplyP.jsp`、`jsp/mpjjYLLCApplyP01.jsp`、`jsp/mpjjYLLCApplyP02.jsp` | `mpjcYLLCApplyP` |
| 信用狀修狀 | `jsp/mpjjYLLCAmend.jsp`、`jsp/mpjjYLLCAmendP.jsp` | `mpjcLCAmend`、`mpjcLCAmendMAP`、`mpjcYLLCAmend` |
| 信用狀條款 | `jsp/mpjjLCTermEdit.jsp` | `mpjcLCApply` |

#### 3.7.4 控制重點

- 信用狀資料需與國外訂單連動。
- 修狀資料需可追溯原信用狀申請內容。

### 3.8 收貨與驗收模組

#### 3.8.1 功能目的

處理採購到貨、驗收、勞務驗收及特定鋼品驗收，形成付款與報支的依據。

#### 3.8.2 主要功能

- 收貨作業。
- 一般驗收作業。
- 勞務驗收作業。
- 驗收暫存資料。
- 驗收單列印。
- 鋼胚驗收。
- 鋼捲驗收。
- PDA 收貨支援。

#### 3.8.3 主要畫面與程式

| 作業 | 畫面 | Java 類別 |
| --- | --- | --- |
| 收貨作業 | `jsp/mpjjConsign.jsp` | `mpjcRcvP`、`mpjcReceiveQuery` |
| 一般驗收 | `jsp/mpjjYLCheckedHead.jsp`、`jsp/mpjjYLChecked2.jsp` | `mpjcYLCheckedMAN`、`mpjcYLChecked`、`mpjcChecked` |
| 勞務驗收 | `jsp/mpjjYLCheckedLaborServ.jsp` | `mpjcYLCheckedLaborServMAN`、`mpjcCheckedLaborServ` |
| 驗收暫存 | `jsp/mpjjYLCheckTmp.jsp` | `mpjcChecked` |
| 驗收單列印 | `jsp/mpjjYLCheckedP.jsp`、`jsp/mpjjYLCheckedP2.jsp` | `mpjcCheckedP` |
| 鋼胚驗收 | `jsp/mpjjSlabChecked.jsp` | `mpjcSlabChecked` |
| 鋼捲驗收 | `jsp/mpjjCoilChecked.jsp` | `mpjcCoilChecked` |
| PDA 收貨 | `jsp/mpjjRcvForPDA.jsp` | `mpjcRcvForPDA` |

#### 3.8.4 控制重點

- 驗收資料需對應訂單與收貨資料。
- 驗收完成後需作為報支、付款與統計報表依據。
- 勞務驗收與物料驗收應依不同資料欄位與流程處理。

### 3.9 報支與付款模組

#### 3.9.1 功能目的

處理採購案件報支、發票通知書列印、付款查詢與付款相關報表。

#### 3.9.2 主要功能

- 購案報支。
- 發票通知書列印。
- 付款查詢。
- 驗收付款查詢。
- 付款時程與付款報表。
- 報支統計。

#### 3.9.3 主要畫面與程式

| 作業 | 畫面 | Java 類別 |
| --- | --- | --- |
| 購案報支 | `jsp/mpjjYLBillNew.jsp`、`jsp/mpjjBillNew.jsp` | `mpjcYLFC`、`mpjcFCNew`、`mpjcBillNew` |
| 發票通知書列印 | `jsp/mpjjBillNewP.jsp` | `mpjcYLBillP`、`mpjcBillP` |
| 付款查詢 | `jsp/mpjjPayQuery.jsp`、`jsp/mpjjYLPayQuery.jsp` | `mpjcPayQuery`、`mpjcYLPayQuery` |
| 驗收付款查詢 | `jsp/mpjjChkPayQuery.jsp` | `mpjcChkPayQuery` |
| 付款報表 | `xml/dr/mpjrPayRpt.xml`、`xml/dr/mpjrPayQueryM.xml` | `mpjcPayReport`、`mpjcPayRpt` |

#### 3.9.4 控制重點

- 報支需以驗收完成資料為基礎。
- 發票與付款資料需與訂單、驗收資料一致。
- 查詢結果需支援財會核對與付款進度追蹤。

### 3.10 鋼胚與鋼捲專用採購模組

#### 3.10.1 功能目的

提供鋼胚、鋼捲等特定物料的請採購、規格維護、接案維護及驗收作業。

#### 3.10.2 主要功能

- 鋼胚請採購。
- 鋼捲請採購。
- 鋼胚規格維護。
- 鋼胚請採購接案維護。
- 鋼胚驗收。
- 鋼捲驗收。
- 鋼捲請購單列印。

#### 3.10.3 主要畫面與程式

| 作業 | 畫面 | Java 類別 |
| --- | --- | --- |
| 鋼胚請採購 | `jsp/mpjjSlabReq.jsp` | `mpjcSlabReq`、`mpjcSlabReqMAP` |
| 鋼捲請採購 | `jsp/mpjjCoilReq.jsp` | `mpjcCoilReq`、`mpjcCoilReqMAP` |
| 鋼捲請購列印 | `jsp/mpjjCoilReqP.jsp` | `mpjcCoilReqP` |
| 鋼胚規格維護 | `jsp/mpjjSlabSpec.jsp` | `mpjcSlabSpec`、`mpjcSlabSpecMAP` |
| 鋼胚接案維護 | `jsp/mpjjSlabCon.jsp` | `mpjcSlabCon`、`mpjcSlabConMAP` |
| 鋼胚驗收 | `jsp/mpjjSlabChecked.jsp` | `mpjcSlabChecked` |
| 鋼捲驗收 | `jsp/mpjjCoilChecked.jsp` | `mpjcCoilChecked` |

#### 3.10.4 控制重點

- 鋼品規格、材質、用途、交期與驗收條件需與一般物料採購分開管理。
- 專用請購資料需可銜接一般採購流程中的詢價、議價、訂單與驗收。

### 3.11 簽核與流程管理模組

#### 3.11.1 功能目的

支援採購文件簽核、主管同意、文件流程設定與流程查詢。

#### 3.11.2 主要功能

- 文件流程設定。
- 部門流程設定。
- 主管同意作業。
- 簽核畫面與簽核控制。
- 採購案件流程追蹤。
- 電子簽核報表輸出。

#### 3.11.3 主要畫面與程式

| 作業 | 畫面 | Java 類別 |
| --- | --- | --- |
| 主管同意 | `jsp/mpjjBossAgree.jsp` | `mpjcBossAgree` |
| 簽核作業 | `jsp/mpjjSign.jsp` | `mpjcCtrSign` |
| 文件流程 | `jsp/mpjjDocFlow.jsp` | `mpjcCtrDocFlow`、`mpjcCtrDoc` |
| 流程控制 | `jsp/mpjjFlow.jsp` | `mpjcCtrFlow`、`mpjcCtrFlow2`、`mpjcFlowCtrl` |
| 稽核作業 | `jsp/mpjjAudit01.jsp`、`jsp/mpjjAudit03.jsp` | `mpjcAudit01Func`、`mpjcAudit03Func` |

#### 3.11.4 控制重點

- 不同單據應依金額、部門、採購類別或文件狀態進入不同簽核流程。
- 流程節點與簽核紀錄需可查詢與列印。

### 3.12 供應商與基礎資料模組

#### 3.12.1 功能目的

提供採購作業所需的供應商、分類、物料、會計科目、專案、用途與基礎選單資料。

#### 3.12.2 主要功能

- 供應商查詢。
- 供應商分類選擇。
- 依品項查供應商。
- 物料查詢。
- 採購類別維護。
- 會計科目與帳戶查詢。
- 專案號、部門、人員與付款條件查詢。
- 下拉選單與遠端查詢標籤。

#### 3.12.3 主要畫面與程式

| 作業 | 畫面 | Java 類別 |
| --- | --- | --- |
| 供應商查詢 | `jsp/mpjjVendorQuery.jsp`、`jsp/mpjjVendorInquire.jsp` | `mpjcVendorQuery`、`mpjcVendorInquire` |
| 依品項查供應商 | `jsp/mpjjVendorByItem.jsp` | `mpjcVendorByItem` |
| 採購分類 | `jsp/mpjjCategory.jsp`、`jsp/mpjjCategoryM.jsp` | `mpjcCategory` |
| 會計科目 | `jsp/mpjjAccounting.jsp`、`jsp/mpjjChooseAccount.jsp` | `mpjcAccounting`、`mpjcAA`、`mpjcYLAA` |
| 共用查詢標籤 | `src/com/icsc/mp/tag`、`src/com/icsc/mp/sg` | `mpjcSelect*`、`mpjcSug*`、`mpjcRemote*` |

#### 3.12.4 控制重點

- 基礎資料需供各採購作業一致引用。
- 遠端查詢與模糊查詢需維持資料來源一致性。

### 3.13 合約、變更與特殊採購模組

#### 3.13.1 功能目的

支援合約訂單、長約、訂單變更、OTCO／CCVO 及 CPALI 等特殊採購或外部流程。

#### 3.13.2 主要功能

- 合約訂單維護。
- 長約資料處理。
- 訂單變更。
- OTCO 資料維護、彙總與列印。
- CCVO 資料維護、彙總與修訂。
- CPALI 相關作業、彙總與轉檔。

#### 3.13.3 主要畫面與程式

| 作業 | 畫面 | Java 類別 |
| --- | --- | --- |
| 合約訂單 | `jsp/mpjjContractPO.jsp`、`jsp/mpjjYlContractPO.jsp` | `mpjcLongContract` |
| 訂單變更 | `jsp/mpjjPOAmd.jsp`、`jsp/mpjjCoilPOAmd.jsp` | `mpjcPO`、`mpjcCoilReq` |
| OTCO | `jsp/mpjjOTCO.jsp`、`jsp/mpjjOTCOSum.jsp` | `mpjcOTCO01`、`mpjcOTCO02`、`mpjcOTCOSum01`、`mpjcOTCOSum02` |
| CCVO | `jsp/mpjjCCVO.jsp`、`jsp/mpjjCCVOSum.jsp` | `mpjcCCVO01`、`mpjcCCVO02`、`mpjcCCVOSum01`、`mpjcCCVOSum02` |
| CPALI | `jsp/mpjjCPALI.jsp`、`jsp/mpjjCPALISum.jsp`、`jsp/mpjjCPALITran.jsp` | `mpjcCPALI01`、`mpjcCPALISum01`、`mpjcCPALITran01` |

#### 3.13.4 控制重點

- 特殊採購資料需與一般訂單或外部流程保持關聯。
- 彙總、列印與轉檔需保留可追溯資料來源。

### 3.14 查詢、統計與報表模組

#### 3.14.1 功能目的

提供採購案件、訂單、收貨、付款、延遲、未結案與統計資料查詢。

#### 3.14.2 主要功能

- 採購案件查詢。
- 訂單查詢。
- 收貨查詢。
- 付款查詢。
- 延遲查詢與違約報表。
- 未結請購、未結訂單、未訂購資料查詢。
- YL 統計報表。
- 新式圖表查詢頁。

#### 3.14.3 主要畫面與程式

| 作業 | 畫面 | Java 類別／報表 |
| --- | --- | --- |
| 採購查詢 | `jsp/mpjjPurQuery.jsp`、`jsp/mpjjYLPurQuery.jsp` | `mpjcPurQuery`、`mpjcYLPurQuery` |
| 訂單查詢 | `jsp/mpjjPOQuery.jsp`、`jsp/mpjjOrderQuery.jsp` | `mpjcPOQuery`、`mpjcOrderQuery` |
| 收貨查詢 | `jsp/mpjjReceiveQuery.jsp` | `mpjcReceiveQuery` |
| 延遲查詢 | `jsp/mpjjDelayQuery.jsp`、`jsp/mpjjQueryDelay.jsp` | `mpjcDelayQuery`、`mpjcQueryDelay` |
| 違約報表 | `jsp/mpjjViolateRpt.jsp` | `mpjcViolateRptFunc`、`xml/dr/mpjrViolateRpt.xml` |
| 未結報表 | 無獨立入口確認，依報表樣板輸出 | `mpjrUnClosePO.xml`、`mpjrUnClosePur.xml`、`mpjrUnPo.xml` |
| 年度扁鋼胚進耗存推移表 | `html/app/mpwh003App.html` | `mp_app.ini`、`D0R01160`、`D0R01160A` |

#### 3.14.4 控制重點

- 查詢條件需支援採購單號、請購單號、供應商、日期、狀態等關鍵條件。
- 報表結果需與交易資料一致，並可支援列印或匯出。

### 3.15 批次與介接模組

#### 3.15.1 功能目的

支援採購資料批次處理、外部系統介接與通知作業。

#### 3.15.2 主要功能

- 批次作業管理。
- 外部資料接收或轉入。
- 電子採購、電子交易、電子檢驗、電子供應商資料處理。
- MQ 接收。
- 郵件或通知發送。
- 檔案下載與資料匯出。

#### 3.15.3 主要畫面與程式

| 作業 | 畫面 | Java 類別 |
| --- | --- | --- |
| 批次作業 | `jsp/mpjjBatchJob.jsp`、`jsp/mpjjBatchJob01.jsp` 至 `jsp/mpjjBatchJob06.jsp` | `mpjcBatchJob01` 至 `mpjcBatchJob06` |
| 電子交易 | `jsp/mpjjETrade.jsp` | `mpjcETrade01`、`mpjcETrade02`、`mpjcETrade03` |
| 電子供應商 | `jsp/mpjjEVendor.jsp` | `mpjcEVendor`、`mpjcEVendor02`、`mpjcEVendor03` |
| 電子檢驗 | `jsp/mpjjEInspection.jsp` | `mpjcEInspection` |
| MQ 接收 | 無 JSP 入口確認 | `mpjcMQRecv_SSJ109`、`mpjcMQRecv_SSJ209` |
| 通知 | `jsp/mpjjSendMessage.jsp`、`jsp/mpjjReserveNotify.jsp` | `mpjcSendMessage`、`mpjcReserveNotifyFunc` |
| 檔案下載 | `jsp/util/mpjjDownload.jsp` | `mpjcFileDownload` |

#### 3.15.4 控制重點

- 批次作業需保留執行結果與錯誤訊息。
- 介接資料需有格式驗證與例外處理。
- 外部作業需與採購主流程資料保持一致。

## 4. 主要採購流程摘要

### 4.1 一般採購流程

1. 使用單位建立請購單。
2. 系統執行請購資料驗證與單號控管。
3. 採購單位建立採購方式卡。
4. 依採購方式進行詢價或直接採購。
5. 供應商報價資料登錄。
6. 採購人員進行議比價與決標。
7. 建立採購訂單。
8. 供應商交貨後進行收貨與驗收。
9. 驗收完成後進入報支與付款作業。
10. 系統提供查詢、列印與統計報表。

### 4.2 國外採購與信用狀流程

1. 建立國外採購訂單。
2. 建立信用狀申請資料。
3. 列印信用狀申請文件。
4. 必要時進行信用狀修狀。
5. 後續依訂單進行收貨、驗收與付款。

### 4.3 鋼胚／鋼捲採購流程

1. 建立鋼胚或鋼捲請採購資料。
2. 維護鋼胚規格或鋼捲相關資料。
3. 銜接詢價、報價、議比價與訂單流程。
4. 到貨後執行鋼胚或鋼捲專用驗收。
5. 完成驗收後進入報支、付款與統計報表。

## 5. 後續補強建議

若要將本手冊提升為完整交付版，建議補齊下列內容：

- 每個 JSP 畫面的欄位清單、按鈕功能與狀態控制。
- 每個主流程的狀態碼與狀態轉換圖。
- `dao/*.dao` 對應資料表、主鍵與欄位定義。
- 簽核流程條件，例如金額、部門、採購類別與主管層級。
- 報表樣板逐張欄位、資料來源與輸出格式。
- 外部系統介接規格，例如會計、庫存、供應商、電子採購與 MQ。
- 例外處理規格，例如退件、作廢、變更、取消結案與重送。
