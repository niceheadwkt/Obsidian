---
type: source-summary
tags: [MCP, Claude, Gemini, NotebookLM, Gemini Notebook, 交叉驗證, 一天一AI]
sources: ["[[AI/raw/2026-11-26T134523+0800-Claude分析完，還能交給Gemini挑毛病！官方MCP設定教學，免費方案也能用.md|Claude分析完，還能交給Gemini挑毛病！官方MCP設定教學（數位時代，2026-11-25）]]"]
created: 2026-11-26
updated: 2026-11-26
---

# Claude 分析交 Gemini Notebook 挑毛病：官方 MCP 設定

數位時代「一天一 AI」專欄（韋惟珊，2026-11-25）。這篇介紹 Google 推出的 Gemini Notebook（原 NotebookLM）官方 MCP：讓 Claude 電腦版把討論好的分析直接寫進 Gemini 筆記本，再到 Gemini 做成網站、語音，或換個角度挑毛病。作者實測兩邊用免費方案都能操作。

**一句話重點**：用官方 MCP 把 Claude 分析交給 Gemini 挑毛病

## 一、這個 MCP 能做什麼、不能做什麼

| 項目 | 說明 |
|---|---|
| 能做 | 建立、查看、管理筆記本；新增與查看來源（文字、網址、YouTube 影片） |
| 不能做 | 不能透過 MCP 直接上傳 PDF。可以先請 Claude 把 PDF 整理成文字再新增，或到 Gemini Notebook 手動上傳 |
| 不負責 | 互動網站、語音摘要、簡報等產出，要到 Gemini Notebook 介面操作 |
| 費用 | Gemini Notebook API 與 MCP 還在公開預覽，API 暫時免費；Claude 免費方案也能用自訂連接器 |
| 資料去向 | 新增的資料存進你的**個人** Google 帳號 |

開始前要確認三件事：
- 使用最新版 Claude 電腦版。
- 用個人 Google 帳號，並且至少登入過一次 Gemini Notebook。
- Claude 免費方案**只能新增一個自訂連接器**，已經接了別的自訂 MCP 時，可能要先移除。

## 二、設定步驟

### 第一段：Google Cloud 建立專案與 OAuth 憑證
1. 到 Google Cloud Console 用個人帳號建立新專案。
2. 搜尋「Gemini Notebook API」並啟用。
3. 「OAuth 同意畫面」選「外部」，填寫應用程式名稱和聯絡信箱，把自己加進「測試使用者」；在「資料存取」加入 `https://www.googleapis.com/auth/notebook` 權限。
4. 「憑證」→ 建立「OAuth 用戶端 ID」，類型選「網頁應用程式」：
   - 已授權的 JavaScript 來源：`https://claude.ai`
   - 已授權的重新導向 URI：`https://claude.ai/api/mcp/auth_callback`
5. 複製用戶端 ID 和密鑰。**密鑰只會顯示一次，也不要貼進 AI 對話**。

### 第二段：Claude 新增連接器並授權
6. Claude 電腦版 → 設定 → 外掛程式 →「瀏覽外掛程式」→「新增自訂連接器」，網址填 `https://notebook.googleapis.com/mcp`，再貼上用戶端 ID 和密鑰。
7. 在 Google 登入畫面選個人帳號。
8. 出現「這個應用程式未經 Google 驗證」時，確認是自己建的應用程式、帳號和權限都正確，再按「繼續」和「允許」。
9. 測試：「請使用 Gemini Notebook 連接器，列出我所有的筆記本。」

> [!NOTE]
> OAuth 應用程式還在**測試模式**時，授權可能 **7 天後到期**。突然連不上時，重新授權即可。

## 三、工作流：Claude 定稿 → 筆記本 → Gemini 產出與反向檢查

1. **在 Claude 完成分析**（文中範例是「該選哪個雲端服務」），再請它寫進筆記本：
   > 整理剛剛的分析評估，以最後確認的版本為準。請用 Gemini Notebook 建立一個新筆記本，名稱叫「＿＿」。把結論、比較表和還沒確定的地方整理成一份來源加進去。評估時參考的網址，也請各自加成來源。完成後，列出筆記本裡的來源清單給我核對。
2. **在 Gemini Notebook 產出**：做成互動式網站（可以切換比較三個平台），並且要求「沒有資料的地方標示待確認，不要自行補數字」。「工作室」也能做語音摘要、影片摘要和簡報，可用功能依帳號開放情況而異。
3. **讓 Gemini 換角度挑毛病**：在 Gemini 選取這本筆記本，然後問：
   > 請根據這本筆記本，扮演會否決這份提案的財務主管：1. 找出 3 個最可能被質疑的地方。2. 舉出一個可能讓方案失敗的反例。3. 列出哪些結論還缺乏證據，以及可以去哪裡補資料。回答時，請標明哪些資訊來自筆記本，哪些來自網路搜尋。

Gemini 的意見只是另一個檢查角度，採不採納還是由人判斷。

## 我可以怎麼用

- **ERP 規劃案的交叉審查**：在 Claude Code 整理好的系統規劃或選型評估，送進 Gemini 筆記本，讓 Gemini 扮演「會否決提案的主管」或「現場使用者」來挑毛病。這和 [[Felix Rieseberg 訪談：把 AI 用大、對抗式審查與並排跑]] 提到的跨模型對抗式審查是同一個思路。
- **給主管看的版本**：結論、比較表和待確認事項寫成一份來源，再用 Gemini Notebook 做成可點選的互動網站或通勤語音，就不用另外做簡報。
- **注意帳號與機密**：這個 MCP 走**個人** Google 帳號，公司 ERP 資料、zpq 查詢結果、客戶資料不要送進去；只用在公開資料或去識別化的評估。
- **連接器額度**：如果用 Claude 免費方案，自訂連接器只有一個，要和其他自訂 MCP 取捨。
- **PDF 先轉文字**：規格書、法規 PDF 要先請 Claude 整理成文字來源，或手動上傳。

## 關聯頁面

- [[NotebookLM 綜合指南]]：Gemini Notebook（原 NotebookLM）功能總覽。
- [[Gemini 筆記本打造 AI 學習教練：考照與孩子複習]]：同一個專欄的 Gemini 筆記本用法。
- [[AI Agent 實戰與 MCP 伺服器整合]]：其他 MCP 伺服器的整合實務。
- [[Felix Rieseberg 訪談：把 AI 用大、對抗式審查與並排跑]]：多模型交叉審查的觀念。
- [[Google AI Pro 訂閱權益與八大工具選用]]：Gemini Notebook 的定位與額度。
