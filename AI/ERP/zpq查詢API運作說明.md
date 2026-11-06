---
title: zpq 查詢 API 運作說明
date: 2026-11-06
tags: [ERP, zpq, 查詢API, ZP, 連線池]
---

# zpq 查詢 API 運作說明

> 整理自 2026-11-06 對話。依據本機原始碼：
> - 用戶端 `C:/Users/ch26788/.zpq/zpq.py`（v3.1）
> - 端點 `erp.war/zp/jsp/zpjjQueryApi.jsp`（CVS 1.5，v3.4，ch26295）
> - 核發頁 `erp.war/zp/jsp/zpjjQueryApiToken.jsp`（CVS 1.11，v3.3.6，ch26295）
> - 設定頁 `erp.war/zp/jsp/zpjjQueryApiAdm.jsp`（CVS 1.2，v3.3，ch26295）
>
> 三支 JSP 都是 26295 負責，不屬於 EA。全專案只有這三支 JSP 會參照 `zpjjQueryApi`，沒有 Java 或 XML 程式依賴它。

## 一、整體架構

zpq 本身沒有資料庫連線，它是一支 Python 小程式。每次執行時，它用 HTTP POST 把查詢送到 ERP 正式機上的查詢 API（一支 JSP），由 ERP 那邊去查 DB2，再把結果用 JSON 傳回來。

```
zpq（本機 Python）
   │  HTTP POST，表單編碼 cp950，標頭 X-API-TOKEN
   ▼
http://erp.chsteel.com.tw/erp/zp/jsp/zpjjQueryApi.jsp
   │  在 ERP 伺服器端：驗證 Token、檢查等級與管制群組、只放行唯讀 SQL、限制列數與次數
   ▼
ERP 共用連線池 jdbc/dsyl → 正式機 DB2
   │
   ▼
JSON 回傳 → zpq 排成表格印出
```

- 所有權限控管都在伺服器端的 JSP 裡，本機改不了，所以不能繞過，也不需要在本機設定資料庫帳號。
- 因為走的是 ERP 網頁伺服器，只要能連到 `erp.chsteel.com.tw` 就能用，不需要裝 DB2 Client。

## 二、用戶端 zpq.py

| 項目 | 說明 |
|---|---|
| 端點網址 | 依序取環境變數 `ZPQ_URL`、`%USERPROFILE%/.zpq/url` 第一行，都沒有就用預設的 `zpjjQueryApi.jsp` |
| Token | 程式自己從 `%USERPROFILE%/.zpq/token` 讀出來放進請求，不會出現在命令列，也不會印到輸出或錯誤訊息裡 |
| 編碼 | SQL 用 cp950（Big5）編碼後送出；有 Big5 存不了的字，送出前就擋下，結束碼 2 |
| 重試 | 伺服器忙碌（HTTP 429／503）而且回應說可以重試時，依回應建議的秒數自動等，最多等 15 秒、重試 2 次 |
| 到期提醒 | 到期前 5 天起，每天第一次執行會在桌面跳出「要不要展延 Token」視窗 |

**指令和送出參數的對應**

| zpq 指令 | 送出的參數 |
|---|---|
| `zpq "SELECT ..."` | `action=query`、`sql`、`rows` |
| `--describe TB...` | `action=describe`、`table` |
| `--tables --prefix/--q` | `action=tables` |
| `--user` / `--user-name` | `action=user`、`no` / `name` |
| `--ping` | `action=ping` |

**結束碼**：0 成功；2 查詢被拒或 SQL 錯誤（修正後再送）；3 忙碌，重試後仍失敗；4 Token 問題；5 設定或連線錯誤。

## 三、查詢端點 zpjjQueryApi.jsp

### 1. 安全模型
資料庫層沒有另外控管，端點直接借用 ERP 共用的連線池 `jdbc/dsyl`，所有防護都寫在這支 JSP 裡：
1. 來源要是公司內網，加上個人 Token；Token 在伺服器只存 SHA-256 雜湊，用固定時間比對。
2. 自己把 SQL 拆成一個個詞來檢查：只允許一句 SELECT 或 WITH 查詢；寫入、異動語法判為嚴重違規；表格採允許清單。
3. 交易防線：關掉自動 commit 執行，程式註解寫「不論結果一律 rollback」。
4. 資源限制：每句逾時 10 秒；限制列數；Token 和全公司都有頻率上限；全公司同時最多 5 句。
5. 稽核：每次請求都寫一筆 `DB.TBZPQ020`。

