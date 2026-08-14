**ORM（Object-Relational Mapping，物件關聯對映）** 是一種程式設計技術，主要用來在物件導向程式語言（如 Java, Python, C#）**與**關聯式資料庫（如 PostgreSQL, MySQL, DB2）之間搭起一座溝通橋樑。

簡單來說，ORM 讓你**不用手寫 SQL 語法**，就能像操作一般的物件（Object）或類別（Class）一樣，對資料庫進行 CRUD（新增、讀取、更新、刪除）操作。

## 核心概念：資料轉換對照

ORM 會將資料庫的結構映射到程式碼中的物件結構：

|**關聯式資料庫 (RDBMS)**|**物件導向程式語言 (OOP)**|
|---|---|
|**資料表 (Table)**|**類別 (Class)**|
|**資料行 (Column / Field)**|**屬性 (Property / Attribute)**|
|**資料列 (Row / Record)**|**物件實例 (Object Instance)**|

## 傳統 SQL vs. 使用 ORM

假設要查詢「狀態為啟用 (active) 的使用者」：

### 傳統手寫 SQL (以 Python 搭配 DB API 為例)

Python

```
cursor.execute("SELECT id, name, email FROM users WHERE status = %s", ('active',))
rows = cursor.fetchall()
for row in rows:
    print(f"User ID: {row[0]}, Name: {row[1]}")
```

### 使用 ORM (以 SQLAlchemy / Django ORM 為例)

Python

```
# 程式直接以物件方式存取
users = User.query.filter_by(status='active').all()
for user in users:
    print(f"User ID: {user.id}, Name: {user.name}")
```

## ORM 的優缺點

### 主要是優點：

1. **提高開發效率**：減少重複寫 SQL CRUD 程式碼的時間。
    
2. **跨資料庫移植性高**：大部分 ORM 工具支援切換 底層資料庫（例如從 PostgreSQL 切換至 MySQL），業務邏輯程式碼幾乎不需要修改。
    
3. **防止 SQL 注入（SQL Injection）**：ORM 通常會自動對傳入參數進行轉義（Escape）或採用預編譯查詢（Parameterized Queries）。
    
4. **維護性佳**：資料庫 Schema 變更時，透過ORM Migration 工具集中管理版控較容易。
    

### 隱含的缺點與挑戰：

1. **效能耗損 (Overhead)**：物件與 SQL 之間的轉譯會帶來些微效能開銷。
    
2. **複雜查詢處理較弱**：遇到極度複雜的多表關聯、報表分析或特定資料庫專屬優化語法時，ORM 產生的 SQL 可能不夠精簡，甚至需要退回手寫原生 SQL（Native SQL）。
    
3. **N+1 查詢問題**：若沒有注意 Lazy Loading（延遲載入）與 Eager Loading（預先載入）的設定，容易觸發大量額外查詢導致資料庫過載。
    

## 常見語言的代表性 ORM 框架

- **Java**: Hibernate, JPA (Java Persistence API)
    
- **Python**: SQLAlchemy, Django ORM, Peewee, SQLModel
    
- **JavaScript / TypeScript**: Prisma, TypeORM, Sequelize
    
- **C# (.NET)**: Entity Framework (EF Core)
    
- **PHP**: Eloquent (Laravel)

---
在資料庫存取層的架構選擇上，**原生 SQL**、**Query Builder (SQL 構建器 / 半 ORM)** 與 **全功能 ORM** 代表了從「完全掌控 SQL」到「完全物件化」的三種不同抽象程度。

以下為三者的綜合比較與適用情境分析：

## 綜合比較表

