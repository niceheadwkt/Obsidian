---
title: "【SQL】 超簡易 SQLite 入門教學！SQLite 很可能是世界上最多用戶使用的 SQL 引擎？(中文字幕) (可調節速度)"
source: "https://www.youtube.com/watch?v=srVKdS2RG4g"
author:
  - "[[Dex IT Flipped Classroom]]"
published: 2024-04-11
created: 2026-09-04
description: "SQLite SQL 教學廣東話 2026 HKDSE ICT Database Syllabus 清Concept 回應「資訊及通訊科技」課程及評估指引 (中四至中六) (DSE ICT Syllabus)Elective A 選修部分A: 第31頁的部分內容https://www.edb.gov.hk/attachment/tc/curriculum-development/kla/t"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=srVKdS2RG4g)

SQLite SQL 教學廣東話 2026 HKDSE ICT Database Syllabus 清Concept  
  
回應「資訊及通訊科技」課程及評估指引 (中四至中六) (DSE ICT Syllabus)  
Elective A 選修部分A: 第31頁的部分內容  
https://www.edb.gov.hk/attachment/tc/curriculum-development/kla/technology-edu/curriculum-doc/ICT\_C&A%20Guide\_c\_final.pdf#page=391  
學習重點： 數據庫及數據庫管理系統 DBMS 有關的概念及應用技巧  
  
#ictnotes #ictdse #ict懶人包 #ict雞精 #教學新常態 #翻轉教學  
  
本影片建基於前設介紹，如 未觀看 / 想重溫 可到👇🏻：  
  
【DEX IT 概念速成】CMD/PowerShell 列出目錄/開啟檔案 改變工作目錄 列出檔案及資料夾 開啟檔案 dir ls cd 教學 (中文字幕) (可調節速度)  
https://youtu.be/cm4rhvlcAHs  
  
【SQL】 Access SQL DDL CREATE / ALTER TABLE 建立/修改表格、CONSTRAINT 條件約束、PRIMARY KEY 主關鍵碼 教學 (中文字幕) (可調節速度)  
https://youtu.be/YifAxM77Ock  
  
【SQL】 Access SQL SELECT, WHERE 過濾、ORDER BY 排序、DISTINCT, AS 教學 (中文字幕) (可調節速度)  
https://youtu.be/q7f00TnrMqQ  
  
🏃‍ 本頻道影片以扼要講述為本 🐇 如果覺得語速太快，或需時消化，可以嘗試：  
1\. 🐌 調節影片至合適的速度，例如0.75x倍速  
2\. ⏸️ 暫停影片，⏪ 返回再播放  
🏋 更鼓勵大家跟隨短片中示範進行測試，從實淺中自主學習！感謝各位觀眾支持！😁  
  
0:00 前言  
0:46 SQLite 特色/特性  
2:31 下載及啟動 SQLite 命令列工具  
3:45 Transient in-memory database 短暫記憶資料庫  
4:10 開啟數據庫檔案 (.open)  
4:52 列出連接資料庫的名稱和檔案路徑 (.databases)  
5:08 建立表格 (CREATE TABLE)  
6:24 列出表格名稱 (.tables)  
6:40 顯示模式/表格架構 (.schema)  
7:06 顯示索引名稱 (.indexes)  
7:21 顯示使用提示 (.help)  
7:45 輸入記錄 (INSERT INTO)  
8:14 輸入日期之注意事項  
9:06 抽取數據庫記錄 (SELECT)  
9:35 為什麼輸入 SELECT \* 後什麼都沒有顯示？  
9:52 設定輸出模式 (.mode)  
10:16 開啟或關閉表頭/欄位標題顯示 (.headers)  
10:36 這些工作到底有沒有儲存在檔案中？  
10:52 再次開啟數據庫檔案 (.open) 驗證數據是否儲存在檔案中  
11:41 在系統命令外殼中執行指令參數 (.shell)  
11:55 將數據庫內容呈現為一系列 SQL 語句 (.dump)  
13:33 退出 sqlite3 (.quit)  
13:48 SQLite 的限制  
15:36 結語  
  
如果大家喜歡 Dex IT Flipped Classroom ，記得Like👍🏻、訂閱📧，和分享👨‍👩‍👧‍👧給你的朋友啊！順手按下訂閱旁的鈴鐘🔔，可以第一時間收到我的新影片🎞發佈通知🔔  
  