### 2. 一次請求的處理順序（`process()`）
1. **來源檢查**：只接受 POST，來源 IP 要是 `10.*` 或 `192.168.*`。同一個 IP 10 分鐘內 Token 驗證失敗 10 次，就鎖那個 IP。
2. **Token 驗證**：依序檢查雜湊比對、狀態要是 A（否則 REVOKED）、到期日（否則 EXPIRED）、擁有者 `TBDU01.VALIDDATE` 還沒過期（否則 USER_INACTIVE，等於離職就自動失效）、限定的來源 IP。Token 資料快取 5 秒，所以撤銷或展延最慢 5 秒內生效。
3. **等級檢查**：等級設定存在 `TBZPQ030～033`，快取 60 秒。等級被停用，或擁有者已不在使用範圍，就回 `LEVEL_DENIED`。
4. **頻率限制**：依等級限制每分鐘、每天的次數；全公司合計每分鐘 300 次；連續失敗 5 次，冷卻 5 分鐘。
5. **依 action 分派工作**：
   - `ping`：回傳等級、不可查的群組、今日用量、各項上限。
   - `tables`／`describe`：從可查表格清單回應。可查的表是 DB 綱要的所有實體表，扣掉 `TBZPQ*` 和這個等級沒解鎖的管制群組；view 預設不開放。
   - `query`：先檢查 SQL，通過後才執行。
   - `user`：只回傳工號、姓名、部門、職位、狀態。
6. **稽核**：寫入 `TBZPQ020`，內容包括工號、IP、action、結果、SQL 和當時的等級。

### 3. SQL 檢查（`checkSql()`）
1. 先移除註解，之後送進資料庫執行的，就是移除註解、檢查過的那句 SQL。
2. **嚴重違規**：出現 INSERT、UPDATE、DELETE、MERGE、CALL、CREATE、ALTER、DROP、TRUNCATE、GRANT、REVOKE 等詞，或 `FINAL/NEW/OLD TABLE`、`NEXT/PREVIOUS VALUE`、`EXCLUSIVE LOCKS`。24 小時內第 3 次會直接撤銷 Token。
3. 只允許一句 SELECT 或 WITH 開頭的查詢。
4. 每個 `DB.xxx` 和 FROM／JOIN 後面接的表，都要在可查清單裡：
   - 系統目錄（SYSCAT、SYSSTAT、SYSIBM 等）一律拒絕，只放行 `SYSIBM.SYSDUMMY1` 和內建函式。
   - 不能呼叫 `DB.` 自訂函式，也不能呼叫其他限定名稱的函式。
5. SQL 沒寫 `FETCH FIRST`／`LIMIT` 時，會自動補上「`FETCH FIRST` 列數＋1」，多抓的那一列用來判斷結果有沒有被截斷。
6. SQL 長度上限 8,000 字。

### 4. 執行時的防線（`runQuery()`）
- 關掉自動 commit，隔離層級設 READ UNCOMMITTED（等於 `WITH UR`，不會鎖到正式機的交易）。
- 同時用 `setMaxRows` 限制列數、`setQueryTimeout(10)` 限制時間。逾時回 `TIMEOUT`，並提示改用索引欄位當條件。
- 同一個 Token 最多同時跑 2 句，全公司最多 5 句。
- 相同的 SQL 和列數，60 秒內直接回快取結果，不再查資料庫，也不佔同時執行的名額。

### 5. 主要設定值

| 設定 | 值 |
|---|---|
| 預設列數／未設定時的上限／硬上限 | 100／1,000／5,000 |
| 每 Token 每分鐘／每天（預設） | 30／2,000 |
| 硬上限：每分鐘／每天 | 120／20,000 |
| 全公司每分鐘 | 300 |
| 逾時 | 10 秒 |
| 系統管理者 | 26295（寫死在程式裡） |