|**比較維度**|**原生 SQL (Native SQL)**|**Query Builder / 半 ORM(如 Knex, MyBatis, jOOQ)**|**全功能 ORM(如 Hibernate, Prisma, EF Core)**|
|---|---|---|---|
|**核心理念**|直接撰寫原生資料庫語法|用程式碼 API 或 XML 動態組裝 SQL|將資料表直接抽象映射為 OOP 物件|
|**SQL 控制度**|**完全掌控** (100%)|**高度掌控** (精細控制產出的 SQL)|**低度掌控** (由框架自動生成 SQL)|
|**開發效率 (CRUD)**|較低 (需手寫大量重複 SQL)|中等 (簡單 CRUD 順暢，動態條件方便)|**極高** (單表 CRUD 與關聯操作免寫 SQL)|
|**執行效能**|**極佳** (零抽象層開銷)|**優異** (僅極輕微的 API 組裝開銷)|中等 (有物件轉換與 SQL 生成開銷)|
|**學習曲線**|需熟悉 SQL 與 DB 特性|平緩 (只要懂得 SQL 概念即可上手)|較陡峭 (需理解生命週期、快取、Lazy Loading 等)|
|**動態查詢處理**|困難且危險 (易字串拼接)|**極佳** (條件式鏈式呼叫，安全簡潔)|良好 (但複雜條件 API 較繁瑣)|
|**跨 DB 移植性**|差 (高度綁定特定 DB 語法)|中等 (Builder API 會處理部分語法差異)|**高** (換 DB 通常只需改 Dialect 設定)|

## 深度剖析與適用情境

### 1. 原生 SQL (Native SQL / JDBC)

直接在程式碼中以字串形式撰寫 SQL，並透過資料庫驅動程式（如 JDBC、DB API）執行。

- **優點**：
    
    - **無效能損耗**：沒有任何中間抽象層，執行速度最快。
        
    - **發揮資料庫極限**：能直接使用特定資料庫的專屬優化語法（如 DB2/Oracle 特有 Hint、Window Functions、複雜 Stored Procedures）。
        
    - **除錯直覺**：日誌印出的就是最終執行的語法，沒有框架產生的「黑盒子」。
        
- **缺點**：
    
    - **程式碼冗長**：需人工處理欄位對映（Mapping ResultSet 到 Class）、連線管理與異常處理。
        
    - **安全風險**：若不小心用字串拼接參數，極易引發 **SQL Injection**。
        
    - **維護成本高**：動態條件查詢（如有多個可選搜尋過濾器）時，拼湊字串極難維護。
        
- **適用情境**：
    
    - 報表系統、大數據批次處理（Batch Processing）。
        
    - 對效能有極致要求、微秒必較的核心交易模組。
        
    - 呼叫既有的複雜預存程序（Stored Procedures）。
        

### 2. Query Builder / 半 ORM (如 MyBatis, Knex.js, jOOQ)

提供程式化 API（如鏈式呼叫 `.where().join()`）或將 SQL 抽離至映射檔（如 MyBatis XML），介於原生 SQL 與 ORM 之間的折衷方案。

- **優點**：
    
    - **優雅處理動態 SQL**：透過程式邏輯或標籤靈活組合 `WHERE` 條件，徹底告別字串拼接。
        
    - **自動預編譯**：預設採用 Parameterized Queries，自動防止 SQL Injection。
        
    - **保有 SQL 優化彈性**：開發者明確知道產出的 SQL 長怎樣，方便針對索引進行慢查詢優化。
        
- **缺點**：
    
    - **仍需理解資料庫結構**：開發者仍需手動設計 SQL 與關聯。
        
    - **多表關聯映射需設定**：比起 ORM 的自動加載，複雜關聯的資料對映仍需寫些許配置。
        
- **適用情境**：
    
    - 大型企業級系統、金融/電商等資料庫 Schema 龐大且複雜的專案。
        
    - 團隊對 SQL 優化有嚴格要求，但不希望維護原生 SQL 字串。
        
    - 專案中有大量靈活的動態條件搜尋功能。
        

### 3. 全功能 ORM (如 Hibernate, Django ORM, SQLAlchemy, Prisma)

