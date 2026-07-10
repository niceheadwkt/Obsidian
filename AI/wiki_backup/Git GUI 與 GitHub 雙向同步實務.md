---
type: concept
tags: [Git, GitGUI, GitHub, 版本控制, 同步, 衝突解決]
sources: [
  "[[raw/Git GUI 與 GitHub 雙向同步全面操作指南.md]]",
  "[[raw/Git_GUI_GitHub_Comprehensive_Guide.pdf]]",
  "[[raw/Git GUI 與 GitHub 雙向同步全面指南(整合實戰衝突、底層邏輯與問答精華之技術對談紀錄).md]]",
  "[[raw/Google 雲端硬碟偏好設定調整與 Git Gui 遠端綁定故障排除指南.md]]",
  "[[raw/VS_Code與GitHub雙向同步之環境衝突、防範配置與推送錯誤排除指南.md]]"
]
created: 2026-06-13
updated: 2026-06-24
---

# Git GUI 與 GitHub 雙向同步實務

**Git GUI 與 GitHub 雙向同步實務** 旨在提供利用圖形介面與命令行進行 Git 雙向同步的標準作業流程（SOP）、底層運作邏輯，以及針對常見同步衝突（特別是 Obsidian 產生的介面暫存檔衝突）的防禦與修復技術。

---

## 1. 上傳流程：本地端 $\rightarrow$ GitHub 雲端

當您在本地端完成筆記撰寫或代碼修改後，請遵循以下四步驟將變更備份至雲端：

1.  **掃描變更 (Rescan)**：
    *   開啟 Git GUI，點擊左下角的 **`Rescan`**（快捷鍵 `F5`）。
    *   此時左上角橘色區域 **`Unstaged Changes`** 會顯示所有已被修改但尚未被 Git 追蹤的檔案。
2.  **移至暫存區 (Stage Changed)**：
    *   點擊左下角的 **`Stage Changed`**（快捷鍵 `Ctrl + T`）。
    *   檔案會移動至左下角綠色區域 **`Staged Changes (Will Commit)`**，代表已進入準備打包的名單中。
3.  **打包存檔 (Commit)**：
    *   在右下角 **`Commit Message`** 輸入本次修改的備註（例如：`v2 整理投資思維`）。
    *   點擊 **`Commit`**。此時綠色區域清空，代表修改已成功存入**您電腦本地的歷史紀錄**中。
4.  **推上雲端 (Push)**：
    *   點擊右下角 **`Push`** 按鈕。
    *   確認彈出視窗中的 **Source Branches** 為您當前使用的分支（如 `main` 或 `master`）。
    *   點擊 **`Push`**，等待進度條跑完並顯示 `Success`，雲端備份即告完成。

---

## 2. 下載流程：GitHub 雲端 $\rightarrow$ 本地端

原生 Git GUI 為了確保安全性，並未提供一鍵 Pull 的直覺按鈕，而是將其拆解為 **Fetch（下載）** 與 **Merge（合併）** 兩個安全步驟：

### 標準 GUI 操作法
*   **步驟一：擷取雲端狀態 (Fetch)**
    *   點選頂部選單的 **`Remote`** $\rightarrow$ **`Fetch from`** $\rightarrow$ **`origin`**。
    *   Git 會將雲端最新歷史紀錄抓取到本地快取，此時**本地資料夾尚未被修改**。完成後點擊 `Close`。
*   **步驟二：融合至本地 (Merge)**
    *   點選頂部選單的 **`Merge`** $\rightarrow$ **`Local Merge...`**。
    *   在 **Tracking Branches** 下選擇對應的雲端分支（例如：`origin/main`）。
    *   點擊 **`Merge`**，雲端變更正式寫入並更新您的本地資料夾。

### 命令行快速捷徑 (PowerShell)
若覺得 GUI 連續點選較為繁瑣，可在專案根目錄開啟 PowerShell 輸入以下指令，一鍵自動完成 Fetch 與 Merge：
```powershell
git pull origin main
```