### 6. 其他
- 第 37 行內網網段的註解還寫著「待確認」。
- 程式的撰寫限制是 Java 1.4 語法（不能用泛型、for-each、StringBuilder），存檔是 Big5。

## 四、Token 核發頁 zpjjQueryApiToken.jsp

- 一般 ERP 頁面，要登入 SSO 加 2FA。工號直接取自登入資訊 `_dsCom.user.ID`，所以只能管自己的 Token。
- 進頁時檢查 `TBDU01.VALIDDATE` 是否在職，再依 `TBZPQ030` 的等級和 `TBZPQ033` 的使用範圍，算出可以選哪些等級。登錄在 `TBZPQ034` 的人算「設定管理者」，畫面上會出現分級設定頁的連結。
- 表單用 Session 隨機碼（nonce）防止跨站偽造請求。

| 動作 | 規則 |
|---|---|
| **核發**（create） | ① 名稱 1～30 字。② 每人最多 3 組有效 Token，管理者最多 10 組。③ 預設 30 天，也可選 90 或 180 天，但超過 30 天必須限定來源 IP。④ Token 格式是 `zpq_` 加 12 碼 ID 加 64 碼十六進位亂數，用 SecureRandom 產生；資料庫 `TBZPQ010` 只存 SHA-256 雜湊，明文只在核發當下顯示一次 |
| **展延**（extend） | ① 只能展延自己名下、有效、到期前 5 天內（含到期當天）、仍在該等級使用範圍的 Token。② 新到期日從當天起算 30 天；限定 IP 的 Token 可選 30、90 或 180 天。③ Token 本身不變。④ 更新時用舊到期日當條件，避免重複送出；成功後寫一筆 `TBZPQ035` |
| **撤銷**（revoke） | 狀態改成 R。一般人只能撤銷自己的，管理者可以撤銷任何人的 |
| **重新生效／管理者展延**（restore／admExtend） | 只限管理者，而且不受「到期前 5 天」的限制。擁有者已離職的不能恢復；已過期的 Token 恢復後，到期日從當天起算 30 天 |

管理者另外有「全部 Token」「違規事件」（近 7 日）「查詢失敗」（近 7 日，依原因分類）三個頁籤。

## 五、分級設定頁 zpjjQueryApiAdm.jsp

- 一般 ERP 頁面，要登入 SSO 加 2FA，也會檢查是否在職。
- 只有系統管理者（`ADMINS`，26295）和設定管理者（`TBZPQ034`）可以使用。

| 頁籤 | 資料表 | 內容 |
|---|---|---|
| 等級 | `TBZPQ030` | 等級代號、名稱、列數上限、每分鐘上限、每日上限、狀態、排序；上限不能超過程式硬上限 |
| 管制群組 | `TBZPQ031` | 群組的表名規則，例如 `TBH*,TBXX0010`（前綴至少 2 字元），以及例外表名 |
| 可查矩陣 | `TBZPQ032` | 每個等級解鎖哪些管制群組 |
| 使用範圍 | `TBZPQ033` | U 是工號、D 是部門（可用 `A3*` 前綴）、X 是排除工號（等級可填 `*`，代表全部等級）；另可設「有效至」日期 |
| 設定管理者 | `TBZPQ034` | 只有系統管理者能新增或移除 |
| 異動紀錄 | `TBZPQ035` | 每次異動都記錄修改前後的內容，畫面顯示最新 50 筆 |

- **生效時間**：查詢端點對這些設定快取 60 秒，所以改完 60 秒內生效，已核發的 Token 不用重發。停用某個等級，該等級的 Token 全部被拒絕；從使用範圍移除某人，他的 Token 會被拒絕。
- **固定底線**：`TBZPQ*` 和系統目錄寫死在端點程式裡，這頁怎麼設定都打不開。
- **判斷某人能用哪些等級**：只看啟用的等級，跳過已超過「有效至」日期的範圍設定；工號（U）或部門（D）符合就算命中，被排除（X）的不能用；系統管理者不受排除影響，全部等級都能用。這套規則在端點、核發頁、設定頁三支程式裡各寫了一份，以後若要修改，三支都得同步改。