將資料庫完全「物件化」，開發者直接操作程式裡面的 Class 與 Object，框架會自動將物件動作轉譯為 SQL 語法。

- **優點**：
    
    - **快速開發與敏捷迭代**：簡單的 CRUD 完全不需要寫任何 SQL，大幅節省開發時間。
        
    - **自動化 Schema 遷移 (Migration)**：自動根據模型程式碼變更資料庫結構。
        
    - **型態安全 (Type Safety)**：配合強型態語言，可在編譯期捕捉欄位名稱寫錯等錯誤。
        
- **缺點**：
    
    - **隱形陷阱 (如 N+1 查詢問題)**：若不熟悉 Lazy Loading 與 Eager Loading 機制，容易產生成千上萬條無效查詢。
        
    - **黑盒子優化困難**：ORM 生成的 SQL 有時過於複雜或帶有冗餘 `JOIN`，難以調整為最佳執行計劃。
        
    - **學習成本高**：要精通框架的狀態管理（如 Hibernate 的 Persistence Context、Session 週期）需要長時間累積。
        
- **適用情境**：
    
    - 新創專案驗證 (MVP)、業務邏輯頻繁變更的系統。
        
    - 以單表 operations / 輕度關聯為主的 RESTful API 服務。
        
    - 領域驅動設計 (DDD)，以物件模型為核心構建的系統。
        

## 實務上的最佳選擇建議

在實際的軟體架構中，**三者並非完全互斥**，許多大型系統會採取「混合模式」：

> 💡 **常見的混合搭配模式：**
> 
> - **主框架使用 ORM**：處理 80% 的日常單表/簡單關聯 CRUD，提升 3~5 倍開發速度。
>     
> - **關鍵模組補上 Query Builder / 原生 SQL**：在遇到「複雜多表統計報表」、「高並發核心交易」或「大資料量匯入匯出」時，手寫 SQL 或呼叫 Query Builder 進行精細優化。


---
在實際的企業級系統開發中，**混合使用 ORM 與原生 SQL** 是非常常見且務實的架構決策（即所謂的「80/20 法則」：80% 的日常簡單 CRUD 交給 ORM 快速開發，20% 的複雜查詢與高效能批次交給原生 SQL）。

然而，若沒有建立明確的架構規範，混合使用容易導致**快取不一致、事務（Transaction）失效或程式碼混亂**。以下總結混合架構下的**5 大最佳實踐**與 **4 大核心注意事項**：

## 5 大最佳實踐 (Best Practices)

### 1. 貫徹 CQRS 概念：職責明確分工

- **Command (寫入/更新)**：優先使用 **ORM**。ORM 的狀態追蹤、驗證機制與動態變更（Dirty Checking）能確保資料寫入的封裝性與一致性。
    
- **Query (複雜讀取/報表)**：優先使用 **原生 SQL / DTO Mapping**。跳過 ORM 的關聯加載與物件轉換開銷，直接對映至唯讀的 DTO (Data Transfer Object)。
    

### 2. 嚴格限定原生 SQL 的存在位置

- **禁止在 Service / Business Layer 寫 SQL 字串**。
    
- 原生 SQL 必須被封裝在 **DAO / Repository 層** 的特定方法內，或是集中管理在獨立的 `.sql` / `.xml` 檔案中（如 MyBatis 或 External SQL Files）。
    
- 讓業務邏輯層（Service）保持乾淨，只調用介面，不關心底層是用 ORM 還是原生 SQL 實作。
    

### 3. 共享相同的「交易與連線上下文 (Transaction Context)」

- **最常見的致命錯誤**：ORM 與原生 SQL 使用了不同的連線或交易管理器，導致「ORM 剛寫入但未 Commit 的資料，原生 SQL 查不到」。
    
- **作法**：確保原生 SQL 執行器（如 Spring 的 `JdbcTemplate` 或 SQLAlchemy 的 `session.execute()`）使用的是**同一個 Thread / Request 綁定的 Session 與 Transaction**。
    

