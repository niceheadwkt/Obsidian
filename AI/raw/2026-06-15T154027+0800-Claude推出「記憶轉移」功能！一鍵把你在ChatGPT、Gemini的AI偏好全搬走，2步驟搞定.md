---
title: "Claude推出「記憶轉移」功能！一鍵把你在ChatGPT、Gemini的AI偏好全搬走，2步驟搞定"
source: "https://www.bnext.com.tw/article/90203/claude-switch-to-claude-without-starting-over"
author:
  - "[[數位時代 BusinessNext]]"
published: 2026-03-03
created: 2026-06-15
description: "Anthropic推出記憶匯入功能，讓用戶可一鍵將ChatGPT、Google Gemini等平臺的個人偏好與對話記憶轉移至Claude。"
tags:
  - "clippings"
---
[![免費報名觀展 🌟](https://bnextmedia.s3.hicloud.net.tw/pumpkin/image/photo/2026-05/img-1777882923-82452.gif)](https://eventgo.bnextmedia.com.tw/event/detail/e87238u69ae91f1cf750?utm_campaign=2026AITWEM&utm_source=web_bn&utm_medium=logo_banner&utm_content=162601&utm_term=channel_all)

2026.03.03 | [AI與大數據](https://www.bnext.com.tw/categories/ai)

Anthropic推出記憶匯入功能，讓用戶可一鍵將ChatGPT、Google Gemini等平臺的個人偏好與對話記憶轉移至Claude。

[＃Claude](https://www.bnext.com.tw/tags/Claude)

---

對長期使用AI的用戶來說，換平臺最大的障礙，就是得重新調教新的AI，像是習慣、寫作風格、進行中的專案，全都要從頭來過。

Anthropic 近日推出「Switch to Claude」的記憶匯入功能，這項功能瞄準目前在多個 AI 平臺之間游移的用戶，試圖降低轉換門檻，讓原本使用 ChatGPT、Google Gemini 或 Microsoft Copilot 的用戶，能夠透過單次複製貼上的動作，將過去累積的使用習慣與對話脈絡無痛轉移至 Claude，省去重新設定的繁瑣過程。

## 記憶轉移怎麼做？2步驟教你完成

首先，要使用記憶轉移功能前，須匯出舊平臺資料，Anthropic 官方提供了匯入至Claude的專用提示詞，2個步驟就能完成轉移：

掌握最新AI、半導體、數位趨勢！訂閱《數位時代》日報及社群活動訊息

### 步驟1

在Chatgpt、Gemini等現有的 AI 平臺對話中，輸入 Anthropic 提供的專用提示詞（下方表格），要求 AI 彙整出個人偏好與使用背景。

| 專用提示詞（中文） | 專用提示詞（英文） |
| --- | --- |
| 我要轉移到其他服務了，需要匯出我的資料。請列出你儲存的所有關於我的記憶，以及你從過去對話中學到關於我的任何背景資訊。請將所有內容輸出在單一個程式碼區塊（code block）中，以便我複製。   每個項目的格式請設定為：\[儲存日期（如果有的話）\] - 記憶內容。   請務必涵蓋以下所有內容——並盡可能一字不漏地保留我的原話：   \- 我給過你關於如何回應的指示（語氣、格式、風格、「總是做 X」、「絕不做 Y」）。   \- 個人詳細資訊：姓名、所在地、工作、家庭、興趣。   \- 專案、目標與經常討論的話題。   \- 我使用的工具、程式語言和框架。   \- 我對你的行為所設定的偏好與糾正紀錄。   \- 其他未包含在上述項目中，但已儲存的背景資訊。   請勿對任何項目進行總結、分類或省略。在程式碼區塊之後，請向我確認這是否為完整的資料，還是還有任何未列出的項目。 | I'm moving to another service and need to export my data. List every memory you have stored about me, as well as any context you've learned about me from past conversations. Output everything in a single code block so I can easily copy it. Format each entry as: \[date saved, if available\] - memory content. Make sure to cover all of the following — preserve my words verbatim where possible:   \- Instructions I've given you about how to respond (tone, format, style, 'always do X', 'never do Y').   \- Personal details: name, location, job, family, interests. Projects, goals, and recurring topics.   \- Tools, languages, and frameworks I use.   \- Preferences and corrections I've made to your behavior.   \- Any other stored context not covered above.   Do not summarize, group, or omit any entries. After the code block, confirm whether that is the complete set or if any remain. |

此時建議先將輸出內容貼入文字編輯器人工微調，刪去不想保留的條目，每筆記憶均以獨立文字段落儲存方便篩選，再將整理好的內容貼回Claude。

### 步驟2

進入Claude「設定 → 隱私權」，將生成的內容直接貼入「記憶設定」頁面（如下圖），系統便會自動解析並更新記憶，讓 Claude 能夠「從上次停下的地方繼續」。整個過程無需技術背景，一般用戶可自行完成。

要確認是否匯入成功，可開啟新對話詢問Claude「你對我有哪些瞭解？」即可驗證。

日後若想清除記憶，可至記憶設定頁面手動刪除，或直接在對話中告知Claude移除所有已儲存的記憶，AI會立即執行。

![claude memory功能](https://image-cdn.learnin.tw/bnextmedia/image/album/2026-03/sp53-1772530009.jpg?w=1200&output=webp)

圖／ claude

除了上述轉移方式，根據外媒Techcrunch報導，以 ChatGPT 為例，還有三種匯出舊數據方法可選擇，再貼到 Claude記憶設定中：

### 方法一

進入ChatGPT的「設定 → 個人化 → 記憶 → 管理」，檢視儲存的記憶並更新已儲存的偏好設定，確認無誤後複製需要保留的內容。

### 方法二

透過「設定 → 資料控管 → 匯出資料」匯出完整對話紀錄，ChatGPT會將聊天記錄整理成文字或JSON檔案並以電子郵件寄出，資料量龐大時可能需要等待較長時間。

### 方法三

以手動方式複製重要對話，或直接請ChatGPT摘要整理你的主要偏好、常討論的主題及自訂指令。

## 記憶轉移免費開放，打破生態鎖定

值得注意的是，「Switch to Claude」功能必須搭配 Claude 的記憶功能才可運作，過去僅限付費方案（Pro、Max、Team、Enterprise）使用，Anthropic則在3月2日宣佈，記憶功能正式向免費方案用戶開放，所有人都能免費搬家。

此次免費解鎖，被外界解讀為Anthropic刻意降低「轉換成本」的策略，不需要花一毛錢，任何人都能帶著在ChatGPT或Gemini的使用偏好，直接無痛遷移至Claude。

資料來源： [Techcrunch](https://techcrunch.com/2026/03/02/users-are-ditching-chatgpt-for-claude-heres-how-to-make-the-switch/) 、 [ZDNET](https://www.zdnet.com/article/claude-sonnet-4-6-delivers-frontier-level-ai-for-free-and-cheap-seat-users/) 、 [9to5Mac](https://9to5mac.com/2026/03/02/free-claude-users-can-now-use-memory-and-import-context-from-rivals/)

關鍵字： [＃Claude](https://www.bnext.com.tw/tags/Claude)

往下滑看下一篇文章

即時熱門文章

[1 2026世足賽哪裡看？臺灣轉播平臺、賽程表、分組名單懶人包](https://www.bnext.com.tw/article/91241/2026-fifa-world-cup-taiwan) [2 宏碁賣行李箱被當「電腦贈品」！3年後淨利衝1770萬元，離PC最遠的生意反成獨立公司](https://www.bnext.com.tw/article/91217/acer-lifestyle-luggage-success-strategy) [3 博客來副總何禮旭宣佈離職！她如何3年讓單季虧741萬的博客來，翻出連3年獲利？](https://www.bnext.com.tw/article/91233/books-store-boolstore-dreamplaza) [4 ChatGPT指令大全！70組提示詞一次整理，復古膠片朦朧風、生日海報、簡報封面全搞定](https://www.bnext.com.tw/article/90908/chatgpt-image-2-prompt-guide-complete) [5 Computex 大展臺灣科技實力，看圓剛、TRYX、Silicon Power 如何透過亞馬遜佈局全球市場？](https://www.bnext.com.tw/article/91208/amazon_computex_2026) [6 Claude Code Skill怎麼寫、SKILL.md放什麼？Anthropic官方揭9大實戰用法](https://www.bnext.com.tw/article/91235/build-effective-claude-code-skills-with-folders-gotchas-and-9-types)

![Computex 大展臺灣科技實力，看圓剛、TRYX、Silicon Power 如何透過亞馬遜佈局全球市場？](https://image-cdn.learnin.tw/bnextmedia/image/album/2026-06/p6ci-1780997559.jpg?w=900&output=webp)

2026.06.09 | [商業經營](https://www.bnext.com.tw/categories/management)

Computex 大展臺灣科技實力，看圓剛、TRYX、Silicon Power 如何透過亞馬遜佈局全球市場？

臺灣經濟持續成長，靠的不只是半導體、晶片代工等科技巨頭，更有一群臺灣科技電子品牌，正利用亞馬遜全球開店，打破實體通路的壁壘，在世界舞臺發光發熱。

---

分享

2026年，臺北國際電腦展（Computex）再度引爆全球科技熱潮，來自世界各地的業者、買家與媒體蜂擁而至，讓臺北成為最受矚目的世界科技中心。

在這場盛會背後，除了有大眾熟悉的半導體、晶片代工等產業巨頭 ，還有一群具深厚底蘊的臺灣科技品牌，早已利用亞馬遜全球開店，跨越線下通路的傳統壁壘。例如：用一套影音設備點燃創作者經濟的圓剛、以散熱器重新定義電競美學的TRYX，以及提供完整的記憶卡方案陪伴全球用戶記錄每個珍貴瞬間的廣穎電通，逐步以產品征服全球市場。

## 進軍跨境電商市場，圓剛精準觸及數位原生客群

對許多造訪寶島的旅客來說，圓剛科技（AVerMedia）是踏入國門遇到的第一個臺灣品牌，「不管在桃園、松山、臺中、高雄機場，旅客通關時抬頭看的那顆鏡頭，就是圓剛產品。」資深處長Betty Kuo透露，圓剛成立36年來對品質有著近乎「龜毛」的堅持，要求研發、製造都要留在臺灣，深信企業有著不容妥協的使命與社會責任。

這份硬實力也充分展現在今年的Computex。圓剛除了展示影音擷取本業，還秀出攜手Nvidia耕耘多年的邊緣運算（Edge AI）量能，利用AI晶片打造能辨識車流的智慧紅綠燈、救護車優先通行等智慧城市基礎建設和服務。

![amazon_2.jpg](https://image-cdn.learnin.tw/bnextmedia/image/album/2026-06/guiw-1780997559.jpg?w=1200&output=webp)

圓剛攜手Nvidia，利用AI晶片打造能辨識車流的智慧紅綠燈，可以判別讓救護車優先通行或是依據交通狀況調節秒數，為智慧城市提供更多可能。

圖／ 數位時代

在深耕線下B2B的大型基礎建設之餘，面對線上B2C的消費市場，圓剛同樣具備精準洞察。近年隨著創作者經濟爆發，圓剛發現，自家產品的主力客群，多為千禧世代、Z世代等相當依賴線上消費的數位原生族群。看準亞馬遜的高觸及和曝光率，圓剛決定透過亞馬遜全球開店，進軍跨境電商市場，「當企業進軍陌生的海外市場，亞馬遜的物流系統、商機探測器等工具，能大幅降低進入門檻。」Betty Kuo說。

事實上，圓剛就是將各項工具用到極致的最佳案例。圓剛科技課長Jimmy Liu舉例，團隊在線下展會發現美國玩家對「寶可夢卡牌」二手交易、拆卡直播的熱潮後，便立刻回到亞馬遜賣家後臺，透過數據交叉驗證需求，接著迅速重新包裝一款能同時拍攝玩家臉部表情、卡牌等細節的雙鏡頭攝影機，結果一上線便被搶購一空。又或者是圓剛直接將消費者購物後留下的評論，視為內部研發的重要KPI，Betty透露，如果新產品的評價掉到4.2顆星以下，就會被團隊視為「大事」，立即啟動跨部門檢討，徹查問題，「那些最真實的回饋，其實正是我們研發、創新的來源之一。」

憑藉著出色的研發、製造實力，再搭配亞馬遜的後臺數據、多元工具，2025年Prime Day，圓剛創下年增長59％的佳績；2026年第一季，即便競爭對手狂砸行銷預算，圓剛依然靠著產品硬實力和精準的高階產品定位，寫下年增長6％的成績。

![amazon_3.jpg](https://image-cdn.learnin.tw/bnextmedia/image/album/2026-06/dg79-1780997560.jpg?w=1200&output=webp)

圓剛科技透過亞馬遜後臺數據與線下展會洞察，敏銳捕捉到玩家對「寶可夢卡牌」拆卡直播的熱潮，迅速推出能同時拍攝玩家臉部表情與卡牌細節的雙鏡頭攝影機（Dual-View Live Streaming），一上線即被搶購一空。

圖／ 數位時代

## TRYX 注入創新靈魂，將散熱器化身藝術品

有別於圓剛身處的多媒體視訊產業，電腦零組件（PC DIY）市場早已是一片紅海、競爭激烈，也因此，新銳品牌TRYX的崛起，顯得格外引人注目。

![amazon_4.jpg](https://image-cdn.learnin.tw/bnextmedia/image/album/2026-06/kwvc-1780997560.jpg?w=1200&output=webp)

TRYX全球電商營運負責人Paso分享品牌如何憑藉來自亞馬遜的數據洞察，精準預判市場狀況與玩家痛點，成功將具備美學與科技感的裸眼 3D 水冷散熱產品推向全球市場。圖為本次重量級新品「HOLO全息視覺顯示水冷散熱器」，利用佩珀爾幻象（Pepper’s Ghost），將GIF動畫、短影音直接投射在散熱器上。

圖／ 數位時代

TRYX創辦人Nelson認為，電腦零組件市場長年深陷價格、效能戰，讓許多品牌失去「創新的靈魂」。但機會就藏在痛點中，為了改善市場現況，Nelson先是融合了設計、美學和頂尖技術，打造出全球第一款裸眼3D水冷散熱器PANORAMA、融入家居布面設計的FLOVA機箱等代表性產品；今年Computex中，TRYX再端出重量級新品「HOLO全息視覺顯示水冷散熱器」，是利用佩珀爾幻象（Pepper’s Ghost），將GIF動畫、短影音直接投射在散熱器上，並和圖庫平臺GIPHY合作，讓玩家能無限擴充素材，將冰冷的硬體化做藝術品。

有趣的是，這份創新並非憑空想像，而是來自亞馬遜的數據洞察。TRYX全球電商營運負責人Paso指出，TRYX採用了亞馬遜的「選品指南針」（Product Opportunity Explorer），「這就像我們的『市場雷達』。過去團隊決策可能只憑感覺，現在透過細分類目的銷售數據和趨勢，團隊能精準預判市場狀況，讓供應鏈更穩、現金流更健康。」

而「VINE評論工具」則是TRYX的「信任放大器」。團隊會邀請評測者，針對新品發表影片、照片與專業分析等回饋，這對整合了抗反光塗層、克服曲率折射等複雜工程技術的3D水冷散熱器來說，無疑是最具說服力的評價。

2024年，TRYX首度在亞馬遜上架高單價的螢幕水冷散熱器時，原先預估一天只能賣個3到5臺，沒想到美國市場強大的購買力，加上團隊善用亞馬遜的各項工具拆解數據，讓單日銷量直接飆破20臺；而TRYX進軍亞馬遜後僅1年，品牌營收便達到197％的成長，「亞馬遜的多站點優勢，讓我們只要專心把產品做好，就能在全世界找到最適合的市場！」Paso透露，接下來，TRYX預計再進軍德國、法國、英國等歐洲市場和亞太地區，「我們希望讓更多玩家，體驗到TRYX的創新精神。」

![amazon_5.jpg](https://image-cdn.learnin.tw/bnextmedia/image/album/2026-06/4fga-1780997559.jpg?w=1200&output=webp)

新銳品牌 TRYX 顛覆傳統電腦零組件市場，結合設計、美學與頂尖技術，將冰冷的硬體化做藝術品，為玩家帶來無限的視覺擴充體驗。

圖／ 數位時代

## Silicon Power 建立即時地區化策略，開拓 B2B 商機

全球記憶體領導品牌Silicon Power看準線上通路的潛力，並為了貫徹「國際化品牌」的定位，將亞馬遜全球開店視為品牌跨境的關鍵，「Silicon Power每進入一個新市場，亞馬遜都是我們優先考量的線上通路選擇，因為它能迅速幫助我們建立品牌曝光和銷售體系。」Silicon Power Sales Deputy Manager Benson指出，透過亞馬遜賣家中心（Amazon Seller Central），採靈活的「地區化策略」，針對當地消費者習慣、法規稅務，即時調整價格和庫存。

![amazon_6.jpg](https://image-cdn.learnin.tw/bnextmedia/image/album/2026-06/9ark-1780997560.jpg?w=1200&output=webp)

看準線上通路潛力，Silicon Power將亞馬遜全球開店視為品牌跨境的關鍵，透過靈活的「地區化策略」即時調整價格與庫存，更運用 Amazon Business 功能敲開全球企業級 B2B 市場的大門。圖為Silicon Power 銷售副理 Benson（左）與董事長陳慧民（右）於 Computex 展位合影。

圖／ 數位時代

在行銷上，Silicon Power則善用亞馬遜廣告（Amazon ADs），精準設定投放目標、掌握搜尋趨勢。更重要的是，亞馬遜的「Amazon Business」功能，讓Silicon Power的醫院、教育機構等企業用戶，能以批量採購方式下單，等於敲開了B2B市場的大門，「這是一個關鍵轉折，因為我們不再只服務個人消費者，也能為企業客戶提供企業級需求的記憶體解決方案。」

正因從亞馬遜獲得了全方位數據，Silicon Power利用這份對消費者的理解，在今年的Computex中，跳脫了「單一產品框架」的思維，首度展出專為創作者打造的「CreatePro 系列」。團隊不盲目模仿競品，而是精準切入內容創作者的工作流程，將需求拆分為錄影、後製、備份、長期保存等四個階段，並為每個階段提供完整對應的儲存方案，「不是競爭者做什麼，我們就去做什麼，我們還是會利用從亞馬遜等平臺獲得的數據，回到消費者需求，完整提供產品的解決方案。」Benson笑稱，如今，團隊已將「亞馬遜賣家學習中心」視為內部的成長基地，同仁會搭配亞馬遜的建議、策略，持續升級自身戰力。

![amazon_7.jpg](https://image-cdn.learnin.tw/bnextmedia/image/album/2026-06/g3m1-1780997560.jpg?w=1200&output=webp)

廣穎電通跳脫單一產品框架，利用從亞馬遜等平臺獲得的全方位數據回到消費者需求，精準切入內容創作者的工作流程，完整提供相對應的儲存方案。

圖／ 數位時代

對圓剛、TRYX和Silicon Power來說，在這場跨境出海的戰役中，亞馬遜不僅是銷售貨物的通路，更扮演了品牌向全球拓展的「加速」角色。從前期透過商機探測器，進行市場洞察、需求驗證，進而預判趨勢、調整選品、開發新品；到中期藉由真實的消費者評論和成熟的廣告系統，快速累積海外信任度、建立品牌；最後再利用強大的FBA物流網絡和多站點優勢，將臺灣的創新產品遞送至全球，正是亞馬遜被視為出口跨境關鍵的原因。

從三家品牌的成功軌跡，可以看出科技產業的全球化趨勢，已從過去的「硬體代工製造」，邁向「數據驅動品牌」的階段。無論是哪一種產業，品牌只要專心將產品做到極致，搭配亞馬遜全球開店提供的成長與加速服務等，就能在全球找到最適合的市場，讓世界看見臺灣的創新能量。

[立即下載＿亞馬遜 2026 消費性電子品類攻略手冊｜掌握下一波成長動能](https://www.surveycake.com/s/0A8B9)

[![amazon-8.png](https://image-cdn.learnin.tw/bnextmedia/image/album/2026-05/gqmt-1778478314.png?w=1200&output=webp)](https://www.surveycake.com/s/0A8B9)

圖／ Amazon

即時熱門文章

[1 2026世足賽哪裡看？臺灣轉播平臺、賽程表、分組名單懶人包](https://www.bnext.com.tw/article/91241/2026-fifa-world-cup-taiwan) [2 宏碁賣行李箱被當「電腦贈品」！3年後淨利衝1770萬元，離PC最遠的生意反成獨立公司](https://www.bnext.com.tw/article/91217/acer-lifestyle-luggage-success-strategy) [3 博客來副總何禮旭宣佈離職！她如何3年讓單季虧741萬的博客來，翻出連3年獲利？](https://www.bnext.com.tw/article/91233/books-store-boolstore-dreamplaza) [4 ChatGPT指令大全！70組提示詞一次整理，復古膠片朦朧風、生日海報、簡報封面全搞定](https://www.bnext.com.tw/article/90908/chatgpt-image-2-prompt-guide-complete) [5 Computex 大展臺灣科技實力，看圓剛、TRYX、Silicon Power 如何透過亞馬遜佈局全球市場？](https://www.bnext.com.tw/article/91208/amazon_computex_2026) [6 Claude Code Skill怎麼寫、SKILL.md放什麼？Anthropic官方揭9大實戰用法](https://www.bnext.com.tw/article/91235/build-effective-claude-code-skills-with-folders-gotchas-and-9-types)

[![代理式商務連動百兆商機](https://image-cdn.learnin.tw/bnextmedia/image/album/2026-05/8e6m-1779880883.jpg?w=600&output=webp)](https://www.bnext.com.tw/magazine/view/130167)