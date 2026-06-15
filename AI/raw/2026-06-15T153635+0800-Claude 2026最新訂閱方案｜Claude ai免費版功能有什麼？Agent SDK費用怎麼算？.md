---
title: "Claude 2026最新訂閱方案｜Claude ai免費版功能有什麼？Agent SDK費用怎麼算？"
source: "https://www.bnext.com.tw/article/90109/claude-ai"
author:
  - "[[陳祈安]]"
published: 2026-05-19
created: 2026-06-15
description: "Claude 6月15日起調整計費方式，新制最關鍵的變化是「互動式使用」與「程式化使用」將切割為兩個獨立額度池，一次看懂新方案："
tags:
  - "clippings"
---
Anthropic 宣布自 2026 年 6 月 15 日起調整 Claude 計費方式，起因是 「Claude Agent SDK 第三方代理工具 Conductor 和 OpenClaw 等第三方工具大量呼叫 Agent SDK（程式化用量），導致訂閱額度迅速耗盡，衝擊統一費率定價模式。

新制最關鍵的變化是一分為二：互動式使用（Claude.ai 對話、互動式 Claude Code、Claude Cowork）與程式化使用（Agent SDK、claude -p 指令、Claude Code GitHub Actions 及基於 Agent SDK 的第三方應用程式），將切割為兩個獨立額度池，不再互相佔用。程式化使用新增每月專屬額度，用盡後若已啟用「額外用量」選項，將以完整 API 費率計費；若未啟用，則 Agent SDK 請求暫停至下個計費週期重置。Anthropic 預計於 6 月 8 日寄送 email，說明如何領取額度。

無論你是每天靠 Claude 寫稿、做分析的商務工作者，還是用 Claude Code 跑專案的工程師，這次的調整都值得你重新審視手上的方案是否仍划算。本文將介紹 Claude AI 的特色功能，並完整比較免費與各付費方案的差異。點擊以下目錄即可跳至指定區段。

掌握最新AI、半導體、數位趨勢！訂閱《數位時代》日報及社群活動訊息

