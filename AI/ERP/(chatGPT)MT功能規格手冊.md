# MT 模組功能規格手冊

文件日期：2026-08-18

適用範圍：`D:\CHSBrowser_erp\erpHome\yl.ear\erp.war\mt`

## 1. 系統概述

### 1.1 系統定位

`MT` 模組為 ERP 系統中的進口材料、船運、信用狀、費用、付款及關帳相關作業模組。系統採用傳統 Java Web 架構，前端以 JSP 為主要畫面，後端以 Java 控制類別處理查詢、新增、修改、刪除、計算、產生單據與關帳等作業，資料存取則透過 DAO／VO 類別對應資料表。

本模組主要服務對象為採購、進口、財務、會計及系統維護人員，用於管理進口材料從採購／船運資料建立、信用狀與到貨資料維護、各類費用申請、付款／折讓／保險等處理，到月底成本或關帳資料產生的完整流程。

### 1.2 主要作業目標

- 建立與維護進口材料相關主檔與明細資料。
- 管理船運、信用狀、到貨、提單、材料項次與重量金額等資訊。
- 支援進口相關費用、應付帳款、發票、付款與折讓資料處理。
- 提供成本、費用、關帳與轉會計資料的彙總計算。
- 依使用者權限控制查詢、新增、修改、刪除、計算與列印功能。
- 提供共用查詢視窗、下拉選單、代碼轉換、銀行／供應商／客戶等輔助資料選取。

### 1.3 系統使用角色

| 角色 | 主要用途 |
| --- | --- |
| 採購／進口承辦 | 維護採購、船運、信用狀、到貨及材料明細資料。 |
| 財務／會計人員 | 處理費用申請、付款、應付帳款、傳票及關帳資料。 |
| 主管或審核人員 | 查詢資料狀態、核對金額、檢視列印報表。 |
| 系統管理人員 | 維護程式功能、訊息、序號、共用代碼與權限設定。 |

### 1.4 核心資料範圍

依 DAO 設定可辨識，本模組主要使用 `db.tbmt*` 系列表格。主要資料表整理如下：

