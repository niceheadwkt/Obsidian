---
type: concept
tags: [Git, GitGUI, GitHub, 版本控制, 同步, 衝突解決]
sources: [
  "[[raw/Git GUI 與 GitHub 雙向同步全面操作指南.md]]",
  "[[raw/Git_GUI_GitHub_Comprehensive_Guide.pdf]]",
  "[[raw/Git GUI 與 GitHub 雙向同步全面指南(整合實戰衝突、底層邏輯與問答精華之技術對談紀錄).md]]",
  "[[raw/Google 雲端硬碟偏好設定調整與 Git Gui 遠端綁定故障排除指南.md]]"
]
created: 2026-06-13
updated: 2026-06-23
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

## 6. Google 雲端硬碟同步衝突與 Git Gui 私有庫連線故障排除
根據 [[raw/Google 雲端硬碟偏好設定調整與 Git Gui 遠端綁定故障排除指南.md|Google雲端與Git遠端綁定排障指南]]，當將本地 Obsidian 知識庫與 GitHub 進行雙向同步時，需特別留意雲端硬碟的運作模式與私有庫的安全授權：

### ▍ 1. Google 雲端硬碟電腦版同步模式調整
*   **「串流檔案」模式的潛在風險**：在此模式下，檔案實體儲存於雲端，本地僅顯示虛擬投影。Git 在執行掃描、暫存與提交時需要瞬間頻繁讀寫 `.git` 目錄下成百上千個微小索引，這會引發頻繁的網路 I/O 衝突，並在背景產生大量 `.tmp.driveupload` 同步暫存檔，造成 Git 誤判大量未追蹤變更，甚至引發 Git 索引損壞或程序卡死。
*   **🛠️ 解決方案**：強烈建議將同步處理選項變更為**「雙向同步檔案」（鏡像模式）**。這會將檔案 100% 實體下載至本地硬碟，讓 Git 的讀寫回歸純粹的本機高速操作，避開雲端同步程序的鎖定衝突。

### ▍ 2. Git Gui 綁定 GitHub 私有庫（Private Repo）失敗排除
*   **錯誤現象**：在 Git Gui 中執行 `Remote -> Add...` 綁定 GitHub 私有庫網址時，彈出 `Failed to add remote...` 錯誤。
*   **根本原因**：在「Add New Remote」視窗中，下方 **Further Action** 預設勾選了 **`Fetch Immediately`（立即抓取）**。當 Git Gui 嘗試立即連線至 GitHub 抓取資料時，因本地此時尚未通過安全驗證，連線會被 GitHub 私有庫直接拒絕，進而判定遠端登記失敗。
*   **🛠️ 標準解決步驟**：
    1.  重新進入 `Remote -> Add...`，填入名稱（如 `origin`）與私有庫網址。
    2.  ✨ **關鍵調整**：將下方的 Further Action 改勾選為 **`Do Nothing Else Now`（現在什麼都不做）**，然後點擊 `Add`，即可繞過即時檢查順利新增成功。
    3.  若提示名稱重複，可先至 `Remote -> Remove...` 中將已存在的 `origin` 刪除後重試。

### ▍ 3. GitHub Private 倉庫首次 Push 授權驗證
當遠端網址登記成功後，首次點擊 **`Push`** 時，必須通過權限校驗：
*   **產生 Token**：登入 GitHub $\rightarrow$ `Settings` $\rightarrow$ `Developer settings` $\rightarrow$ `Personal access tokens (classic)` $\rightarrow$ `Generate new token (classic)`。勾選 **`repo`** 權限，複製生成的 `ghp_` 開頭金鑰。
*   **憑證綁定**：在 Git Gui 點選 `Push`，彈出驗證視窗時：
    *   **Username**：輸入您的 GitHub 帳號名稱（如 `niceheadwkt`）。
    *   **Password**：**直接貼上複製的 `ghp_` 開頭 Token 金鑰**（勿輸入 GitHub 登入密碼）。驗證成功後，系統憑證管理員會自動記憶此憑證，後續即可直接一鍵 Push。

*(相關基礎命令與環境配置可交叉檢索：[[前端與系統開發常用技術]])*
