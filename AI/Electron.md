**Electron** 是一個由 GitHub 開發的開源框架，它允許開發者使用 Web 前端技術（**HTML、CSS 和 JavaScript**）來建構跨平台的**桌面應用程式**。

簡單來說，它可以讓你用寫網頁的技術，做出在 Windows、macOS 和 Linux 上執行的安裝軟體。

## 核心架構：它是如何運作的？

Electron 的核心結構本質上是將兩個強大的技術結合在一起：

1. **Chromium（Google Chrome 的核心）**：負責渲染網頁介面，這讓開發者可以用極其豐富的 Web 生態系統來設計 UI。
    
2. **Node.js**：負責底層作業系統的互動（例如：檔案系統讀寫、執行本機指令等），突破了傳統瀏覽器沙盒的限制。
    

### 主進程與渲染進程

Electron 採用了多進程架構，主要分為兩大角色：

- **主進程（Main Process）**：
    
    - 每個應用只有一個主進程。
        
    - 負責管理應用程式的生命週期（啟動、退出）。
        
    - 負責建立作業系統視窗（`BrowserWindow`）。
        
    - 擁有完整的 Node.js 權限，可以直接與作業系統溝通。
        
- **渲染進程（Renderer Process）**：
    
    - 每個被打開的視窗都是一個獨立的渲染進程。
        
    - 負責呈現 HTML/CSS 畫面與執行前端 JavaScript。
        
    - 為了安全起見，現代 Electron 預設會限制渲染進程直接存取 Node.js，必須透過 **IPC（進程間通訊）** 管道與主進程傳遞訊息，再由主進程執行底層操作。
        

## 為什麼要用 Electron？（優點）

- **跨平台**：寫一次代碼，就能同時打包成 Windows (.exe)、macOS (.app) 和 Linux 的安裝檔。
    
- **降低開發成本**：網頁前端工程師不需要學習 Swift、Objective-C 或 C#，就能直接上手開發桌面軟體。
    
- **強大的生態圈**：不論是前端的 React、Vue、Angular，還是 Node.js 的數百萬個 npm 套件，全都能直接無縫使用。
    
- **熱更新（Auto-update）**：支援自動更新機制，維護與發布新功能非常方便。
    

## 有什麼缺點或代價？

雖然 Electron 非常方便，但它也經常被戲稱為「記憶體巨獸」，主要原因如下：

- **記憶體與硬碟佔用大**：因為每個 Electron 應用都打包了一個完整的 Chromium 瀏覽器和 Node.js 環境，即使是一個簡單的 Hello World 程式，打包後可能也要 100MB 以上，執行時也會消耗不少 RAM。
    
- **效能瓶頸**：在處理極度消耗 CPU/GPU 的重度運算（如大型遊戲或複雜的 3D 繪圖）時，效能表現依舊原生應用（C++、Rust 或原生作業系統 API）。
    

## 哪些知名軟體是用 Electron 寫的？

你可能每天都在使用 Electron 寫出來的軟體，例如：

- **Visual Studio Code (VS Code)**
    
- **Discord**
    
- **Slack**
    
- **WhatsApp Desktop**
    
- **Obsidian**（筆記軟體）
    
- **Postman**（API 測試工具）
　
- Microsoft Teams


## 簡單範例：建立一個視窗

在 Electron 的 `main.js`（主進程）中，初始化一個視窗的核心程式碼非常直覺：

JavaScript

```
const { app, BrowserWindow } = require('electron')

function createWindow () {
  // 建立瀏覽器視窗
  const win = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      nodeIntegration: false, // 現代安全性建議
      contextIsolation: true  // 隔離上下文以確保安全
    }
  })

  // 載入應用程式的 index.html
  win.loadFile('index.html')
}

// 當 Electron 準備就緒時，啟動視窗
app.whenReady().then(createWindow)
```

### Electron 與 Tauri 比較

|項目|Electron|Tauri|
|---|---|---|
|核心技術|Chromium + Node.js|系統 WebView + Rust|
|應用大小|較大|較小|
|記憶體占用|較高|較低|
|學習成本|低|較高|
|生態系|非常成熟|成長中|
|開發速度|快|中等|

如果你是要開發桌面 App，我也可以示範：

- 使用 React + Electron 建立專案
- Electron 與後端 API 整合
- IPC（主程序與渲染程序通訊）
- 打包成 `.exe`、`.dmg` 或 Linux 安裝檔
- Electron 安全性最佳實踐
- Electron + TypeScript 完整範例專案架構