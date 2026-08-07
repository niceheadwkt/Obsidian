# mcp-drink 工作筆記

## 上次做到哪 (2026-08-07)
- **修正網頁內置 AI 點餐識別與幻覺點餐 Bug**：
  - 優化 [app.js](file:///c:/aiTest/mcp-drink-main/app.js) 的 `callWebLLM` 與 `callLocalOllama` 系統提示詞、降低推理溫度至 `0.1`，並加入「不加料」 Few-Shot 範例，改善對「小平平」等三人名及否定規格的識別。
  - 新增歷史紀錄過濾器，自動移除包含 `✅`/`❌`/`成功為` 的工具執行結果文字，避免小模型因上下文模仿而產生「假成功、未寫入 DB」的幻覺。
- **優化快取檢測與 Qwen 2.5 3B 識別**：
  - 重構 `getCachedModels` 匹配邏輯，忽略非英數字元（如點 `.`, 減號 `-` 等），並支援對 OPFS 目錄名稱的模糊對齊，順利偵測出 Qwen 2.5 3B 快取。
- **下拉選單白底白字樣式修正**：
  - 在 [style.css](file:///c:/aiTest/mcp-drink-main/style.css) 寫入全域 `select option` 樣式，強制深色底、淺色字，防止原生 Light 模式渲染白底白字。
- **知識庫文件整理與匯入 (第十九批 Ingest)**：
  - 全量匯入 `AI/raw/` 目錄中剩餘 20 份文獻（包含 AI Agent 基本功系列 EP01-EP07、一沐日雲端點餐 MCP 專案啟動說明、Kimi 發展專題等）。
  - 新增 4 個 Wiki 頁面（`Kimi 與月之暗面 (Moonshot AI) 發展專題`、`AI Agent 基本功系列實踐指南 (EP01-EP07)`、`一沐日雲端點餐與 MCP 系統開發實務`、`深度學習與大語言模型架構全景`）。
  - 修訂 6 個現有概念頁面，並同步更新 [index.md](file:///g:/%E6%88%91%E7%9A%84%E9%9B%B2%E7%AB%AF%E7%A1%AC%E7%A2%9F/Obsidian/AI/wiki/index.md)、[log.md](file:///g:/%E6%88%91%E7%9A%84%E9%9B%B2%E7%AB%AF%E7%A1%AC%E7%A2%9F/Obsidian/AI/wiki/log.md) 與 [dashboard.html](file:///g:/%E6%88%91%E7%9A%84%E9%9B%B2%E7%AB%AF%E7%A1%AC%E7%A2%9F/Obsidian/AI/dashboard.html)。

## ⚠️ 本週卡關與已解決/待解決之架構挑戰 (2026-08-07 更新)

本週研發與測試過程中，遇到之技術卡關與架構挑戰依**時間演進順序（從 Streamlit 早期環境、Gemini 對接、PWA 重構、行動端自適應至內置 AI 精細調優）**整理如下：

---

### 【8/3 ── Streamlit 與 Cloud 部署基礎建立階段】

#### 1. Streamlit Cloud 非同步事件循環衝突 ── `asyncio` 被主執行緒佔用報錯
*   **實務現象**：點餐系統早期部署於 Streamlit Community Cloud 時，執行非同步 FastMCP 工具調用時拋出事件循環衝突、已被佔用或未啟動的錯誤。
*   **核心原因**：Streamlit 架構本身有獨立的事件循環管理機制，直接以常規的 `asyncio.run()` 呼叫非同步函式會與主執行緒產生衝突。
*   **解決對策**：改為引進 `anyio` 架構，並微調 Streamlit 非同步事件循環的進入點，確保 MCP 與 UI 能併發且安全地執行。

#### 2. `TaskGroup` 多工併發異常堆疊 (Traceback) 遺失 ── 調試困難
*   **實務現象**：點餐的並行子任務（如同時查重複與點單）在 `TaskGroup` 內發生崩潰時，網頁 UI 僅顯示模糊錯誤，缺乏詳細 Traceback，無法定位哪一筆點單出錯。
*   **核心原因**：Python `TaskGroup` 會將併發錯誤打包成 `ExceptionGroup` 拋出，Streamlit 預設無法妥善解構並顯式輸出其底層詳細報錯堆疊。
*   **解決對策**：利用 `traceback` 模組，捕獲異常後手動格式化完整 Stack Trace 並安全輸出至 Streamlit 畫面，解決非同步多工的偵錯瓶頸。

#### 3. Anthropic API 信用額度卡關 ── 後端 LLM 緊急路由切换為 Gemini 2.5
*   **實務現象**：測試過程中 Anthropic 帳戶信用額度用盡 (Low Credit/Over Limit)，點餐助理全面停擺報錯。
*   **核心原因**：Anthropic 平台 API 調用頻繁且受到額度硬性限制。
*   **解決對策**：緊急將 LLM 核心後端重構為 Google Gemini 2.5 Flash API，並支援在 Streamlit Secrets 中動態偵測並排定金鑰讀取順序，繞過額度封鎖。

---

### 【8/4 ── Gemini 工具對接與 PWA 架構重大重構階段】

#### 4. Gemini API 傳入工具 Schema 解析報 `400 Bad Request` ── Schema 格式不相容
*   **實務現象**：使用 Gemini 2.5 Flash 進行 Function Calling 時，一呼叫 API 即報錯 `400 Bad Request`，工具調用失敗。
*   **核心原因**：Gemini 對 Tool 的 JSON Schema 規範極為嚴格，不允許出現 Anthropic 或 OpenAI Schema 中常見的非標準欄位，且 `required` 參數格式要求極為固定。
*   **解決對策**：實作專屬清理函式 `cleanSchemaForGemini`，在發送前將不相容欄位完全過濾；後續修復了 `required` 陣列在清理時被誤判並轉為物件的 Bug，確保 Schema 格式 100% 合規。

#### 5. Gemini 密集調用 API 觸發 `429 Too Many Requests` ── 速率限制限制 (Rate Limit)
*   **實務現象**：AI 連續執行「查詢重複」與「點餐」等多步工具，或多輪快速對答時，網頁頻繁拋出 Gemini API 429 錯誤。
*   **核心原因**：免費或低階 Gemini API Key 受到每分鐘請求次數 (RPM) 的嚴格限制。
*   **解決對策**：在 AI 請求與工具處理層實作**指數退避重試機制 (Exponential Backoff Retry)**，偵測到 429 狀態時自動延時重試，大幅提升多步驟點單的成功率。

#### 6. Streamlit 效能與行動端自適應受阻 ── 架構重構為輕量 HTML PWA 直連 Firestore
*   **實務現象**：Streamlit 在行動裝置上的排版不易調整，不支援離線快取（PWA），且多人使用時 Streamlit Server 記憶體耗費巨大、滑動與連線卡頓。
*   **核心原因**：Streamlit 是 Server-rendered 架構，不適合高頻、多裝置、要求即時響應的 PWA 行動應用。
*   **解決對策**：全面重構架構，改為前端 HTML/JS/CSS PWA 靜態網頁（部署於 Vercel），利用 Firebase Client SDK 直連 Firestore 雲端資料庫，降低伺服器開銷並提升響應速度。

#### 7. 點餐助理對話歷史上下文遺失 ── 無法進行多輪「修改/去冰」承接對答
*   **實務現象**：點餐完說「那幫我改去冰」，AI 助理無法理解指的是哪一杯飲料或什麼動作，每次發言都被當作獨立的新點單。
*   **核心原因**：前端與 Vercel 代理端 (Vercel Serverless Proxy) 原先沒有設計對話歷史 (Chat History Context) 的陣列傳遞。
*   **解決對策**：在 PWA 前端與 Proxy API 間實作多輪歷史上下文串接，並在歷史紀錄中妥善格式化使用者與助理的對話，使小模型也能完美理解「那改去冰呢」等承接上文的指令。

#### 8. 語音輸入同音錯字造成點餐/修改失敗 ── `fuzzyMatchName` 姓名模糊比對容錯
*   **實務現象**：當使用語音點餐時，容易將人名識別為同音字（如將「國炯」轉寫為「國烔」），修改或刪除時系統回報「找不到此人，無法操作」。
*   **核心原因**：資料庫採用精確姓名比對，無法容忍語音轉文字 (STT) 所帶來的錯別字。
*   **解決對策**：在前端 `app.js` 實作基於 Levenshtein Distance（編輯距離）的姓名模糊匹配函式 (`fuzzyMatchName`)，將容錯相似度閾值微調至 `>= 0.45`（確保雙字錯 1 字的 50% 相似度能被正確校正），自動對齊資料庫內真實姓名。

#### 9. 更新前端程式碼使用者手機無同步更新 ── PWA 快取失效限制
*   **實務現象**：姓名模糊匹配發佈後，使用者手機開啟網頁卻依然報錯，確認是執行了舊版程式碼。
*   **核心原因**：PWA 的 Service Worker 具備極強的快取機制，若未更新快取版本，手機瀏覽器將無限期使用本地快取之舊版 `app.js`。
*   **解決對策**：手動將 `sw.js` 的快取版本識別號手動更新為 `v2`，強制客戶端瀏覽器刷除舊快取並下載最新的 JavaScript 與 CSS 修正。

---

### 【8/6 ── PWA 行動端與部署環境最佳化階段】

#### 10. Vercel 部署 Python 版本衝突 ── 冗餘測試檔案觸發自動 Serverless Functions 建置
*   **實務現象**：在對點餐系統 PWA 執行 Vercel 雲端部署時，編譯程序突然報錯中斷，並噴出 Python 與虛擬環境依賴套件衝突。
*   **核心原因**：專案根目錄中留有未使用的 `main.py` 測試檔案，導致 Vercel 自動偵測並誤判為 Python Serverless 應用程式，在建置時嘗試安裝 Python 依賴，而與實際 Node.js/靜態網頁環境產生建置衝突。
*   **解決對策**：刪除冗餘的 `main.py` 檔案，並在 `.vercelignore` 裡明確排除所有非必要的本地 Python 測試腳本，使 Vercel 順利判定為靜態網頁與 Node.js API 架構，解決部署報錯。

#### 11. 手機 PWA 側邊欄抽屜缺乏遮罩與點擊外部關閉功能 ── 行動端 PWA UI 自適應缺陷
*   **實務現象**：在手機版 PWA 中展開 AI 助理與設定的側邊欄抽屜（Drawer）時，背景無暗色遮罩，且點擊抽屜外側空白處無法自動收回抽屜。此外，抽屜原先僅佔螢幕高度的 `60vh`，空間狹小，導致操作體驗極差。
*   **核心原因**：`index.html` 內缺乏半透明背景遮罩（Backdrop）節點，且 `style.css` 在 Mobile 媒體查詢中未定義對應的樣式與事件，高度設定偏低。
*   **解決對策**：於 `index.html` 增加 `<div class="sidebar-backdrop">`，在 `style.css` 加入毛玻璃與暗化效果，並以 JavaScript 綁定「點擊遮罩即收合抽屜」的事件處理，同時將抽屜高度調升至 `75vh`，優化行動端介面操作。

---

### 【8/7 ── 內置 AI 點餐精細化調試與樣式修補階段】

#### 12. 手機端外部 Ollama 服務連線受阻 ── HTTPS 安全限制 (Mixed Content Block)
*   **實務現象**：原先規劃於手機安裝 PocketPal App 或將電腦端 Ollama 服務對外暴露，供點餐網頁跨裝置調用本地 AI 進行點餐。然而測試時手機瀏覽器完全無法與該服務連線。
*   **核心原因**：點餐 PWA 網頁部署於安全的 **HTTPS** 環境下（如 Vercel），而手機本地的 PocketPal 或電腦 Ollama API 僅提供未加密之 **HTTP** 協定。瀏覽器基於安全性會強制阻擋混合內容（Mixed Content）跨來源請求。
*   **解決對策**：全面放棄手機端外部 API 連線方案，改用 **WebLLM 網頁內置引擎**（藉由 WebGPU/WebAssembly 直接在瀏覽器沙盒內跑模型），完全避開跨來源 HTTP 安全阻擋。

#### 13. 行動端 WebView 載入 WebLLM 失敗 ── 手機瀏覽器 WebGPU 硬體相容性限制
*   **實務現象**：在舊款 iPhone（如 iPhone 11/12，iOS 17 以下）或直接使用 LINE 內建瀏覽器開啟點餐網頁時，切換至內置 AI 模式進度條卡在 `0%`，主控台（Console）報錯 `WebGPU is not supported`。
*   **核心原因**：WebLLM 高度依賴 WebGPU 硬體加速。舊版 iOS 的 Safari 預設未啟用此實驗性功能，且 LINE、WeChat 等通訊軟體內建的 WebView 為了安全與效能通常封鎖了 WebGPU API。
*   **解決對策**：於網頁加入 WebGPU 特徵檢測，一旦偵測到不支援，主動彈窗提示引導使用者「建議改用 Safari 或 Chrome 完整瀏覽器開啟」，並自動 Fallback 退回雲端 API 模式。

#### 14. 行動網路下首次加載緩慢 ── 首次下載模型流量過大體驗不佳 (Network Bottleneck)
*   **實務現象**：使用者在戶外以 4G/5G 行動網路開啟網頁，切換為內置模式時，下載進度條每數秒才跑 `1%`，需長達數分鐘且消耗數百 MB 至 1GB 以上之手機流量。
*   **核心原因**：即使最輕量的 Llama 3.2 1B 模型，分片下載也需約 600MB，行動網路不穩定時傳輸體驗極差，易使使用者放棄使用。
*   **解決對策**：在首次下載前加入預警提示窗：「*首次載入將下載約 600MB 模型，建議連接 Wi-Fi。快取後下次開啟不耗流量*」，並搭配瀏覽器 Cache Storage 與 OPFS 檔案系統將模型鎖定快取，避免重複下載。

#### 15. 手機記憶體容量不足 (OOM) 導致瀏覽器崩潰 ── 手機硬體資源瓶頸
*   **實務現象**：中低階 Android 手機或實體記憶體較小（如 4GB RAM）的舊款 iPhone 在下載並加載 `Qwen 2.5 3B` 模型時，進度條跑完或即將載入完成之際，網頁會突然變白重新整理，或是整個瀏覽器 App 閃退。
*   **核心原因**：3B 規模的模型運行需要消耗近 2GB 的實體 RAM。當手機實體記憶體不足時，手機作業系統的 OOM (Out of Memory) 機制會強制終止高能耗的瀏覽器分頁。
*   **解決對策**：在設定選單中為 Qwen 2.5 3B 標註「⚠️ 需大記憶體避免閃退」，且手機行動端預設強制選擇最輕量的 `Llama 3.2 1B (600MB)`。

#### 16. 內置 AI 切換 Gemma 2 2B 報錯 ── 靜態宣告與 WebLLM 註冊表大小寫不一致
*   **實務現象**：在網頁設定中選擇 `Gemma 2 2B` 內置模型時，進度條直接中斷，網頁主控台噴出模型載入失敗與找不到 URL 資源的錯誤。
*   **核心原因**：在 [index.html](file:///c:/aiTest/mcp-drink-main/index.html) 與 [app.js](file:///c:/aiTest/mcp-drink-main/app.js) 中，我們靜態宣告的 Model ID 為 `Gemma-2-2B-it-q4f16_1-MLC`（首字母大寫）。然而，WebLLM 官方 Hugging Face 與模型註冊表 (registry) 限制該模型 ID 必須為全小寫的 `gemma-2-2b-it-q4f16_1-MLC`。大小寫不一致導致 CDN 無法對應模型下載位址。
*   **解決對策**：將 [index.html](file:///c:/aiTest/mcp-drink-main/index.html) 與 [app.js](file:///c:/aiTest/mcp-drink-main/app.js) 中的該 Model ID 一律變更為小寫形式 `gemma-2-2b-it-q4f16_1-MLC`，重新部署後即正常。

#### 17. 小模型 (SLM) 在點餐意圖下的推理不穩定與幻覺 ── 參數量限制 (Prompt & Context Sensitivity)
*   **實務現象**：
    1.  *人名與規格混淆*：「幫小平平訂烏龍綠」，模型常將 3 字人名誤判為中杯/大杯規格，造成 name 欄位落空。
    2.  *否定語意理解失敗*：「烏龍綠，不要加粉粿」，小模型會因抓到「粉粿」關鍵字，誤將其塞入 `toppings`（反而變成要加料）。
    3.  *對話歷史模仿導致的「幻覺點餐（假成功）」*：當多輪對話歷史帶有先前工具執行結果文字（如 `✅ 點餐成功`），模型在下一輪回答會直接模仿歷史，擅自說出「已成功為您點購...」或「已刪除成功」，實際卻根本沒有調用 `place_drink_order` 或 `delete_drink_order` 等 API。
*   **核心原因**：1B/2B 等 SLM 推理規模受限，易受對話歷史的文本特徵干擾（強烈模仿傾向），且對複雜的否定語義與邊界提取敏感度低。
*   **解決對策**：
    *   將推理溫度降低至 `0.1`，並在 System Prompt 中加入「不加料 Few-shot 範例」與明確的人名對比機制。
    *   在 [app.js](file:///c:/aiTest/mcp-drink-main/app.js) 發送 `chatHistory` 給模型前，新增**歷史過濾器**，自動移除包含 `✅`/`❌`/`成功為` 的工具輸出文本，破除模型的上下文模仿幻覺。

#### 18. 快取檢測未辨識 Qwen 2.5 3B ── OPFS 目錄名稱匹配干擾
*   **實務現象**：使用者瀏覽器已確實下載並快取 `Qwen 2.5 3B` 模型，但網頁快取管理器中卻無法顯示與進行清除管理。
*   **核心原因**：原本的 `getCachedModels` 在讀取 OPFS 目錄時，直接將帶有小數點 `.`（如 Qwen2.5）或減號 `-` 的實際快取資料夾名稱與預設的模型 ID 列表做嚴格的完全字串比對，導致比對被字元干擾而失效。
*   **解決對策**：重構 `getCachedModels` 匹配邏輯，在比對時自動忽略非英數字元，並對 OPFS 快取目錄名稱進行模糊對齊（Fuzzy Alignment），成功偵測出並展現 `Qwen 2.5 3B` 快取。

#### 19. 原生 Light 模式下選單「白底白字」看不見 ── 瀏覽器下拉選項 (Option) 繼承衝突
*   **實務現象**：當使用者在 Windows Chrome 瀏覽器使用系統原生 Light 模式開啟點餐網頁，打開「快取管理」選單時，未被選取的選項呈白底白字，完全看不見選項內容。
*   **核心原因**：全域網頁設定了 `color: #fff;`（白色文字），當瀏覽器處於 Light 模式時，下拉選單選項（Option）會使用瀏覽器原生的白色背景，繼承白色文字後，即形成白底白字。
*   **解決對策**：於 [style.css](file:///c:/aiTest/mcp-drink-main/style.css) 中加入專屬樣式規則，強制將 `select option` 背景色指定為深色底（`#1e293b`），文字指定為淺色（`#f8fafc`），確保所有主題與瀏覽器下之對比度正常。

## 下一步
- **點餐意圖測試**：測試並觀察多種內置 AI 模型（如 Gemma 2 2B, Llama 3.2 1B）在各種點餐/修改/刪除意圖下的工具調用穩定度。