### 4. 原生 SQL 查詢結果請對映至 DTO，而非 ORM Entity

- 當使用原生 SQL 進行複雜 `JOIN` 或多表統計時，查詢結果應直接對映為 **純資料載體 (DTO / VO)**。
    
- **避免將原生 SQL 的結果強行轉為 ORM 的 Managed Entity**，否則容易破壞 ORM 一級快取的持久化狀態管理。
    

### 5. 一律採用參數化查詢 (Parameterized Query)

- 離開了 ORM 的保護傘後，手寫原生 SQL 務必使用佔位符（`?` 或 `:param`），**絕對禁止用字串拼接（`+` 或 `f-string`）** 組裝 SQL 變數，徹底防止 **SQL Injection**。
    

## 4 大注意事項與常見踩坑點 (Pitfalls)

### ⚠️ 1. 一級快取 (First-Level Cache / Persistence Context) 不一致

- **情境**：ORM（如 Hibernate/JPA）會在 Session 內快取查詢過的 Entity。如果你此時用原生 SQL 直接改了資料庫（如 `UPDATE users SET status = 'INACTIVE' WHERE ...`），**ORM 的一級快取並不知道資料庫已經變了**。
    
- **後果**：同一個 Transaction 內後續用 ORM 讀取該物件時，依然會拿到舊的快取資料。
    
- **解法**：
    
    - 執行原生 SQL 更新/刪除動作前，先呼叫 ORM 的 `flush()` 將記憶體變更推送到 DB。
        
    - 執行原生 SQL 後，呼叫 ORM 的 `clear()` / `evict()` 強制清空快取，迫使 ORM 下次查詢時重新讀取 DB。
        

### ⚠️ 2. 併發與鎖定 (Locks) 衝突導致死鎖

- ORM 自動產生的 SQL 更新順序（例如更新關聯表的順序）與你手寫的原生 SQL 更新順序可能不同。
    
- 如果高併發下兩者同時存取相同資料列，極易引發資料庫 **Deadlock（死鎖）**。
    
- **解法**：涉及多表更新的業務流程，盡量統一更新機制，或嚴格規範 Table 存取的順序。
    

### ⚠️ 3. 破壞資料庫移植性 (DB Dialect Lock-in)

- ORM 的優點之一是隱藏了不同 DB 之間的語法差異（如 DB2、PostgreSQL、MySQL 的分頁或時間函數）。
    
- 一旦使用了原生 SQL 專屬語法（如特定 Window Function 或 Hint），即失去跨 DB 移植性。
    
- **解法**：在程式碼中明確註記 DB 專屬語法，並將這些 SQL 模組化，以便未來替換。
    

### ⚠️ 4. 資料庫版本遷移 (Schema Migration) 脫節

- 專案中若同時有 ORM 自動生成 Schema（如 `hibernate.hbm2ddl.auto`）與手寫 SQL 腳本，極易引發 Schema 不一致。
    
- **解法**：在混合架構中，**關閉 ORM 的自動建表功能**。統一使用獨立的 Schema 變更工具（如 **Flyway** 或 **Liquibase**）作為唯一的資料庫版本控管來源。
    

## 系統架構檢視清單

```
【客戶端請求】
     │
     ▼
【Service 業務邏輯層】──(統一控管 @Transactional)
     │
     ├───────────┬───────────┐
     ▼                       ▼
【ORM Repository】    【Native SQL DAO】
 (處理單表/寫入/CRUD)    (處理複雜報表/高效能批次)
     │                       │
     └───────────┬───────────┘
                 ▼
    【共享相同的 DB Connection / Session】
                 │
                 ▼
          【Database】
```

---
在 Python 的 **SQLAlchemy** (以 2.0+ 現代寫法為例) 中，混合使用 ORM Session 與 Raw SQL 是非常常見且支援良好的情境。