| 資料表 | VO／DAO | 功能定位 | 主要用途 | 關聯功能 |
| --- | --- | --- | --- | --- |
| `db.tbmta010` | `mtjca010VO`／`mtjca010DAO` | A 類主檔或信用狀相關資料 | 維護 A 類作業主資料，作為船運、信用狀、金額與日期資料的基礎。 | `MTA01`、`mtjja02*`、`mtjca01` |
| `db.tbmta020` | `mtjca020VO`／`mtjca020DAO` | A 類明細或材料項次資料 | 維護採購項次、材料規格、重量、單價與金額等明細，並可彙總至 B 類資料。 | `MTA01`、`tbmtb020`、`tbmtp020` |
| `db.tbmta030` | `mtjca030VO`／`mtjca030DAO` | A 類附屬明細資料 | 保存 A 類作業延伸資料，支援多段資料維護。 | `MTA01`、`mtjja03*` |
| `db.tbmtb010` | `mtjcb010VO`／`mtjcb010DAO` | B 類主檔／船運主資料 | 維護船號、採購號、重量、匯率、商務費用、到港與船運相關主檔資訊。 | `MTB01`、`MTA01`、`MTD01`、費用計算 |
| `db.tbmtb020` | `mtjcb020VO`／`mtjcb020DAO` | B 類材料明細資料 | 保存船運或到貨項次資料，承接 A 類明細彙總後的材料、尺寸、重量與金額。 | `MTB01`、`MTA01`、`tbmta020` |
| `db.tbmtb030` | `mtjcb030VO`／`mtjcb030DAO` | B 類附屬資料 | 保存 B 類作業延伸資訊，支援第三層頁籤或明細維護。 | `MTB01`、`mtjjb03*` |
| `db.tbmtc010` | `mtjcc010VO`／`mtjcc010DAO` | C 類主檔資料 | 維護 C 類作業主資料，供後續明細、計算與列印使用。 | `MTC01`、`mtjjc01*` |
| `db.tbmtc020` | `mtjcc020VO`／`mtjcc020DAO` | C 類明細資料 | 保存 C 類作業明細，支援新增、修改、刪除與查詢。 | `MTC01`、`mtjjc02*`、`mtjjc03*` |
| `db.tbmtd010` | `mtjcd010VO`／`mtjcd010DAO` | D 類主檔資料 | 維護 D 類作業資料，並可與 FC 類費用資料進行備份、刪除或重建。 | `MTD01`、`tbmtfc030`、費用資料同步 |
| `db.tbmte010` | `mtjce010VO`／`mtjce010DAO` | E 類主檔資料 | 維護 E 類作業資料，供查詢、列印與後續關聯流程使用。 | `MTE01`、`MTG02` |
| `db.tbmtf010` | `mtjcf010VO`／`mtjcf010DAO` | F 類主檔資料 | 維護 F 類作業主資料，支援材料尺寸、重量與費用相關計算。 | `MTF01`、`mtjjf01*` |
| `db.tbmtf020` | `mtjcf020VO`／`mtjcf020DAO` | F 類明細資料 | 保存 F 類第一層明細資料。 | `MTF01`、`mtjjf02*` |
| `db.tbmtf030` | `mtjcf030VO`／`mtjcf030DAO` | F 類附屬明細資料 | 保存 F 類第二層明細或延伸資料。 | `MTF01`、`mtjjf03*` |
| `db.tbmtfc010` | `mtjcfc010VO`／`mtjcfc010DAO` | FC01 費用基礎資料 | 維護費用類基礎主檔或申請前置資料。 | `MTFC01`、費用申請流程 |
| `db.tbmtfc020` | `mtjcfc020VO`／`mtjcfc020DAO` | FC01／FC02 費用明細資料 | 保存費用類明細或階段性資料，供後續應付與付款流程使用。 | `MTFC01`、`MTFC02` |
| `db.tbmtfc025` | `mtjcfc025VO`／`mtjcfc025DAO` | FC02 延伸費用資料 | 保存 FC02 作業延伸資料或補充明細。 | `MTFC02`、費用計算 |
| `db.tbmtfc030` | `mtjcfc030VO`／`mtjcfc030DAO` | FC03 申請或費用主檔 | 作為應付、發票、費用產生與取消流程的核心資料。 | `MTFC03`、`MTD01`、`MTM01`、AP／Invoice |
| `db.tbmtfc040` | `mtjcfc040VO`／`mtjcfc040DAO` | FC03 應付主檔關聯資料 | 保存 AP 主檔產生或回寫所需資料。 | `MTFC03`、`createApMaster`、`cancelFC040` |
| `db.tbmtfc050` | `mtjcfc050VO`／`mtjcfc050DAO` | FC03 應付明細或發票關聯資料 | 保存 AP 明細、發票或費用明細回寫資料。 | `MTFC03`、`mtjjComExp`、`createApDetail`、`createInvoice` |
| `db.tbmtfc060` | `mtjcfc060VO`／`mtjcfc060DAO` | FC 類補充資料 | 保存 FC 類流程中的補充或中介資料。 | FC 類費用流程 |
| `db.tbmtfc065` | `mtjcfc065VO`／`mtjcfc065DAO` | FC 類發票或沖銷關聯資料 | 保存發票、付款或沖銷流程中的關聯資料。 | `MTFC03`、`MTFC05`、`mtjjComExp` |
| `db.tbmtfc070` | `mtjcfc070VO`／`mtjcfc070DAO` | FC04 付款或費用主檔 | 保存 FC04 階段資料，支援總額計算、更新與取消。 | `MTFC04`、`MTFC05`、`calcFC070Total` |
| `db.tbmtfc080` | `mtjcfc080VO`／`mtjcfc080DAO` | FC04 付款或費用明細 | 保存 FC04 明細資料，供付款、費用展開或後續修改使用。 | `MTFC04`、`MTFC05`、`mtjjComExp` |
| `db.tbmtfc090` | `mtjcfc090VO`／`mtjcfc090DAO` | FC05 付款或費用主檔 | 保存 FC05 階段主資料，支援匯率、付款、修改與取消。 | `MTFC05`、`calcFC090Total` |
| `db.tbmtfc100` | `mtjcfc100VO`／`mtjcfc100DAO` | FC05 付款或費用明細 | 保存 FC05 明細資料，供付款、折讓、費用展開與後續會計處理使用。 | `MTFC05`、`mtjjComExp`、`calcFC100Total` |
| `db.tbmtg020` | `mtjcg020VO`／`mtjcg020DAO` | 序號與編碼規則資料 | 維護表格欄位的序號產生規則，例如年、月、日、前綴、後綴與目前流水號。 | `MTG02`、`mtjcsn`、各類單號產生 |
| `db.tbmtm001` | `mtjcm001_vo`／`mtjcm001_dao` | 成本主檔資料 | 保存進口材料成本或月結主資料。 | `MTM01`、`mtjjMCost01` |
| `db.tbmtm002` | `mtjcm002_vo`／`mtjcm002_dao` | 成本附屬設定資料 | 保存成本類作業的補充設定或分類資料。 | `MTM01`、成本計算 |
| `db.tbmtm010` | `mtjcm010VO`／`mtjcm010DAO` | M 類主檔資料 | 維護 M 類成本或月結基礎資料。 | `MTM01`、`mtjcm01` |
| `db.tbmtm020` | `mtjcm020_vo`／`mtjcm020_dao` | 進口費用展開主資料 | 保存費用展開主資料，供關帳、反關帳、付款與費用產生使用。 | `mtjjComExp01`、`mtjcComExp01` |
| `db.tbmtm021` | `mtjcm021_vo`／`mtjcm021_dao` | 進口費用展開明細資料 | 保存費用展開第一層明細，支援重新計算與更新。 | `mtjjComExp02`、`mtjcComExp02` |
| `db.tbmtm022` | `mtjcm022_vo`／`mtjcm022_dao` | 進口費用展開附屬明細 | 保存費用展開第二層明細，並可產生 FC 類資料。 | `mtjjComExp03`、`mtjcComExp03`、`tbmtfc050`、`tbmtfc080`、`tbmtfc100` |
| `db.tbmtp010` | `mtjcp010VO`／`mtjcp010DAO` | 採購主檔引用資料 | 保存採購主檔資料，供船運與 A 類作業帶入採購號、合約、重量與供應商等資訊。 | `MTP01`、`MTA01`、`tbmtb010` |
| `db.tbmtp020` | `mtjcp020VO`／`mtjcp020DAO` | 採購明細引用資料 | 保存採購項次與材料明細，供進口材料、尺寸、重量與到貨資料回寫。 | `MTP01`、`MTA01`、`tbmta020`、`tbmtb020` |
| `db.tbmtpb010` | `mtjcpb010VO`／`mtjcpb010DAO` | PB 類基礎主資料 | 維護 PB 類基礎資料或付款分類主檔。 | `MTPB01`、基礎資料維護 |
| `db.tbmtpb020` | `mtjcpb020VO`／`mtjcpb020DAO` | PB 類基礎明細資料 | 保存 PB 類明細或分類資料。 | `MTPB01`、`mtjjpb0102*` |
| `db.tbmtpb07` | `mtjcpb07VO`／`mtjcpb07DAO` | PB07 基礎資料 | 保存特定 PB07 類別資料，供查詢與維護。 | `MTPB07`、`mtjjpb07*` |
| `db.tbmtsm010` | `mtjcsm010VO`／`mtjcsm010DAO` | 系統程式與訊息維護資料 | 維護系統代號、程式代號、程式名稱、維護人員與顯示訊息。 | `MTSM01`、`mtjjShowMsg`、權限與訊息顯示 |
| `db.tbmtCom01` | `mtjcCom01VO`／`mtjcCom01DAO` | 共用關帳／月結控制資料 | 保存公司、成本類別、資料年月、關帳日期、預估／實際傳票號碼與關帳狀態。 | `mtjjCom01`、`mtjjRaw01`、關帳／取消關帳／列印 |

