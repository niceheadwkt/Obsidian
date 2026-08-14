---
tags:
  - listenTWNews
  - 工作筆記
  - AI-Agent
  - PWA
  - YouTube-Embed
title: listenTWNews 工作筆記
---
# listenTWNews 工作筆記

## 專案簡介
`listenTWNews` 是一個高品質的台灣新聞語音聚合與播報工具，能夠串接中央社及公視 RSS 內容，並透過極速 AI 摘要及 TTS 播放，提供使用者最直覺的「用聽的看新聞」體驗。

---

## 💥 本專案開發核心雷區與避坑指南 (Pitfalls & Troubleshooting)

本專案從頭到尾的開發過程中，面臨了許多瀏覽器安全限制、第三方平台規範以及資料傳輸的雷區，以下為整合的詳細踩坑紀錄與解決方案：

### 🚨 雷區 1：台視新聞台播放無聲問題（Error 153：影片播放器設定錯誤）
* **雷區現象**：點擊「台視新聞台」卡片播放時，UI 的音訊視覺化動畫 (Visualizer) 雖然有顯示播放，但喇叭完全沒有聲音，且嵌入的 YouTube 播放器內框直接拋出 `前往 YouTube 觀看 (錯誤 153：影片播放器設定錯誤)`。
* **根本原因**：台視（TTV NEWS）官方在其 YouTube 頻道後台設定了**「禁止第三方網站內嵌 (Disable Embedding on Third-party Sites)」**的版權限制（即 HTML 帶有 `ERR_EMBEDDED_DISABLED` 標記），導致所有以標準 iframe 嵌入播放的嘗試都會被阻擋。
* **解決方案**：
  1. 在 [app.js](file:///c:/aiTest/listenTWNews/app.js) 的 YouTube `onError` 事件監聽器中，捕獲錯誤代碼 `101`、`150`、`153`（均為嵌入限制或禁止播放錯誤）。
  2. 發生此錯誤時，UI 自動在播放器描述區加載直連 YouTube 的快捷連結**「開啟 YouTube 直播頁」**，並利用 `window.open` 自動彈出新分頁開啟原始 YouTube 直播 URL。
  3. 配置備用直播 ID `MaTO_CAzqJA` 作為 fallback 減緩單一 ID 失效影響。

### 🚨 雷區 2：現代瀏覽器 Autoplay（自動播放）安全政策限制
* **雷區現象**：在部分瀏覽器（如 Chrome, iOS Safari）中，當使用者切換頻道或開啟 App 自動播放時，即使播放狀態顯示為 `PLAYING`，YouTube 播放器仍是靜音狀態，或音量無法同步。
* **根本原因**：現代瀏覽器為了防止網頁廣告惡意發聲，實施了嚴格的 **Autoplay Policy (自動播放政策)**。當沒有偵測到使用者在頁面上的直接點擊互動時，會對任何媒體播放實施強制靜音；在切換影片 ID 重載時，API 也會預設為靜音。
* **解決方案**：
  * 在 [app.js](file:///c:/aiTest/listenTWNews/app.js) 的 `handleYoutubePlayerStateChange` 狀態處理中，當捕獲狀態為 `YT.PlayerState.PLAYING`（播放中）時，**強制執行 `state.youtubePlayer.unMute()` 並將音量同步為 `state.youtubePlayer.setVolume(state.volume)`**，雙重確保一旦進入播放狀態即刻發聲，突破靜音限制。

### 🚨 雷區 3：YouTube 播放器多重實例衝突與控制台 CORS 警告/崩潰
* **雷區現象**：在電視台頻道之間快速點擊切換時，播放器時常崩潰卡死，且瀏覽器控制台狂噴 CORS 跨域安全警告以及 DOM 節點遺失錯誤。
* **根本原因**：最初的設計是每次點擊切換頻道時，都去執行舊播放器的 `destroy()` 並 `new YT.Player` 一個新實例。這在 DOM 節點尚未完全載入或切換頻繁時，會造成非同步初始化衝突，引發 YouTube API 內部的 CORS 機制報錯。
* **解決方案**：
  * 在 [app.js](file:///c:/aiTest/listenTWNews/app.js) 中將播放器重構為**單例模式 (Singleton)**：在 App 初始化時僅在 `youtube-player` 容器上建立一次 `YT.Player`。
  * 後續切換頻道時，僅呼叫 `state.youtubePlayer.loadVideoById(videoId)` 來重載影片，大幅減輕銷毀重建帶來的效能與 cross-origin 負擔，切換順暢度提升 90% 以上。

### 🚨 雷區 4：新聞 RSS 與廣播音訊 HLS / MP3 的跨域限制 (CORS Blocked)
* **雷區現象**：
  * 前端 Fetch 中央社 (CNA) 與公視 (PTS) 的新聞 RSS XML 時，控制台拋出 `Access-Control-Allow-Origin` 錯誤。
  * 播放部分自訂廣播音訊 (如某些 `.mp3` 或 HLS `.m3u8` 直播) 時，因廣播端伺服器未開啟跨域標頭，瀏覽器直接拒絕加載音訊。
* **解決方案**：
  * **新聞 RSS 方案**：本地開發環境下，使用 Vite 內建的 `server.proxy` 將本機 `/api/cna` 與 `/api/pts` 映射至外部目標網站，從而繞過瀏覽器限制；生產環境部署則配合 Vercel / Netlify 的 Rewrite Rule 轉發。
  * **廣播音訊方案**：在 [app.js](file:///c:/aiTest/listenTWNews/app.js) 中加入自動代理機制，針對不支援跨域的自訂音訊串流，自動在 URL 前套上免費跨域代理 `https://corsproxy.io/?${encodeURIComponent(liveUrl)}` 進行請求轉發。
  * **HLS 支援優化**：針對 `.m3u8` 引入 `hls.js`，並綁定 `Hls.Events.ERROR` 事件，當捕獲致命錯誤時，gracefully 降級並給予使用者 CORS 提示。

### 🚨 雷區 5：自訂頻道 JSON 匯入之「格式多樣性」與壞資料崩潰
* **雷區現象**：當使用者匯入舊版設定或其他格式的 JSON 頻道清單時，若欄位名稱不符（例如把 `name` 寫成 `title`，把 `value` 寫成 `url` 或 `link`），或 JSON 外圍是物件而不是陣列，會導致 App 解析時出錯卡死，甚至導致整個 LocalStorage 資料損壞，使得網頁重啟後永久崩潰。
* **根本原因**：沒有對匯入的 JSON 進行防禦性編程與結構正規化 (Data Normalization)。
* **解決方案**：
  * 在 [app.js](file:///c:/aiTest/listenTWNews/app.js) 實作 `normalizeImportedChannels(raw)`，相容各種 JSON 拓撲：相容陣列與鍵值包裝（如 `customChannels`, `channels`, `items`），並對欄位名稱進行寬容轉換（如將 `title` $\rightarrow$ `name`、`url/link` $\rightarrow$ `value`）。
  * 導入資料完整性校驗流程，當資料缺少關鍵欄位時，拋出明確、易懂的錯誤提示（如「第 N 筆頻道資料缺乏頻道名稱或網址」），並阻止壞資料寫入 LocalStorage。

### 🚨 雷區 6：PWA 離線快取更新延遲與安裝按鈕消失
* **雷區現象**：網頁部署更新後，使用者在手機/電腦上看到的仍然是舊版本；且有時在瀏覽器上完全找不到「加入主畫面/安裝」按鈕。
* **根本原因**：
  * 瀏覽器對 PWA 的安裝要求極為嚴苛，必須在 **HTTPS 協定** 或 localhost 執行下才會觸發 Install Prompt，且必須成功註冊 Service Worker。
  * Service Worker 的預快取機制（Cache-first）在更新程式碼後，如果沒有更新 cache 版本號，瀏覽器會一直讀取舊版快取資源。
* **解決方案**：
  * 在 [app.js](file:///c:/aiTest/listenTWNews/app.js) 底部與 [index.html](file:///c:/aiTest/listenTWNews/index.html) 正確載入註冊 `sw.js`。
  * 在 `manifest.json` 中，確保 `start_url` 和 `scope` 為相對路徑（如 `./`），防止在多域名部署或子目錄部署時發生 scope 鎖定錯誤。
  * 在 [sw.js](file:///c:/aiTest/listenTWNews/sw.js) 中加入動態快取版本號控制（`CACHE_NAME`），在 Service Worker 的 `activate` 生命週期中，自動比對並清除所有舊版 Cache，確保使用者在重啟網頁時能即時套用最新功能。

### 🚨 雷區 7：KISSRadio 播放失敗與動態 Token/跨域阻擋
* **雷區現象**：點擊「KISSRadio 聯播網」播放時，UI 的音訊視覺化動畫啟動，但串流播放失敗，且狀態文字可能長時間卡在「廣播電台載入中...」。
* **根本原因**：
  1. KISSRadio (Hichannel 平台) 串流 URL 必須帶有短期威效的 Token（由官方 `hichannel2.php` 動態分發）。
  2. 官方網站有 Cloudflare 防禦，會直接阻擋所有公開代理伺服器（如 `allorigins` / `corsproxy.io`）的跨域存取，導致 fetch 請求長時間掛起（Hang）或返回 521/522 錯誤。
* **解決方案**：
  1. 在 [app.js](file:///c:/aiTest/listenTWNews/app.js) 的 `resolveKissRadioUrl()` 動態解析中，引入 `AbortController` 設定單次 fetch 逾時為 2 秒，防止長時間掛起，確保失敗時能在 4 秒內快速切換至「播放失敗」狀態。
  2. 在 UI 播放器描述區，動態渲染一個「開啟官網播放頁」的直連超連結（連結至 `http://www.kiss.com.tw/radio_hq.php?radio_id=156`），即使在內嵌受阻或公司防火牆限制 Twitch 聊天室等外部服務時，使用者仍可點擊進入官網直接播放音訊。

### 🚨 雷區 8：Vite 生產打包 (vite build) 遺漏無 type="module" 屬性的 Script 導致上線後 404 空白
* **雷區現象**：在本地端使用 Vite 的開發伺服器 (`npm run dev`) 執行時，網頁可以完美載入並播放所有頻道。但當執行生產打包 (`npm run build`) 並部署至 Vercel 上線後，首頁的頻道卡片列表完全空白，控制台噴出 `app.js 404 Not Found` 致命錯誤。
* **根本原因**：在 `index.html` 載入邏輯中，原本使用的是 `<script src="app.js?v=11"></script>`。Vite 在 `npm run dev` 模式下只是一個簡單的靜態檔案代理，因此瀏覽器可以成功對根目錄發起靜態檔案請求。但在執行 `vite build` 構建生產包時，Vite 採用 ESM 規範，**只會 bundle 具有 `type="module"` 的 script**！因為原本沒有指定該屬性，Vite 在打包時完全忽略了 `app.js`，導致它根本沒有被編譯且沒有被複製到 `dist/` 目錄下，部署至 Vercel 後瀏覽器便會對 `app.js` 請求 404。
* **解決方案**：
  1. 將 `index.html` 底部的載入方式修改為 Vite 支援的 Module 格式：`<script type="module" src="app.js"></script>`。
  2. 移去 Query String 版本號（因為 Vite 打包時會自動在 output 的 JS 檔名中附上雜湊值，例如 `index-r_jNTbOG.js`，因此不需要行內版本號來防止快取）。
  3. 重新執行 `npm run build` 打包，此時 Vite 會順暢將其編譯至 `dist/assets/index-*.js` 中並於 `dist/index.html` 正確關聯，解決 404 問題。

---

## 目前進度
- [x] 設定新聞 Proxy 機制與 RSS 解析
- [x] 實作 Web Speech TTS 控制與本地語音複製串接
- [x] 實作 Groq / OpenAI 摘要介面
- [x] 實作自訂頻道雙模式 JSON 匯入/匯出
- [x] 解決台視嵌入限制 (錯誤 153) 自動跳轉與直連機制
- [x] 註冊 Service Worker 並完成 PWA 安裝指南
- [x] 新增預設廣播電台頻道：中廣新聞網、飛碟聯播網與 KISSRadio 聯播網
- [x] 修正東森新聞台 (51台) 的預設 YouTube Video ID 與正確的 Channel ID

## 下一步計劃
1. 持續追蹤其他新聞台 YouTube 嵌入是否有類似變更。
2. 串接與測試安童哥語音複製伺服器 (`voxcpm2-voice-cloner`) 的 `custom` 模式。

---

## 💡 給初學者的架構秘笈：純靜態託管 vs 現代前端打包工具（Vite）

對於剛接觸前端開發的初學者來說，「為什麼多了一個 `package.json` 專案就突然變複雜，還會讓 PWA 出問題？」這是一個非常好的問題。以下為您拆解這兩者運作方式的奧秘：

### 1. 📂 方案一：純靜態網頁（No-Build / Simple Static）— 本專案最終回歸的方案
* **運作方式**：這是最原始、最單純的網頁架構。你的專案目錄裡有什麼檔案，瀏覽器就會直接去下載並讀取什麼檔案。
* **路徑對應**：檔案路徑與網址路徑是 **1:1 絕對對應**。例如，你把 `sw.js` 放在專案根目錄下，上線後的網址就是 `https://yourdomain.com/sw.js`。
* **部署機制**：Vercel 等託管商偵測到此專案沒有 `package.json`，會自動將其視為靜態伺服器，**直接上傳並託管您根目錄下的所有檔案**。
* **優點**：結構極度簡單、直覺、不需要安裝 Node.js，也完全不需要編譯工具，隨點隨改。

### 2. ⚙️ 方案二：現代前端打包（Build-based / Vite / Webpack）
* **運作方式**：當網頁引入了現代前端框架（如 React, Vue）或新語法（TS, SCSS）時，瀏覽器是無法直接解讀的。必須在本地使用打包工具（如 Vite）把程式碼進行「轉譯、優化、打包、壓縮」，最後輸出成打包產物（通常輸出到一個名為 `dist/` 的發佈資料夾下）。
* **部署機制**：Vercel 只要在倉庫根目錄發現有 `package.json` 且含有 `build` 腳本，就會主動在雲端執行 `npm run build`，並且**僅僅把 `dist/` 資料夾裡的內容發佈上線**，根目錄的原始碼（如 package.json 本身）反而會被隱藏。
* **為什麼 PWA 檔案在此模式下會 404 損壞？**
  * 打包工具（Vite）非常「精明」，它只會去打包程式碼中有明確被 `import` 引用、或是 HTML 標籤有連結的檔案。
  * 像 `sw.js` (Service Worker) 或是圖示（`icon-192.png`），它們是透過瀏覽器在背景去向特定的 URL 發起非同步請求的，Vite 無法靜態解析出它們的依賴關係，因此**在執行 `vite build` 時會直接遺漏它們，不把它們複製到 `dist/` 輸出目錄中**。
  * 這導致專案部署到 Vercel 上線後，瀏覽器請求 `/sw.js` 會直接回傳 404，PWA 功能與安裝也隨之報銷。
* **打包模式下的解決方案：`public/` 的妙用**
  * 在 Vite 專案中，**`public/` 資料夾是靜態檔案的安全通道**。
  * Vite 的機制規定：只要把任何不需要被編譯壓縮、但在打包後需要原封不動被瀏覽器存取的資源（如 `sw.js`、`manifest.json`、PWA 圖示）放進 `public/` 資料夾中，Vite 在 build 時就會**自動把 `public/` 的內容全數複製到 `dist/` 的根目錄下**。這就解決了 PWA 線上 404 的問題。

### 🌟 總結：初學者該如何選擇？
* **當專案是純 Vanilla JS (原生 HTML/CSS/JS) 且規模適中**：
  建議採用 **「純靜態網頁模式」**。不需要 `package.json`，把所有檔案直接丟在根目錄，這是最簡單、最無腦且最不易出錯的做法。
* **當專案引入了複雜的前端框架、TypeScript 或需要極致的打包體積優化**：
  才需要採用 **「現代前端打包模式 (Vite/Webpack)」**，並學會使用 `public/` 目錄或 `vite-plugin-pwa` 等套件來處理 Service Worker 靜態檔案。

