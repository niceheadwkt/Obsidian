這支影片《【SQL】 超簡易 SQLite 入門教學！SQLite 很可能是世界上最多用戶使用的 SQL 引擎？》由 **Dex IT Flipped Classroom** 發佈，主要介紹 SQLite 的特色與基本操作教學 [[00:06](https://www.youtube.com/watch?v=srVKdS2RG4g&t=6)]。

以下為影片內容摘要整理：

### 1. 什麼是 SQLite？[[00:06](https://www.youtube.com/watch?v=srVKdS2RG4g&t=6)]

- **廣泛應用**：SQLite 被認為是世界上部署最廣、使用最普及的資料庫引擎 [[01:07](https://www.youtube.com/watch?v=srVKdS2RG4g&t=67)]，常見於 Android、iOS (iPhone/iPad)、Mac、Windows 10/11、瀏覽器（如 Chrome/Safari）以及各種智慧電視與軟體應用中 [[01:24](https://www.youtube.com/watch?v=srVKdS2RG4g&t=84)]。
    
- **輕量與單檔架構**：SQLite 是 Serverless、非 Client-Server 模式的本地資料庫（Local Database）[[00:47](https://www.youtube.com/watch?v=srVKdS2RG4g&t=47)]，整個資料庫就是單一檔案，不需複雜安裝或設置 [[00:55](https://www.youtube.com/watch?v=srVKdS2RG4g&t=55)]。
    
- **跨平台支援**：支援 Windows、Mac、Linux、Android、iOS 等多元平台 [[02:08](https://www.youtube.com/watch?v=srVKdS2RG4g&t=128)]，且 Python、PHP 等程式語言皆有原生或內建函式庫支援 [[01:30](https://www.youtube.com/watch?v=srVKdS2RG4g&t=90)]。
    

### 2. SQLite 工具安裝與啟動 [[02:30](https://www.youtube.com/watch?v=srVKdS2RG4g&t=150)]

- **下載與執行**：可至 SQLite 官網下載適用於作業系統的預編譯工具包（Bundle of Tools，如 sqlite3.exe）[[02:40](https://www.youtube.com/watch?v=srVKdS2RG4g&t=160)]。
    
- **Windows 提示處置**：若執行時出現 Microsoft Defender SmartScreen 的警告 [[03:16](https://www.youtube.com/watch?v=srVKdS2RG4g&t=196)]，是因為可執行檔未簽署數位簽章，選擇「仍要執行」即可 [[03:30](https://www.youtube.com/watch?v=srVKdS2RG4g&t=210)]。
    
- **建立與連接資料庫**：
    
    - 直接開啟 `sqlite3.exe` 時，預設會建立暫時性的記憶體資料庫（`in-memory database`）[[03:45](https://www.youtube.com/watch?v=srVKdS2RG4g&t=225)]。
        
    - 指令 `.open <檔名.db>`（例如 `.open dexit.db`）：可開啓或新建實體資料庫檔案並寫入硬碟 [[04:15](https://www.youtube.com/watch?v=srVKdS2RG4g&t=255)]。
        

### 3. 基本 SQL 語法與指令實作 [[05:02](https://www.youtube.com/watch?v=srVKdS2RG4g&t=302)]

- **建表（CREATE TABLE）與索引**：
    
    - 可透過 `CREATE TABLE` 建立資料表並指定欄位型態 [[05:02](https://www.youtube.com/watch?v=srVKdS2RG4g&t=302)]。
        
    - 支援定義主鍵（PRIMARY KEY）、自動建立 Index 索引 [[07:00](https://www.youtube.com/watch?v=srVKdS2RG4g&t=420)]。
        
- **SQLite 系統點指令（Dot Commands）**：
    
    - `.tables`：列出資料庫內所有的 Table [[06:29](https://www.youtube.com/watch?v=srVKdS2RG4g&t=389)]。
        
    - `.schema`：顯示建表時的完整 SQL 結構 [[06:52](https://www.youtube.com/watch?v=srVKdS2RG4g&t=412)]。
        
    - `.indices`：查看相關索引設定 [[07:00](https://www.youtube.com/watch?v=srVKdS2RG4g&t=420)]。
        
    - `.help`：顯示所有 SQLite 內建的點指令說明 [[07:30](https://www.youtube.com/watch?v=srVKdS2RG4g&t=450)]。
        
- **資料操作與日期格式**：
    
    - 使用 `INSERT INTO` 插入資料與 `SELECT` 查詢資料 [[07:47](https://www.youtube.com/watch?v=srVKdS2RG4g&t=467)]。
        
    - **日期格式提醒**：不同資料庫對日期的語法略有差異，在 SQLite 中，日期通常以字串形式（如 `'YYYY-MM-DD'`）來儲存與處理 [[08:19](https://www.youtube.com/watch?v=srVKdS2RG4g&t=499)]。
        

### 4. 輸出格式調整與備份技巧 [[10:00](https://www.youtube.com/watch?v=srVKdS2RG4g&t=600)]

- **文字模式調整**：
    
    - `.mode column`：將查詢結果以表格欄位對齊顯示 [[10:00](https://www.youtube.com/watch?v=srVKdS2RG4g&t=600)]。
        
    - `.headers on`：顯示欄位名稱標頭 [[10:10](https://www.youtube.com/watch?v=srVKdS2RG4g&t=610)]。
        
- **資料庫備份與移植（`.dump`）**：
    
    - `.dump` 指令可將資料庫的所有結構（Schema）與資料（INSERT 敘述）導出成 SQL 腳本文字 [[11:59](https://www.youtube.com/watch?v=srVKdS2RG4g&t=719)]。
        
    - 可利用 `.output <檔名.sql>` 將 dump 出來的內容儲存成文字檔，非常容易進行備份、版本控管或移轉到其他 SQL 資料庫系統 [[12:30](https://www.youtube.com/watch?v=srVKdS2RG4g&t=750)]。
        

### 5. SQLite 的特性與注意事項 [[13:50](https://www.youtube.com/watch?v=srVKdS2RG4g&t=830)]

- **語法限制**：SQLite 的 `ALTER TABLE` 功能相對有限（例如無法直接刪除特定欄位或修改欄位 Constraint），複雜的結構更動通常需要重新建表與遷移資料 [[13:59](https://www.youtube.com/watch?v=srVKdS2RG4g&t=839)]。
    
- **併發性與鎖定**：屬於單檔案架構，較不適合極高併發的多使用者（Multi-user）同時寫入情境 [[15:20](https://www.youtube.com/watch?v=srVKdS2RG4g&t=920)]。
    
- **未來主題預告**：後續影片將會介紹 GUI 圖形介面工具，以及如何透過 Python 連接並操作 SQLite 資料庫 [[15:37](https://www.youtube.com/watch?v=srVKdS2RG4g&t=937)]。