---

## 3. 實戰常見錯誤與排除方案

Git 擁有嚴格的保護機制，在同步雙向變動時，常因以下痛點導致流程中斷：

### 🚨 痛點一：下載時被暫存檔卡住 (Your local changes would be overwritten...)
*   **情境**：執行 `git pull` 時出錯，提示某些檔案（如 Obsidian 的 `workspace.json`）將被合併覆蓋，導致下載中止。
*   **原因**：`workspace.json` 是 Obsidian 的視窗佈局暫存檔，只要軟體開啟就會隨時變動。Git 偵測到雲端有新版本，但本地版本亦有未 Commit 的變動，為防止覆蓋您的本地修改而自動煞車。
*   **解決方案**：若確定該本地變更不重要（如視窗佈局），可在 PowerShell 中執行以下指令強制還原該檔案，再重新 Pull：
    ```powershell
    git restore .obsidian/workspace.json
    ```

### 🚨 痛點二：遭遇 Merge Conflict (合併衝突) 導致倉庫鎖定
*   **情境**：Pull 後提示 `CONFLICT (content): Merge conflict in...`，Git GUI 出現紅藍相間的驚嘆號，且不允許進行其他操作。
*   **原因**：雲端與本地同時對同一個檔案（如 `workspace.json`）進行了不同修改，Git 在嘗試自動融合時失敗，因無法抉擇而將倉庫「鎖定」。
*   **三步驟強行解鎖方案**：由於 `workspace.json` 僅為軟體介面暫存檔而不含核心筆記，無須手動對齊，直接在 PowerShell 執行以下三行，指定以本地（Ours）版本為主並結案：
    ```powershell
    git checkout --ours .obsidian/workspace.json
    git add .obsidian/workspace.json
    git commit -m "Resolve workspace.json conflict"
    ```

### 🚨 痛點三：PowerShell 畫面出現 `>>` 凍結卡住
*   **情境**：輸入指令後無反應，一直換行跳出 `>>` 符號。
*   **原因**：複製貼上時夾帶了未閉合的引號（`"` 或 `'`）或特殊換行字元，使 PowerShell 誤認為「指令尚未輸入完畢」而原地等待。
*   **解決方案**：按下 **`Ctrl + C`** 強制結束卡死狀態，重新乾淨輸入指令即可。

---

## 4. 深度觀念釐清：為什麼下載也需要 Commit？

許多剛接觸 Git 的使用者常會產生疑問：
> **「我明明是要從雲端下載檔案，為什麼 Git 還要我點右下角的 `Commit`？這不是上傳在用的嗎？」**

*   **解答**：這裡的 Commit **不是為了上傳，而是為了「幫下載後的合併（Merge）結果簽字畫押」**。
*   當您執行 `git pull` 時，雲端的檔案其實已經下載到您的電腦了。但因為兩邊檔案發生了衝突，Git 沒辦法自動融合。我們用指令宣告解決衝突後，點擊 **`Commit`** 就是告訴 Git：
    > *「衝突我已經處理完畢了。請幫我把這次下載並融合完畢的最終成果正式打包存檔！」*
*   點下 Commit 的那一刻，合併程序才算真正「結案」，倉庫才會解除鎖定。這與是否要 Push 上傳無關。

---

## 5. 終極防禦：利用 `.gitignore` 一勞永逸

諸如 `workspace.json` 這類隨操作介面即時變動的環境暫存檔，本質上並無任何備份或團隊協作同步的價值，頻繁同步只會徒增雙向衝突的機率。

### 建議配置步驟
在您專案的根目錄（例如 Obsidian 儲存庫資料夾的第一層）建立一個名為 **`.gitignore`** 的純文字檔案，並在檔案內寫入以下規則：
```plaintext
.obsidian/workspace.json
```
儲存後，Git 從此便會徹底無視該檔案的任何變動。無論您如何頻繁地開啟、關閉軟體或調整介面，它都不會再出現在 Git GUI 的掃描清單中，讓雙向同步流程回歸純粹與順暢。

