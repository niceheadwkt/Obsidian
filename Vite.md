**Vite**（法文原意為「快速」，讀音類似 `/veet/`）是由 Vue.js 創辦人尤雨溪（Evan You）開發的**新一代前端開發與打包工具**。

它旨在解決傳統打包工具（如 Webpack、Parcel）在大型專案中**啟動極慢**與**熱模組替換（HMR）延遲**的問題。

## 核心優勢與運作機制

### 1. 開發環境（Dev Server）極速啟動

- **原生 ES 模組（Native ESM）：** 開發時不需要將所有程式碼預先打包。瀏覽器會直接請求 ES 模組，Vite 僅需依需求處理並提供該頁面需要的檔案，實現秒級啟動。
    
- **Go 語言預構建：** 使用以 Go 寫成的 **esbuild** 來預打包第三方套件（node_modules），速度比 JavaScript 撰寫的打包器快 10 至 100 倍。
    

### 2. 閃電般的熱模組替換（HMR）

修改程式碼時，無論專案多大，Vite 都能維持極快更新，因為它讓瀏覽器僅重新請求改變的模組，不會重新編譯整個 bundles。

### 3. 生產環境打包（Production Build）

打包時內建使用 **Rollup**，提供高度優化的代碼分割（Code Splitting）、Tree-shaking 及靜態資源處理，確保部署的最佳效能。

## Vite 與 Webpack 對比

|**特性**|**Vite**|**傳統 Webpack**|
|---|---|---|
|**開發啟動方式**|原生 ESM + 需求載入|先完整打包才啟動 Server|
|**冷啟動速度**|毫秒～秒級 (毫無察覺)|數十秒甚至數分鐘|
|**預建構工具**|esbuild (Go)|JS-based 工具|
|**生態系與配置**|開箱即用、配置極簡|設定較為繁複 (需配置眾多 Loader/Plugin)|

## 快速開始

你可以使用 npm 或 pnpm 在幾秒鐘內建立全新的前端專案（支援 Vue、React、Svelte、Vanilla JS 等）：

Bash

```
# 使用 npm 建立專案
npm create vite@latest my-app

# 進入專案目錄並安裝套件
cd my-app
npm install

# 啟動開發伺服器
npm run dev
```

---
## Vite 的外掛機制與 vite.config.js 常用配置項目。

Vite 的強大之處在於其**基於 Rollup 擴充的外掛生態系**以及**極簡且靈活的配置系統**。

## 一、 Vite 的外掛（Plugin）機制

Vite 的外掛介面高度相容於 **Rollup**，這代表大部分現成的 Rollup 外掛可以直接在 Vite 中無縫使用。此外，Vite 還額外提供了專屬的鉤子（Hooks），用於控制開發伺服器與 HMR 行為。

### 1. 外掛生命週期鉤子（Plugin Hooks）

外掛本質上是一個回傳特定物件的函式，主要包含以下三類鉤子：

- **Rollup 相通鉤子（開發與打包皆適用）：**
    
    - `resolveId`：自訂模組解析邏輯（如處理虛擬模組或特殊路徑）。
        
    - `load`：自訂模組載入方式（例如從記憶體或網路讀取）。
        
    - `transform`：轉換模組內容（例如將 TypeScript/JSX/Sass 轉譯成 JS/CSS）。
        
- **Vite 獨有鉤子（Vite-specific Hooks）：**
    
    - `config`：在解析 Vite 配置之前修改配置。
        
    - `configResolved`：讀取解析後的最終 Vite 配置。
        
    - `configureServer`：自訂開發伺服器（Dev Server），可用於加入 Connect/Express 中間件（Middleware）。
        
    - `transformIndexHtml`：動態修改 `index.html`（例如注入 `<script>` 或 `<meta>`）。
        
    - `handleHotUpdate`：自訂熱模組替換（HMR）的更新處理邏輯。
        

### 2. 外掛控制參數 (`enforce` 與 `apply`)

你可以透過外掛物件的屬性，精細控制外掛的執行順序與環境：

JavaScript

```
function myPlugin() {
  return {
    name: 'my-custom-plugin',
    // 執行順序：'pre' (在 Vite 核心外掛前執行) 或 'post' (在 Vite 建構外掛後執行)
    enforce: 'pre',
    // 適用環境：'serve' (僅開發環境) 或 'build' (僅生產打包)
    apply: 'serve',
    transform(code, id) {

      return code;
    }
  }
}
```

## 二、 `vite.config.js` 常用配置範例與解析

以下是一個涵蓋實務開發中最常用功能的 `vite.config.js` 設定檔範例：

JavaScript

```
import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue'; // 或 @vitejs/plugin-react
import path from 'path';

export default defineConfig({
  // 1. 專案基礎路徑 (預設 '/'，若部署在子路徑如 '/my-app/' 需更改)
  base: '/',

  // 2. 外掛配置
  plugins: [
    vue(),
  ],

  // 3. 路徑解析與別名
  resolve: {
    alias: {
      // 將 '@' 指向 'src' 目錄
      '@': path.resolve(__dirname, './src'),
    },
    // 允許省略副檔名（不建議省略太多，以免影響解析效能）
    extensions: ['.mjs', '.js', '.ts', '.jsx', '.tsx', '.json'],
  },

  // 4. 開發伺服器設定 (Dev Server)
  server: {
    host: '0.0.0.0', // 允許外部 IP 連線 (如用手機測試)
    port: 3000,       // 指定開發 Server 埠號
    open: true,       // 啟動時自動開啟瀏覽器
    cors: true,       // 允許跨域
    
    // API 代理設定 (解決開發時跨域 CORS 問題)
    proxy: {
      '/api': {
        target: 'https://api.example.com', // 目標後端伺服器
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, ''), // 去除 /api 前綴
      },
    },
  },

  // 5. 生產環境打包設定 (Build)
  build: {
    outDir: 'dist',        // 打包輸出目錄
    assetsDir: 'assets',    // 靜態資源存放子目錄
    sourcemap: false,       // 是否產生 Source Map (線上除錯用，正式環境建議關閉)
    chunkSizeWarningLimit: 1500, // 檔案過大警告門檻 (KB)
    
    // 底層 Rollup 細節設定
    rollupOptions: {
      output: {
        // 自訂第三方庫拆包策略 (Code Splitting)
        manualChunks: {
          vendor: ['vue', 'vue-router', 'pinia'], // 將核心套件獨立打包成 vendor.js
        },
      },
    },
  },

  // 6. CSS 預處理器全域設定
  css: {
    preprocessorOptions: {
      scss: {
        // 自動在每個 SCSS 檔案開頭引入全域變數檔
        additionalData: `@import "@/assets/styles/variables.scss";`,
      },
    },
  },

  // 7. 全域替換常數
  define: {
    __APP_VERSION__: JSON.stringify('1.0.0'),
  },
});
```