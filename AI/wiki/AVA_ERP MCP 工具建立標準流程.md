---
type: source-summary
tags: [MCP, AVA-GPT, AVA_ERP, ERP, 會議室, 工具定義, FastMCP, AI-Agent, 企業內部系統]
sources: ["[[AI/raw/2026-10-08T140253+0800-AVA-GPT 對話：AVA_ERP MCP 工具建立標準流程.md|AVA-GPT 對話：AVA_ERP MCP 工具建立標準流程]]"]
created: 2026-10-08
updated: 2026-10-08
---

# AVA_ERP MCP 工具建立標準流程

本頁整理 2026-10-08 一段公司內部 AVA-GPT 對話。對話先問 AVA-ERP 有哪些功能，接著發現工具被「強制禁用」，最後追問這些工具是怎麼建立的。重點是第 8 輪 AVA-GPT（Claude-Sonnet-4.6）回答的「**建立一個像 `erp_query_meeting_rooms` 這樣的工具，其標準流程**」，並由 Claude Code 依 MCP 實際規格補充修正。

一句話結論：**AI 助理本身不會「造工具」；工具由後端工程師寫成服務，再透過 MCP 伺服器公布給 AI 使用，能不能呼叫則由平台管理員的政策決定。**

---

## 1. AVA_ERP 現有的 MCP 工具

AVA-ERP 目前的核心服務是「會議室資源查詢與預訂」，工具完整名稱帶有 `_mcp_AVA_ERP` 後綴，表示由 AVA_ERP 這個 MCP 伺服器提供。

| 工具 | 功能 | 主要參數 |
| :--- | :--- | :--- |
| `erp_query_meeting_rooms` | 查詢指定日期所有會議室的完整預訂排程與時段使用狀況 | 日期（YYYY-MM-DD） |
| `erp_list_available_rooms` | 列出指定日期還有空檔的會議室，可依樓層（如 18F）篩選 | 日期、樓層 |
| `erp_check_room_availability` | 檢查單一會議室在指定時段（如 14:00–15:00）是否可預訂 | 會議室代碼、日期、起訖時間 |
| `erp_book_meeting_room` | 送出預訂，寫入會議室、時間、事由與主持人 | 會議室代碼、起訖時間、事由、主持人工號（選填） |

- **自然語言用法範例**：「幫我查明天 19 樓有哪些會議室可以預約？」「確認 18F-0001 明天下午 2 點到 4 點有沒有人借？」「預訂明天 14:00–15:30 的 18F-0002，事由『專案進度審查』。」
- **預訂時要提供**：日期、起訖時間、會議室代碼或樓層、預訂事由、主持人工號（未指定時通常以申請人為主）。

> [!WARNING]
> 對話當天（2026-10-08），這 4 個工具在 AVA-GPT 上都處於**強制禁用**狀態。AI 能從知識庫「介紹」功能，但實際呼叫會被更高層的系統政策擋下，使用者也無法自行開啟。要恢復使用，須向 IT 或 AVA 系統管理團隊提出需求。

---

## 2. AVA-GPT 回答的標準流程（第 8 輪）

### 階段一：後端開發（軟體工程師）
1. **撰寫核心邏輯**：用 Python、Java 等撰寫程式，以 `erp_query_meeting_rooms` 為例：
   - 連到公司 ERP 資料庫。
   - 接收日期參數（如 `2026-10-08`）。
   - 查詢該日的會議室預訂資料表。
   - 整理結果，以 JSON 等結構化格式回傳。
2. **部署成服務**：把程式部署在應用程式伺服器（AVA_ERP MCP Server），提供可以被呼叫的端點。

### 階段二：工具整合（系統管理員或 AI 整合工程師）
3. **定義工具規格**：提供工具名稱、參數與說明文字（docstring），這是 AI 判斷「何時用、怎麼用」的使用說明書。例如：

```python
def erp_query_meeting_rooms_mcp_AVA_ERP(date: str) -> dict:
    """
    查詢指定日期的會議室資料
    此工具用於獲取特定日期所有會議室的可用時段資訊。
    Args:
      date: 日期格式為 YYYY-MM-DD (例如：'2025-06-02')
    """
```