---

## 6. VS Code 嵌套 Git 儲存庫衝突與 `.gitignore` 防範配置

在結合使用 VS Code 與 Git GUI 進行雙向同步時，常見因多重儲存庫嵌套而引發的偵測異常。

### 🚨 痛點四：VS Code 內 GitLens 誤判為 `Untracked`
*   **情境**：在 VS Code 中開啟筆記檔案時，明明該檔案已在主儲存庫提交推送過，但 GitLens 卻顯示為 `Uncommitted changes`，懸停顯示 `Working Tree · Untracked`，無法檢視過往歷史。
*   **原因**：本地存在**兩個互相嵌套的 Git 儲存庫**（例如最外層 `/Obsidian/` 為主儲存庫，而 `/Obsidian/AI/` 因過去下載範例或意外執行 `git init` 產生了子儲存庫）。在 VS Code 中點開位於 `AI/wiki/` 的檔案時，VS Code 機制優先向下識別最鄰近的 `AI/` 子儲存庫 `.git`。對子儲存庫而言，該檔案從未提交，因而誤判。
*   **解決方案**：
    1.  刪除子目錄 `/Obsidian/AI/` 底下不必要的隱藏系統資料夾：`.git`（核心子倉庫設定）、`.obsidian` 與 `.trash`。
    2.  刪除後，GitLens 會自動向上追溯，與最外層的 `Obsidian (main)` 倉庫綁定，即可恢復歷史紀錄。

### 🛠️ 防嵌套 `.gitignore` 配置與快取整理
為了根除並防止未來下載外部專案或 MCP 伺服器時，再度產生 `.git` 干擾主倉庫，應在最外層（`/Obsidian/` 根目錄）的 `.gitignore` 中加入以下阻斷規則：
```text
# 強制忽略任何子資料夾底下的隱藏 .git 資料夾，防止本地偵測機制錯亂
**/.git/
```
若子倉庫的 `.git` 狀態已被主倉庫誤當成檔案追蹤，請執行以下命令刷清 Git 快取：
```powershell
# 僅清除 Git 的追蹤快取索引（不會刪除硬碟上的實體檔案）
git rm -r --cached .
# 依照全新 .gitignore 重新捕捉檔案並提交
git add .
git commit -m "chore: 配置防嵌套 .gitignore 規則並刷新 Git 索引快取"
```

---

## 7. Google 雲端硬碟同步、推送遭拒與清理排障

根據 [[raw/Google 雲端硬碟偏好設定調整與 Git Gui 遠端綁定故障排除指南.md|Google雲端與Git遠端綁定排障指南]] 與 [[raw/VS_Code與GitHub雙向同步之環境衝突、防範配置與推送錯誤排除指南.md|VS Code與GitHub雙向同步排障指南]]，當將本地倉庫存放於雲端硬碟時，需特別防範同步與清理衝突：

### ▍ 1. Google 雲端硬碟電腦版同步模式調整
*   **「串流檔案」的潛在風險**：實體存於雲端，本地僅顯示虛擬投影。Git 頻繁讀寫微小索引時會引發大量網路 I/O 衝突，並在背景產生 `.tmp.driveupload` 暫存檔，造成 Git 誤判變更，甚至引發 Git 索引損壞。
*   **🛠️ 解決方案**：將同步模式變更為**「雙向同步檔案」（鏡像模式）**，使檔案 100% 下載至本地硬碟，讓 Git 的讀寫回歸本機高速操作。