### 資料表總覽

| 表 | 用途 |
|---|---|
| TBZPQ010 | Token（雜湊、狀態、到期日、限定 IP、等級） |
| TBZPQ020 | 查詢稽核紀錄 |
| TBZPQ030 | 等級 |
| TBZPQ031 | 管制群組 |
| TBZPQ032 | 等級與群組的對應（可查矩陣） |
| TBZPQ033 | 使用範圍 |
| TBZPQ034 | 設定管理者 |
| TBZPQ035 | Token 與設定的異動紀錄 |

## 六、ERP 共用連線池 jdbc/dsyl

`jdbc/dsyl` 是 ERP 這個 Web 應用程式向應用伺服器借資料庫連線的「名稱」。連線池由伺服器建立和管理，程式只用這個名稱借連線、用完歸還，不必自己處理 DB2 的帳號密碼。整個機制分三層。

### 1. 伺服器端：定義連線池
本機開發用的 Tomcat 8.5，設定在 `erpHome/yl.ear/erp.war/server.xml`（帳號密碼已遮蔽）：

```xml
<Resource name="jdbc/dsyl" auth="Container" type="javax.sql.DataSource"
          driverClassName="com.ibm.db2.jcc.DB2Driver"
          url="jdbc:db2://testdb.chsteel.com.tw:50000/IDBYL"
          username="***" password="***"
          initialSize="5" maxTotal="60" maxIdle="5" maxWaitMillis="15000"
          removeAbandonedOnBorrow="true" removeAbandonedTimeout="180" logAbandoned="true" ... />
```

| 參數 | 意義 |
|---|---|
| `initialSize=5` | 啟動時先建 5 條連線 |
| `maxTotal=60` | 最多同時借出 60 條 |
| `maxIdle=5` | 閒置時最多保留 5 條 |
| `maxWaitMillis=15000` | 60 條都被借走時，最多等 15 秒，還借不到就拋例外 |
| `removeAbandoned…180` | 借出超過 180 秒沒歸還的連線，視為被遺棄並強制收回，同時記 log |

- 本機這份連的是**測試機** `testdb`。
- 正式機的連線池設定在正式機伺服器上，不在本機原始碼裡。`resource-ref` 的 id 格式看起來像 WebSphere 產生的；正式機實際用哪種伺服器、連線池參數多少，本機看不到。

### 2. 應用程式：在 web.xml 宣告要用這個名稱

```xml
<resource-ref>
    <res-ref-name>jdbc/dsyl</res-ref-name>
    <res-type>javax.sql.DataSource</res-type>
    <res-auth>Container</res-auth>
    <res-sharing-scope>Shareable</res-sharing-scope>
</resource-ref>
```

這段讓程式可以用 `java:comp/env/jdbc/dsyl` 查到伺服器提供的連線池。`res-auth=Container` 的意思是帳號密碼由伺服器負責，程式裡不出現。

### 3. 程式：借連線的兩種寫法

**寫法 A：ERP 框架 `dejc301`（一般作業的標準寫法，EA 程式都用這種）**

```java
dejc301 de301 = new dejc301();
try {
    Connection con = de301.getConnection(this.dsCom, this.AppId); // 向連線池借連線
    de301.setAutoCommit(false);                                   // 開始交易
    eajcRE03DAO dao = new eajcRE03DAO(this.dsCom, con);
    dao.create(vo);
    de301.commit();
} catch (Exception e) {
    this.handleTransacException(e, de301);   // rollback 並顯示錯誤
} finally {
    de301.close();                           // 歸還連線池（一定要寫在 finally）
    de301 = null;
}
```

- `dejc301` 包在 `de.jar` 裡，內部應該也是查 `jdbc/dsyl`。它會帶入 `dsCom`（登入者環境）和 `AppId`，推測是框架用來記錄哪個使用者、哪支程式借了連線（`de.jar` 沒有反組譯，這兩點是推測）。
- 一般作業一律用這種寫法，DAO 共用同一條 `con`，交易才會一致。

**寫法 B：直接查 JNDI（查詢 API 的寫法）**

