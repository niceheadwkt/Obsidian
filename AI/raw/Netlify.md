**Netlify** 是一個非常受歡迎的**雲端網頁代管與自動化部署平台**，專門為現代網頁開發（特別是 Jamstack 架構、靜態網站以及前端框架）而設計。它讓開發者可以非常輕鬆地將程式碼從 GitHub、GitLab 等平台，直接變成線上的網站。

簡單來說，它可以幫你處理網站「從寫好程式碼到讓全世界看到」之間的所有繁雜步驟。

## 核心功能與優勢

- **Git 自動化部署 (Continuous Deployment):** 只要你將程式碼推（Push）到 GitHub、GitLab 或 Bitbucket，Netlify 就會自動偵測、抓取最新程式碼、進行建置（Build），並在幾秒鐘內更新線上網站。
    
- **免費的 SSL 憑證:** 一鍵就能為你的自訂網域啟用 `https://` 加密，而且完全免費。
    
- **全球 CDN 加速:** Netlify 會自動將你的網站分發到全球的內容傳遞網路（CDN），確保不論使用者的地理位置在哪，網站載入速度都極快。
    
- **分支預覽 (Deploy Previews):** 當你發出 Pull Request (PR) 時，Netlify 會自動為該分支生成一個專屬的臨時網址，讓你和團隊在合併程式碼前先預覽畫面是否正確。
    
- **Serverless Functions (無伺服器函式):** 雖然它是代管靜態網站起家，但你也可以輕鬆寫幾行 JavaScript/TypeScript 丟給它，它會自動幫你部署成後端的 API 端點。
    
- **表單處理 (Forms) 與身分驗證 (Identity):** 內建簡單的表單收集功能，你的聯絡表單不需額外寫後端程式碼就能收信；同時也提供基礎的主辦方會員登入系統。
    

## 適合用 Netlify 部署什麼？

Netlify 是以下技術應用的絕佳舞台：

- **靜態網站產生器 (SSG):** Gatsby, Hugo, Jekyll, Astro, Eleventy 等。
    
- **現代前端框架:** React (Vite/CRA), Vue, Angular, Svelte 等。
    
- **混合型 SSR 框架 (部分支援):** Next.js, Nuxt.js 等（雖然它們在 Vercel 支援度更高，但 Netlify 同樣支援）。
    
- **個人作品集、部落格、活動登陸頁 (Landing Page)。**
    

## 基本運作流程

1. **開發:** 在本機端寫網頁程式碼。
    
2. **推送:** 將程式碼 `git push` 到 GitHub。
    
3. **觸發:** Netlify 收到通知，自動開始編譯。
    
4. **上線:** 編譯完成，網站自動分發到 CDN，即刻上線。
    

對於個人開發者或小型團隊來說，Netlify 的免費方案（Free Tier）非常大方，提供了充足的每月的建置時間與流量，是目前前端開發者幾乎必備的工具之一。

請問你是正打算用 Netlify 部署你的網站，想了解具體的操作步驟，還是想將它與其他平台（如 Vercel、GitHub Pages）做比較呢？