### ▍ 2. 實務排障：推送遭拒 (rejected main -> main fetch first)
*   **情境**：在 Git GUI 點擊 `Push` 被拒絕，提示遠端包含本地沒有的變更。
*   **🛠️ 解決方案**：
    1.  先在 Git GUI 內提交本機修改，讓工作區變乾淨。
    2.  在專案根目錄開啟終端機，執行一鍵變基合併命令：
        ```powershell
        git pull --rebase origin main
        ```
    3.  合併成功後，即可回到 Git GUI 順利 Push。

### ▍ 3. 實務排障：清理資料庫失敗 (Deletion of directory failed)
*   **情境**：在 Git GUI 執行壓縮或清理資料庫（`git gc`）時，提示刪除 `.git/objects/...` 暫存資料夾失敗。
*   **原因**：Google 雲端硬碟同步程序一偵測到暫存碎片變動，即刻鎖定該檔案準備上傳，導致 Git 刪除失敗。
*   **🛠️ 方案**：
    1.  點擊 Windows 右下角 Google 雲端硬碟小雲朵圖示。
    2.  點擊「設定」 $\rightarrow$ **「暫停同步 (Pause Syncing)」**。
    3.  回到 Git GUI 重試（此時檔案已被釋放鎖定，能秒速清理完成）。
    4.  完成後點選 **「恢復同步 (Resume Syncing)」**。

### ▍ 4. Git Gui 綁定私有庫失敗與首次 Push 驗證
*   **綁定失敗解決**：在 `Remote -> Add...` 填入名稱與網址時，將 Further Action 改勾選為 **`Do Nothing Else Now`（現在什麼都不做）**，即可繞過私有庫即時檢查順利新增。若名稱重複，先至 `Remote -> Remove...` 刪除 `origin`。
*   **首次 Push 憑證綁定**：在 GitHub 上生成個人訪問 Token (`Personal access tokens (classic)`) 並勾選 `repo` 權限。在首次 Push 驗證時，**Username 輸入帳號名稱，Password 貼上該 Token 金鑰**（勿輸入 GitHub 密碼）。

---

## 8. GitHub 網頁端跨版本比對與 Diff 介面解讀

當本地端正在調整環境時，GitHub 網頁端提供了極度穩定的跨版本對比功能與進階差異檢視工具。

### ▍ 1. 跨版本對比操作
*   **手動拼湊網址對比法**：GitHub 支援直接在網址後方使用 `compare/舊版本SHA...新版本SHA`。例如：
    ```text
    https://github.com/niceheadwkt/Obsidian/compare/055c45b...65d3fb5
    ```
*   **免打字全滑鼠點擊比對法**：
    1.  在 GitHub 進入該檔案頁面，點擊右上角 **`History`** 進入 Commit 歷史。
    2.  複製第 1 版的短 SHA 值或完整 SHA 金鑰。
    3.  進入 **`Pull requests`** 標籤頁面，點擊 **`New pull request`**。
    4.  在比對控制列的 `compare: main` 下拉選單中貼上複製的第 1 版 SHA 並回車，系統會自動比對渲染。

### ▍ 2. GitHub 差異檢視介面進階解讀
*   **Split View（左右分欄）模式**：在差異檢視畫面正上方，點擊 **`齒輪圖示 (Settings)`** $\rightarrow$ 將 Diff view 從 Unified 改為 **`Split`**。左側顯示舊版（紅色刪除），右側顯示新版（綠色新增），更利於 Markdown 長文閱讀。
*   **Hunk Header（代碼區塊標頭）解讀**：
    差異畫面上出現的藍色橫條（例如 `@@ -4,10 +4,11 @@ tags: [...]`）代表：
    *   `-4,10`：舊版（`-`）從第 4 行開始，顯示了 10 行。
    *   `+4,11`：新版（`+`）從第 4 行開始，顯示了 11 行。
    *   背景文字：Git 自動抓取的最鄰近標題或 Front Matter 欄位。
    *   雙向小箭頭：點擊可展開被自動收折的未修改內容。

*(相關基礎命令與環境配置可交叉檢索：[[前端與系統開發常用技術]])*