💣DON'T CLICK ME! 咪亂撳! http://bit.ly/d0ntcl1ckme  
  
HKDSE DSE ICT Database FlippedClassroom Chinese Cantonese #香港Youtuber 粵語 廣東話 中文字幕  
\*概念上可能幫到手  
\*純屬概念分享  
\*歡迎交流  
  
This is a non-sponsored video. 此影片並非廣告。  
  
本影片採用 SQLite3 在 Windows 10 進行示範  
  
拍攝工具  
Logitech BRIO  
Rode Wireless Go II  
Screencast-O-Matic 2.3  
  
製作軟件  
Adobe Premiere Pro 2024  
Amplify Music Launchpad  
Subtitle Edit 3.5

## Transcript

### 前言

**0:07** · 大家好 歡迎回來 Dex IT 之前介紹過使用 MS Access 的 Database (數據庫 / 資料庫) 學習不同的 SQL 操作 不過大家有沒有思考過日常使用的應用程式 包括在手機或電腦中使用的應用程式 (APP) 其實背後大部分都是使用 SQL 引擎儲存資料

**0:26** · 今天介紹一個 SQL 引擎 不論你是想設計一個程式給自己或別人使用 或是你正在修讀 HKDSE ICT 想練習一下 SQL Statement 不論是新舊課程的 Database Elective (選修單元: 數據庫) 這個軟件都是相對地比較簡單 不是太複雜 今天的介紹會幫到大家 SQLite 引擎的特色就是它是一個 Local (本機) 的資料庫

### SQLite 特色/特性

**0:50** · 也沒有任何 Client Server (客戶端伺服器) 的模式 不需要特別設立 Server (伺服器) 也不需要做任何繁複的設定 都能夠使用得到 基本上整個資料庫就是儲存在一個 File (檔案) 裡 同時它也十分可靠 相對來說是比較穩定的資料庫引擎 適合一些中小型軟件使用 也很容易整合在不同的應用程式裡 根據它的官網描述 SQLite 是世界上最多 deployment (部署) 和最被廣泛使用的資料庫引擎

**1:19** · 很多有名的公司也是 SQLite 的用家 每一個 Android 裝置、 每一個 iPhone 或 iOS 裝置、 每一個 Mac 或 Windows 10 machine、 或是各類型的 Browser (瀏覽器) 其實它們在背後都是使用到 SQLite 引擎 PHP 和 Python 也有一個 SQLite 資料庫的 Library (函式庫) 不用安裝也可以直接使用 以後的影片也會向大家介紹如何在 Python 使用 SQLite 有趣的是原來大部分電視和機頂盒也是使用 SQLite 儲存資料

**1:55** · 操作上 SQLite 都是使用標準的 SQL Query (查詢) 和 Command (指令) 等等 大部分 SQL 都能在 SQLite 上使用 還有就是 SQLite 是一個跨平台的應用 例如 Windows 裝置、Android 裝置、Apple 的 iOS、Mac 或 Linux 平台等等

**2:12** · 其實全部能被 SQLite 支援 我們一起來看看如何操作這個軟件 以及看看它有什麼好壞處 和需要注意的地方 這裡會分享不同範疇的 IT 實用技巧 包含網絡技術運作、編程、數據庫、MS Word、Excel、PowerPoint、網絡保安 以及 HKDSE 系列 絕對適合在職場工作 想進修 IT 知識 或是修讀 DSE 的你 記得訂閱 Dex IT 啊！

### 下載及啟動 SQLite 命令列工具

**2:32** · 如何下載 SQLite？

**2:33** · 最容易的方法就是下載它的 executable (執行檔) 去 SQLite 的官網 Latest Release 的位置按 Download 你會看到它有專門為 Mac 或 Linux 等裝置的下載軟件 我這次的介紹會使用 Windows 電腦做示範 以 Windows 裝置來說 最容易操作的就是 sqlite-tools 這個會連同一些 command-line tools (命令列工具) 給你使用 這次示範主要會使用到 command-line shell program (命令列殼層程式)

**3:03** · 我們可以下載這個 zip 檔案 下載後開啟這個 zip 檔案 按 Compressed Folder Tools (壓縮的資料夾工具) 再選擇 Extract all (解壓縮全部) 開啟這個藍色有一條羽毛在旁的檔案就可以開始操作了 這時通常會彈出 Microsoft Defender SmartScreen 的一個警告 為什麼會這樣？

