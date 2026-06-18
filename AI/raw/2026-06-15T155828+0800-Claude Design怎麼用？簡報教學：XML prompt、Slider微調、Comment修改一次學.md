---
title: "Claude Design怎麼用？簡報教學：XML prompt、Slider微調、Comment修改一次學"
source: "https://www.bnext.com.tw/article/90717/claude-design-vs-figma-adobe-canva-workflow-shift"
author:
  - "[[數位時代 BusinessNext]]"
published: 2026-04-20
created: 2026-06-15
description: "Anthropic 推出對話式設計工具 Claude Design，能以自然語言直接產出簡報。"
tags:
  - "clippings"
---
Anthropic 4 月 17 日發布 [Claude Design](https://www.anthropic.com/news/claude-design-anthropic-labs) ，同日 Figma 股價一度下跌 7%、Adobe 跌 2.7%、Wix 跌 4.7%；不到 24 小時內， [Canva 宣佈與 Anthropic 合作](https://www.canva.com/newsroom/news/canva-claude-design/) ，強調使用者在 Claude Design 產出初稿後可無縫切到 Canva 完稿。

股價是市場的直覺反應，但更重要的問題是：Claude Design 到底在做什麼，為什麼設計工具三強（Figma、Adobe、Canva）同時緊張？

## Claude Design可以用在哪？

簡單來說，Claude Design 是 Anthropic 推出的 **對話式設計工具** 。你用中文或英文描述想要什麼，它直接產出可以用的成品檔。目前五種主要輸出：

掌握最新AI、半導體、數位趨勢！訂閱《數位時代》日報及社群活動訊息

1. **簡報（slides / pptx）** ：pitch deck、產品發布簡報、季度報告、會議內容整理
2. **Landing page / 行銷網頁** ：從 Hero 區塊到整頁，支援 standalone HTML 匯出，可直接部署
3. **One-pager** ：單頁產品說明、活動 DM、募資頁面
4. **App / 網站 UI 原型（prototype）** ：模擬介面長相與互動流程，給工程師看或給投資人展示
5. **影片與互動設計（frontier design）** ：Anthropic 自稱的高階用法，支援動畫、3D、互動效果、影片 demo

**匯出格式** 依類型而異：簡報類匯出 PPTX、PDF；網頁類匯出 standalone HTML；多數輸出都能產 PDF 截圖。

此外，設計可以打包成結構化 handoff（含 layouts、images、dev notes、元件註解）送進 Claude Code，讓工程師直接接手成完整應用程式。

## 為什麼 Figma 和 Adobe 同時緊張？

因為三家公司本來各守一塊：Figma 做 UI 設計與工程協作、Canva 做簡報與社群圖、Adobe 做高階設計（XD、Illustrator、Photoshop）。Claude Design 打破的是 **「工具邊界」** 。

**對 Figma 的威脅** ：它跳過 Figma 的核心動作（拉元件、排版、對齊），讓你用自然語言直接生成 UI 原型，還能讀你 Git repo 裡的 CSS 變數（品牌色、字體設定），自動套用到設計。Figma 目前只能「畫畫」，沒辦法把設計跟程式碼雙向同步。

**對 Canva 的威脅** ：Canva 強在模板多、社群協作順。Claude Design 不跟你比模板，直接用 Opus 4.7 的視覺能力生成「不是模板」的內容。Canva 的反應是 24 小時內宣佈整合合作，代表它看清這不是競爭，是改朝換代。

**對 Adobe 的威脅** ：Adobe 系列工具學習曲線最陡。Claude Design 的目標就是 **讓不會用 Photoshop 的人也能做出能看的設計** 。Adobe 的護城河正在被繞開。

一句話概括來說，這代表 Claude Design 真正讓設計軟體業界緊張的點不是模型強，而是 **工作流被重新定義** 。

## Claude Design做簡報怎麼用？

以下是一份從零開始的建議流程，做一份「Apple 2027 AI 穿戴戰略解讀」簡報。素材取自《數位時代》近期報導〈 [蘋果智慧眼鏡代號 N50！4 種設計、3 款配色搶先看，明年上市正面對決 Meta](https://www.bnext.com.tw/article/90608/apple-ai-glasses-n50) 〉，全程共有 6 個步驟。

### Step 1：認真回答開場問卷，別用單字敷衍

**為什麼重要** ：打開 Claude Design 後，可以先填寫下方的「 **Set up your design system** 」，這份「意圖問卷」問的是目標、受眾、風格偏好，因此答案品質會直接決定輸出地板，建議仔細填寫清楚。

![圖一：Claude Design介面](https://image-cdn.learnin.tw/bnextmedia/image/album/2026-04/ac8x-1776669863.png?w=1200&output=webp)

首次打開Claude Design，可以點「Set up your design system」，進行設計語彙的設定。

圖／ Claude

**建議這樣回答** （以《數位時代》編輯日常使用為例，填一次就能跨專案重用）：

- **目標** ：一句話說清楚你要做什麼。例如「整理某件產業事件的重點懶人包」、「做一份產業格局分析簡報」、「把一場訪談精華轉成 one-pager」
- **受眾** ：關注科技產業的商業讀者，習慣讀業內脈絡、熟悉 AI／半導體／軟體產業的關鍵玩家，但不一定懂底層技術細節
- **風格偏好** ： **要** 什麼、 **不要** 什麼都寫清楚。例如「要資訊密度高、有比較表、有時間軸、有 diagram，參考 The Information、The Verge、Stratechery 長文配圖質感」、「不要 SaaS 通用版型、不要 keynote 極簡白底、不要花俏漸層」

![圖二：Set up your design system](https://image-cdn.learnin.tw/bnextmedia/image/album/2026-04/kn2e-1776669950.png?w=1200&output=webp)

依照說明填入資訊，Claude就會生成符合描述的元件。

圖／ Claude

填完送出後，系統會耗費約5分鐘產出一份「你的品牌設計規範檔」，等於幫你把視覺 DNA 數位化。設定完一次，後續都不用再填因此，花個 3 分鐘把受眾、風格、 **不要什麼** 講清楚，可省掉後面 30 分鐘的 re-prompt。

![圖三：Review draft design system](https://image-cdn.learnin.tw/bnextmedia/image/album/2026-04/vs53-1776670025.png?w=1200&output=webp)

輸入資訊後，Claude會在10分鐘內完成設計元件，使用者可以一筆一筆審核。

圖／ Claude

### Step 2：用 XML 標籤結構化寫破題 prompt

完成設定後，回到初始的 Claude Design 介面，就可以點選 Slide Deck 標籤來接續製作。

接下來，可以選擇用 XML 標籤結構化寫破題 prompt，或用自然語言也沒問題。

![圖四：New slide deck](https://image-cdn.learnin.tw/bnextmedia/image/album/2026-04/ihxi-1776670157.png?w=1200&output=webp)

回到初始介面來選擇製作形式。

圖／ Claude

**為什麼重要** ：Claude 模型系列對 XML 標籤格式有大量訓練資料。把 prompt 拆成 `<task>` 、 `<context>` 、 `<brand>` 、 `<constraints>` 等結構化區塊，是最高 CP 的一招。系統提示本身就是結構化格式，你的 prompt 越像它，越合拍。

**建議直接複製以下 prompt 到 Claude Design** ：

```xml
<task>
設計一份 6-8 頁的簡報，主題是「Apple 2027 AI 穿戴戰略解讀」。
</task>

<context>
素材：《數位時代》2026-04 報導
關鍵事實：
- Apple 代號 N50 智慧眼鏡，2026 年底-2027 年初發表，2027 上市
- 4 種鏡框設計（Ray-Ban Wayfarer 風大矩形、Tim Cook 風細矩形、大橢圓/圓形、小橢圓/圓形）
- 3 種配色（黑、海洋藍、淺棕）
- 鏡頭為直立橢圓設計搭配環繞燈（區隔 Meta 的圓形設計）
- 三件組戰略：眼鏡 + 新 AirPods + 相機吊墜
- 對手：Meta（EssilorLuxottica 合作）、Google / Samsung（Warby Parker 合作）
- 真正 AR 眼鏡（帶顯示）預估 2020 年代末才成熟，較原計畫（mid-2022）延後約 8 年
</context>

<brand>
語氣：產業分析、直接、有觀點
參考：The Information 配圖質感、Stratechery 文末 diagram
配色：深灰底（#1a1a1a）+ 蘋果風銀灰 + 一抹亮色強調
字型：不用 Inter、不用 Roboto。請用有個性的 serif 搭配 sans-serif 組合
</brand>

<constraints>
- 不要 Apple keynote 極簡白底
- 不要通用 SaaS 漸層
- 每頁資訊密度要夠，不要一頁只放一句話
- 時間軸頁必須有、競爭格局比較表必須有
</constraints>

<structure>
1. 封面：一句話概括 Apple 戰略
2. N50 眼鏡規格一覽
3. 三件組戰略圖
4. 時間軸（2026-2030）
5. 競爭格局比較表（Apple / Meta / Google）
6. 判斷：Apple 路徑與 Apple Watch 的相似性
</structure>

請先給我 3 個不同視覺方向的初稿，我再挑一個發展下去。
```

![圖五：填入prompt](https://image-cdn.learnin.tw/bnextmedia/image/album/2026-04/ps3r-1776670306.png?w=1200&output=webp)

使用者可依照需求填入Prompt，此時建議填入結構化的大綱與內容，才能生成需要的架構。

圖／ Claude

**重點** ：最後一句「請先給我 3 個不同視覺方向的初稿」是順應系統提示內建規則（主動提供變體）。主動要它分叉，會比產一版回來再逐版改更省 token。

![圖六：三種方案生成中](https://image-cdn.learnin.tw/bnextmedia/image/album/2026-04/q5p9-1776670415.png?w=1200&output=webp)

直接要求Claude生成三種方案，會比後續再提出要求更省Token。

圖／ Claude

### Step 3：貼風格參考截圖，別用形容詞

**為什麼重要** ：「做得乾淨一點」沒用。Opus 4.7 是 Anthropic 最強的視覺模型，直接貼截圖當 inline reference，它能精準提取字型、間距、配色系統。系統提示也明訂 Claude 要「源用既有 UI kit 的配色、間距、字型」，貼圖正是在餵它既有參考。

**建議做法** ：從 3 個初稿中選最接近想像的那個，接著貼 1-2 張參考圖（例如你欣賞的報導配圖、diagram 範本）。下一句指令可以寫：「把選定的初稿微調，版面密度對齊參考圖 1，比較表頁參考圖 2 的 diagram 風格。」

**重點** ：停止描述，開始貼圖。具體參考（像 Stratechery、Linear 2023 年那版）比抽象形容詞（專業、乾淨）有效太多。

### Step 4：用 Comment 做局部修改

**為什麼重要** ：過去 Midjourney、v0 改一處就整張重生，好的部分一併消失。Claude Design 可以直接在頁面某個元素上留 comment，它只迭代那個元素。Ryan Mather 的實戰建議：第一版產出後通常有幾十個細節要調，別用嘴巴描述，直接「點它、評它」。

**建議嘗試的 comment 類型** ：

- 對某個表格：「這個表格太密，拆成 N 個 card 形式」
- 對時間軸某節點：「這個節點放大，加 badge 凸顯」
- 對比較表某一欄：「這一欄換成品牌色系，其他欄用灰階」

每條 comment 都隻影響它指的那個元素，其他部分不動。

![圖七：透過comment局部修改](https://image-cdn.learnin.tw/bnextmedia/image/album/2026-04/3b6i-1776670519.png?w=1200&output=webp)

在Claude介面中，可以點選想要修改之處，就可以請AI局部調整。

圖／ Claude

**重點** ：Comment 是 Claude Design 跟所有上一代 AI 設計工具最大的差異。學會它，就不會因為「想改一個小地方結果整張重畫」而崩潰。

### Step 5：叫它生出自訂 Slider，微調整體感覺

**為什麼重要** ：Claude Design 可以為你的 **特定設計** 生成調整滑桿（不是通用模板）。根據實測，你在對話裡要求「為這個設計生成 slider」，系統會根據你的素材產出專屬滑桿，維度可能包括字體密度、顏色冷暖、版面鬆緊等。

**建議嘗試的指令** ：「為這份簡報生成幾個 slider，讓我可以微調整體視覺感覺。」

系統會根據這份簡報的素材判斷哪些維度值得提供 slider。拉完滑桿，整份簡報會在幾秒內依這些維度統一調整，不用重新下指令。

只要要求「為這份簡報生成slider」，就可以透過滑桿微調版面元素。

圖／ Claude

**重點** ：Slider 是 Claude Design 最被低估的功能。它把「要改什麼、改多少」這件事從 **語言** 變成 **直覺操作** 。實際生成的 slider 名稱與數量會因設計而異。

### Step 6：知道什麼時候該自己動手

**為什麼重要** ：雖然用AI生成簡報很方便，但仍要注意某些細節影響力特別大的地方，例如icon、插圖、命名等，這些值得你手動慢慢做。

在 agentic 設計的快速節奏中，知道 **什麼時候該慢** ，本身就是一門手藝。

**建議檢視的三個地方** ：

- **封面標題** ：AI 生成的標題通常偏「平敘」，人工改寫成有衝突感或具體度更高的版本往往更抓眼球
- **品牌 logo** ：若 Claude 用生成式 icon，可能看起來太「AI 味」。手動換成官方品牌 logo，專業感立刻拉昇
- **結論句** ：AI 產出的結論常是類比型通用語，值得用記者本身的觀點改寫得更精準

**重點** ：交給 AI 做的事，跟 **該自己定案的事** ，分開。標題的 hook、品牌辨識的 logo、結論的精準度，這三類就是該自己動手的。辨認出這條界線，就是從「Claude Design 新手」走向「熟手」的關鍵。

> [點我檢視簡報pdf成品](https://drive.google.com/file/d/1uBiXcPQKaq2uPKZ9fK6LML65wuyAXesD/view?usp=sharing)  
> 體驗 Claude Design [請點我](https://claude.ai/design)

跑完整流程後，你會拿到一份資訊密度足、視覺風格有個性的簡報。相比傳統 Keynote / Google Slides 手動排版，產出效率絕對更高。

最後可以說，資深設計師的價值未來不再是執行速度，而是品味、系統思考、約束設定。若你的工作內容主要是「把 Figma 推得快」，重新技能配置的時間到了。

> 延伸閱讀： [Google簡報Gemini新功能教學！3步驟生成可編輯投影片，標題內文都能直接修改](https://www.bnext.com.tw/article/90659/google-slides-gemini-ai-tutorial)

資料來源： [30 things to know to become a claude design engineer（@the\_smart\_ape）](https://x.com/the_smart_ape/status/2045493173951103455) 、 [Ryan Mather 技巧 thread（@Flomerboy，Anthropic verticals team）](https://x.com/Flomerboy/status/2045162321589252458) 、 [Claude Design 系統提示洩漏（CL4R1T4S 倉庫）](https://github.com/elder-plinius/CL4R1T4S/blob/main/ANTHROPIC/Claude-Design-Sys-Prompt.txt) 、 [Anthropic 官方發布](https://www.anthropic.com/news/claude-design-anthropic-labs) 、 [《數位時代》蘋果智慧眼鏡 N50 報導](https://www.bnext.com.tw/article/90608/apple-ai-glasses-n50) 、 [Canva × Anthropic 合作公告](https://www.canva.com/newsroom/news/canva-claude-design/)

本文初稿為AI編撰，整理．編輯/ 李先泰