### 1.5 權限與稽核概念

前端 JSP 頁面會依 `_AppId` 與使用者代號呼叫權限檢查，常見功能權限包含：

- `INSERT`：新增。
- `UPDATE`：修改。
- `DELETE`：刪除。
- `CALCULATE`：計算、彙總或產生相關資料。

後端 Java 類別於新增、修改、刪除與計算時，會寫入維護人員、維護日期、維護時間等欄位，並搭配交易控制進行資料一致性處理。

## 2. 系統架構總覽

### 2.1 目錄結構

| 目錄 | 說明 |
| --- | --- |
| `jsp` | 前端 JSP 畫面，包含主畫面、查詢、清單、編輯、列印、共用彈窗與工具頁。 |
| `src\com\icsc\mt` | 主要商業邏輯、控制流程、共用工具、批次與設定類別。 |
| `src\com\icsc\mt\web` | Web 入口 Servlet 類別，負責承接 JSP 表單送出的請求。 |
| `src\com\icsc\mt\dao` | DAO／VO 資料存取層，負責 SQL 與資料表對應。 |
| `src\com\icsc\mt\tag` | JSP 自訂標籤或選單元件，提供幣別、保險、品項、產品分類等下拉選單。 |
| `src\com\icsc\mt\util` | 日誌、字串與共用工具類別。 |
| `config\yl\mt` | 結構設定檔，例如 `mtStructs.xml`。 |
| `html` | 靜態 HTML、CSS、JSS 共用資源。 |
| `dao` | 外部 DAO 設定檔，與資料表操作定義相關。 |

### 2.2 架構分層

```text
使用者瀏覽器
  ↓
JSP 畫面層：mtjj*.jsp
  ↓
Web 入口層：mtjs*.java
  ↓
商業邏輯層：mtjc*.java
  ↓
資料存取層：mtjc*DAO.java／mtjc*VO.java
  ↓
資料庫：db.tbmt*、跨模組資料表
```

### 2.3 請求處理流程

