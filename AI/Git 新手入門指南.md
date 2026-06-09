學習使用 Git 其實就像是在為你的專案建立一個「時光機」**與**「儲存分身」的系統。它可以幫你記錄程式碼（或檔案）的每一次修改，讓你在寫壞時隨時「倒帶」，或是同時進行不同的功能開發。

以下為你整理最核心、最實用的 Git 新手入門指南，我們一步一步來：

## 步驟一：安裝與基本設定

在開始使用 Git 之前，必須先讓電腦認識它，並告訴它你是誰（這樣未來的修改紀錄才會知道是誰做的）。

1. **下載與安裝**：
    
    - 前往 [Git 官方網站](https://git-scm.com/) 下載適合你作業系統（Windows / Mac / Linux）的版本並安裝（基本上一直點下一步即可）。
        
2. **開啟終端機 (Terminal)**：
    
    - **Windows**：請搜尋並開啟 `Git Bash`（安裝 Git 時附帶的工具，最推薦）。
        
    - **Mac**：開啟 `終端機 (Terminal)`。
        
3. **設定使用者資訊**（一生只要設定一次）：
    
    請在終端機輸入以下指令（請將引號內換成你的名字和 Email）：
    
    Bash
    
    ```
    git config --global user.name "Your Name"
    git config --global user.email "your_email@example.com"
    ```
    

## 步驟二：建立你的第一個 Git 專案（初始化）

我們要告訴 Git 開始監控某個資料夾。

1. **建立並進入資料夾**：
    
    在電腦裡建立一個測試用的資料夾（例如 `git-demo`），並用終端機切換到該目錄。
    
    Bash
    
    ```
    cd /path/to/your/git-demo
    ```
    
2. **初始化專案**：
    
    輸入以下指令，這會在專案內建立一個隱藏的 `.git` 資料夾，正式啟動時光機：
    
    Bash
    
    ```
    git init
    ```
    
當你在一個已經有檔案的資料夾中執行 `git init` 時，它**完全不會刪除、修改或覆蓋**你原本的任何檔案。

它的唯一作用，就是在這個資料夾裡建立一個名為 `.git` 的**隱藏資料夾**。這個隱藏資料夾就像是 Git 的「大腦」或「紀錄本」，用來存放未來的版本歷史紀錄和設定。

## 步驟三：日常開發工作流（核心：加到暫存、提交存檔）

這是你每天使用 Git 最頻繁的步驟。請記住 Git 的核心邏輯：

**「工作目錄（寫程式）」 $\rightarrow$ 「暫存區（挑選要存檔的檔案）」 $\rightarrow$ 「儲存庫（正式封裝存檔）」**。

### 1. 檢查目前狀態

不論何時，你都可以輸入這行指令來查看目前的檔案狀態：

Bash

```
git status
```

### 2. 建立新檔案並加入「暫存區 (Staging Area)」

假設你新增了一個 `index.html` 檔案，現在你想把這個變更準備拿去存檔：

Bash

```
git add index.html
```

> 💡 **實用小技巧**：如果你一口氣改了很多檔案，想全部一起暫存，可以使用 `git add .`（後面的句點代表全部）。

### 3. 提交存檔 (Commit)

這步就像是在遊戲裡點擊「儲存進度」，並寫下一段備忘錄（Commit Message），說明這次改了什麼：

Bash

```
git commit -m "建立首頁 HTML 結構"
```

> ⚠️ **注意**：`-m` 後面的訊息非常重要，請務必簡短、清楚地說明這次的修改目的。

## 步驟四：查看歷史紀錄（查看過去的存檔）

當你累積了幾次 Commit 之後，你可以隨時查看你的時光機紀錄：

Bash

```
git log
```

這會顯示每一次 Commit 的**作者、時間、以及一串代表該次存檔的「雜湊碼 (SHA-1 ID)」**。如果紀錄太多，可以按鍵盤的 `q` 鍵離開。

> 💡 想要看精簡版的一行指令：`git log --oneline`

## 步驟五：分支管理 (Branch) —— 同時做不同的事

分支是 Git 最強大的功能。假設你的網站已經上線（主線叫 `main` 或 `master`），現在你想開發一個「新功能」，但又怕寫爛影響到原本正常的網站，這時你就需要開一個「分身（分支）」。

1. **建立新分支**（例如建立一個叫 `feature-login` 的分支）：
    
    Bash
    
    ```
    git branch feature-login
    ```
    
2. **切換到該分支**：
    
    Bash
    
    ```
    git checkout feature-login
    ```
    
    _(在較新的 Git 版本中，也可以使用 `git switch feature-login`)_
    
3. **在分支上工作與存檔**：
    
    在這個分支下，你可以放心修改程式碼、進行 `git add` 和 `git commit`，完全不會影響到主線。
    
4. **合併分支 (Merge)**：
    
    當新功能寫好、測試沒問題，想把它抓回主線時：
    
    - 先切換回主線：`git checkout main`
        
    - 把新功能合併進來：`git merge feature-login`
        
5. **刪除用不到的分支**：
    
    Bash
    
    ```
    git branch -d feature-login
    ```
    

## 步驟六：與遠端儲存庫同步（以 GitHub 為例）

當你需要把程式碼備份到雲端，或是與他人協作時，就會用到 GitHub / GitLab / Bitbucket 等平台。

1. **在 GitHub 上建立一個新的 Repository（儲存庫）**，並複製該儲存庫的 HTTPS 或 SSH 網址。
    
2. **將本地專案連結到遠端 GitHub**：
    
    Bash
    
    ```
    git remote add origin https://github.com/你的帳號/你的專案名稱.git
    ```
    
3. **將本地的程式碼推送到雲端 (Push)**：
    
    Bash
    
    ```
    git push -u origin main
    ```
    
    _(之後只要簡寫輸入 `git push` 即可)_
    
4. **如果是在別台電腦想把雲端的專案下載下來 (Clone)**：
    
    Bash
    
    ```
    git clone https://github.com/你的帳號/你的專案名稱.git
    ```
    
5. **如果雲端有更新，想把最新進度抓回本地電腦 (Pull)**：
    
    Bash
    
    ```
    git pull
    ```
    

## 💡 新手必備的四大防呆指令卡

- **「我剛剛到底改了什麼？」** $\rightarrow$ `git diff`（查看尚未暫存的修改內容）
    
- **「我想放棄某個檔案剛才的修改，回到上次存檔狀態」** $\rightarrow$ `git checkout -- <檔名>`
    
- **「完蛋，我剛才那台時光機開錯分支了/做錯了，我想強制退回上一次 Commit 的狀態」** $\rightarrow$ `git reset --hard HEAD` _(警報：此指令會清除未存檔的修改，請小心使用)_
    
- **「指令太多記不住怎麼辦？」** $\rightarrow$ 可以先下載圖形化介面工具（如 **Sourcetree**、**GitKraken**，或是直接使用 **VS Code** 內建的 Git 面板），配合這些圖像操作，會更容易理解分支與暫存的概念！