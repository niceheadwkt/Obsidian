## ⬆️ 第一部分：上傳篇（本地端 ➡️ GitHub 雲端）

當你在本地寫好筆記、改好程式碼，想要同步到 GitHub 備份時，請走這套標準流程：

### 步驟 1：掃描並檢查變更 (Rescan)

1. 開啟 Git GUI，點擊左下角的 **`Rescan`**（快捷鍵 `F5`）。
    
2. **`Unstaged Changes`（左上角橘色區）**：會顯示你剛剛動過、但 Git 還沒記錄的檔案。
    

### 步驟 2：移至暫存區 (Stage Changed)

1. 點擊左下角的 **`Stage Changed`**（快捷鍵 `Ctrl + T`），把所有變更移下來。
    
2. 檔案會跑到 **`Staged Changes (Will Commit)`（左下角綠色區）**，代表它們已經進入準備打包的名單中。
    

### 步驟 3：撰寫備忘錄並打包 (Commit)

1. 在右下角的 **`Commit Message`** 框中輸入這次修改的重點（例如：`v2 修正筆記`）。
    
2. 點擊 **`Commit`** 按鈕。此時綠色區的檔案會消失，代表已經成功存入你電腦本地的歷史紀錄中。
    

### 步驟 4：推上雲端 (Push)

1. 點擊右下角的 **`Push`** 按鈕。
    
2. 在彈出的視窗中，確認 **Source Branches** 選中的是你目前的分支（例如 `main` 或 `master`）。
    
3. 點擊 **`Push`**，等待進度條跑完出現 `Success`，雲端就同步完成了！
    

## 📥 第二部分：下載篇（GitHub 雲端 ➡️ 本地端）

在原生的 Git GUI 中，並沒有一鍵 Pull 的按鈕，必須拆解為 **Fetch（下載）** 與 **Merge（合併）** 兩步：

### 步驟 1：擷取雲端最新狀態 (Fetch)

1. 點選頂部選單的 **`Remote`** -> **`Fetch from`** -> **`origin`**。
    
2. 這時 Git 會把 GitHub 上最新的檔案和歷史紀錄「抓取」到電腦的快取中（此時還不會改動你資料夾裡的檔案）。
    
3. 跑完後點擊 `Close`。
    

### 步驟 2：融合進本地資料夾 (Merge)

1. 點選頂部選單的 **`Merge`** -> **`Local Merge...`**。
    
2. 在 **Tracking Branches** 底下，選擇 **`origin/main`**（依你的雲端分支而定）。
    
3. 點擊 **`Merge`**，檔案就會正式下載並更新到你的本地資料夾中。
    

> **💡 命令列一鍵下載捷徑：** 如果覺得 GUI 點選兩次很麻煩，直接在專案目錄的 PowerShell 輸入這行，就能同時完成 Fetch + Merge：
> 
> PowerShell
> 
> ```
> git pull origin main
> ```

## 🛠️ 第三部分：實戰常犯錯誤與解決方案（精選精華）

這幾天我們遇到的大小阻礙，本質上都是因為 Git 的**保護機制**。以下為你梳理核心原因與解法：

### 🚨 痛點一：下載時被暫存檔卡住（Error: Your local changes would be overwritten...）

- **慘況還原**：輸入 `git pull` 時，Git 噴出錯誤，說 `workspace.json` 會被覆蓋，自動終止下載。
    
- **原因**：`workspace.json` 是 Obsidian 的視窗佈局暫存檔。你只要開著 Obsidian 它就會隨時變動。Git 擔心直接下載雲端檔案會吃掉你目前的變動，所以自動煞車。
    
- **解法（拋棄本地暫存變更）**： 在 PowerShell 中輸入以下指令還原該檔案，再重新 Pull 即可：
    
    PowerShell
    
    ```
    git restore AI/.obsidian/workspace.json
    ```
    

### 🚨 痛點二：遇到 Merge Conflict（合併衝突）

- **慘況還原**：Pull 之後，Git 噴出 `CONFLICT (content): Merge conflict in...`，並且在 Git GUI 畫面上出現紅藍相間的驚嘆號，不讓你做任何事。
    
- **原因**：雲端的 `workspace.json` 和你本地上一次提交的內容完全不同，Git 融合成同一個檔案時失敗了，不知道該聽誰的，只好把倉庫「鎖定」等你處理。
    
- **解法（三步驟暴力解鎖）**： 因為它只是介面暫存檔（不含筆記內容），不用逐行對齊，直接在 PowerShell 執行這三行，指定聽本地的（Ours）並結案：
    
    PowerShell
    
    ```
    git checkout --ours AI/.obsidian/workspace.json
    git add AI/.obsidian/workspace.json
    git commit -m "Resolve workspace.json conflict"
    ```
    

### 🚨 痛點三：PowerShell 畫面出現 `>>` 凍結卡住

- **慘況還原**：輸入指令後，畫面沒有反應，只是一直跳出 `>>` 符號。
    
- **原因**：在複製貼上或輸入指令時，不小心夾帶了未閉合的引號、特殊換行字元，導致 PowerShell 誤以為你「話還沒說完」，在原地傻傻等你。
    
- **解法**：
    
    1. 按下鍵盤 **`Ctrl + C`** 強制結束卡死狀態。
        
    2. 重新乾淨地輸入指令即可。
        

## 🧠 觀念大澄清：為什麼我想「下載」，Git 卻叫我「Commit」？

這是很多人剛學 Git 時最常轉不過去的彎：

> **「我明明是要從雲端拿檔案下來，為什麼 Git GUI 還要我點右下角的 `Commit`（提交）？這不是上傳在用的嗎？」**

**正解：這裡的 Commit 不是為了上傳，而是為了「幫下載後的合併（Merge）蓋章簽字」。**

當你執行 `git pull` 時，雲端的檔案**其實已經下載到你的電腦裡了**。但因為兩邊檔案長得不一樣（引發衝突），Git 沒辦法自動幫你融合，此時你的倉庫就像一個「組裝到一半、零件散落一地的機器人」。

我們用指令化解衝突後，點擊 **`Commit`**，就是告訴 Git：

> _「好了！這兩個檔案撞衫的危機我已經處理好了。請幫我把這次**下載並融合完畢的最終成果**，正式打包存檔！」_

點下 `Commit` 的那一刻，合併程序才算真正「結案」，你的倉庫才會解除鎖定。至於要不要再點 `Push`，那就看你想不想把本地新寫的筆記順便備份回雲端囉！

## 🛡️ 終極防禦：如何一勞永逸？

為了避免 `workspace.json` 這個煩人的系統暫存檔以後天天出來阻礙你下載，強烈建議在專案根目錄（`C:\Obsidian`）建立一個名為 **`.gitignore`** 的純文字檔，並在裡面寫入這一行：

Plaintext

```
.obsidian/workspace.json
```

這樣一來，Git 以後就會徹底無視這個檔案的任何變動，保證你的上下傳流程從此順暢無阻！

目前這套同步流程在你的電腦上運作起來，還有遇到其他不順手或卡住的地方嗎？