**3:20** · 原因是 SQLite 的這個檔案沒有做 Digital Signature (數碼簽署 / 公鑰數位簽章) 因此 當 Microsoft Defender 看到這個沒有數碼簽署的執行檔案就會彈出警告 因為 SQLite 是我們信任的軟件開發商 基於這個信任 我們都可以按下 Run anyway (執行) 以開啟檔案 如果你真的不放心 都可以嘗試把這個 Zip 檔案上載到 VirusTotal 掃描一次 現在開啟了 SQLite Command-line tools 第一句會看到的就是 “Connected to a transient in-memory database” 什麼意思呢？

### Transient in-memory database 短暫記憶資料庫

**3:55** · 即是預設會把你的工作掛載在一個短暫記憶資料庫 如果你只是測試它的功能 它就不會幫你儲存任何東西在你的檔案 如果你想開啟一個檔案儲存之後的工作 這裡都有教你如何處理 .open 這個 Command (命令 / 指令) 就可以處理到 我們嘗試輸入 .open dexit.db 以建立一個叫做 dexit.db 的檔案

### 開啟數據庫檔案 (.open)

**4:23** · 按 Enter 這樣就已經開啟了一個新的資料檔 之後繼續的操作就是儲存在這個資料檔裡 現在建立 dexit.db 檔案的動作 就已經在剛才的 SQLite 解壓了資料夾中出現了一個新檔案

**4:42** · 如果你不想把新建立的檔案儲存在原本的這個位置 你都可以在這裡輸入完整路徑 就像之前介紹的操作方式一樣 建立新檔案後 再介紹另一個指令叫做 .databases 按 Enter 後會顯示你正在使用的檔案及其路徑 現在這個檔案是沒有儲存任何資料的 你會看到其檔案大小是 0 KB 要建立 Table (表格) 時就可以使用 CREATE Statement 來處理

### 列出連接資料庫的名稱和檔案路徑 (.databases)

### 建立表格 (CREATE TABLE)

**5:15** · 之前向大家介紹過的指令都可以在 SQLite 上使用 由於時間的關係 我已經準備好 CREATE Statement 把預先準備好的 CREATE Statement 複製並在這裡貼上 當然你也可以手動輸入 或是在其他文件例如 Notepad 預先準備這些指令 然後複製貼上 這個 SQL Statement 有很多分行 在 SQLite 指令工具上輸入 SQL 可以隨意分行

**5:41** · 也可以隨意在中間輸入空白符 讓你更加容易閱讀 也是沒有問題的 這方面就跟之前介紹 Access 時的處理也是一樣 不過凡是有分號出現再按 Enter 的話 它就會執行以上的 SQL Statement 我現在按 Enter 就已經執行了以上建立表格的 SQL Statement 了

**6:06** · 我現在再建立第二個表格 之後就向大家講解如何知道真的是建立了表格 我再次複製預先準備好的 SQL Statement 然後在這裡貼上 這些 SQL Statement 的詳細意思都可以重溫之前的影片 是介紹利用 SQL Statement 建立表格的處理 我就不在這段影片重複了 現在完成建立兩個表格 怎樣檢視已經成功建立這兩個表格呢？

### 列出表格名稱 (.tables)

**6:31** · 再介紹兩個指令給大家 一個就是 .tables 就會列出這個資料檔案裡所有表格的表格名稱 如果你想更詳細地列出表格 例如表格的實際Schema (模式/架構) 有什麼表格、表格裡有什麼 Field (欄位) 有什麼 Datatype (資料類型) 或是有什麼 Constraint (約束) 等等 想檢視以上提及的詳細內容都可以使用另一個指令叫做 .schema 就會出現我剛才輸入的兩個 CREATE Statement 有時候在資料庫的世界 這些 CREATE Statement 都能告訴你資料庫架構的實質內容

### 顯示模式/表格架構 (.schema)

### 顯示索引名稱 (.indexes)

**7:06** · 這次做這個資料庫 都使用了 Index (索引) 介紹一個叫做 .indexes 的指令 按 Enter 後會顯示表格的 Key (鍵碼) 並自動列出了其索引 都能夠從它的名字中得知 其實在 SQLite 裡是可以使用很多不同的 . 指令 想了解更多 可以輸入 .help 指令 就會列出所有以 . 為首並能夠在 SQLite 使用的指令