要確保**連線/事務一致性**以及**避開 ORM 快取不一致**的坑，核心原則為：

1. **使用相同的 `Session` 執行 Raw SQL**：透過 `session.execute(text(...))` 執行，讓 Raw SQL 自動共享當前的 Transaction。
    
2. **手動同步/清空快取 (Session Flush & Expire)**：在用 Raw SQL 修改資料前後，及時將 ORM 記憶體變更推送到 DB 並刷新快取。
    

## 完整實作範例

以下是一個完整的範例，示範如何在同一個事務中處理：

1. **ORM 寫入/更新**
    
2. **Raw SQL 複雜查詢與寫入**
    
3. **處理快取同步與連線一致性**
    

Python

```
from sqlalchemy import create_engine, select, text, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# 1. 初始化資料庫連線與 Session
DATABASE_URL = "sqlite:///:memory:"  # 以記憶體資料庫為例
engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

# 定義範例 ORM 模型
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_state=True, primary_key=True)
    name = Column(String)
    status = Column(String)
    points = Column(Integer)

Base.metadata.create_all(engine)


def mixed_orm_and_raw_sql_example():
    # 使用 context manager 確保 Session 生命週期與 Transaction 一致
    with SessionLocal() as session:
        with session.begin(): # 自動開啟與管理 Transaction
            
            # ----------------------------------------------------
            # 步驟 A: 使用 ORM 建立初始資料
            # ----------------------------------------------------
            user1 = User(name="Alice", status="active", points=100)
            session.add(user1)
            
            # 【重要】Flush: 將 ORM 的新增寫入 DB 緩衝區（取得 ID），但不 Commit
            session.flush() 
            print(f"[ORM] 已建立用戶 {user1.name} (ID: {user1.id})，尚未 Commit")

            # ----------------------------------------------------
            # 步驟 B: 使用 Raw SQL 執行複雜查詢 (與 ORM 共享同一個 Transaction)
            # ----------------------------------------------------
            # 使用 text() 包裹 Raw SQL 並且【使用參數綁定防止 SQL Injection】
            sql_query = text("""
                SELECT id, name, points 
                FROM users 
                WHERE status = :status AND points >= :min_points
            """)
            
            # session.execute 會在【同一個資料庫連線與事務】中執行
            result = session.execute(sql_query, {"status": "active", "min_points": 50})
            
            print("\n[Raw SQL 讀取] 查詢結果：")
            for row in result.mappings(): # mappings() 轉為字典風格讀取 (DTO 形式)
                print(f" - ID: {row['id']}, Name: {row['name']}, Points: {row['points']}")

            # ----------------------------------------------------
            # 步驟 C: 使用 Raw SQL 直接更新資料 (會影響快取！)
            # ----------------------------------------------------
            sql_update = text("""
                UPDATE users 
                SET points = points + 50 
                WHERE id = :user_id
            """)
            session.execute(sql_update, {"user_id": user1.id})
            print(f"\n[Raw SQL 更新] 已直接在 DB 將 User {user1.id} 的 points +50")

            # ⚠️ 此時 ORM 記憶體中的 user1.points 依然是 100 (舊快取)！
            print(f"[快取警告] ORM 記憶體中的 points 依然是舊值: {user1.points}")

            # ----------------------------------------------------
            # 步驟 D: 解決快取不一致 (Expire / Refresh)
            # ----------------------------------------------------
            # 做法 1: 單一物件刷新
            session.refresh(user1) 
            
            # 做法 2: 若一次用 Raw SQL 改了多筆，可清空 Session 所有 ORM 物件快取
            # session.expire_all()

            print(f"[快取同步後] ORM 重新從 DB 載入後的 points: {user1.points}")

        # 離開 with session.begin() 時，若無例外會自動執行 COMMIT
        # 若有例外發生則會自動 ROLLBACK (ORM 與 Raw SQL 的變更會一併復原)

mixed_orm_and_raw_sql_example()
```

