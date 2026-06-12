---
type: entity
tags: [AI工具, Ollama, Qwen, DeepSeek, RAG, 智能體]
sources: [
  "[[sources/01_AI_Tools/Ollama 中Launch 選項codex app與codex 之差異為何.md]]",
  "[[sources/01_AI_Tools/Ollama 可以針對LOCAL設專案目錄來運作？.md]]",
  "[[sources/01_AI_Tools/在 Ollama 中使用 Qwen 是完全免費的.md]]",
  "[[sources/01_AI_Tools/目前LLM模組有哪些可以在LOCAL執行引用，列出其優缺點.md]]"
]
created: 2026-06-11
updated: 2026-06-11
---

# Ollama (本地 AI 模型執行引擎)

**Ollama** 是一款開源、免費的本地端 AI 模型執行引擎。它簡化了模型部署與運行的繁瑣手續，提供了一鍵下載、管理與 API 轉發功能，是目前個人與企業實現 **「資料不出機、完全本地化」** 開發的最佳方案。

---

## 1. 系統定位與架構

- **純本地推論**：模型完全下載至本地硬碟，利用本機 CPU 或 GPU 進行運算，完全離線且無須帳號，具備極高的資安隱私。
- **無訂閱/API 費**：不限制使用次數與生成字數，唯一的成本是本機電費與硬體配備。
- **API 服務端**：Ollama 啟動後會在背景開啟 API 服務（預設埠為 `http://localhost:11434`），可直接與 **Cursor、vLLM、[[Dify]]、Aider** 等前端客戶端無縫對接。
- **專案管理**：Ollama 本身不具備「專案目錄」的概念，它專注於模型服務；專案的管理與文件讀取需透過客戶端（如 Aider、Continue.dev、Open WebUI）掃描後，再呼叫 Ollama 進行推理。

---

## 2. 核心模型與運行指南

### Qwen (通義千問) 系列
中文理解與 Tool Calling 能力最強的本地模型之一。目前最熱門的是 **Qwen 2.5**：
```bash
# 輕度測試、一般筆電可用（約需 4GB 記憶體）
ollama run qwen2.5:3b

# 效能與速度平衡的黃金版本（建議 16GB 記憶體，或有 6GB 以上顯存）
ollama run qwen2.5:7b

# 程式開發與 Debug 優化版
ollama run qwen2.5-coder:7b
```

### 其他推薦本地模型
- **DeepSeek-R1**：當前推理邏輯與數學最強的開源模型（例如 `DeepSeek-R1 Distill 8B / 14B`）。
- **Llama 3.3 (70B)**：Meta 的旗艦開源模型，綜合英文能力極佳，但硬體資源要求高。
- **Gemma 3 (4B / 12B)**：Google 的輕量小模型，適合個人筆電或邊緣端順暢執行。
- **Phi-4**：微軟的小型高推理模型，適合家用 NAS 或本地 Copilot。

---

## 3. 本地硬體配置推薦

- **16GB RAM**：適合跑 Qwen 2.5 (3B/7B)、Gemma 3 (4B)。
- **32GB RAM**：適合跑 Qwen 2.5 (8B/14B)、DeepSeek-R1 Distill (8B)。適合個人本地知識庫。
- **12GB VRAM 顯卡 (RTX 4070 等)**：適合跑 Qwen 2.5 (14B Q4)、DeepSeek-R1 (14B)，推理速度極佳。
- **24GB+ VRAM 顯卡 (RTX 4090 等)**：適合跑 Qwen 2.5 (32B)、DeepSeek-R1 (32B)，可流暢執行本地 RAG 與 Agent。

---

## 4. `ollama launch` 功能詳解：整合 Codex

Ollama 提供了啟動 OpenAI Codex 軟體載體的橋接指令，主要區分為兩類：

### A. `ollama launch codex-app` (桌面 App 模式)
- **載體**：啟動 Codex 桌面獨立應用程式（圖形介面 GUI）。
- **特點**：
  - 支持多任務與多 Agent 在同專案並行。
  - 內建瀏覽器標註，支持邊看網頁邊要求 AI 修改前端樣式。
  - 提供直觀的程式碼變更 Diff 對比。
- **工作原理**：Ollama 會自動將該桌面 App 的 API 端點劫持並修改為 `http://localhost:11434/v1`，實現**免 OpenAI 訂閱費、100% 本地且代碼不外流**的圖形化 Agent 工作區。
- **專案啟動建議**：在 Windows 環境下，可於專案目錄建立批次檔 `.bat` 一鍵開啟：
  ```bat
  @echo off
  cd /d "C:\您的專案路徑"
  ollama launch codex-app --model qwen2.5-coder:7b
  ```

### B. `ollama launch codex` (命令列 CLI 模式)
- **載體**：控制 Codex CLI 終端機工具。
- **特點**：輕量、無 GUI、資源佔用極低。完全在 Terminal 環境下運作，易於與 Git 工作流或 CI/CD 自動化腳本集成。

---

> [!TIP]
> 當您使用 `ollama launch` 啟動桌面 App 時，若想確認是否真的在使用本地模型，請盯著您的 PowerShell 終端機。如果您發問時畫面開始瘋狂滾動 `127.0.0.1 POST /v1/chat/completions` 的日誌，即代表資料安全地保留在本機，正由您的 GPU 和 Ollama 進行推論。