### 顯示使用提示 (.help)

**7:35** · 當然你也可以到 SQLite 官網 裡面也有詳細的介紹 這次我會嘗試示範一些我覺得能即時幫到大家的指令 現在我建立了兩個表格 是沒有任何記錄 (Record) 在這兩個表格的 跟之前學習使用 SQL 一樣 可以利用 Insert 指令輸入記錄 我現在就示範一下 INSERT INTO PRODUCT VALUES (1, ‘Strawberry’,

### 輸入記錄 (INSERT INTO)

**8:04** · 日期就是 ‘2023-02-15’ 這些都是隨便的例子 現在的貨量是 1000 再輸入分號就可以了 介紹到這裡 就想向大家分享一下 為什麼日期要使用引號呢？

### 輸入日期之注意事項

**8:20** · 現在看上去比較像是一個 String (字串) 是的 我的看法是在不同資料庫系統 日期的 Syntax (語法) 都有不一樣 大家以後可能不只是接觸 Access 或 SQLite 可能還會使用其他種類的資料庫系統 不同的資料庫系統在 日期 的語法是會有不一樣的 這個位置大家要多加留意 如果是 SQLite 的話 把日期當作字串以 ‘年-月-日’ 中間用 Hyphen (連字號) 串連的方式輸入

**8:57** · 這個寫法是正確的 由於時間關係 我們把其他 INSERT Statement 都複製貼上 完成輸入八句不同的記錄後 我們可以利用之前學過的 SELECT Statement 抽取出資料庫的記錄

### 抽取數據庫記錄 (SELECT)

**9:15** · 現在嘗試輸入 SELECT \* FROM PRODUCT; 它就會列出表格 PRODUCT 的所有記錄了 再嘗試輸入 SELECT \* FROM ORDERS; 表格 ORDERS 是沒有任何記錄的 這個方法都是使用我們之前學習過的 SQL Statement 有時候有一些同學會有趣地問 為什麼輸入 SELECT \* 後什麼都沒有顯示？

### 為什麼輸入 SELECT \* 後什麼都沒有顯示？

**9:43** · 為什麼會這樣？

**9:44** · 這是因為裡面真的是沒有任何記錄 這個都是同學們常問的問題 現在你會看到在 SQLite 的環境裡 這些抽取出來的記錄沒有任何 Header (表頭/欄位標題) 也不是以表格的形式來顯示這些記錄 如果想更容易地閱讀 再介紹多一個工具給大家 就是 .mode 指令 例如先輸入 .mode columns 再輸入 SELECT Statement 來顯示當中的記錄

### 設定輸出模式 (.mode)

**10:12** · 它現在就會欄位的形式整齊地顯示這些記錄 還有一個 .headers的指令 輸入 .headers on 再輸入 SELECT Statement 就會顯示欄位標題以及其記錄 但如果你不想顯示欄位標題 你都可以輸入 .headers off 再輸入 SELECT Statement 就會隱藏了記錄上的欄位標題 直接顯示記錄 現在都輸入了一些記錄 工作有一些進展 不過這些工作到底有沒有儲存在檔案中？

### 開啟或關閉表頭/欄位標題顯示 (.headers)

### 這些工作到底有沒有儲存在檔案中？

**10:44** · 我可以告訴你 是的 因為我們是直接開啟了資料庫檔案進行工作 現在這個檔案的檔案大小已經增長到 24KB 如果下一次想再次開啟這個資料出來 要怎樣處理呢？

### 再次開啟數據庫檔案 (.open) 驗證數據是否儲存在檔案中

**10:58** · 現在先把它關掉再重新開啟讓大家看一次 讓大家知道是真的可以重新開啟這些東西出來的 輸入 .quit 離開這個 SQLite 的環境 然後再次開啟 sqlite3 的程式 這次就沒有 Microsoft Defender SmartScreen 的警告 直接開啟了 SQLite 環境 因為上次已經告訴它是可以直接開啟的 嘗試輸入 .open dexit.db 以開啟剛才的檔案 然後想看看剛才輸入的記錄和表格是否仍然存在

**11:27** · 可以輸入 .schema 看看 都看到表格依然存在 嘗試輸入 SELECT \* FROM PRODUCT; 所有記錄都依然存在 代表表格和記錄是已經儲存在這個檔案 再介紹另一個指令叫做 .shell .shell 是平時 CMD 會使用的指令 是直接 Call (呼叫) 系統處理一些事情 例如我想 Clear Screen (屏幕清除) 輸入 .shell cls 按 Enter 就已經清除了屏幕 剛才示範的過程中都有使用過 只是剛才沒有特別介紹 離開這次的示範前

### 在系統命令外殼中執行指令參數 (.shell)

### 將數據庫內容呈現為一系列 SQL 語句 (.dump)

**11:58** · 我想介紹多一個指令給大家認識 就是一個叫做 .dump 的指令 它會把你所有的表格和記錄 以文字的方式顯示出來 例如這裡的 CREATE TABLE PRODUCT 不同的欄位 也顯示所有要列出記錄的 INSERT Statement

**12:22** · 還有這個檔案的其他表格 理論上把這段文字複製 貼上在另一個資料庫 就可以重新建立整個資料庫 連同所有模式、約束、記錄 都能夠全部重新建立出來 所以這個 SQLite 資料庫是可以 Port (移植) 去另一個 SQLite 資料庫

**12:45** · 甚至可以做一些簡單的修改 把整個 SQLite 資料庫移植去其他資料庫引擎 例如 MySQL、Oracle 等等 理論上都沒有太大的問題 也不需要大修改 這個都是其中一個 SQLite 的好處 比較 Portable (可移植) 我現在又快速做一個示範 把這段文字複製 然後關閉這個檔案 再開啟另一個檔案 例如 .open dexit2.db

**13:17** · 把複製的文字在另一個檔案貼上 執行完畢後輸入 .schema 看看 就會看到整個模式都是一樣的 嘗試輸入 SELECT \* FROM PRODUCT 所有記錄都是一樣的 就是這樣 最後離開檔案輸入 .quit 這裡看到這兩個檔案的檔案大小都是一樣的 是透過 dump (轉存) SQL Statement 成功地由一個資料庫轉存去另一個資料庫

### 退出 sqlite3 (.quit)

### SQLite 的限制

**13:48** · 不過 SQLite 都有一些限制 與其他 Client Sever 模型的資料庫引擎有少許不一樣 第一個就是 ALTER TABLE 的支援 普遍認識 ALTER TABLE 相關的指令 例如 RENAME TABLE、ADD COLUMN、RENAME COLUMN、DROP COLUMN 等都是支援的 但是 ALTER COLUMN 例如修改資料類型 或是ADD CONSTRAINT 等等

**14:15** · SQLite 是不支援的 當然 如果你工作途中想有這些操作 都有一些比較轉折的方法處理 有機會再與大家分享 不過一般來說都不太建議的 第二就是 Trigger 的支援 我們沒有介紹過的 有一些資料庫系統容許在某些動作後會 Trigger (觸發) 另一個 SQL 指令的執行

**14:38** · 之後介紹相關內容時再詳細分享 SQLite 也不是完全不支援 Trigger 的 第三就是 Writing to VIEWs 大家可能在 Access 都留意得到 例如在不太複雜的 Query (查詢) 上 直接修改查詢上的資料 但是 SQLite 的 View 就完全是 Read Only (唯讀) 不能在 View 或 儲存了的查詢上做任何修改

**15:08** · 不過這裡就介紹你使用 Trigger 的方法處理部分修改 意思不完全是一樣 但是它提供了其他可行方案來處理一些修改 最後的 GRANT and REVOKE 就是一些比較大型、multi-users (多個使用者) 的資料庫 是可以在表格和欄位為不同使用者設定一些權限等等 不過因為 SQLite 的存在方法是 Local File (本機檔案) GRANT and REVOKE 的操作與 SQLite 都不太相關 SQLite 就沒有處理這個部分的限制 以上是關於在命令列界面使用 SQLite 的介紹 有沒有一些 Graphical User Interface GUI (圖形用戶界面) 的選擇呢？

### 結語

**15:44** · 其實是有的 之後再向大家介紹 都預告一下 因為之前都介紹過 Python 我們是否可以把 SQLite 在 Python 上使用？

**15:54** · 當然是可以的 也是一個十分常見的操作 稍後都會向大家一一介紹 請大家密切期待 如果你喜歡以上的介紹 記得 Like, Subscribe 和 Send 給你的朋友！

**16:05** · Database 和 Python 程式系列會繼續陸續有來 我們很快又再見！