## 關鍵技術解密：連線一致性與快取處理

### 1. 如何確保連線與事務一致性 (Connection & Transaction Consistency)？

- **機制**：直接呼叫 **`session.execute(text(...))`**，而不是建立新的 `engine.connect()`。
    
- **原理**：`Session` 在第一條指令執行時會向 Engine 借用一個連線並開啟 Transaction。後續無論是 ORM 操作（如 `session.add()`、`session.scalar()`）或是 Raw SQL (`session.execute(text())`)，**使用的都是該 Session 內部綁定的同一個 DB Connection**。
    
- **優勢**：當你使用 `session.commit()` 或 `session.rollback()` 時，ORM 與 Raw SQL 所做的所有修改會**原子性地 (Atomically) 一起生效或復原**。
    

### 2. 如何正確處理快取 (Cache Synchronization)？

ORM 的核心是「Identity Map（單例對映）」，它會把已載入的物件存放在記憶體中。Raw SQL 的 `UPDATE` / `DELETE` 是繞過 ORM 直接對 DB 操作，會導致記憶體物件與 DB 資料不一致。

解決流程順序如下：

```
[1. ORM 異動] ──> session.flush() ──> [2. 執行 Raw SQL] ──> session.refresh(obj) 或 expire_all() ──> [3. 後續 ORM 操作]
```

1. Raw SQL 執行「前」— `session.flush()`：
    
    - 如果 ORM 記憶體有尚未寫入的變更（例如新增的 `user` 或修改的屬性），必須先 `flush()` 刷入 DB，否則 Raw SQL 讀不到或改不到最新的資料。
        
2. Raw SQL 執行「後」— `session.refresh(obj)` 或 `session.expire_all()`：
    
    - **更新單一/少數物件**：調用 `session.refresh(instance)`，ORM 會立刻發送一條 `SELECT` 將最新的資料蓋掉舊快取。
        
    - **批次更新多筆資料**：調用 `session.expire_all()`，將目前 Session 內所有 Entity 標記為「過期」。下次程式存取該 Entity 屬性時，ORM 就會自動發送 `SELECT` 撈取最新狀態。
        

## 建議與避坑清單

1. **強制使用 `text()` 與綁定參數**：
    
    Python
    
    ```
    # ❌ 危險！不要用 f-string 拼接
    session.execute(text(f"SELECT * FROM users WHERE name = '{user_name}'"))
    
    # ✅ 安全！使用 :param 綁定
    session.execute(text("SELECT * FROM users WHERE name = :name"), {"name": user_name})
    ```
    
2. Raw SQL 讀取結果映射至字典 (Mappings)：
    
    - `session.execute(text(...))` 回傳的是 `Result` 物件。
        
    - 推薦使用 `result.mappings().all()`，它會回傳字典樣式的列物件（RowMapping），非常適合轉成 Pydantic 模型或 JSON / DTO 回傳給前端，避免強行轉換成 ORM Entity 導致快取狀態混亂。

---
在 Spring Boot 專案中，**Spring Data JPA**（全功能 ORM）與 **`JdbcTemplate`**（原生 SQL 執行器）是極為常見且強大的混合組合。

由於兩者底層預設都透過 Spring 的 `PlatformTransactionManager`（即 `JpaTransactionManager`）管理連線，**只要標註 `@Transactional`，兩者就會自動共享相同的 DB 連線與事務 (Transaction)**。

要避免的主要陷阱是 **JPA 一級快取（Persistence Context / EntityManager）與原生 SQL 更新不同步** 的問題。以下提供完整的實作範例與機制說明。

## 完整實作範例

### 1. 服務層實作 (`UserService.java`)

透過 `@Transactional` 確保事務一致性，並透過 `EntityManager` 手動處理 JPA 快取同步。

Java

