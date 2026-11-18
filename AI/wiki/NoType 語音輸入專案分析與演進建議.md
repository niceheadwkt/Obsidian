---
type: analysis
tags: [NoType, 語音輸入, Electron, Whisper, Groq, 台灣詞庫, 技術選型, UIPI, SogaType]
sources: ["[[AI/raw/NoType 專案深度分析與演進建議書.md|NoType 專案深度分析與演進建議書]]"]
created: 2026-11-18
updated: 2026-11-18
---

# NoType 語音輸入專案分析與演進建議

使用者自製的語音輸入工具 NoType（本機專案 `C:\aiTest\NoType`）的技術分析：剖析現有實作、和商用工具 SogaType 橫向比較，並針對台灣詞庫、資料庫選型、Windows 相容性（UIPI、熱鍵衝突）與延遲提出可落地的方案。延遲與詞庫規模數字為文件中的估計值。

**一句話重點**：收音架構勝過 SogaType，詞庫、延遲與熱鍵待補

## 一、NoType 與 SogaType 對比

| 維度 | NoType | SogaType | 啟示 |
|------|--------|----------|------|
| 技術棧 | Electron＋Node.js＋koffi（FFI） | .NET 8 WPF／WinForms | NoType 有跨平台潛力 |
| 收音 | Chromium `getUserMedia`＋`MediaRecorder`（底層 WASAPI） | NAudio WinMM `WaveInEvent` | **NoType 勝**：不受 WinMM 端點停用（`0x2`）影響 |
| 語音辨識 | 自帶金鑰（OpenAI Whisper／Groq `whisper-large-v3`） | 封閉雲端管線 | NoType 零月租、隱私可控；SogaType 開箱即用 |
| 文字潤飾 | 兩段呼叫：Whisper → GPT-4o-mini／Llama 3.3 | 後端合併成單一請求＋台灣語料校正 | SogaType 約 1.5 秒；NoType 約 2～4 秒 |
| 詞庫 | 未實作（只靠提示詞要求繁體） | 內建約 22.5 萬台灣詞＋雲端自訂詞庫 | NoType 最需要補強 |
| 情境感知 | 無 | 抓前景視窗的程式名稱與標題送給 AI | 可依軟體調整輸出風格 |
| 輸出 | koffi 呼叫 `keybd_event` 模擬 Ctrl+V | 同 | 都會碰到 UIPI 與剪貼簿還原時差 |
| 熱鍵 | 長按 `Alt+Space`（輪詢 `GetAsyncKeyState`） | 預設按一下開／關，也支援長按 | Toggle 適合長篇、不易誤觸系統選單 |

## 二、NoType 現有優勢

1. **現代音訊架構**：走 Chromium／WASAPI，對多聲道、耳機切換與驅動狀態容錯高；SogaType 遇到端點停用會直接報錯（見 [[SogaType 語音輸入 Windows 排錯紀錄]]）。
2. **純 JS FFI（koffi）**：免 `node-gyp` 與 Visual Studio C++ 編譯器，直接載入 `user32.dll`，打包 NSIS／Portable 乾淨。
3. **便宜又快**：Groq Whisper 約 300 ms、Llama 3.3 約 400 ms，免費額度即可應付日常。

## 三、改善建議

