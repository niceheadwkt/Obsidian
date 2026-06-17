**Google AI Studio** 是一個由 Google 推出的網頁端整合開發環境（IDE），專為開發者與創作者設計，旨在提供一個快速測試、原型設計（Prototyping）以及部署生成式 AI 應用的實驗室。

如果你想要將 AI 功能整合到自己的專案中，或者想快速開發一個 AI 應用，這裡是最核心的基底。

## 核心功能與特色

- **一站式模型體驗：**
    
    支援 Google 最新、最頂尖的模型系列，包括具備強大推理能力的 **Gemini 3**、適合即時語音與視訊互動的 **Gemini Flash Live**，以及影像生成（Veo）、音樂生成（Lyria）和文字轉語音（TTS）等精選模型。
    
- **靈活的 Prompt 測試環境（Playground）：**
    
    提供直覺的介面讓使用者編寫 **System Instructions（系統指令）** 來規範 AI 的角色與語氣，並支援 Chat Prompt（多輪對話測試）。同時提供參數微調面板，可調整 Temperature（隨機性）、Top P、最大輸出長度（Output Length）等。
    
- **Vibe Coding 與 New App 功能：**
    
    不限於傳統的 API 測試，你可以直接用自然語言描述你的想法（例如：「幫我做出一個可以計算房貸並畫出圖表的網頁」），AI Studio 就會自動生成前端與後端程式碼，甚至提供瀏覽器內的模擬器供你即時 Preview。
    
- **一鍵部署至雲端：**
    
    與 Google Cloud 生態系深度整合。在畫面上點擊「Publish」，就能直接將寫好的應用程式部署到 **Cloud Run**。針對剛入門的開發者，Google 還提供免費額度（如 Starter Tier 可免費部署前兩個 App，無需綁定信用卡）。
    
- **管理 API Key：**
    
    開發者可以在此處快捷申請與管理 **Gemini API Key**，並取得 Python、JavaScript、Go、Java、C++ 等多種語言的官方 SDK 程式碼範例（Get Code），方便無縫將模型串接到自己的本地開發環境。
    
- **生態系整合與行動端支援：**
    
    支援直接存取 Google Workspace（如 Sheets、Drive）的資料來建立儀表板，並推出了行動版 App，讓開發者在手機上也能隨時調整 Prompt、瀏覽 App 畫廊並進行 Remix（複製並修改他人專案）。
    

## Google AI Studio 與 Gemini App（一般消費者版）的差別

|**功能/特性**|**Google AI Studio**|**Gemini App (gemini.google.com)**|
|---|---|---|
|**主要定位**|開發者實驗室、API 測試、App 原型建立|個人 AI 助理、日常問答、文案協作|
|**功能重點**|調整參數（Temperature）、切換不同版本模型、生成程式碼、管理 API Key|直接對話、整合 Google 擴充功能（如 Maps、YouTube）|
|**隱私機制**|**免費版**的資料可能會被人工審查以改進產品；若綁定 **Google Cloud Billing（付費專案）**，資料則完全保密，不會被用於訓練模型。|