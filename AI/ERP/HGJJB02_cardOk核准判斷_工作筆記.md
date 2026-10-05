# HGJJB02（承攬商工作證申請作業）cardOk 核准判斷 工作筆記

## 上次做到哪 (2026-10-01)
- **需求**：分析 `(HGJJB02) 承攬商工作證申請作業` 新增明細時，明細行 `cardOk`（是否核准）是怎麼取得的，以及 `checkValidDate()` 各規則引用了哪些程式。
- **核心結論**：
  - 畫面下拉 `v2.cardOk` 的值會帶進後端，Bs 也會先放進 `tbhg202.isOk`，但 `hgjcb02StaffEntity.create()／update()` 會呼叫 `checkValidDate()` 重新判斷，並**強制覆寫** isOk，所以畫面選的值實際上沒有作用。
  - `checkValidDate()` 共五段：規則 0 上傳資料跳過；規則 1 核發期限超出申請單；規則 2 人事基本資料必須存在（唯一的硬性檢核，會丟例外讓整張單回復）；規則 3 停權期間重疊（tbhg303）；規則 4 已有其他有效證件（tbhg202）。
  - 父類別的 `msg` 從來沒被賦值，實際只靠 `tips` 決定 isOk（有內容就是 N、isAllot 設為 Y）。
- **程式閱讀範圍**：
  - [hgjjb02Apply.jsp](file:///D:/CHSBrowser_erp/erpHome/yl.ear/erp.war/hg/jsp/hgjjb02Apply.jsp)、[hgjjGuestIdSelect.jsp](file:///D:/CHSBrowser_erp/erpHome/yl.ear/erp.war/hg/jsp/hgjjGuestIdSelect.jsp)
  - [hgjcb02Apply.java](file:///D:/CHSBrowser_erp/erpHome/yl.ear/erp.war/hg/src/com/icsc/hg/controller/hgjcb02Apply.java)（controller）
  - [hgjcb02ApplyBs.java](file:///D:/CHSBrowser_erp/erpHome/yl.ear/erp.war/hg/src/com/icsc/hg/bs/hgjcb02ApplyBs.java)（Bs）
  - [hgjcb02StaffEntity.java](file:///D:/CHSBrowser_erp/erpHome/yl.ear/erp.war/hg/src/com/icsc/hg/entity/hgjcb02StaffEntity.java)、`hgjcEntity.java`、`hgjcEntityFactory.java`
  - `hgjctb102VO／201DAO／202VO／202DAO／206VO／303DAO`
  - 框架：`html/de/dejtab09New.jss`、`WEB-INF/lib/de.jar` 的 `dejcWebInfoIn`、`dejcWebObjConverter`（用 javap 反組譯，確認 `getSequenceVOs` 是用反射呼叫 setter）
- **輸出成果**：
  - [HGJJB02_cardOk核准判斷分析.md](file:///D:/CHSBrowser_erp/erpHome/yl.ear/erp.war/hg/HGJJB02_cardOk核准判斷分析.md)（本機版，未加入 CVS）
  - 同一份已複製到本資料夾：[[HGJJB02_cardOk核准判斷分析]]
- **發現的問題（尚未修改程式）**：
  1. 規則 2：「無此人事基本資料」在同一個 try 裡被 `catch (Exception)` 接住，改丟「讀取人事基本資料異常」，使用者看不到真正原因。
  2. `tips = ""` 寫在規則 0 的 `return` 之後，Entity 被重複使用時，上傳資料可能沿用上一筆的 tips。
  3. 規則 1 用 `&&`（兩端都超出才算），而且新增時 202 的起迄日是直接從 201 複製的，所以永遠不會成立。
  4. 規則 3、4 的 `size() > 0` 判斷多餘；有多段重疊時只顯示第一段。
  5. `isAllot` 的用法跟註解「已製證」不一致。
- **踩坑紀錄**：
  - ERP 的原始碼是 Big5，用 `python open(..., encoding='cp950')` 轉成 UTF-8 存到 scratchpad 再讀；直接 print 到 console 會出現亂碼，要加 `sys.stdout.reconfigure(encoding='utf-8')`。
  - 報表範本 `xml/*.xml` 是 UTF-8，不是 Big5。
  - 框架 class 在 `WEB-INF/lib/de.jar`，可以用 `D:/CHSBrowser_erp/zulu-jdk8.0.322/bin/javap -c -p` 反組譯。

## 下一步
- 如果要修正第 1、2 點（規則 2 的訊息被蓋掉、tips 殘留），先確認需求再改 `hgjcb02StaffEntity.java`，改完用 `erp-cvs` 提交，並填 DAJJU1 上線申請。
- 確認畫面上的 cardOk 下拉是否需要真的讓承辦人手動否決；如果需要，要調整 Entity 覆寫的邏輯。