1. 使用者由主頁或功能頁進入 `mtjj*.jsp`。
2. JSP 依 `_AppId` 檢查使用者可執行的功能按鈕。
3. 使用者執行查詢、新增、修改、刪除、列印或計算時，表單送至對應 `mtjs*.java`。
4. Web 入口類別整理請求參數，呼叫對應 `mtjc*.java` 商業邏輯。
5. 商業邏輯依 `txtFunc`、`_action` 或頁面參數判斷作業種類。
6. 商業邏輯透過 DAO 讀寫 `tbmt*` 資料表，必要時呼叫其他 ERP 模組 DAO。
7. 處理結果以 `HashMap`、VO、List 或 Vector 回傳 JSP 顯示。
8. 若作業涉及新增、修改、刪除、計算或產生單據，後端使用交易控制確保資料一致性。

### 2.4 主要程式命名規則

| 類型 | 命名範例 | 說明 |
| --- | --- | --- |
| JSP 主頁 | `mtjja01.jsp`、`mtjjfc05.jsp` | 功能入口頁，通常載入清單或頁籤。 |
| JSP 清單頁 | `mtjja01List.jsp` | 顯示查詢結果、執行批次操作、開啟編輯區。 |
| JSP 編輯頁 | `mtjja01Edit.jsp` | 單筆資料新增、修改、查詢與瀏覽。 |
| JSP 查詢頁 | `mtjja01Search.jsp` | 條件輸入或彈窗查詢。 |
| JSP 列印頁 | `mtjja01Print.jsp` | 報表或清單列印。 |
| Web 入口 | `mtjsa01.java` | 對應 `mtjja01*` 頁面表單送出。 |
| 商業邏輯 | `mtjca01.java` | 對應 A 類功能的後端處理。 |
| DAO | `mtjca010DAO.java` | 對應資料表讀寫。 |
| VO | `mtjca010VO.java` | 對應單一資料表欄位資料。 |

### 2.5 共用元件

| 元件 | 職責 |
| --- | --- |
| `mtjcController.java` | 共用控制入口或頁面導向支援。 |
| `mtjcCon.java` | 商業邏輯基底類別，提供交易、訊息、連線等共用能力。 |
| `mtjcCommon.java` | 幣別、銀行、供應商、品項、船運、費用總額與代碼轉換等共用查詢／計算。 |
| `mtjcSetting.java` | 共用訊息格式，例如查詢、新增、修改、刪除、計算成功或失敗訊息。 |
| `mtjcAuth.java` | 權限資訊設定與動作檢查支援。 |
| `mtjcsn.java` | 序號產生與登錄處理。 |
| `mtjcBatch.java` | 批次作業入口。 |
| `mtjcLogUtil.java` | 日誌紀錄工具。 |

### 2.6 新舊框架並存

本模組同時存在兩種畫面與請求風格：

- 舊式作業：JSP 表單直接送至 `mtjs*.java`，以 `txtFunc` 判斷 `Q`、`N`、`U`、`D`、`I`、`P`、`C` 等功能。
- 新式作業：JSP 送至 `/erp/mt/do?_pageId=...`，以 `_pageId` 與 `_action` 對應 Controller／CR 類別，例如 `mtjjCom01Edit`、`mtjjRaw01Edit`、`mtjjComExp01`。

## 3. 功能模組詳細說明

### 3.1 A 類作業：`MTA01`

| 項目 | 說明 |
| --- | --- |
| 主要頁面 | `mtjja01.jsp`、`mtjja01List.jsp`、`mtjja01Edit.jsp`、`mtjja01Search.jsp`、`mtjja02*`、`mtjja03*`、`mtjja04List.jsp` |
| Web 入口 | `mtjsa01.java` |
| 後端邏輯 | `mtjca01.java` |
| 主要資料表 | `tbmta010`、`tbmta020`、`tbmta030`、並與 `tbmtb010`、`tbmtb020`、`tbmtp010`、`tbmtp020` 互動 |

功能說明：

- 管理 A 類進口作業資料，依程式內容推定包含船運主檔、信用狀資料、明細項次與相關計算。
- 提供查詢、單筆查詢、新增、修改、刪除、列印、計算與產生資料等操作。
- 可由採購資料帶入船運資料，並依採購號、船號、信用狀號、項次等關鍵欄位建立關聯。
- 可計算重量、單價、外幣金額、新台幣金額、商務費用、押匯或相關費用。
- 可同步或更新採購明細資料，包含材料代碼、厚度、寬度、長度、重量等欄位。
- 可產生或取消外部 FL 相關資料，程式中可見 `createFlyl307`、`createFlyl308`、`deleteFlyl307`、`deleteFlyl308` 等處理。

主要作業：

| 作業 | 說明 |
| --- | --- |
| 查詢 | 依公司、船號、採購號、供應商、日期、信用狀等條件查詢。 |
| 新增 | 新增主檔、信用狀或明細資料。 |
| 修改 | 修改日期、金額、匯率、材料與船運相關欄位。 |
| 刪除 | 刪除主檔或明細，同步處理關聯資料。 |
| 計算 | 彙總重量、金額、費用、成本或信用狀相關金額。 |
| 列印 | 產生清單或單據列印資料。 |

