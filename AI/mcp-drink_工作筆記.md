# mcp-drink 工作筆記

## 上次做到哪 (2026-08-07)
- **修正網頁內置 AI 點餐識別與幻覺點餐 Bug**：
  - 優化 [app.js](file:///c:/aiTest/mcp-drink-main/app.js) 的 `callWebLLM` 與 `callLocalOllama` 系統提示詞、降低推理溫度至 `0.1`，並加入「不加料」 Few-Shot 範例，改善對「小平平」等三人名及否定規格的識別。
  - 新增歷史紀錄過濾器，自動移除包含 `✅`/`❌`/`成功為` 的工具執行結果文字，避免小模型因上下文模仿而產生「假成功、未寫入 DB」的幻覺。
- **優化快取檢測與 Qwen 2.5 3B 識別**：
  - 重構 `getCachedModels` 匹配邏輯，忽略非英數字元（如點 `.`, 減號 `-` 等），並支援對 OPFS 目錄名稱的模糊對齊，順利偵測出 Qwen 2.5 3B 快取。
- **下拉選單白底白字樣式修正**：
  - 在 [style.css](file:///c:/aiTest/mcp-drink-main/style.css) 寫入全域 `select option` 樣式，強制深色底、淺色字，防止原生 Light 模式渲染白底白字。
- **知識庫文件整理與匯入 (第十九批 Ingest)**：
  - 全量匯入 `AI/raw/` 目錄中剩餘 20 份文獻（包含 AI Agent 基本功系列 EP01-EP07、一沐日雲端點餐 MCP 專案啟動說明、Kimi 發展專題等）。
  - 新增 4 個 Wiki 頁面（`Kimi 與月之暗面 (Moonshot AI) 發展專題`、`AI Agent 基本功系列實踐指南 (EP01-EP07)`、`一沐日雲端點餐與 MCP 系統開發實務`、`深度學習與大語言模型架構全景`）。
  - 修訂 6 個現有概念頁面，並同步更新 [index.md](file:///g:/%E6%88%91%E7%9A%84%E9%9B%B2%E7%AB%AF%E7%A1%AC%E7%A2%9F/Obsidian/AI/wiki/index.md)、[log.md](file:///g:/%E6%88%91%E7%9A%84%E9%9B%B2%E7%AB%AF%E7%A1%AC%E7%A2%9F/Obsidian/AI/wiki/log.md) 與 [dashboard.html](file:///g:/%E6%88%91%E7%9A%84%E9%9B%B2%E7%AB%AF%E7%A1%AC%E7%A2%9F/Obsidian/AI/dashboard.html)。

## 下一步
- **點餐意圖測試**：測試並觀察多種內置 AI 模型（如 Gemma 2 2B, Llama 3.2 1B）在各種點餐/修改/刪除意圖下的工具調用穩定度。