```
package com.example.demo.service;

import com.example.demo.entity.User;
import com.example.demo.repository.UserRepository;
import jakarta.persistence.EntityManager;
import jakarta.persistence.PersistenceContext;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;
import java.util.Map;

@Service
public class UserService {

    private final UserRepository userRepository; // Spring Data JPA
    private final JdbcTemplate jdbcTemplate;     // Native SQL

    @PersistenceContext
    private EntityManager entityManager;         // 用於管理 JPA 一級快取

    public UserService(UserRepository userRepository, JdbcTemplate jdbcTemplate) {
        this.userRepository = userRepository;
        this.jdbcTemplate = jdbcTemplate;
    }

    /**
     * 混合使用 JPA 與 JdbcTemplate 的核心邏輯
     */
    @Transactional
    public void mixedOperationExample(Long userId) {

        // =========================================================
        // 步驟 1: 使用 JPA 新增或載入資料 (進入 Persistence Context 快取)
        // =========================================================
        User user = userRepository.findById(userId)
                .orElseThrow(() -> new RuntimeException("User not found"));
        System.out.println("[JPA 讀取] 初始用戶 Name: " + user.getName() + ", Points: " + user.getPoints());

        // 模擬 JPA 修改資料 (尚未推送到 DB)
        user.setName("Alice (Updated by JPA)");

        // 【關鍵點 1: Flush】在執行 JdbcTemplate 前，務必將 JPA 記憶體變更推送到 DB
        // 否則 JdbcTemplate 讀不到或改不到 JPA 剛剛在記憶體中修改的最新狀態
        entityManager.flush();
        System.out.println("[JPA Flush] 變更已同步至 DB 緩衝區");


        // =========================================================
        // 步驟 2: 使用 JdbcTemplate 執行複雜查詢 / 批次更新 (共享同一個 Transaction)
        // =========================================================
        
        // 2a. 原生 SQL 複雜查詢 (結果直接對映為 DTO 或 Map)
        String sqlQuery = "SELECT id, name, points FROM users WHERE status = ? AND points > ?";
        List<Map<String, Object>> richUsers = jdbcTemplate.queryForList(sqlQuery, "ACTIVE", 50);
        System.out.println("[JdbcTemplate 查詢] 符合條件筆數: " + richUsers.size());

        // 2b. 原生 SQL 批次更新 (此動作會繞過 JPA 記憶體快取！)
        String sqlUpdate = "UPDATE users SET points = points + 100 WHERE id = ?";
        int updatedRows = jdbcTemplate.update(sqlUpdate, userId);
        System.out.println("[JdbcTemplate 更新] 已更新 DB 筆數: " + updatedRows);


        // =========================================================
        // 步驟 3: 清空或刷新 JPA 快取 (避免一級快取髒讀)
        // =========================================================
        
        // ⚠️ 此時 user.getPoints() 在 JPA 記憶體中依然是舊值！
        System.out.println("[快取警告] JPA 記憶體中的 Points 仍為舊值: " + user.getPoints());

        // 【關鍵點 2: Clear / Refresh】
        // 作法 A: 若只更新特定 Entity，直接使用 refresh 重新從 DB 載入
        entityManager.refresh(user);

        // 作法 B: 若使用原生 SQL 做了大範圍 Batch Update，直接清空整個 Persistence Context 快取
        // entityManager.clear(); 
        // user = userRepository.findById(userId).get(); // 清空後重新讀取

        System.out.println("[快取同步後] 重新讀取 JPA Entity Points: " + user.getPoints());

        // 離開 @Transactional 方法時：
        // 若無異常發生 -> 自動 COMMIT (JPA 與 JdbcTemplate 的變更一併生效)
        // 若拋出 RuntimeException -> 自動 ROLLBACK (兩者的操作一併復原)
    }
}
```

### 2. Entity 與 Repository 定義

#### `User.java` (JPA Entity)

Java