### 3.2 B 類作業：`MTB01`

| 項目 | 說明 |
| --- | --- |
| 主要頁面 | `mtjjb01.jsp`、`mtjjb01List.jsp`、`mtjjb01Edit.jsp`、`mtjjb01Search.jsp`、`mtjjb01Print.jsp`、`mtjjb02*`、`mtjjb03*` |
| Web 入口 | `mtjsb01.java` |
| 後端邏輯 | `mtjcb01.java` |
| 主要資料表 | `tbmtb010`、`tbmtb020`、`tbmtb030` |

功能說明：

- 管理 B 類進口作業資料，與 A 類作業關係密切，依資料表與程式推定為船運、提單或到貨後續處理。
- 提供主檔與多段明細維護，包含查詢、新增、修改、刪除、列印。
- 可取得保險資料清單，程式中可見 `getInsuranceList`。
- 支援金額、重量與到貨資料的延伸處理。

### 3.3 C 類作業：`MTC01`

| 項目 | 說明 |
| --- | --- |
| 主要頁面 | `mtjjc01.jsp`、`mtjjc01List.jsp`、`mtjjc01Edit.jsp`、`mtjjc01Search.jsp`、`mtjjc01Print.jsp`、`mtjjc02*`、`mtjjc03*` |
| Web 入口 | `mtjsc01.java` |
| 後端邏輯 | `mtjcc01.java` |
| 主要資料表 | `tbmtc010`、`tbmtc020` |

功能說明：

- 管理 C 類進口作業資料，包含主檔與至少二組明細或子作業。
- 支援查詢、新增、修改、刪除、計算與列印。
- 可依頁面按鈕權限控制計算功能。
- 後端提供 `querySingle`、`querySingle1`、`querySingle2`，表示同一功能下存在多個資料層級或頁籤。

### 3.4 D 類作業：`MTD01`

| 項目 | 說明 |
| --- | --- |
| 主要頁面 | `mtjjd01.jsp`、`mtjjd01List.jsp`、`mtjjd01Edit.jsp`、`mtjjd01Search.jsp`、`mtjjd01Print.jsp`、`mtjjd02*`、`mtjjd03*` |
| Web 入口 | `mtjsd01.java` |
| 後端邏輯 | `mtjcd01.java` |
| 主要資料表 | `tbmtd010`，並與 `tbmtfc030` 有資料備份與重建關係 |

功能說明：

- 管理 D 類進口作業資料，包含主檔與多階明細。
- 支援查詢、新增、修改、刪除、計算、列印。
- 程式內含 `setBackupData`、`removeMTFC030`、`insertMTFC030`，表示此模組可重建或同步 FC 類費用資料。
- 適合歸類為費用產生前的基礎資料或異動資料管理。

### 3.5 E 類作業：`MTE01`／`MTG02`

| 項目 | 說明 |
| --- | --- |
| 主要頁面 | `mtjje01.jsp`、`mtjje01List.jsp`、`mtjje01Edit.jsp`、`mtjje01Search.jsp`、`mtjje01Print.jsp`、`mtjjg0201List.jsp`、`mtjjg0201Edit.jsp` |
| Web 入口 | `mtjse01.java`、`mtjsg02.java` |
| 後端邏輯 | `mtjce01.java`、`mtjcg02.java` |
| 主要資料表 | `tbmte010`、`tbmtg020` |

功能說明：

- `MTE01` 管理 E 類主檔資料。
- `MTG02` 與 `tbmtg020` 對應，依 `mtjcsn.java` 可推定與序號規則、表格欄位流水號或編碼維護相關。
- 支援資料維護、查詢、刪除及列印。
- 可提供其他模組自動產生單號或序號時使用。

### 3.6 F 類作業：`MTF01`

| 項目 | 說明 |
| --- | --- |
| 主要頁面 | `mtjjf01.jsp`、`mtjjf01List.jsp`、`mtjjf01Edit.jsp`、`mtjjf01Search.jsp`、`mtjjf01Print.jsp`、`mtjjf02*`、`mtjjf03*` |
| Web 入口 | `mtjsf01.java` |
| 後端邏輯 | `mtjcf01.java` |
| 主要資料表 | `tbmtf010`、`tbmtf020`、`tbmtf030` |

功能說明：

- 管理 F 類資料，包含一個主檔與兩組明細或附屬資料。
- 支援查詢、新增、修改、刪除、計算與列印。
- 後端包含厚度、寬度、長度轉換方法，可推定與材料尺寸、重量或單價計算有關。

### 3.7 FC01 至 FC05 費用／付款類作業

