---
type: source-summary
tags: [AgentBot, AI-Agent, GrokBot, Dart, Muse, RemoteControl, 多Agent協作, Claude-Code, Codex, 三師爸]
sources: [
  "[[AI/raw/2026-11-02T074859+0800-Agent Bot，一次搞懂基本原理.md|Agent Bot，一次搞懂基本原理（三師爸 Sense Bar，YouTube J47Q77nFRUM）]]",
  "[[AI/raw/2026-11-10T141555+0800-最新世代 AI Agent bot，一次搞懂基本原理.md|最新世代 AI Agent bot，一次搞懂基本原理（同場直播另一網址 1MV-yuYLiV4，附重點整理）]]"
]
created: 2026-11-18
updated: 2026-11-18
---

# Agent Bot 基本原理與分層指揮架構

整理自三師爸 Sense Bar 2026-11-02 直播〈Agent Bot，一次搞懂基本原理〉。兩個剪輯檔是同一場直播（YouTube 網址分別為 J47Q77nFRUM 與 1MV-yuYLiV4），內容相同，合併為本頁。講者用兩張圖說明 AI 的三個階段與「人類 → Agent Bot → 本機 Agent」的分層架構，並實際展示每天在用的 Grok Bot。

**一句話重點**：Agent Bot 有自己的電腦，當秘書指揮本機 Agent

> 產品名稱、價格與用量為 2026-11 直播時的資訊，Agent Bot 產品迭代快，使用前請以官方最新說明為準。

---

## 一、核心定義：Agent Bot 與 AI Agent 的差別

- **一句話關鍵**：Agent Bot 是「有自己電腦」的雲端 Agent；AI Agent 則跑在「你的電腦」上。
- 目前主流的三個 Agent Bot：

| 產品 | 廠商 | 價格 | 備註 |
| --- | --- | --- | --- |
| Muse | Meta | 免費 | 臺灣需 VPN 跨區申請，講者未實測 |
| Grok Bot | Grok | 每月 30 美金 | 講者主力使用；可開多隻 Bot |
| Dart | ChatGPT | 每月 100 美金 | 用法相同、可語音通話；目前只能有一隻 |

## 二、AI 使用的三個階段

| 階段 | 運作方式 | 優點 | 限制 |
| --- | --- | --- | --- |
| 1. 生成式 AI | 透過瀏覽器連到雲端伺服器 | 生成文字、媒體 | 碰不到本機，產出須自行下載再加工；影片編輯等需本機硬體的工作做不了 |
| 2. AI Agent | 本機應用程式搭框架，讓雲端 LLM 帶著權限與工具操作你的電腦 | 可代理人類操作電腦完成工作 | 有權限限制；人在外面須靠 Remote Control，彈性不足 |
| 3. Agent Bot | 雲端 AI＋自己的雲端電腦，同時可控制本機 | 結合前兩者優點，手機即可交付工作 | 需付費；本機主機仍須 24 小時開著 |

術語定義另見 [[AI 時代的 Agent 術語與核心概念]]。

## 三、工作架構：分層指揮

```
人類（總指揮：決策、指派、審核）
   │  手機／任何裝置對話
   ▼
雲端 Agent Bot（中間層：調度資源、擁有自己的雲端電腦與已登入帳號）
   │  以 CLI 背景啟動本機 Agent
   ▼
本機 AI Agent（Claude Code、Codex、OpenCode、AGY 等，負責實際重度工作）

另一分支：人類 ──Remote Control──▶ 本機 AI Agent（直接指揮）
```

- Agent Bot 本身**不是最聰明的模型**（無法選模型、沒有思考強度設定），定位是「秘書／指揮官」，把需要高智力的工作轉交給本機的頂級 Agent（如 [[Claude（Anthropic）|Claude]] Code）。
- 完成後由本機 Agent 回報 Agent Bot，再由 Agent Bot 回報人類。
- **Remote Control 與 Agent Bot**：Remote Control 仍可用，但需事先開啟、無法新開對話或做複雜設定，彈性比 Agent Bot 低。

## 四、為什麼「有自己的電腦」很關鍵

- 本機 Agent 很難「打開檔案總管、點選上傳」；要上傳 YouTube 得另外寫程式並處理授權認證，很麻煩。
- Agent Bot 的做法：從本機抓取影片、字幕、metadata 複製到自己的雲端電腦，再用已登入的 YouTube／粉專帳號直接上傳。
- 在 Agent Bot 的雲端電腦登入 LINE、Facebook、YouTube 等帳號後，它就擁有對應的操作權限。
- 安全性：成熟產品依指示行事，回覆留言等對外動作要經使用者同意，不會自己亂發。