```java
DataSource ds = (DataSource) new InitialContext().lookup("java:comp/env/jdbc/dsyl");
Connection conn = ds.getConnection();
try {
    conn.setAutoCommit(false);
    // 執行 SQL ...
} finally {
    conn.rollback();   // 查詢 API：不論結果一律 rollback
    conn.close();      // 不是真的斷線，而是歸還連線池
}
```

查詢 API 改用這種寫法，推測原因是：它設定 `session="false"`，不經 ERP 登入，所以沒有 `dsCom` 可以傳給 `dejc301`；而且它需要自己控制隔離層級、查詢逾時和強制 rollback。

### 4. 重點
- **close() 等於歸還**：連線池裡的連線呼叫 `close()` 不會真的斷線，只是放回池中。忘了 close，連線就一直被佔著，直到 180 秒後被強制收回；在這之前若 60 條都被佔滿，其他人借連線會等 15 秒後失敗，畫面看起來就像整個 ERP 卡住。
- **共用的代價**：查詢 API 和全公司 ERP 畫面共用同一個連線池，所以它在程式裡另外限制全公司同時最多 5 句、每句 10 秒逾時，避免把連線池佔滿影響線上作業。
- **權限**：這條連線用的資料庫帳號有寫入權限，資料庫本身不會擋寫入，所以查詢 API 的唯讀完全靠 JSP 裡的 SQL 檢查。

## 七、閱讀時發現、可回報 26295 的地方（不影響使用）

**核發頁**
1. 撤銷紀錄不完整：只有管理者撤銷會寫 `TBZPQ035`；本人撤銷不寫，只留在 `TBZPQ010` 的 REVOKE 欄位（第 441 行）。
2. 撤銷原因可能不準：管理者撤銷自己的 Token，原因欄也會寫「管理者撤銷」（第 436 行）。
3. 預設等級不一致：核發時如果沒帶等級參數，程式取可用等級清單的第一個（排序最前），和畫面預選的「範圍內最後一個」不同（第 388 行）。正常從畫面操作都會帶等級，只有直接送請求才會遇到。
4. 服務 Token 開放範圍：v3.3.4 起一般同仁也能申請 180 天的服務 Token，只要限定 IP 就行。這是規則上的放寬，不是 bug，要不要這樣由 26295 決定。

**設定頁**
1. 設定管理者可以替自己升級：能改使用範圍和可查矩陣，所以可以把自己加進更高等級，或替自己的等級解鎖「人事」群組。程式沒有擋，事後只能從 `TBZPQ035` 查到。
2. 停用群組等於全面開放：把管制群組改成停用，該群組的表就對所有等級開放，影響很大；從處理邏輯看沒有二次確認（畫面 JS 沒有逐行讀過）。
3. 只有矩陣儲存有完整交易：其他操作的資料異動和異動紀錄是分開寫入、各自 commit，理論上可能出現「設定改了、紀錄沒寫到」的情況，機率很低。

## 八、使用守則（摘自個人 CLAUDE.md）
- 步驟固定：`zpq --tables` 找表 → `zpq --describe <表>` 看欄位與索引 → 才寫查詢；表格一律寫 `DB.` 前綴。
- WHERE 條件優先用索引欄位；估計列數超過 10 萬的表，沒有索引條件不要查；不要 `SELECT *`。
- 不能嘗試寫入語法，24 小時內 3 次會自動撤銷 Token。
- 被管制群組擋下的表不要繞過，回報主管調整等級；`TBZPQ*` 與系統目錄一律不可查。
- 不讀取、不印出 `%USERPROFILE%/.zpq/token` 的內容。

## 附：實例（2026-11-06）
- `zpq --ping`：工號 26788，等級 BASIC（一般），Token 到期 20261205；不可查稽核、資訊登錄、人事三個群組；每分鐘 30 次、每天 2,000 次，列數上限 1,000，同時最多 2 句。
- 查 `DB.TBDAU1`／`DB.TBDAU3` 確認 RQ11510012 上線申請 `20261105_162613` 狀態 A（已核准），4 支程式和預期相同；但 `COMMITVERSION` 欄是空的，對不到版本號，生效時間也查不到。