| 模組 | 主要頁面 | Web 入口 | 後端邏輯 | 主要資料表 |
| --- | --- | --- | --- | --- |
| `MTFC01` | `mtjjfc01.jsp`、`mtjjfc0101List.jsp`、`mtjjfc0102List.jsp`、`mtjjfc0102Edit.jsp` | `mtjsfc01.java` | `mtjcfc01.java` | `tbmtfc010`、`tbmtfc020`、`tbmtfc025` |
| `MTFC02` | `mtjjfc02.jsp`、`mtjjfc0201List.jsp`、`mtjjfc0201Edit.jsp` | `mtjsfc02.java` | `mtjcfc02.java` | `tbmtfc020`、`tbmtfc025` |
| `MTFC03` | `mtjjfc03.jsp`、`mtjjfc0301*`、`mtjjfc0302*`、`mtjjfc0303*` | `mtjsfc03.java` | `mtjcfc03.java` | `tbmtfc030`、`tbmtfc040`、`tbmtfc050`、`tbmtfc065` |
| `MTFC04` | `mtjjfc04.jsp`、`mtjjfc0401*`、`mtjjfc0402*` | `mtjsfc04.java` | `mtjcfc04.java` | `tbmtfc070`、`tbmtfc080` |
| `MTFC05` | `mtjjfc05.jsp`、`mtjjfc0501*`、`mtjjfc0502*`、`mtjjfc0503*` | `mtjsfc05.java` | `mtjcfc05.java` | `tbmtfc090`、`tbmtfc100`、並整合 `tbmtfc030`、`tbmtfc065`、`tbmtfc070`、`tbmtfc080` |

功能說明：

- FC 類為本模組中最密集的財務處理區，處理費用申請、應付資料、發票、付款、沖銷、取消與修改。
- 後端程式包含 `createApMaster`、`createApDetail`、`createInvoice`，表示會建立應付主檔、應付明細與發票資料。
- 支援 `updateFC040`、`updateFC050`、`updateFC070`、`updateFC080`、`updateFC090`、`updateFC100` 等不同階段資料回寫。
- 支援 `cancelFC040`、`cancelFC050`、`cancelFC070`、`cancelFC080`、`cancelFC090`、`cancelFC100` 等取消流程。
- `MTFC05` 額外支援匯率取得、付款或折讓資料修改，以及多個 FC 階段資料整合。

主要控制點：

| 控制點 | 說明 |
| --- | --- |
| 應付建立 | 產生 AP 主檔與明細資料。 |
| 發票建立 | 依申請或費用資料產生發票資料。 |
| 費用回寫 | 將付款、應付或發票狀態回寫至 FC 資料表。 |
| 取消作業 | 撤回已產生資料並同步還原關聯狀態。 |
| 金額彙總 | 透過共用方法重新計算申請總額。 |

### 3.8 M 類成本／月結作業：`MTM01`、`mtjjMCost*`

| 項目 | 說明 |
| --- | --- |
| 主要頁面 | `mtjjm01.jsp`、`mtjjm01List.jsp`、`mtjjm01Edit.jsp`、`mtjjMCost.jsp`、`mtjjMCost01.jsp`、`mtjjMCost02.jsp`、`mtjjMCost02List.jsp`、`mtjjMCost03.jsp` |
| Web 入口 | `mtjsm01.java` 或 `/erp/mt/do?_pageId=mtjjMCost*` |
| 後端邏輯 | `mtjcm01.java`、`mtjcMCost01.java`、`mtjcMCost02.java`、`mtjcMCost02List.java` |
| 主要資料表 | `tbmtm001`、`tbmtm002`、`tbmtm010`、`tbmtm020`、`tbmtm021`、`tbmtm022` |

功能說明：

- 管理進口材料成本、月結或成本分攤相關資料。
- 支援成本資料查詢、新增、修改、刪除、產生與發送。
- `mtjcMCost01` 含 `sendingM` 與 `createMCostId`，表示可產生成本批號並執行傳送或拋轉流程。
- `mtjcMCost02List` 含 `purge`，表示可清理或重建清單資料。
- 與 FC 類資料互動，支援費用資料重建、備份或同步。

### 3.9 共用關帳／原始資料重建作業：`mtjjCom01`、`mtjjRaw01`

| 項目 | 說明 |
| --- | --- |
| 主要頁面 | `mtjjCom01.jsp`、`mtjjCom01Edit.jsp`、`mtjjRaw01.jsp`、`mtjjRaw01Edit.jsp` |
| Web 入口 | `/erp/mt/do?_pageId=mtjjCom01Edit`、`/erp/mt/do?_pageId=mtjjRaw01Edit` |
| 後端邏輯 | `mtjcCom01CR.java`、`mtjcRaw01CR.java` |
| 主要資料表 | `tbmtCom01`，並與多個 `tbmt*` 資料表整合 |

功能說明：