## 五、講者的實際應用

1. **影片上架**：手機一句話「幫我上架到 YouTube 和粉專」，自動處理封面、說明與檔案上傳（直播中示範孟子對荀子饒舌對決）。
2. **指揮本機 Claude Code 做影片**：Grok 開啟 Claude Code 的 Rap Battle 專案；人類審核指出「手部糊掉」，Grok 轉交 Claude 逐秒截圖檢查修正，再產出手機版傳回對話檢視。
3. **多 Agent 討論投票**：同時開四個 Agent（Codex、Claude、AGY、OpenCode），加上 Bot 自己共五方討論同一提案、互相投票（不能投自己），回覆結論與優缺點；用於腦力激盪，token 消耗不多。
4. **社群 Bot**：每晚 9 點整理 YouTube 與臉書留言、建議回覆，經同意後代為回覆。
5. **導師 Bot**：辨識班服名條統計尺寸，存進雲端硬碟「班級事務」資料夾；聯絡本、行事曆、課表、導師匯報都在同一個對話處理。
6. **數感課堂**：Bot 當大腦，Claude Code 主開發、Codex 審核，互審提升品質；上課前用手機回報 bug 並要求限時部署（教育應用另見 [[Wordwall 與教育科技的 AI Agent 自動化實務]]）。
7. **邀約／行事曆 Bot**：專門回覆研習邀約信件與排程。

## 六、建置前提與注意事項

- **一台 24 小時開機的主力電腦**（如 Mac mini 或桌機），記憶體與硬碟要足夠，裝好所有工作用的 Agent。
- Grok Bot 應用程式**目前只能連一台電腦**；裝在哪台就能控制哪台，並與手機 App 對話同步。
- 本機 Agent 的**專案要先建好**（例如在 Claude Code 設定好專案），Bot 以 CLI 在背景開啟，不跳視窗，可多工並行。
- **雲端硬碟同步**：本機裝雲端硬碟應用程式，建議用「鏡像」模式（串流有時間差，較不適合複雜工作，但也能用）。
- 多隻 Bot 之間可以互相對談、查詢彼此做過的事。
- 用量參考：Grok 30 美金方案以 7 天為週期重設，講者單日用量約 13%，一般工作足夠。

## 七、結論

- 想用好 Agent Bot，**前提仍是要會用本機 Agent**，不會的地方直接問 AI。
- 真正要學的是「人類 → Agent Bot → 本機 Agent」的邏輯架構，理解後才能正確分派工作。
- 講者建議：預算有限選 Grok Bot 即可，Dart（100 美金）目前不必買。

## 我可以怎麼用

- **先把本機 Agent 用熟**：目前已用 Claude Code 搭配 skill（ERP 查詢、CVS 提交、Wiki 入庫與健檢）完成實際工作，這正是 Agent Bot 的前提；要導入時，Bot 只需負責分派，專案與 skill 沿用現有的。
- **適合交給 Bot 的工作**：需要「已登入帳號」或「人不在電腦前」的事，例如手機一句話觸發 Wiki 入庫、每晚整理 `AI/raw` 並回報摘要（呼應 [[Claude＋Obsidian 第二大腦七步法]] 的例行排程）。
- **ERP 情境要守邊界**：正式機查詢只能唯讀且有 Token 等級限制，不宜交給雲端 Bot 代登入；Bot 只做通知與彙整，實際查詢仍由本機 Agent 依規範執行。
- **多 Agent 投票**可用於方案評估：把同一個 ERP 設計問題丟給 Claude、Codex 各自提案再互評，對應現有的 decision-plan 決策流程。
- 本機雲端硬碟目前是「串流檔案」模式；講者建議 Bot 搭配「鏡像」模式，導入前要評估兩者差異（見 [[Git GUI 與 GitHub 雙向同步實務]]）。

## 關聯頁面
- [[AI 越聰明，你越省力_直播總結與學習卡]]（三師爸 2026-10-18 直播，AI 工具三代演進）
- [[AI 時代的 Agent 術語與核心概念]]
- [[Claude 基本功與個人 AI 工作流實戰]]
- [[AI Agent 實戰與 MCP 伺服器整合]]
- [[Wordwall 與教育科技的 AI Agent 自動化實務]]
- [[Claude＋Obsidian 第二大腦七步法]]
- [[Anthropic 野心提示詞：高度、深度、廣度三招]]（同樣強調 AI 要有自己的電腦、接得到原始資料）
