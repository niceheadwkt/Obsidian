---
type: analysis
tags: [Obsidian, 手機, iOS, Android, GitHub, Obsidian Git, Personal Access Token, 唯讀, 同步]
sources: ["[[WorkLog]]"]
created: 2026-11-27
updated: 2026-11-27
---

# 手機唯讀瀏覽 Obsidian 知識庫設定指南

2026-11-27 與 Claude Code 討論「手機能不能看 Obsidian」後整理。保管庫在電腦上放在 Google 雲端硬碟（`G:/我的雲端硬碟/Obsidian`），並推送到 GitHub 私人 repo `niceheadwkt/Obsidian`。手機版 Obsidian 不能直接開 Google 雲端硬碟裡的資料夾，所以改從 GitHub 取得內容，**只看不改**。

**一句話重點**：手機用唯讀 Token 從 GitHub 拉，只看不推最安全

> [!NOTE]
> App 介面名稱、外掛功能與 GitHub 設定頁位置可能隨版本變動，實際操作以畫面為準。

---

## 一、兩種做法比較

| 項目                     | 做法一：GitHub App／瀏覽器 | 做法二：Obsidian App＋唯讀 Token |
| ---------------------- | ------------------ | ------------------------- |
| 設定                     | 免設定，登入 GitHub 即可   | 建 Token、裝 Git 外掛、clone 一次 |
| Markdown 排版、表格、Mermaid | 有                  | 有                         |
| `[[雙向連結]]` 可點          | 不行，只顯示文字           | 可以                        |
| 關係圖、全文搜尋               | 沒有關係圖，只能在 repo 內搜尋 | 都有，和電腦一樣                  |
| 適合                     | 偶爾查一兩頁             | 常在手機翻 Wiki                |

兩種做法看到的都是 **GitHub 上的版本**：電腦改完要 push，手機才看得到。開工、收工流程已包含 push，正常使用不用另外處理。

## 二、做法一：GitHub App

1. 安裝 **GitHub App**（或用手機瀏覽器開 github.com），用 `niceheadwkt` 帳號登入。
2. 進入 `niceheadwkt/Obsidian` → **Code** → 依資料夾點進要看的頁面，例如 `AI/wiki/`。
3. 找頁面：從 `AI/wiki/index.md` 開始，或用 repo 的搜尋功能。

## 三、做法二：Obsidian App＋唯讀 Token

### 1. 建立唯讀 Token（GitHub）

1. GitHub 右上角頭像 → **Settings** → **Developer settings** → **Personal access tokens** → **Fine-grained tokens** → **Generate new token**。
2. 設定：
   - **Token name**：`obsidian-mobile-readonly`
   - **Expiration**：建議 90 天，到期再換
   - **Repository access**：**Only select repositories**，只勾 `niceheadwkt/Obsidian`
   - **Permissions → Repository permissions → Contents**：**Read-only**（Metadata 自動為 Read）
3. 按 Generate，**立刻複製 Token**，離開頁面後就看不到了。

唯讀 Token 的好處是：手機就算誤按 commit，也推不上 GitHub，不會影響電腦端資料。

### 2. 手機安裝與 clone

1. 安裝 **Obsidian**（App Store／Google Play），建立**新的空白保管庫**，例如 `Obsidian`。iOS 請選「在我的 iPhone 上」，不要放 iCloud。
2. **設定 → 第三方外掛（Community plugins）**：關閉「限制模式」→「瀏覽」搜尋 **Git**（作者 Vinzent，原名 Obsidian Git）→ 安裝 → 啟用。
3. **Git 外掛設定 → Authentication**：
   - Username：`niceheadwkt`
   - Password／Personal access token：貼上唯讀 Token
4. 開命令面板執行 **Git: Clone an existing remote repo**：
   - URL：`https://github.com/niceheadwkt/Obsidian.git`
   - 目錄：輸入 `.`（clone 到保管庫根目錄）
   - depth：填 `1`（淺層複製，只抓最新版）
5. 完成後**完全關閉 Obsidian 再重開**。

### 3. 唯讀相關設定

| 設定位置 | 設定值 | 目的 |
| --- | --- | --- |
| Git 外掛 → Pull on startup | 開啟 | 每次打開 App 自動更新到最新版 |
| Git 外掛 → Auto commit-and-sync interval | `0`（關閉） | 不自動 commit |
| 設定 → 編輯器 → 預設檢視模式 | 閱讀檢視 | 打開筆記不進編輯狀態，避免誤改 |

### 4. 日常使用

- 打開 App 就會自動 pull，想手動更新時執行 **Git: Pull**。
- 若不小心改到檔案導致 pull 衝突：最簡單的處理是刪掉手機上的保管庫，重新做一次第 2 步的 clone。

## 四、注意事項

- **第一次 clone 接 Wi-Fi**：repo 打包後約 88 MB、740 個檔案（2026-11-27 實測）。iOS 版 Git 外掛較慢，clone 可能要等幾分鐘，中途不要切走 App。
- **`.obsidian` 設定**：repo 只追蹤 `app.json`、`appearance.json`、`core-plugins.json`、`graph.json`，不包含外掛資料夾，clone 下來不會蓋掉手機的 Git 外掛設定；`workspace-mobile.json` 已列入 `.gitignore`。
- **公司資料**：手機上會有完整的 `AI/ERP/` 筆記（正式機表名、查詢語法、內控底稿），放到手機前先確認符合公司資安規範。
- **手機遺失**：到 GitHub → Settings → Developer settings → Fine-grained tokens，把這組 Token **Revoke**；唯讀 Token 外洩也只能讀、不能改。
- **手機上不能做的事**：Claude Code、`wiki_tool.py` 等腳本無法在手機執行，入庫、健檢仍在電腦上做。

## 我可以怎麼用

- **開會或現場查資料**：在使用單位討論需求時，用手機打開 [[index]] 或 ERP 工作筆記，快速查之前的分析結論與表格欄位，不必回座位開電腦。
- **通勤時複習新入庫的頁面**：每天入庫的影片、文章摘要，可以在手機上用閱讀模式看，有想法先記在別處，回電腦再請 Claude 整合進 Wiki。
- **之後要在手機編輯**：把 Token 權限改成 Contents **Read and write**、關掉閱讀檢視預設，再用 **Git: Commit-and-sync** 推回。兩邊同時改同一頁容易衝突，衝突時回電腦處理。

## 關聯頁面
- [[Git GUI 與 GitHub 雙向同步實務]]：電腦端 Google Drive＋Obsidian＋Git 的分工。
- [[Google 雲端硬碟串流、鏡像與離線存取設定指南]]：電腦端保管庫所在的雲端硬碟模式與卡死風險。
- [[Claude＋Obsidian 第二大腦七步法]]：Obsidian 當第二大腦的整體做法。
- [[簡訊驗證碼風險與 passkey 帳號防護設定]]：手機是所有驗證的終點，螢幕鎖、passkey 與遺失時的處理。