> ### 目錄
> 
> [Claude AI 是什麼？](#what-is-claude)  
> [Claude AI 三大特色功能](#features)  
> [Claude 有哪些好用功能？](#new-features)  
> [Agent SDK 費用怎麼算？Claude AI 收費方案一覽](#sdk-pricing)

## Claude AI 是什麼？

Claude AI 是由 Anthropic 開發的生成式人工智慧。與強調對話互動的 [ChatGPT](https://fc.bnext.com.tw/articles/view/4435?utm_source=article&utm_medium=read-around) ，或主打生態系整合的 [Gemini](https://fc.bnext.com.tw/articles/view/4432?utm_source=article&utm_medium=read-around) 不同，它擅長處理涉及語言、推理、分析、程式編寫等任務。主要功能包括文字和程式碼生成（文字摘要、問題回答、資料擷取、文字翻譯以及程式碼解釋和產生）和視覺處理（處理和分析視覺輸入，並從圖像產生文字和程式碼）。

此外，Claude AI 主打安全性及高品質的推理輸出，它內建一套行為準則（合憲 AI），讓模型具備自我監督與修正能力，過濾偏見之餘，更大幅降低「AI 幻覺」發生率，使得在處理極低容錯率的任務時更顯可靠。

最新一代模型包括：

- Claude Opus 4.7 - 最聰明模型的最新版本，也是全球最佳的編碼、企業代理和專業工作模型。
- Claude Sonnet 4.6 - 兼具性能和實用性，適用於包括編碼和代理在內的大多數用途。
- Claude Haiku 4.5 - 速度最快，擁有接近前沿智慧的模型。

> 延伸閱讀： [Claude 三款模型怎麼選？Opus、Sonnet、Haiku 完整比較，沒切換模型可能會多花 5 倍成本](https://fc.bnext.com.tw/articles/view/4553?utm_source=article&utm_medium=read-around)

## Claude AI 三大特色功能

Anthropic 旗下的 Claude 系列模型，被認為是擁有最強大寫程式能力的 AI 模型，也是首選的 Vibe Coding 模型。此外，Claude 最突出的長項是它的「上下文視窗（Context Window）」，也就是一次能處理的文字上限。以下介紹 Claude AI 的特色功能：

### Claude Cowork：具代理功能的數位助理

Claude Cowork 最大特色在於：不只是回答問題，更具備代理能力，使用者不需具備軟體工程相關背景也能使用。當使用者授權 Claude Cowork 讀取特定資料夾後，它能直接存取使用者的本機檔案、操作應用程式，並在背景完成多步驟（如自動讀取、修改或建立檔案）的複雜任務。

舉例來說，它可以像數位助理一樣幫你整理電腦桌面上被隨意排列的資料夾，或將一堆收據照片自動轉化為依日期、金額等項目整理好的 Excel 報表，甚至直接將一份長篇研究報告生成 PPT 初稿。

> **實測看這邊：** [Claude Cowork是什麼？Cowork教學：簡報、報帳、整理雲端硬碟5個超實用場景](https://www.bnext.com.tw/article/89996/claude-cowork-transforming-generative-ai-into-a-digital-colleague)

而在正式執行任務前，它也會事先擬定執行計劃，並透過圖形界面與使用者進行執行步驟確認，避免執行錯誤（如誤刪重要檔案）的情況發生。最終使用者可直接在本機上看到產出成果。在架設環境要求上，目前僅支援 macOS 桌面版應用程式，且需具備 Claude Pro、Max、Team 或 Enterprise 訂閱。

### Claude code：開發者的代理式編碼助手

[Claude code](https://www.bnext.com.tw/article/90460/claude-map-to-master) 是專為軟體工程師設計的「代理式」開發工具，提供命令行介面（CLI）與網頁版兩種靈活型態。與傳統僅提供代碼建議的 AI 不同，它具備高度自主執行能力，能直接深入專案根目錄讀取整體架構、編輯檔案、運行測試腳本並進行除錯。

透過網頁版，開發者可直接串接 GitHub 儲存庫，在雲端環境非同步執行複雜任務，甚至同時處理多個專案的 Pull Request（PR）與 Git 版本管理。結合 CLAUDE.md 的專案規範設定，Claude Code 能確保 AI 生成的代碼完全符合企業內部的編碼風格與安全性標準，讓 AI 能自主驗證結果並縮短交付週期。

此功能開放給 Pro、Max、Team、Enterprise 方案訂閱者，或有 [Claude Console](https://console.anthropic.com/) 帳戶者使用。

> 延伸閱讀： [Claude Code 10組完整提示詞！教你如何自動整理檔案、分析帳單⋯零技術新手也OK](https://www.bnext.com.tw/article/89967/claude-code-ai-prompt)

### Skills：將 SOP 變成可重複使用的 AI 技能包

Skills 是將標準作業程序（SOP）轉化為 AI 可讀指令的技術。透過編寫 SKILL.md 檔案，使用者可自行定義任務的說明文件，如在其中寫入使用方式、進階指引、定義輸出格式…等，並將其封裝成一份 ZIP 檔。每當要執行任務時，將將檔案上傳給 Claude，它就會在執行任務時，自動讀取說明書，並依照其中流程執行。如此，將可以省去使用者重複輸入提示詞的時間。

Skills 功能為 Claude code 的擴充功能，需訂閱 Pro、Max、Team、Enterprise 方案使用，或有 [Claude Console](https://console.anthropic.com/) 帳戶者才可使用。

> 延伸閱讀： [免費Agent Skills課程來了！2小時上完、新手友善，教你打造高效工作流](https://www.bnext.com.tw/article/90058/agent-skills-free-course-deeplearning-ai-anthropic-latest-partnership)

## Claude 有哪些好用功能？

### 1\. Claude in Excel：一鍵完成分析與建模

Claude 現在已直接嵌入 Excel 側邊欄，並協助用戶進行數據分析、建立財務預測模型，甚至可根據數據自動生成專業圖表。這代表，面對繁複的數據，使用者不再需要手動拉公式、調整表格、選擇適合呈現數據的圖表，而是改用對話的方式向 Claude 說明需求，如「計算去年各季度的毛利，並找出成長率最高的產品」，它就會自動在對應的儲存格寫下正確公式。

這項功能目前僅提供給 Pro、Max、Team 和 Enterprise 方案的訂閱用戶，免費帳戶需要付費升級才能使用。

**安裝步驟說明：**

1. 在 [Microsoft Marketplace](https://www.microsoft.com/zh-tw) 中搜尋「Claude by Anthropic in Excel」 [► 點我下載](https://marketplace.microsoft.com/zh-tw/product/WA200009404?tab=Overview)
2. 點擊「立即取得」，並登入 Microsoft 帳號，下載完成後，點選「在 Excel 打開」圖示。
3. 開啟 Excel 啟動外掛程式：

\- Mac：工具 > 增益集  
\- Windows：首頁 > 常用 > 增益集

1. 登入 Claude 帳號後，就能開始使用

![Claude in Excel](https://image-cdn.learnin.tw/bnextmedia/image/album/2026-01/gkt7-1769507122.png?w=1200&output=webp)

圖／ 數位時代

> 延伸閱讀：  
> [CLAUDE.md這樣寫才對！12條規則一次整理，讓Claude Code錯誤率從41%降至3%](https://www.bnext.com.tw/article/90965/claude.md-claude-code)

### 2\. Slack、Canva、Figma 等整合進聊天室

過去，Claude 以「工具調用」的方式替使用者執行第三方服務，但多半以背景 API 方式進行。然而，現在在互動式介面中，使用者可以在 Claude 聊天室中直接修改 Canva 簡報、預覽 Slack 訊息草稿，或是與 Claude 協作調整 Figma 上的設計原型，徹底解決在多個分頁間頻繁切換的痛點。

這功能目前已在網頁版與桌面版 Claude 上線，開放給 Pro、Max、Team 與 Enterprise 方案使用者。

> 延伸閱讀： [ChatGPT Image 2.0指令大全！50組提示詞一次整理，LINE貼圖、簡報封面、插畫菜單全搞定](https://www.bnext.com.tw/article/90908/chatgpt-image-2-prompt-guide-complete)

### 3\. Claude for Healthcare：醫療行政救星

這是一款具備 HIPAA（美國健保隱私法）合規認證的 Claude 醫療版，專為醫療機構設計。它能協助自動化醫學編碼、整理病歷摘要，並協助臨床試驗方案的草擬。

它能串接業界常用的資料庫，如 CMS 覆蓋資料庫、ICD-10（國際疾病分類第十版）和 PubMed（生醫文獻資料庫）等，協助醫護人員自動化處理病歷摘要、事前授權（Prior Authorization）、理賠等情境，有助於醫護人員大幅縮減跨系統比對的時間，並減輕行政負擔。

> 延伸閱讀： [Anthropic官方發布新創AI使用指南！4大階段＋3款工具，教你打造AI原生公司](https://www.bnext.com.tw/article/90974/ai-native-startup-founders-playbook-anthropic-claude)

### 4\. Claude in PowerPoint：不再走鐘的品牌簡報自動化

過往 AI 生成簡報最大的問題在於，產出風格往往與公司品牌格格不入。透過 Claude in PowerPoint，它不只是在投影片上貼上文字，而是能事先讀取提供給它的範例投影片的母片設定、版面配置、字型與顏色規範。

之後，使用者只需以自然語言下令（如：新增三頁市場分析內容），Claude 便會自動產出符合企業視覺識別（CI）的新頁面，而非自行創造不相容的設計元素，確保品牌形象不被破壞，大幅減輕設計人員後續校對與重新美化的負擔。

此功能目前處於測試版研究預覽階段，僅供 Max、Team 和 Enterprise 方案使用。

## Agent SDK 費用怎麼算？Claude AI 收費方案一覽

以下整理 Claude AI 現有的訂閱方案給讀者參考。

| 項目/方案 | 免費版 | Pro | Max | Team | Enterprise |
| --- | --- | --- | --- | --- | --- |
| 費用 (美元) | $0/月 | $20/月 | Max 5x：$100/月   Max 20x：$200/月 | $25-$125/每人每月 | 專案報價 |
| **Agent SDK 月度額度（6/15 起）** | X | **$20 美元** | **Max 5x：$100 美元   Max 20x：$200 美元** | **標準座位：$20 美元   高階座位：$100 美元** | **依座位類型，最高 $200 美元** |
| 適合 | 偶而使用 | 定期使用 | Max 5x 適合經常使用   Max 20x 適合每天使用且需經常協作者 | 適用於 5 到 75 人的團隊 | 大型組織 |
| 訊息用量 | 有限制，每 5 小時重置一次 | 5 倍於免費版 | 可選擇 5 倍或 20 倍於 Pro 用量 | ・標準座位：比 Pro 更多的使用量   ・高階座位：比標準座位多 5 倍的使用量 | \- |
| 跨平台使用 | V（網頁、iOS、Android、桌面端） | V | V | V | V |
| 基本內容生成（編程、分析、視覺化等） | V | V | V | V | V |
| 尖峰時段優先權 | X | X | V | \- | \- |
| 連線 Slack 和 Google Workspace 服務 | V | V | V | V，還可連線 Microsoft 365 | V，還可連線 Microsoft 365 |
| Claude Cowork | X | V | V | V | V |
| Claude Code | X | V | V | V | V |
| Skills | X | V | V | V | V |
| Claude in Excel | X | V | V | V | V |
| Claude in PowerPoint | X | X | V | V | V |
| 使用 HIPAA 就緒產品 | X | X | X | X | V |
| Project（專案知識庫） | 有限使用 | V | V | V，並可共享 | V，並可共享 |
| 企業搜尋 | X | X | X | V | V |
| 特色及限制 | ・無法使用 Opus 模型   ・無 Cowork 自動化功能 | ・支援 Projects   ・支援長文本處理 | ・所有任務的輸出限制更高   ・提前訪問高階 Claude 功能 | ・中央管理後台   ・Claude 桌面應用程式的企業部署   ・支援單點登入、零數據訓練保證 | ・支援跨域身份管理系統、審計日誌、零數據訓練保證   ・提供專屬技術顧問   ・增強的上下文視窗 |

注意：使用 API 金鑰（Claude Platform）的開發者不受上述 Agent SDK 額度規則影響，仍維持按量計費。

除了以上方案外，Claude 還有針對全球教育機構推出的 [Education plan（教育計畫）](https://claude.com/solutions/education) 。不僅提供學生及教師專屬的優惠定價，更強調符合學術界的資安標準，如 FERPA（家庭教育權利與隱私權法案）與 COPPA（兒童線上隱私權保護法）規範。教師可透過 Projects 功能打造客製化的教學助手，實現教案生成與個人化啟發教學；研究者則能利用長文本分析加速文獻歸納。

[► 前往訂閱 Claude AI](https://claude.com/pricing)

### Claude AI 與 Gemini、ChatGPT 個人付費方案比較

| 項目比較 | Claude AI | [Gemini](https://fc.bnext.com.tw/articles/view/4432?utm_source=article&utm_medium=read-around) | [ChatGPT](https://fc.bnext.com.tw/articles/view/4435?utm_source=article&utm_medium=read-around) |
| --- | --- | --- | --- |
| 月付費用 | **・Pro：** $20美元/月，使用額度為免費版的 5 倍   **・Max 5x：** $100美元/月，使用額度為 Pro 版的 5 倍   **・Max 20x：** $200美元/月，使用額度為 Pro 版的 20 倍 | **・Google AI Plus：** NTD$260/月，思考型及 Pro 模型每日上限加總為 120 個提示詞；上下文視窗達 128k 個詞元   **・Google AI Pro：** NTD$650/月，思考型及 Pro 模型每日上限加總為 400 個提示詞；上下文視窗達 100 萬個詞元 | **・GhatGPT Go：** NTD$270/月，有限制的訊息及檔案傳輸；有限制上下文視窗；有限度使用 GPT-5.2 模型   **・GhatGPT Plus：** NTD$690/月，10 倍於免費版的訊息及檔案傳輸；優於免費版的上下文視窗；可使用進階推理模型（含 Go 所有功能）   **・GhatGPT Pro：** NTD$3,300/月，無限制的訊息及檔案傳輸；最高上限的上下文視窗；GPT-5.2 專業級推理 Pro（含 Plus 所有功能）ChatGPT |
| 主打特色 | 擅長語言、推理、分析、程式編寫等任務。輸出內容具高安全性（合憲 AI） | Google Workspace 整合、多模態處理能力 | 對話式互動，適合創意發想、大眾化應用 |

> 延伸閱讀：  
> [Claude Code快捷鍵+指令大全！13大類速查不用背，從Ctrl+C到多Agent協作一次整理](https://www.bnext.com.tw/article/90925/claude-code-slash-commands-shortcuts-complete-guide)  
> [Claude Skills零基礎入門教學｜每次都要重貼提示詞？Skill設好沒反應？一篇搞定新手常見困擾](https://www.bnext.com.tw/article/90870/claude-skills-guidebook)

資料來源： [Claude Support](https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan) 、 [Claude API Docs](https://platform.claude.com/docs/zh-TW/intro) 、 [Claude Code Docs](https://code.claude.com/docs/zh-TW/claude-code-on-the-web) 、 [Claude 訂閱方案](https://claude.com/pricing) 、 [The Register](https://www.theregister.com/2026/04/22/anthropic_removes_claude_code_pro)

（本文初稿為 AI 編撰）