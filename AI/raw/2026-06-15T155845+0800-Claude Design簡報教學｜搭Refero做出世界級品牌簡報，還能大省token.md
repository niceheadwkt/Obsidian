---
title: "Claude Design簡報教學｜搭Refero做出世界級品牌簡報，還能大省token"
source: "https://www.bnext.com.tw/article/90873/save-tokens-with-claude-design-and-refero-brand-templates"
author:
  - "[[數位時代 BusinessNext]]"
published: 2026-05-07
created: 2026-06-15
description: "本文介紹如何搭配 Refero 的世界級品牌設計參考庫，讓 Claude Design 直接讀懂大廠設計語言，快速做出專屬簡報版型。"
tags:
  - "clippings"
---
「我在 Claude Design 上一天燒掉 500 美元」——AI Automation Society 創辦人、YouTube 70 萬訂閱的 Nate Herkelman（ [@nateherk](https://x.com/nateherk/status/2049671821193036006) ），在 2026 年 4 月 30 日的 X 貼文上這樣說。

Anthropic 在 4 月 17 日發布 Claude Design 後，他在 Max 20x（月費 200 美元）方案上一天就用掉 30% 的週限額，連續加值好幾次只為了搞清楚「到底怎麼用才不會燒錢」。

順著這個故事往下談。本文接下來借鏡 Nate Herkel 的經驗，探究怎麼把 Claude Design 用得最省；再談如何利用 [Refero](https://styles.refero.design/) 這個「世界級品牌設計參考庫」當作捷徑，讓 Claude Design 直接讀大廠的設計語言當模版，做出一套屬於自己的簡報版型。

掌握最新AI、半導體、數位趨勢！訂閱《數位時代》日報及社群活動訊息

### 怎麼搭最省 token？Chat 規劃 + Design 執行

Claude Design 跟 Claude Code 是同一條技術底層，但跑在 Opus 4.7 的視覺能力上：每次出圖後，模型會自己截圖檢查、抓出問題、修好再給你看，這個自我驗證迴圈是真的能用，但代價是 token 吃得兇，而且 Design 的限額和 Claude／Claude Code 是各自獨立的。

最關鍵的心法只有一條： **不要在 Claude Design 裡腦力激盪** 。Design 的工作是「執行已知 brief」，不是「想 brief 該長什麼樣」。每多一分鐘在 Design 裡空轉，都是真金白銀燒進去。

實作上，整個流程拆成三步：

> 1. **Chat 模式先把需求講清楚** ：在一般 Claude 對話視窗裡產出市場研究、品牌定位、簡報大綱、用色與字型清單。
> 2. **進 Claude Design 填寫資料** ：把 Chat 裡產出的 markdown 規格、Logo PNG、品牌色 hex code 全部餵進去。
> 3. **實作** ：在 Design 的畫布裡用編輯工具細修，重大方向錯了當下就停。

光是把腦力激盪移出 Design，就能省掉不少週限額。現在談完方法後，接下來看具體如何操作。

### 第一步：在 Chat 模式裡寫好「設計規格 markdown」

打開一般 Claude 對話視窗（不是 Design 喔！），讓它幫你產出一份 brand spec markdown，目標是涵蓋：使命、TA、配色、字型、語氣、Logo 概念、競品定位。

可以直接複製下面這段 prompt 當起點：

```
我要為 [品牌名稱] 製作一套品牌設計規格 markdown 文件，預計給 Claude Design 使用。請涵蓋以下章節：

1. Mission（使命，一句話）
2. Audience（核心受眾，含具體職業／情境）
3. Color palette（主色＋輔色，附 hex code，共 4–6 色）
4. Typography（標題字型、內文字型，各給 1 個西文 + 1 個中文選項）
5. Tone of voice（3 個關鍵詞）
6. Visual reference（請列 1–2 個我可以參考的世界級品牌的設計語言，例如「Linear 2023 介面感、字距較密」）

請輸出可直接複製到 .md 檔的格式。
```

實測案例顯示，進 Design 前產出 300+ 行 markdown 並不誇張，標準是進 Design 前已經知道這套品牌長什麼樣。

> [完整設計規格 markdown 範例請點我](https://docs.google.com/document/d/13XohzifbKVSRo_d0dAj3lRgc7apk0UycpO42IbGeJ_8/edit?tab=t.0)

### 第二步：用 Refero 拉一份「世界級品牌的 DESIGN.md」當參考

到這一步，多數人會卡住：手上沒 Logo、沒設計語言參考。這時候 [Refero Styles](https://styles.refero.design/) 就派上用場。

Refero 是一個設計參考資料庫，可以「依品牌、氛圍、配色、字型或網址」搜尋設計風格。每一個風格頁面都會提供：色彩、字型、間距、組件，以及一份 **`DESIGN.md`** 規格檔，是設計類 AI agent（包含 Claude Design）能直接讀懂的格式。

**操作流程：**

> 1. 在 Refero 首頁瀏覽 Trending／Popular／Newest 三類，或直接以氛圍／配色搜尋（例如 minimal、bold、editorial）。
> 2. 找到一份接近你目標風格的設計，下載它的 `DESIGN.md` 。
> 3. 把 `DESIGN.md` 跟你在第一步寫好的 brand spec markdown 一起，丟進 Claude Design。

但要注意，Refero 的 `DESIGN.md` 是「設計語言的骨架」，不是「品牌商標的複製版」。把它丟進 Claude Design，你拿到的是配色邏輯、字型搭配、間距節奏這類底層規則，而不是直接抄哪個品牌的 Logo。

![Refero Styles](https://image-cdn.learnin.tw/bnextmedia/image/album/2026-05/ev9d-1778148337.png?w=1200&output=webp)

Refero Styles 內提攻的 Design.md 檔，說穿了就是記載設計規範的 markdown 資料，下載下來後，就可以當作參考。

圖／ Claude Design

實作時，建議先把 Refero 的 `DESIGN.md` 改名（避免 Claude Design 讀檔混淆），並在 prompt 裡標明「以這份 `DESIGN.md` 為設計語言基礎，套用到我的品牌規格 \[貼上你的 brand spec\]」。

### 第三步：在 Claude Design 裡建立「設計系統」並輸出簡報

進到 Claude Design 後，第一件事是建立「Design System」（設計系統）。它會吃進你前兩步準備好的 markdown，產出一份 `DESIGN.md` ，作為這個專案後續所有素材（簡報、登陸頁、行動版設計）的規格依據。

這一步是關鍵動作：設計系統一旦鎖定，後續每一個輸出都會落在同一套視覺風格裡。

![完成後的Design System](https://image-cdn.learnin.tw/bnextmedia/image/album/2026-05/4nfj-1778147083.png?w=1200&output=webp)

輸入包括設計規格 markdown、公司logo等資料後，Claude會耗費3~5分鐘生成一套Design System，讓你可以套用在任何生成成品上。

圖／ Claude Design

接著開「Slide deck」模式，逐一上傳：

- 你的品牌 spec markdown（第一步成果）
- Refero 的 `DESIGN.md` （第二步成果）
- 簡報大綱（請自行在 Chat 模式產出）

![簡報製作入口](https://image-cdn.learnin.tw/bnextmedia/image/album/2026-05/a4a1-1778147234.png?w=1200&output=webp)

切換到Slide Deck標籤，並選擇套用指定的Design System，就可以產出特色簡報。

圖／ Claude Design

**一個實務提醒** ：你在第一步寫的 brand spec markdown 跟 Refero 的 `DESIGN.md` 其實可能會打架——尤其 brand spec 寫得愈細，衝突愈明顯（色票、字型、間距各有版本，Claude Design 不知道該聽誰的）。

生成前 **建議先在對話框講清楚優先順序、或指定要參考哪些要素** ，例如「以 Refero 的 `DESIGN.md` 為視覺骨架，我的 brand spec 只取 Mission、Audience、Tone 三項」，或更精準到欄位：「Refero 只取字型搭配與間距節奏，配色一律以我的 brand spec 為準」。把這層前置，比生成完才回頭修，省下更多後續 token。

Claude Design 會用 Opus 4.7 開始生成。生成中如果方向偏了， **馬上停下來** ——讓 Claude Design 朝錯方向跑十分鐘，是最貴的失誤。

### 第四步：用「三個編輯介面」省下大量 token

多數人只用 Claude Design 的 chat 對話框改稿，這是 token 黑洞。Design 其實還有三個介面：

- **Edit 工具** ：直接點擊任何元素改字、改色、改尺寸、改 padding。 **這是最便宜的編輯方式** ，不用打 prompt 描述。
- **Draw 工具** ：在畫面上圈一個區域、留下 comment。Claude 會截圖、看你圈的部分、做動作。適合「這個漸層淡一點」這類非元素性的調整。
- **Tweaks 面板** ：預製好的變化包（封面樣式、背景紋理、強調色、投影片裝飾）。一鍵切換，整個簡報跟著變。

![功能列選項](https://image-cdn.learnin.tw/bnextmedia/image/album/2026-05/8tev-1778148896.png?w=1200&output=webp)

上方工具列的 Tweaks、Comment、Edit、Draw 是簡報調整選項，可用來微調版面與內容、留下修改意見、編輯投影片元素，或直接在畫面上標註重點。

圖／ Claude Design

總之，省 Token 的鐵則只有一條， **能不打 prompt 改的，就不要打 prompt 改。**

另一個省 token 的做法是用 **Opus 4.7** 跑規劃 prompt，調整切到 **Sonnet 4.6** （在對話框的齒輪icon那邊）。在規格清楚的前提下，簡報跟動畫素材在 Sonnet 4.6 上調整品質差異其實不大。

> [檢視範例簡報請點我](https://drive.google.com/file/d/1r7TKXRD26BXN0WliZ082xIM8arRu_Mws/view?usp=sharing)

最後要說的是，工具一字排開誰都能用，差別在於知不知道每個工具的「角色定位」。把 Refero 當設計圖書館，把 Chat 當策略室，把 Claude Design 當執行人；三個工具各司其職，一週限額才有機會撐到下次重置。

> 延伸閱讀： [Codex入門完整教學！10步驟＋提示詞範例，打造你的AI專案工作區](https://www.bnext.com.tw/article/90840/getting-started-with-codex-as-your-ai-work-agent)

資料來源： [@nateherk on X](https://x.com/nateherk/status/2049671370099826725) 、 [Refero Styles](https://styles.refero.design/)

本文初稿為AI編撰，整理．編輯/ 李先泰