1. **熱鍵與觸發模式**：`Alt+Space` 是 Windows 保留的視窗系統選單，放開後焦點容易跑到標題列選單，Ctrl+V 貼空。建議預設改 `Ctrl+Shift+Space`、``Alt+` `` 或 `F8`，並加「觸發模式」選項：長按說話（短回覆）／按一下開始、再按一下結束（長篇）。
2. **UIPI 防呆**：一般權限程式送不出按鍵到管理員視窗。打包設定允許提權；偵測到前景視窗是管理員權限（或貼上後剪貼簿沒被取走）時，在浮動提示顯示「請手動按 Ctrl+V 或以管理員執行 NoType」。
3. **前景視窗感知**：在 `src/shortcut.js` 用 koffi 呼叫 `GetForegroundWindow`、`GetWindowTextW`，把視窗標題傳給 `src/api/llm.js` 調整提示詞——通訊軟體輸出口語短句；Word／Outlook 輸出正式段落；IDE／終端機優先保留英文術語與變數名。
4. **記憶體直傳**：目前錄音寫到暫存 `notype-recording.webm` 再讀回；改為直接把 buffer 包成 `Blob` 放進 `FormData`，少一次磁碟讀寫，也不留音訊檔。

## 四、台灣詞庫：兩層攔截

台灣使用者的痛點：同音異字（在／再、的／得、做／作、需／須）、兩岸用語（鼠標／滑鼠、視頻／影片、服務器／伺服器、信息／訊息）、特有詞與中英夾雜（統編、公文、ERP 專案代號）。

```
語音 → 第一層：Whisper prompt 引導選字 → 第二層：LLM 修正＋本地辭典取代 → 模擬 Ctrl+V
```

- **第一層（最關鍵）：Whisper 的 `prompt` 參數**。OpenAI 與 Groq 都支援；它被當作解碼前的「前文」，模型會傾向採用其中出現的詞彙與寫法。上限 244 token（約 100～150 個中文詞）。放「台灣常見用語＋使用者專有名詞」，在辨識階段就避免「滑鼠」變「鼠標」。
- **第二層：LLM 潤飾提示詞**。規定一律台灣繁體、列出兩岸用語替換表、附使用者專有名詞字典、移除贅詞並修同音錯字與標點。

## 五、要不要資料庫？

| | 方案 A：JSON／TXT | 方案 B：SQLite | 方案 C：向量資料庫 |
|---|---|---|---|
| 適用規模 | 1～1,000 筆（個人詞、公司名、專案代號） | 1,000～30 萬筆（全量辭典） | 10 萬筆以上、有語意關聯 |
| 查詢耗時 | < 1 ms | 1～5 ms | 20～100 ms |
| 依賴 | 零 | `better-sqlite3` 需 C++ 編譯；WASM 版體積大 | 需向量模型與原生套件 |
| 維護 | 極低，文字編輯器直接貼 | 中（Schema、Migration、SQL） | 極高 |

**結論：現階段不需要資料庫**。理由：Whisper prompt 只放得下百餘詞，大詞庫送不進去；專案 CLAUDE.md 規定不能用需要 Visual Studio 編譯的原生套件；使用者只想貼一串名詞，文字檔最直覺。

**建議雙軌**：
1. 個人自訂詞庫存在 `electron-store`（JSON），每次 100% 放進 Whisper prompt。
2. 靜態兩岸用語對照表 `src/assets/taiwan-dict.json`（500～1,000 組），LLM 潤飾後在本地用正則再取代一次，確保不漏。
3. 將來真要收教育部 20 萬詞，用純 JS 的 Trie（字典樹）或 Aho-Corasick 自動機，記憶體約 5～10 MB、查詢 0.1 ms 等級、免編譯。

## 六、三階段藍圖

| 階段 | 項目 |
|------|------|
| 一：詞庫與基礎體驗（最快見效） | Whisper／Groq 加台灣基準 prompt；設定頁新增「專有名詞字庫」；預設熱鍵避開 `Alt+Space` 並改善修飾鍵釋放 |
| 二：情境與多模式 | 前景視窗標題感知；中文潤飾 ⇄ 英／日翻譯切換；Toggle 觸發模式 |
| 三：效能與權限 | 記憶體直傳；UIPI 提示；內建兩岸用語本地取代辭典 |

> [!WARNING] 內容衝突
> 根據本頁（NoType 建議書），`Alt+Space` 是 Windows 系統選單，會讓模擬的 Ctrl+V 貼空，不建議當熱鍵；但 [[SogaType 語音輸入 Windows 排錯紀錄]] 的最佳實務建議 SogaType 改用 `Alt+Space`。兩邊的觸發方式不同（NoType 長按、SogaType 按一下開關），是否都會受影響待使用者確認。

## 我可以怎麼用

- **把兩層詞庫用在 ERP 語音輸入**：常用的表名、作業代號（如 DAJJU1）、需求單號格式、同事姓名放進個人詞庫，讓 Whisper 第一層就辨識對；全域規則中的「語音輸入文字正規化」則扮演第二層。
- **技術選型先問兩件事**：資料量多大、怎麼查。百筆以內用 JSON、十萬筆以上才考慮資料庫——這個判斷也適用 ERP 小工具與 Skill 的設定檔設計。
- **守住專案 CLAUDE.md 的限制**：本案因「不得使用需編譯的原生套件」排除 `better-sqlite3`；請 Agent 提方案時，先讓它讀專案規範，避免提出做不到的設計。
- **藍圖當待辦清單**：第一階段三項成本最低、效果最明顯，可以先做；完成後回來更新本頁。
- **延遲優化思路**：兩次雲端來回是延遲主因，合併請求或換更快的服務商（Groq）比調程式碼有效。

## 關聯頁面
- [[SogaType 語音輸入 Windows 排錯紀錄]]（對照的商用工具與 UIPI 細節）
- [[AI Agent 實戰與 MCP 伺服器整合]]（全域設定中的語音輸入正規化）
- [[AI 語音複製與 VoxCPM2 本地部署]]
- [[主權 AI 與 token 帳單三層陷阱]]（自帶金鑰與成本控制）
