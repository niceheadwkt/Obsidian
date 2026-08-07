---
type: concept
tags: [mcp-drink, 專案開發, Firestore, MCP-Server, 點餐助理]
sources: 
  - "[[sources/一沐日雲端點餐與 MCP 系統 (mcp-drink-main)啟動.md]]"
  - "[[sources/一沐日雲端點餐與 MCP 系統.md]]"
created: 2026-08-07
updated: 2026-08-07
---

# 一沐日雲端點餐與 MCP 系統開發實務

本專案（`mcp-drink-main`）是一套為「一沐日」手搖飲設計的雲端智慧點餐與訂單管理系統，完美展現了 **Model Context Protocol (MCP)** 協議與手勢/語意互動的結合。

## 1. 系統核心架構
- **Streamlit 前端 UI (`drink_app.py`)**：提供使用者可視化的網頁點餐、菜單瀏覽與訂單管理介面。
- **Google Cloud Firestore (Firebase)**：作為後端即時資料庫，儲存菜單資料、訂單紀錄與重複訂單統計。
- **MCP 伺服器 (`mcp_server.py`)**：將點餐、修改、刪除、重複訂單篩選及統計功能封裝為 MCP Tools。
- **AI 點餐助手**：AI 模型（如網頁內建的 Web-LLM 或本地 Ollama Qwen 2.5 3B）可以透過 MCP 工具直接存取 Firestore，解析使用者的自然語言意圖（如：「我要一杯小平平無糖微冰，加粉粿，不加珍珠」）並完成點餐。

## 2. 推薦啟動方式 (Windows 環境)
為了確保 Streamlit 網頁與 MCP 伺服器的無縫對接，請在專案根目錄下的 PowerShell 執行：
```powershell
.\.venv\Scripts\python.exe -m streamlit run drink_app.py
```
- **自動連接機制**：啟動 Streamlit UI 後，系統會在背景自動拉起並綁定 MCP 伺服器（`mcp_server.py`），開發者無需手動開啟多個視窗。

## 3. 開發排障與優化重點 (2026-08-07)
- **降低幻覺點餐 (Hallucination Order)**：
  - 將 Web-LLM 與 Local Ollama 的推理溫度（Temperature）降至 `0.1`，並優化 Prompt 加入 Few-Shot 否定範例（例如「不加料」）。
  - 在歷史紀錄中加入過濾器，自動過濾掉 `✅`、`❌`、`成功為` 等工具執行結果關鍵字，防止小模型因模仿上下文而誤判工具執行成功。
- **快取與匹配模糊對齊**：
  - 重構 `getCachedModels` 快取偵測匹配邏輯，忽略非英數字元（如 `.`, `-` 等），以支援對 OPFS 目錄名稱的模糊對齊，順利偵測出 Qwen 2.5 3B 等本地快取模型。
- **網頁選單 CSS 白字白底 Bug 修正**：
  - 在 [style.css](file:///c:/aiTest/mcp-drink-main/style.css) 寫入全域 `select option` 樣式，強制深色背景、淺色字體，解決原生瀏覽器 Light 模式下的白字白底渲染問題。
