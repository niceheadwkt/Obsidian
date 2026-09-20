# NoType 專案深度分析與演進建議書

> 本文件旨在深入剖析 NoType 目前的技術實作，橫向對比商用工具 SogaType 的架構優缺點，並針對**「客製化台灣詞庫整合」**、**「資料庫技術選型」**、**「Windows 系統相容性（UIPI、衝鍵）」**與**「延遲優化」**提出完整、可落地的技術方案，供後續深入研究與重構實作參考。

---

## 目錄
1. [NoType 與 SogaType 橫向深度對比](#一-notype-與-sogatype-橫向深度對比)
2. [NoType 現有架構的亮點與優勢](#二-notype-現有架構的亮點與優勢)
3. [核心體驗與系統相容性改善建議](#三-核心體驗與系統相容性改善建議)
4. [專題剖析：如何加入「客製化台灣詞庫」？](#四-專題剖析如何加入客製化台灣詞庫)
5. [資料庫技術選型：是否需要建立資料庫？](#五-資料庫技術選型是否需要建立資料庫)
6. [分階段實施演進藍圖](#六-分階段實施演進藍圖)

---

## 一、 NoType 與 SogaType 橫向深度對比

| 比較維度 | NoType (`C:\aiTest\NoType`) | SogaType (搜咖科技) | 評析與啟示 |
| :--- | :--- | :--- | :--- |
| **開發技術棧** | **Electron + Node.js + koffi (FFI)** | **.NET 8 WPF / WinForms (C# 原生)** | NoType 具跨平台潛力；SogaType 原生啟動輕量（但單檔 74MB）。 |
| **麥克風音訊擷取** | **Chromium Web API** (`getUserMedia` + `MediaRecorder`) | **NAudio WinMM** (`WaveInEvent` / `waveInOpen`) | **NoType 大勝**。Chromium 底層走 WASAPI，完全免於 Windows 11 舊式 WinMM 端點停用（`0x2`）的硬傷。 |
| **STT 辨識服務** | **BYOK 自帶金鑰**（OpenAI Whisper / Groq `whisper-large-v3`） | **封閉專屬雲端管線** (`voicetype.tvsoga.com`) | NoType 零月租、隱私可控；SogaType 一站式開箱即用。 |
| **AI 文本潤飾** | **二階段調用**：Whisper 轉字 ➔ GPT-4o-mini / Llama 3.3 潤飾 | **後端整合成單一 Request**（STT + 台灣語料校正） | SogaType 延遲低（約 1.5 秒）；NoType 目前兩次雲端來回（約 2～4 秒）。 |
| **詞庫與在地化** | 尚未實作（純靠 LLM 提示詞要求繁體） | **內建 22.5 萬台灣原生詞庫** + 雲端自訂詞庫同步 | SogaType 對台灣口語、專有名詞辨識極準；NoType 急需補強詞庫引導。 |
| **情境脈絡感知** | 無（通用 System Prompt） | **前景視窗感知**（抓取 `app_name`、`window_title` 送給 AI） | SogaType 能根據當前軟體（如通訊軟體或程式編輯器）自動調整輸出風格。 |
| **鍵盤模擬機制** | `koffi` 呼叫 `keybd_event` (Ctrl+V) | `keybd_event` (Ctrl+V) | 兩者機制相同，均會面臨 Windows UIPI 權限隔離與剪貼簿還原時差問題。 |
| **快捷鍵觸發** | 長按說話（`Alt+Space` 輪詢 `GetAsyncKeyState`） | 預設按一下開/關（Toggle），亦支援長按 | SogaType 的 Toggle 模式在長篇輸入時更輕鬆，且不易觸發 Windows 系統選單。 |

---

## 二、 NoType 現有架構的亮點與優勢

1. **現代化 WASAPI 音訊架構（最大隱形優勢）**：
   * SogaType 依賴過時的 WinMM MME API，若系統端點被標記為 `DEVICE_STATE_DISABLED (0x2)`，SogaType 會直接壞死拋錯。
   * NoType 透過 Electron 隱藏視窗調用 Web標準的 `navigator.mediaDevices.getUserMedia`，底層由 Chromium 自動走現代 Windows WASAPI 驅動，對多聲道、耳機麥克風切換與驅動狀態具備極高容錯率。
2. **純 JS FFI 策略（koffi）精準實用**：
   * 成功避開了 `node-gyp`、Visual Studio C++ 編譯器等沉重負擔，直接透過 `koffi` 動態載入 `user32.dll`，在打包 NSIS / Portable 時非常乾淨。
3. **極高性價比與隱私自主**：
   * 支援 Groq API，不僅辨識速度超越 OpenAI 原廠（Groq Whisper 約 300 ms，Llama 3.3 約 400 ms），且成本極低，甚至免費額度即能滿足日常高強度打字需求。

---

## 三、 核心體驗與系統相容性改善建議

### 1. 調整預設快捷鍵與支援「按一下開關（Toggle）」模式
* **現有問題**：NoType 預設為 `Alt + Space`。在 Windows 中，`Alt + Space` 是系統保留的「視窗系統控制選單（還原、移動、大小、關閉）」。長按放開後，Windows 極易將焦點轉移至視窗標題列選單，導致後續模擬的 `Ctrl + V` 貼空。
* **改進建議**：
  * 預設快捷鍵改為不與系統衝鍵的組合，例如：`Ctrl + Shift + Space`、`Alt + \`` 或單鍵 `F8`。
  * 在設定頁加入**「觸發模式」**切換：
    1. **長按說話（Push-to-Talk）**：適合 10 字以內的簡短回覆。
    2. **按一下開始，再按一下結束（Toggle）**：適合會議逐字筆記、長篇文章撰寫。

### 2. 解決 Windows UIPI（使用者介面權限隔離）模擬按鍵失效
* **原理發現**：Windows 安全機制規定，一般權限程式（Medium Integrity）絕對無法向系統管理員身分（High Integrity）執行的視窗發送 `keybd_event`、`SendInput` 或 `WM_PASTE` 訊號。若使用者在以管理員開啟的 Windows Terminal、PowerShell、VS Code 中打字，NoType 會看似毫無動作（文字其實已在剪貼簿中，但 `Ctrl + V` 被系統丟棄）。
* **改進建議**：
  * **打包配置**：在 `package.json` 的 `electron-builder` 配置中，允許提權或預設以最高權限相容性執行。
  * **軟體內防呆提示**：若偵測到當前前景視窗為管理員權限（或貼上後剪貼簿未被取走），在浮動提示視窗（Overlay）顯示：*「目標視窗具備管理員權限，請手動按 Ctrl+V 或將 NoType 設為以管理員身分執行」*。

### 3. 加入「前景應用程式視窗感知」（Context-Awareness）
* **實作方式**：
  * 在 [`src/shortcut.js`](file:///C:/aiTest/NoType/src/shortcut.js) 透過 `koffi` 調用 `user32.dll` 的 `GetForegroundWindow` 與 `GetWindowTextW`。
  * 捕捉使用者按下錄音瞬間正在使用的應用程式（如：`LINE`、`Outlook`、`Notion`、`Visual Studio Code`）。
  * 將該視窗標題動態傳遞給 [`src/api/llm.js`](file:///C:/aiTest/NoType/src/api/llm.js)，動態微調 LLM 的 Prompt：
    * 若在通訊軟體（LINE / Slack）➔ 輸出俐落口語短句，不加過於嚴肅的公文標點。
    * 若在文件 / 郵件（Word / Outlook）➔ 輸出排版整齊的正式段落與標點。
    * 若在 IDE / 終端機 ➔ 英文專有名詞、變數名與程式術語優先採用標準寫法。

### 4. 記憶體直傳優化（免除硬碟落盤 I/O）
* **現有問題**：目前錄音結束後，透過 IPC 將音訊送回主進程，主進程呼叫 `saveAudioBuffer` 寫入 `os.tmpdir()` 為 `notype-recording.webm` 檔案，再由 API 模組用 `fs.readFileSync` 讀出打包成 `Blob`。
* **改進建議**：直接在記憶體中將 `audioBuffer` 轉為 `Blob` / `Uint8Array` 裝入 `FormData` 送出，減少一次 SSD 寫入與讀取延遲，同時降低磁碟殘留隱私音訊檔案的風險。

---

## 四、 專題剖析：如何加入「客製化台灣詞庫」？

台灣使用者在語音輸入時最常遇到的痛點是：
1. **同音異字**（如：在/再、的/得、做/作、需/須）。
2. **兩岸用語差異**（中國用語 vs 台灣慣用語：鼠標/滑鼠、視頻/影片、服務器/伺服器、信息/訊息、網絡/網路）。
3. **台灣特有詞彙與中英夾雜**（如：統編、發票、排程、公文、Line、SogaType、ERP 專案代號）。

在 NoType 架構中，加入客製化詞庫必須採取**「雙層攔截防線」**：

```
使用者語音輸入 
     │
     ▼
【第一層：Whisper STT 偏差引導】 
 透過 API 的 prompt 參數注入關鍵字庫，引導語音模型選字
     │ (產出高準確率之原始繁體文字)
     ▼
【第二層：LLM 語意修正與詞典替換】
 透過 System Prompt 與辭典表，強制將中國用語替換為台灣慣用語，並精準修正個人專有名詞
     │
     ▼
模擬 Ctrl+V 輸出乾淨文字
```

---

### 第一層：Whisper API 的 `prompt` 參數引導（最關鍵）

OpenAI 與 Groq 的 Whisper API 均支援一個未被充分利用但極度強大的參數：**`prompt`**。
* **技術原理**：Whisper 採用自回歸架構，`prompt` 參數會作為語音解碼前的「前文上下文（Previous Context）」。模型會傾向於優先匹配 `prompt` 中出現過的詞彙與拼寫風格。
* **限制**：最長限制為 244 個 Token（約 100～150 個中文字詞）。
* **實作範例**：
  在 [`src/api/whisper.js`](file:///C:/aiTest/NoType/src/api/whisper.js) 與 [`src/api/groq.js`](file:///C:/aiTest/NoType/src/api/groq.js) 中加入：
  ```javascript
  const userVocab = store.get('customVocabulary') || '';
  // 內建台灣高頻慣用語 + 使用者自訂專有名詞
  const baseTaiwanPrompt = '以下為台灣繁體中文對話，常見用語：滑鼠、軟體、影片、專案、排程、訊息、網路、統編、公文。';
  const finalPrompt = userVocab ? `${baseTaiwanPrompt} 專有名詞：${userVocab}` : baseTaiwanPrompt;

  formData.append('prompt', finalPrompt);
  ```
* **效果**：能直接在聲學辨識階段，就防止 Whisper 把「滑鼠」聽成「鼠標」，或把使用者公司名、英文代號寫錯。

---

### 第二層：LLM 語意修正與辭典精確替換

在 [`src/api/llm.js`](file:///C:/aiTest/NoType/src/api/llm.js) 的 `POLISH_PROMPT` 中注入辭典規則：
```markdown
你是一個專為台灣使用者設計的文字編輯助手。
規則：
1. 一律使用繁體中文（台灣標準國語）。
2. 絕對禁止使用中國大陸用語，請自動替換：
   - 鼠標 ➔ 滑鼠
   - 視頻 ➔ 影片
   - 服務器 ➔ 伺服器
   - 軟件 ➔ 軟體
   - 信息 ➔ 訊息
   - 默認 ➔ 預設
   - 鏈接 ➔ 連結
3. 使用者專屬專有名詞字典（請務必嚴格依此拼寫）：
   ${userVocabularyList}
4. 移除口語贅詞（嗯、呃、那個、就是），修復同音錯字與標點。
```

---

## 五、 資料庫技術選型：是否需要建立資料庫？

在思考是否要替 NoType 引入資料庫（如 SQLite）時，需從**資料量級**與**檢索情境**來客觀評估：

### 三種技術方案深度評估

| 評估維度 | 方案 A：輕量本地 JSON / TXT (推薦 MVP) | 方案 B：內嵌 SQLite 資料庫 | 方案 C：向量資料庫 (Vector DB) |
| :--- | :--- | :--- | :--- |
| **技術實作** | `electron-store` (JSON) 或單一 `lexicon.txt` | `better-sqlite3` 或 `sql.js` (WASM) | LanceDB / Voy / 內存 Embedding |
| **適用詞庫規模** | **1 ~ 1,000 筆**（個人專用詞、公司名、專案代號） | **1,000 ~ 300,000 筆**（教育部全量國語辭典、先鋒語料庫） | 100,000 筆以上具複雜語意關聯之知識庫 |
| **檢索耗時** | `< 1 ms`（純記憶體 Array / Set） | `1 ~ 5 ms`（B-Tree 索引查詢） | `20 ~ 100 ms`（向量相似度運算） |
| **相容性與依賴** | **零外部依賴**，完全符合專案現況 | `better-sqlite3` 需要 C++ 編譯環境；若用 WASM 版體積較大 | 需額外引入向量模型與原生套件，極為沉重 |
| **維護成本** | **極低**。使用者可直接用文字編輯器複製貼上整份詞表 | 中等。需要撰寫 Table Schema、Migration 與 SQL 查詢 | 極高。需處理 Embedding 更新與模型載入 |

---

### 評估結論：現階段「不需要」傳統資料庫，建議採「混合文字/JSON 方案」

#### 為什麼目前不需要 SQLite？
1. **Whisper `prompt` 空間有限**：Whisper 每次最多只吃 244 個 Token（約百餘詞），您**不可能也不需要**把 20 萬筆字典一次全部送進 API。
2. **遵守專案防禦規範**：在 `CLAUDE.md` 明確註明 *「此專案不能使用需要 Visual Studio 編譯的原生套件」*。`better-sqlite3` 是著名的原生 C++ 依賴，在 Windows 環境極易引發編譯失敗與打包障礙。
3. **使用者維護極簡化**：如 SogaType 的 `vocabulary.txt`，使用者只想用頓號、逗號或換行貼上數十個專案名稱，用文字檔或 JSON 最直覺。

---

### 最佳推薦實作架構：雙軌詞庫設計

若未來要兼顧「個人常用詞（少量高頻）」與「台灣在地詞典（大量靜態）」，最佳架構為：

1. **軌道一：個人自訂詞庫（儲存於 `store.js` / JSON）**
   * 使用者在設定面板自行輸入，如：
     `nicehead, Sense Bar, ERP系統, 搜咖科技, SogaType`
   * 每次呼叫 Whisper 時，**100% 全量注入** `prompt` 參數中。
2. **軌道二：靜態台灣慣用語轉換表（靜態模組 `taiwan-dict.json`）**
   * 收集常見的 500～1000 組兩岸用語對照表（如 `{"鼠標": "滑鼠", "信息": "訊息", "內存": "記憶體"}`）。
   * 放在 `src/assets/taiwan-dict.json` 中，當 LLM 潤飾完畢後，在本地進行一次急速正則替換，確保 100% 不漏勾。
3. **未來擴充（若真要收錄教育部 20 萬詞庫）**：
   * 不使用 SQLite，改用純 JavaScript 實作的 **Trie（字典樹）** 或 **Aho-Corasick 自動機** 演算法。
   * 記憶體佔用僅約 5MB～10MB，查詢速度在 0.1 毫秒等級，完全免編譯，即可在本地瞬間完成整段文章的台灣詞彙校對。

---

## 六、 分階段實施演進藍圖

當您深入研究完成後，建議可依以下節奏分階段落地：

### 第一階段：詞庫與基礎體驗補強（耗時最短，成效最顯著）
- [ ] **實作 Whisper / Groq `prompt` 參數**：在 API 請求中加入台灣基準 Prompt。
- [ ] **設定頁新增「專有名詞字庫」欄位**：串接 `electron-store`，讓使用者自訂詞彙能直達 Whisper。
- [ ] **調整預設熱鍵**：避開 `Alt+Space`，提供 `Ctrl+Shift+Space` 或 `F8` 選項，並改善修飾鍵釋放邏輯。

### 第二階段：情境脈絡與多模式擴充
- [ ] **前景視窗標題感知**：利用 `koffi` 抓取當前 Window Title 餵給 LLM。
- [ ] **新增「即時多國翻譯模式」**：效法 SogaType，增加一組快捷鍵（或右鍵選單）一鍵切換「中文潤飾 ⇄ 英文/日文翻譯」。
- [ ] **支援「按一下開始/結束（Toggle）」**：降低長按造成的指尖疲勞。

### 第三階段：效能極致化與權限強固
- [ ] **記憶體直傳 Buffer**：移除暫存檔寫入讀出流程。
- [ ] **UIPI 管理員權限提醒**：於 Overlay 中加入權限受阻的友善提示。
- [ ] **內建兩岸用語本地替換辭典**：確保 100% 產出純正台灣繁體慣用語。
