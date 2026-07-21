要啟動此專案，最直接且最穩定的方式是啟動 **Streamlit UI 介面（`drink_app.py`）**。

在設計上，**當您啟動了 Streamlit UI 時，它會在背景自動為您拉起並連接 MCP 伺服器（`mcp_server.py`）**，因此您不需要手動分開執行兩個程式。

以下是針對您的問題所做的詳細啟動說明，以及您提到的三種啟動方式的差別：

---

### 🚀 推薦啟動步驟（Windows 環境）

請在專案根目錄（`c:\aiTest\mcp-drink-main`）開啟 PowerShell，並執行以下指令：

powershell

.\.venv\Scripts\python.exe -m streamlit run drink_app.py

NOTE

**為什麼推薦這個指令？** 我們在測試中發現，直接使用當前專案虛擬環境中的 Python 解譯器來執行 `streamlit`，可以完美避開 Windows 上 `uv` 工具的蹦床路徑解析錯誤（`uv trampoline failed to canonicalize script path`），是目前最保險且一定能運作的方法。

---

### 🔍 深入解析：這三種啟動方式有何不同？

您在 `drink_mcp文件.txt` 中記錄的三種啟動方式，本質上的運作邏輯、限制與必備條件如下：

#### 1. `.\.venv\Scripts\python.exe -m streamlit run drink_app.py` (推薦)

- **運作原理**：直接調用專案底下特定虛擬環境 (`.venv`) 的 Python 主程式，並載入 `streamlit` 模組來執行 `drink_app.py`。
- **限制與前提**：專案目錄下必須有 `.venv` 資料夾，且裡面必須已經安裝了 streamlit 與相關套件（此專案的環境已經完整建置，因此可以直接使用）。
- **優點**：**最安全、最精準**。它強迫系統只使用您這個專案的虛擬環境，不會被您電腦上其他地方安裝的 Python 干擾。

#### 2. `uv run streamlit run drink_app.py`

- **運作原理**：使用現代快速 Python 套件管理工具 `uv` 來執行指令。`uv` 會自動讀取 `pyproject.toml` 中的依賴設定，並在正確的環境中執行 Streamlit。
- **限制與前提**：電腦必須有安裝 `uv` 工具。
- **限制**：在部分 Windows 系統環境下，`uv` 的可執行檔定位機制（Trampoline）有時會拋出 `failed to canonicalize script path` 的錯誤，導致無法啟動。

#### 3. `streamlit run drink_app.py`

- **運作原理**：直接呼叫系統全域環境變數中的 `streamlit` 指令。
- **限制與前提**：必須有將 Streamlit 所在的路徑手動加到 Windows 的 `PATH` 環境變數中。
- **缺點**：容易出錯。如果您的電腦安裝了多個不同的 Python（例如全域 Python、Anaconda、uv 等），這個指令極可能會調用到「沒有安裝此專案依賴套件」的那個 Python 環境，進而噴出 `ModuleNotFoundError`。

---

### 🛠️ 專案運作前置確認

我們已為您檢查過專案的設定，目前皆已準備就緒：

1. **API 金鑰**：`.streamlit/secrets.toml` 中已填寫 Gemini 與 Claude 的 Key。
2. **資料庫金鑰**：根目錄下的 `firebase-adminsdk.json` 金鑰檔案已存在，`db_logic.py` 會自動讀取它來與 Firebase 連線。
3. **依賴環境**：`.venv` 中已確認安裝好 `fastmcp` (3.2.3) 與 `streamlit` (1.56.0)。

您現在只需開啟終端機並執行推薦的指令，即可在瀏覽器中看到點餐 UI 以及右側的「簡易 AI 對話框」囉！如果有遇到任何錯誤訊息，隨時貼給我看，我來幫您排除！