- 提供關帳、重建、列印與傳票相關作業。
- 支援依公司、成本類別、資料年月、關帳日期查詢。
- 可產生預估或實際資料，並可取消已產生資料。
- `mtjcRaw01CR` 設有 `limitDate = "20240101"`，表示部分作業限制於 2024-01-01 以後資料。
- 提供列印作業 `PR1`，用於產生 Transaction 或外部資料輸出。

主要動作：

| 動作 | 說明 |
| --- | --- |
| `E`／`createE` | 產生預估類資料。 |
| `R`／`createR` | 產生實際或回轉類資料。 |
| `RR` | 重新整理或重建資料。 |
| `cancelE` | 取消預估類資料。 |
| `cancelR` | 取消實際或回轉類資料。 |
| `PR1` | 產生列印或交易資料。 |

### 3.10 進口費用展開作業：`mtjjComExp`

| 項目 | 說明 |
| --- | --- |
| 主要頁面 | `mtjjComExp.jsp`、`mtjjComExp01.jsp`、`mtjjComExp02.jsp`、`mtjjComExp03.jsp` |
| Web 入口 | `/erp/mt/do?_pageId=mtjjComExp01`、`mtjjComExp02`、`mtjjComExp03` |
| 後端邏輯 | `mtjcComExp01.java`、`mtjcComExp02.java`、`mtjcComExp03.java` |
| 主要資料表 | `tbmtm020`、`tbmtm021`、`tbmtm022`、`tbmtfc050`、`tbmtfc065`、`tbmtfc080`、`tbmtfc100` |

功能說明：

- 以頁籤方式呈現三段進口費用處理。
- 支援查詢、修改、刪除、匯出 Excel、關帳、反關帳、帳務付款與重新計算稅額。
- 可由成本資料產生 FC 類資料，例如 `addfc050`、`addfc065`、`addfc080`、`addfc100`。
- 可複製、建立與更新 `M020`、`M021`、`M022` 成本明細資料。

### 3.11 P 類與 PB 類資料作業

| 模組 | 主要頁面 | Web 入口 | 後端邏輯 | 主要資料表 |
| --- | --- | --- | --- | --- |
| `MTP01` | `mtjjp01.jsp`、`mtjjp01List.jsp`、`mtjjp01Edit.jsp`、`mtjjp01Search.jsp`、`mtjjp02*` | `mtjsp01.java` | `mtjcp01.java` | `tbmtp010`、`tbmtp020` |
| `MTPB01`／`MTPB07` | `mtjjpb01.jsp`、`mtjjpb0101*`、`mtjjpb0102*`、`mtjjpb07*` | `mtjspb01.java` | `mtjcpb01.java` | `tbmtpb010`、`tbmtpb020`、`tbmtpb07` |

功能說明：

- P 類資料依 DAO 與 A 類互動可推定為採購或採購明細相關資料。
- PB 類資料為基礎參數、付款或分類資料維護。
- 支援查詢、新增、修改、刪除與列印。
- 可供 A 類、B 類、FC 類及成本模組引用。

### 3.12 系統維護作業：`MTSM01`

| 項目 | 說明 |
| --- | --- |
| 主要頁面 | `mtjjsm01.jsp`、`mtjjsm01List.jsp`、`mtjjsm01Edit.jsp` |
| Web 入口 | `mtjssm01.java` |
| 後端邏輯 | `mtjcsm01.java` |
| 主要資料表 | `tbmtsm010` |

功能說明：

- 維護系統、程式代號、程式名稱、維護人員與訊息相關資料。
- 支援查詢、新增、修改、刪除與列印。
- 可由其他功能呼叫 `mtjjShowMsg.jsp` 顯示程式訊息。

### 3.13 共用查詢與輔助畫面

| 頁面 | 說明 |
| --- | --- |
| `mtjjbank.jsp`、`mtjjBankQry.jsp`、`mtjjBkAcctSel.jsp` | 銀行、分行或帳號查詢選取。 |
| `mtjjCustId.jsp`、`mtjjCustQry.jsp` | 客戶或供應商查詢選取。 |
| `mtjjShowSupplier.jsp` | 供應商資料顯示。 |
| `mtjjShowMsg.jsp` | 系統訊息維護或顯示。 |
| `mtjjOrderItemQry.jsp` | 訂單或項次查詢。 |
| `mtjjz001.jsp` | 使用者、部門或區域選取彈窗。 |
| `mtjjClose.jsp`、`mtjjClose1.jsp` | 關閉視窗或返回處理。 |
| `mtjjUtility*.jsp` | 共用 JSP 變數、日期格式、表單送出、列印與 UI 輔助功能。 |

### 3.14 批次與背景作業