```
package com.example.demo.entity;

import jakarta.persistence.*;

@Entity
@Table(name = "users")
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String name;
    private String status;
    private Integer points;

    // Getters and Setters...
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public String getStatus() { return status; }
    public void setStatus(String status) { this.status = status; }
    public Integer getPoints() { return points; }
    public void setPoints(Integer points) { this.points = points; }
}
```

#### `UserRepository.java` (Spring Data JPA)

Java

```
package com.example.demo.repository;

import com.example.demo.entity.User;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Modifying;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

public interface UserRepository extends JpaRepository<User, Long> {

    // 💡 提示：如果是在 Spring Data JPA 的 @Query 中寫原生 SQL 更新，
    // 可以利用 @Modifying 註解自動幫你處理 flush 與 clear！
    @Modifying(clearAutomatically = true, flushAutomatically = true)
    @Query(value = "UPDATE users SET points = points + :addPoints WHERE id = :id", nativeQuery = true)
    int addPointsNative(@Param("id") Long id, @Param("addPoints") Integer addPoints);
}
```

## 核心機制說明

### 1. 事務連線如何實現共享？

Spring 透過 `TransactionSynchronizationManager` 機制將資料庫連線 (Connection) 綁定在當前的執行緒 (Thread) 上。

```
@Transactional (開啟 Transaction)
   │
   ├─► JpaTransactionManager 向 DataSource 借用 Connection A
   │   並綁定至目前 Thread
   │
   ├─► JPA 操作 (EntityManager) ───► 使用 Connection A
   │
   ├─► JdbcTemplate 操作 ──────────► 發現 Thread 已綁定 Connection A ──► 直接使用 Connection A
   │
   └─► 方法結束 ───────────────────► 針對 Connection A 統一執行 COMMIT / ROLLBACK
```

因為兩者使用相同的 `Connection A`，所以**完全不需要額外設定分散式事務（XA Transaction）**，原生 SQL 與 JPA 的動作會包含在同一筆 DB Transaction 裡面。

### 2. 快取處理兩大指令：`flush()` 與 `refresh()` / `clear()`

|**時間點**|**操作**|**API 呼叫**|**目的與作用**|
|---|---|---|---|
|**執行 JdbcTemplate 前**|**刷入 DB**|`entityManager.flush()`|將 JPA 記憶體中（如 `user.setName(...)`）尚未發送的 SQL 寫入 DB 緩衝區，確保 `JdbcTemplate` 能存取到最新狀態。|
|**執行 JdbcTemplate 後**|**刷新單筆**|`entityManager.refresh(entity)`|重新發送 `SELECT` 將特定 Entity 的記憶體狀態蓋掉，同步 `JdbcTemplate` 所做的修改。|
|**執行 JdbcTemplate 後**|**清空整體**|`entityManager.clear()`|將 Persistence Context 內的所有快取標記失效。適合 `JdbcTemplate` 做了大範圍批次更新時使用。|

## 避坑總結與建議

1. **避免在同一個 Transaction 內反覆交叉使用**：
    
    儘量遵循「先 JPA 讀取/處理 → `flush()` → `JdbcTemplate` 執行複雜/批次作業 → `clear()` / `refresh()`」的單向順序，避免頻繁切換導致快取狀態錯亂。
    
2. **優先使用 JPA 的 `@Modifying` 註解**：
    
    如果你只是想在 Repository 介面寫原生 SQL Update/Delete，優先使用 `@Query(nativeQuery = true)` 搭配 `@Modifying(clearAutomatically = true, flushAutomatically = true)`，Spring Data 會自動為你執行 `flush` 和 `clear`，不需手動寫 `EntityManager`。
    
3. **DTO 映射**：
    
    `JdbcTemplate` 查詢複合欄位時，建議搭配 `BeanPropertyRowMapper` 或 Spring 6 / Boot 3 的 `SimplePropertyRowMapper` 直接轉為 DTO，不要試圖將 `JdbcTemplate` 的結果轉成 JPA Managed Entity。