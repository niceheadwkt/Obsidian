# Obsidian MCP 伺服器安裝建立與功能驗收指南

本文件詳細記錄了如何建立與配置 **Obsidian MCP 伺服器** (Model Context Protocol)，使其能安全、穩定地與本地的 Obsidian 庫進行資料串接，並包含詳細的功能驗收測試流程，以及日常使用此 MCP 的功能情境與 Prompt 範例。

---

## 1. 核心運作原理
Obsidian MCP 伺服器是基於 Anthropic 的 Model Context Protocol (MCP) 標準協定。
它透過本地 Node.js 執行環境啟動，藉由 **標準輸入/輸出 (Stdio)** 與 AI 編輯器進行雙向通訊。伺服器底層會被授予存取特定 Obsidian Vault 目錄的檔案讀寫權限，並向 AI 暴露一組受控的 API（如讀取、寫入、搜尋與修改 Frontmatter 等工具）。

---

## 2. 建立與配置步驟

### 步驟 A：環境準備
1. **Node.js**：確保本地已安裝 Node.js 執行環境（建議 v18 以上版本）。
2. **本地 Vault 目錄**：確認您的 Obsidian 本地庫路徑：
   * 本地路徑：`c:/Users/ch26788/我的雲端硬碟 (antonggewkt@gmail.com)/Obsidian`

### 步驟 B：取得與安裝 MCP 伺服器
一般有兩種常見的配置方式：
* **方式一：使用 npx 線上執行（極簡配置）**
  直接在 IDE 設定檔中配置以 `npx` 動態下載並啟動 `mcp-server-obsidian`。
* **方式二：本地下載編譯（適合離線與客製化）**
  將社群或官方開源的 Obsidian MCP 程式碼複製至本地，執行 `npm install` 補齊依賴並編譯為 `dist/index.js`。

### 步驟 C：編輯 IDE MCP 設定檔
在您的 IDE 全域設定檔 `mcp_config.json`（路徑通常位於 `C:/Users/ch26788/.gemini/config/mcp_config.json`）中，加入以下 `obsidian` 伺服器節點設定：

```json
{
  "mcpServers": {
    "obsidian": {
      "command": "node",
      "args": [
        "C:/path/to/obsidian-mcp-server/dist/index.js",
        "--vault",
        "c:/Users/ch26788/我的雲端硬碟 (antonggewkt@gmail.com)/Obsidian"
      ]
    }
  }
}
```
> **注意**：
> 1. 請將 `"C:/path/to/obsidian-mcp-server/dist/index.js"` 替換為您本地實際的伺服器入口檔案路徑，或改用 `npx -y @modelcontextprotocol/server-obsidian`。
> 2. 目錄路徑在 JSON 中需使用正斜線 `/` 或雙反斜線 `\\` 以防逸失字元錯誤。
> 3. 設定完成後需重啟 IDE 以完成設定加載。

---

## 3. 功能工具清單 (Exposed Tools)

成功加載後，AI 將獲得以下 15 個操作您 Obsidian 庫的核心工具：

* **統計與目錄**：`get_vault_stats`、`list_directory`、`get_notes_info`
* **讀取與寫入**：`read_note`、`read_multiple_notes`、`write_note`、`patch_note`
* **搜尋功能**：`search_notes`
* **文件管理**：`move_note`、`move_file`、`delete_note`
* **後設資料管理**：`get_frontmatter`、`update_frontmatter`、`list_all_tags`、`manage_tags`

---

## 4. 如何使用此 MCP：日常功能情境與 Prompt 範例

啟用此 MCP 後，您可以透過自然語言，命令 AI 助手直接對您的 Obsidian 進行日常的知識庫操作。以下是常見的使用情境與對話範例：

### 情境一：開工與進度追蹤（讀取與狀態獲取）
當您需要了解最近修改了哪些筆記、確認工作進度時，可以這樣對 AI 說：
* **Prompt 範例**：
  > 「幫我看一下我最近修改的 3 篇筆記，並摘要我上次做到哪裡。」