4. **AI 呼叫**：AI 決定使用工具時，系統依定義把參數送到後端服務，再把結果交回 AI。

AVA-GPT 的比喻：AI 是**駕駛**，開發者是**汽車工程師**（製造零件、組裝車子），系統管理員則**交出鑰匙與使用手冊**（工具定義）。AI 只會照手冊操作，不能自己製造或修改零件。

---

## 3. 修正與補充

> [!WARNING]
> **內容衝突**：AVA-GPT 在第 6 輪把 MCP 解釋為「Model-Controller-Policy」，這是錯的。MCP 是 **Model Context Protocol**，由 Anthropic 提出的開放協定，與本知識庫 [[AI Agent 實戰與 MCP 伺服器整合]] 的說法一致。

> [!WARNING]
> **流程描述不精確**：AVA-GPT 說管理員要在 AI 系統設定裡另外「加入一段工具定義」，再由系統轉呼叫後端 API。在 MCP 架構下，**工具定義是 MCP 伺服器自己宣告的**：用戶端（AVA-GPT）連上伺服器後，透過 `tools/list` 取得每個工具的名稱、說明與參數 JSON Schema，呼叫時送出 `tools/call`。管理員要做的是**註冊 MCP 伺服器、設定權限政策**，不必另外手寫函式簽名。對話中的 `https://api.mycompany.com/erp/query_rooms` 只是示意網址。

### 3.1 依 MCP 規格修正後的標準流程

| 步驟 | 負責人 | 內容 |
| :---: | :--- | :--- |
| 1 | 需求與規格 | 確定工具用途、輸入參數（型別、格式、必填）、輸出欄位、唯讀或可寫入 |
| 2 | 後端工程師 | 撰寫查詢邏輯，連 ERP 資料庫或呼叫既有 ERP API；查詢類工具用唯讀帳號 |
| 3 | 後端工程師 | 用 MCP SDK（如 Python `FastMCP`）把函式註冊為工具；**函式名稱、型別註記與 docstring 會自動轉成工具定義** |
| 4 | 後端工程師 | 以 stdio（本機）或 HTTP（遠端服務）方式啟動 MCP 伺服器，用 MCP Inspector 等工具測試 |
| 5 | 平台管理員 | 在 AVA-GPT 註冊此 MCP 伺服器，系統自動以 `<工具名>_mcp_<伺服器名>` 命名 |
| 6 | 平台管理員 | 設定權限政策（開放、限定群組或強制禁用）；寫入類工具（如預訂）建議加身分驗證與操作紀錄 |
| 7 | 使用者 | 用自然語言提問，AI 依工具說明決定是否呼叫 |

### 3.2 最小範例（示意）

以下為 Python FastMCP 的寫法示意，**不是 AVA_ERP 的實際程式**；資料表與欄位名稱須依 ERP 實際結構替換。

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("AVA_ERP")

@mcp.tool()
def erp_query_meeting_rooms(date: str) -> dict:
    """查詢指定日期所有會議室的預訂排程。

    Args:
        date: 日期，格式 YYYY-MM-DD，例如 2026-10-08
    """
    rows = query_erp_db(date)  # 以唯讀帳號查詢 ERP 會議室預訂資料（自行實作）
    return {"date": date, "rooms": rows}

if __name__ == "__main__":
    mcp.run()  # 預設 stdio；遠端服務可改用 HTTP 傳輸
```

撰寫重點：
- **docstring 就是給 AI 看的說明書**：寫清楚用途、參數格式與限制，AI 才會在對的時機正確呼叫。
- **參數要有型別**：SDK 依型別註記產生 JSON Schema，AI 傳錯格式時會先被擋下。
- **查詢與寫入分開**：查詢類（query、list、check）和寫入類（book）拆成不同工具，管理員才能分別控管權限。

---

## 4. 與既有知識的關聯

- MCP 協定、Google Tasks／Obsidian MCP 安裝與 ava_sandbox 沙箱：[[AI Agent 實戰與 MCP 伺服器整合]]。
- 用 FastMCP 實作 MCP 伺服器的完整案例：[[一沐日雲端點餐與 MCP 系統開發實務]]。
- Agent、工具與 MCP 等術語：[[AI 時代的 Agent 術語與核心概念]]。
