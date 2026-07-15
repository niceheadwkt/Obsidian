# Google Tasks MCP 伺服器安裝建立與功能驗收指南

本文件詳細記錄了如何從零開始建立、配置與授權 **Google Tasks MCP 伺服器** (Model Context Protocol)，使其能安全地與您的 Google 工作表 (Google Tasks) 進行資料串接，並包含功能工具說明與日常使用 Prompt 範例。

---

## 1. 核心決策與授權路徑
由於 Google Tasks 屬於 Google Workspace 的個人隱私資料，且我們需要**寫入 (Write)** 權限，因此必須採用 **「自建 GCP 專案 ＋ OAuth 2.0 授權碼流程 (Authorization Code Flow)」** 的方式。這能確保您的個人資料在完全受控的安全範圍內被 AI 讀寫，而不需要將密碼或長期權限暴露給外部第三方。

---

## 2. 建立與配置步驟

### 步驟 A：Google Cloud Platform (GCP) 控制台設定
1. **建立專案**：前往 [Google Cloud Console](https://console.cloud.google.com/)，建立一個全新的專案（例如 `gtasks-mcp`）。
2. **啟用 API**：在「API 和服務」庫中搜尋 **Google Tasks API**，並點擊「啟用」。
3. **配置 OAuth 同意畫面 (OAuth Consent Screen)**：
   * 選擇 **外部 (External)** 類型。
   * 填寫必要的應用程式名稱與聯絡信箱。
   * **關鍵步驟**：在「測試使用者」 (Test Users) 頁面中，點擊 **「ADD USERS」**，將您要存取 Tasks 的 Google 帳號（例如 `niceheadwkt@gmail.com` 或您的工作帳號）加入名單中。*（若未加入，登入授權時會遇到 403 access_denied 錯誤）*。
4. **建立憑證**：
   * 移至「憑證」 (Credentials) 頁面 ➜ 點擊「建立憑證」 ➜ 選擇 **OAuth 用戶端 ID** (OAuth client ID)。
   * 應用程式類型選擇 **桌面應用程式 (Desktop app)**。
   * 建立成功後，下載憑證的 JSON 檔案。

### 步驟 B：本地 MCP 伺服器部署 (`gtasks-mcp`)
1. **專案目錄**：在本地建立專案目錄（例如 [gtasks-mcp](file:///C:/aiTest/gtasks-mcp)）。
2. **導入憑證**：將下載的 GCP 憑證 JSON 檔案複製到該目錄下，並改名為 `gcp-oauth.keys.json`。
3. **安裝依賴**：確保目錄中含有 `package.json`，並安裝 `@modelcontextprotocol/sdk`、`googleapis` 以及 `@google-cloud/local-auth`：
   ```bash
   npm install
   ```

### 步驟 C：執行 OAuth 授權流程
由於 AI 在背景啟動 MCP 時無法彈出瀏覽器視窗，我們需要先在本地執行一次授權流程：
1. 在 [gtasks-mcp](file:///C:/aiTest/gtasks-mcp) 目錄下執行授權命令：
   ```bash
   node src/index.js auth
   ```
   *(或執行特別編寫的 `node auth.js`)*。
2. 終端機會輸出一個授權連結，並在本地 `http://localhost:3000` 啟動監聽。
3. 複製連結至瀏覽器打開，登入您的 Google 帳號。
4. 當出現「這個應用程式未經 Google 驗證」警告時，點選 **「進階」** ➜ **「繼續」 (Continue)**，勾選 Tasks 存取權限並按下同意。
5. 授權成功後，本地會產生一個包含 Access/Refresh Token 的 [gcp-oauth.keys.json](file:///C:/aiTest/gtasks-mcp/gcp-oauth.keys.json) 及密鑰檔案 `.gtasks-server-credentials.json`。

### 步驟 D：編輯 IDE MCP 設定檔
在您的 IDE 全域設定檔 `mcp_config.json` 中，配置 `google-tasks` 節點：

```json
{
  "mcpServers": {
    "google-tasks": {
      "command": "node",
      "args": [
        "C:/aiTest/gtasks-mcp/dist/index.js"
      ]
    }
  }
}
```
> **Windows 相容性說明**：
> 原本社群版本可能使用 Bun 啟動，但在 Windows 下容易因為 `__require` 產生編譯錯誤。我們已將專案重新編譯為 **Node.js** 版本，並在 `mcp_config.json` 中使用系統的 `node` 啟動 `dist/index.js`，以保證穩定性。

---

## 3. 功能工具清單 (Exposed Tools)

成功啟動後，AI 將被授予以下 7 個操作您 Google Tasks 的工具：

* `list-tasklists`：列出您所有的工作表清單（如「預設清單」、「niceheadwkt的清單」）。
* `list`：獲取指定清單中的所有任務項目。
* `create`：在指定清單中新增一筆任務（可設定主旨 `title`、備註 `notes` 與到期日 `due`）。
* `update`：更新任務的標題、備註、到期日，或將狀態改為 `completed`（標記已完成）。
* `search`：搜尋任務標題。
* `clear`：清除（隱藏）某個工作清單中所有已完成的任務。
* `delete`：將特定任務從清單中物理刪除。

---

## 4. 如何使用此 MCP：日常功能情境與 Prompt 範例

您可以透過自然語言，命令 AI 助手直接讀寫您的 Google 工作表。以下是常見的使用情境與對話範例：

### 情境一：新增待辦事項（自動寫入與排程）
當您有新任務要排入行事曆或待辦清單時：
* **Prompt 範例**：
  > 「幫我在我的工作清單 'niceheadwkt的清單' 中，新增一個標題為 '準備明天早上十點的教學簡報' 的任務，並在備註寫上 '需要包含 Excel 自動化範例'，到期日設為 2026-07-16。」
* **底層工具調用**：
  1. AI 呼叫 `list-tasklists` 尋找名為 `niceheadwkt的清單` 的 ID（即 `MDA2NDIzODAyOTQyMzUxMTk5NjI6MDow`）。
  2. AI 呼叫 `create(taskListId: "...", title: "...", notes: "...", due: "2026-07-16")` 寫入任務。

### 情境二：查詢與檢索任務（了解今日待辦）
當您需要整理今天的待辦事項時：
* **Prompt 範例**：
  > 「列出我目前在 'niceheadwkt的清單' 裡的所有待辦任務，並幫我按到期日排序。」
* **底層工具調用**：
  1. AI 呼叫 `list(taskListId: "...")` 撈取所有任務。
  2. AI 在本地進行資料排序與格式化，並回報給您。

### 情境三：更新任務狀態（標記已完成）
當您完成某項工作，需要將其勾除時：
* **Prompt 範例**：
  > 「我已經完成 '準備明天早上十點的教學簡報' 這項工作了，幫我把這個任務標記為已完成。」
* **底層工具調用**：
  1. AI 呼叫 `search(query: "準備明天早上十點的教學簡報")` 或 `list` 找到該任務的 `id` 與 `uri`。
  2. AI 呼叫 `update(taskListId: "...", id: "...", uri: "...", status: "completed")` 完成更新。

### 情境四：任務清理與刪除（維護清單整潔）
當您想把作廢的任務或測試資料移除時：
* **Prompt 範例**：
  > 「幫我把名稱為 'AI Agent 連接測試任務' 的測試任務從清單中刪除。」
* **底層工具調用**：
  1. AI 尋找到該任務的 `id`。
  2. AI 呼叫 `delete(taskListId: "...", id: "...")` 進行物理刪除。

---

## 5. 常見排障指引 (Troubleshooting)

* **問題：登入時出現 `403 Access Denied` 錯誤**
  * **診斷**：您的 Google 帳號不在 GCP 專案的 OAuth 同意畫面「測試使用者」名單中。
  * **解決方法**：前往 GCP ➜ APIs & Services ➜ OAuth consent screen ➜ Test users，手動新增您的 Google 帳號。
* **問題：出現 `invalid_grant` 錯誤**
  * **診斷**：Refresh Token 已過期或已被撤銷。這通常發生在專案處於「測試 (Testing)」狀態，測試 Token 的有效期限通常只有 7~14 天。
  * **解決方法**：刪除本地目錄中的 `.gtasks-server-credentials.json`，然後重跑一次 `node src/index.js auth` 重新取得授權。