* **底層工具調用**：
  1. AI 呼叫 `get_vault_stats(recentCount: 3)` 取得最近修改檔案清單。
  2. AI 呼叫 `read_note` 或 `read_multiple_notes` 讀取內容。
  3. AI 整理並回報摘要。

### 情境二：知識庫全局搜尋（跨筆記檢索）
當您想找某個特定主題的舊資料或做專題整理時，可以讓 AI 幫您全局搜尋：
* **Prompt 範例**：
  > 「搜尋我知識庫中所有提到 'Antigravity' 或 '記憶系統' 的筆記，並幫我整理一份綜合對比表。」
* **底層工具調用**：
  1. AI 呼叫 `search_notes(query: "Antigravity")` 取得相關筆記路徑。
  2. AI 呼叫 `read_multiple_notes` 一口氣讀取所有符合的筆記。
  3. AI 進行邏輯歸納，輸出 markdown 對比表格。

### 情境三：工作日誌記錄與標籤管理（寫入、更新與追加）
當您想快速做筆記、在日誌中追加新想法，或分類整理筆記標籤時：
* **Prompt 範例**：
  > 「在我的日誌筆記 `AI/wiki/log.md` 尾端，追加一筆今天完成 Google Tasks 驗收的紀錄，並把它的標籤更新為 #mcp #done。」
* **底層工具調用**：
  1. AI 呼叫 `write_note(path: "AI/wiki/log.md", mode: "append", content: "...")` 寫入進度。
  2. AI 呼叫 `manage_tags` 或 `update_frontmatter` 替筆記加上標籤。

### 情境四：知識庫重構與目錄重整（移動、重命名與刪除）
當您要對知識庫結構進行調整，把舊檔案分類歸檔時：
* **Prompt 範例**：
  > 「幫我在庫中新建一個 `Archive/2026/` 目錄，然後把 `AI/wiki/MCP_Acceptance_Test.md` 移動到該目錄下，並改名為 `old_mcp_test.md`。」
* **底層工具調用**：
  1. AI 呼叫 `move_note(path: "AI/wiki/MCP_Acceptance_Test.md", newPath: "Archive/2026/old_mcp_test.md")`（底層會自動建立缺少的目錄）。

---

## 5. 實戰驗收測試流程 (Acceptance Test)

為了確保權限與連線完全正確，我們於 2026-07-15 執行了端對端功能驗收，所有工具均順利通過測試：

1. **第一步：庫統計讀取 (`get_vault_stats`)**
   * **結果**：成功取得庫統計（265 篇筆記、17 個資料夾）。
2. **第二步：新增暫存筆記 (`write_note`)**
   * **路徑**：`AI/wiki/MCP_Acceptance_Test.md`
   * **結果**：成功在 Vault 寫入一篇測試筆記。
3. **第三步：精準讀取驗證 (`read_note`)**
   * **結果**：成功回傳筆記內容，格式與內容 100% 吻合。
4. **第四步：關鍵字檢索測試 (`search_notes`)**
   * **Query**：`MCP_Acceptance_Test`
   * **結果**：搜尋引擎在 1 秒內精準定位該測試檔案，並回傳所在行數與上下文片段。
5. **第五步：環境清理 (`delete_note`)**
   * **結果**：測試檔案已安全從硬碟上物理刪除，環境復原完畢。

---

## 6. 常見排障指引 (Troubleshooting)

* **問題：出現 `invalid_request` 錯誤**
  * **診斷**：可能是因為啟動參數中有中文或特殊字元，導致 Node 啟動 CLI 時路徑解析失敗。
  * **解決方法**：確保 IDE 設定檔中的路徑全部使用正斜線 `/`，且路徑兩端有正確的雙引號包裹。
* **問題：筆記寫入權限被拒絕 (Permission Denied)**
  * **診斷**：可能因為 Windows 系統下 Google Drive 雲端硬碟的同步鎖定機制作祟，或路徑設為唯讀。
  * **解決方法**：確保路徑指向的資料夾具備本地目前使用者的寫入權限，且 Google Drive 同步串流狀態正常。