| 程式 | 說明 |
| --- | --- |
| `mtjcBatch.java` | 批次入口，提供排程或人工批次執行的框架。 |
| `mtjcCom01CR.java` | 關帳與傳票資料產生／取消。 |
| `mtjcRaw01CR.java` | 原始資料或 Transaction 資料重建與列印。 |
| `mtjcMCost*.java` | 成本資料產生、傳送、清理與重建。 |

### 3.15 主要資料異動控制

本模組常見異動原則如下：

- 單筆新增前會檢查主鍵是否已存在。
- 修改與刪除時會先依主鍵查回原資料。
- 異動資料會補寫維護人員、維護日期與維護時間。
- 多表異動時使用交易控制，成功後提交，失敗時回復。
- 產生資料與取消資料通常成對存在，例如產生 AP、取消 AP、產生發票、取消發票。
- 計算後會回寫總額欄位，常見於 FC 類申請總額與船運成本。

### 3.16 對外或跨模組整合

程式中可見本模組會與下列外部或跨模組資料互動：

- 採購資料：`tbmtp010`、`tbmtp020`。
- 財務／會計資料：AP 主檔、AP 明細、發票與傳票相關 DAO。
- FL 模組資料：A 類作業中可產生或取消 FL 相關資料。
- 銀行／供應商／客戶資料：透過共用查詢與選單功能引用。
- 系統權限：透過 `_AppId` 與動作代號檢查使用者功能權限。

## 4. 附錄：主要模組對照表

| 模組代號 | 入口頁 | Web 入口 | 後端類別 | 用途摘要 |
| --- | --- | --- | --- | --- |
| `MTA01` | `mtjja01.jsp` | `mtjsa01` | `mtjca01` | A 類進口主作業、船運／信用狀／明細與計算。 |
| `MTB01` | `mtjjb01.jsp` | `mtjsb01` | `mtjcb01` | B 類後續資料、提單／到貨或保險相關處理。 |
| `MTC01` | `mtjjc01.jsp` | `mtjsc01` | `mtjcc01` | C 類資料維護與計算。 |
| `MTD01` | `mtjjd01.jsp` | `mtjsd01` | `mtjcd01` | D 類資料與 FC 資料同步／重建。 |
| `MTE01` | `mtjje01.jsp` | `mtjse01` | `mtjce01` | E 類資料維護。 |
| `MTF01` | `mtjjf01.jsp` | `mtjsf01` | `mtjcf01` | F 類資料、材料尺寸與明細處理。 |
| `MTFC01` | `mtjjfc01.jsp` | `mtjsfc01` | `mtjcfc01` | FC01 費用類基礎作業。 |
| `MTFC02` | `mtjjfc02.jsp` | `mtjsfc02` | `mtjcfc02` | FC02 費用類作業。 |
| `MTFC03` | `mtjjfc03.jsp` | `mtjsfc03` | `mtjcfc03` | 應付、發票、費用產生與取消。 |
| `MTFC04` | `mtjjfc04.jsp` | `mtjsfc04` | `mtjcfc04` | FC070／FC080 類付款或費用處理。 |
| `MTFC05` | `mtjjfc05.jsp` | `mtjsfc05` | `mtjcfc05` | FC090／FC100 類付款、匯率、修改與取消。 |
| `MTM01` | `mtjjm01.jsp` | `mtjsm01` | `mtjcm01` | M 類成本或月結基礎資料。 |
| `MTP01` | `mtjjp01.jsp` | `mtjsp01` | `mtjcp01` | 採購主檔與明細引用資料。 |
| `MTPB01` | `mtjjpb01.jsp` | `mtjspb01` | `mtjcpb01` | PB 類基礎或付款分類資料。 |
| `MTSM01` | `mtjjsm01.jsp` | `mtjssm01` | `mtjcsm01` | 系統程式與訊息維護。 |
| `mtjjCom01` | `mtjjCom01.jsp` | `/erp/mt/do` | `mtjcCom01CR` | 共用關帳、預估／實際資料產生與取消。 |
| `mtjjRaw01` | `mtjjRaw01.jsp` | `/erp/mt/do` | `mtjcRaw01CR` | 原始資料重建、列印與傳票相關作業。 |
| `mtjjComExp` | `mtjjComExp.jsp` | `/erp/mt/do` | `mtjcComExp01` 至 `03` | 進口費用展開、成本與 FC 資料產生。 |

## 5. 待確認事項

以下項目需由實際使用者、資料庫欄位中文說明或既有操作手冊補強：

- 各模組正式中文名稱。
- 各 `tbmt*` 資料表的欄位中文定義與主鍵規則。
- 每個 `txtFunc` 與 `_action` 在畫面上的正式按鈕名稱。
- 各類費用、付款、應付與傳票產生流程的實際會計規則。
- 與外部模組，例如採購、財務、會計、FL 系統的正式介面契約。
- 權限角色與各角色可執行功能矩陣。
