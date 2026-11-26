---
type: entity
tags: [AI工具, Ollama, Qwen, DeepSeek, RAG, 智能體]
sources: [
  "[[sources/01_AI_Tools/Ollama 中Launch 選項codex app與codex 之差異為何.md]]",
  "[[sources/01_AI_Tools/Ollama 可以針對LOCAL設專案目錄來運作？.md]]",
  "[[sources/01_AI_Tools/在 Ollama 中使用 Qwen 是完全免費的.md]]",
  "[[sources/01_AI_Tools/目前LLM模組有哪些可以在LOCAL執行引用，列出其優缺點.md]]",
  "[[sources/01_AI_Tools/OPENCODE如何加QWEN3？.md]]",
  "[[AI/raw/2026-11-26T151837+0800-EP460 - 你的電腦能跑什麼 AI？16GB 到 128GB 一次講完｜Ollama、LM Studio 怎麼設定，新手五個坑.md|EP460 你的電腦能跑什麼 AI？（AI懶人報，2026-11-04）]]"
]
created: 2026-06-11
updated: 2026-11-26
---

# Ollama (本地 AI 模型執行引擎)

**Ollama** 是一款開源、免費的本地端 AI 模型執行引擎。它簡化了模型部署與運行的繁瑣手續，提供了一鍵下載、管理與 API 轉發功能，是目前個人與企業實現 **「資料不出機、完全本地化」** 開發的最佳方案。

---

## 1. 系統定位與架構

- **純本地推論**：模型完全下載至本地硬碟，利用本機 CPU 或 GPU 進行運算，完全離線且無須帳號，具備極高的資安隱私。
- **無訂閱與 API 費**：不限制使用次數與生成字數，唯一的成本是本機電費與硬體配備。
- **API 服務端**：Ollama 啟動後會在背景開啟 API 服務（預設埠為 `http://localhost:11434`），可直接與 **Cursor、vLLM、[[Dify]]、Aider** 等前端客戶端無縫對接。
- **專案管理定位**：Ollama 本身不具備「專案目錄」的概念，它專注於模型服務；專案的管理與文件讀取需透過客戶端（如 Aider、Continue.dev、Open WebUI）掃描後，再呼叫 Ollama 進行推理。

---

## 2. 核心模型與運行指南

### 🇨🇳 Qwen (通義千問) 系列
中文理解與 Tool Calling 能力最強的本地模型之一。目前最熱門的是 **Qwen 2.5**：
```bash
# 輕度測試、一般筆電可用（約需 4GB 記憶體）
ollama run qwen2.5:3b

# 效能與速度平衡的黃金版本（建議 16GB 記憶體，或有 6GB 以上顯存）
ollama run qwen2.5:7b

# 程式開發與 Debug 優化版
ollama run qwen2.5-coder:7b
```

### 🧠 其他推薦本地開源模型
- **DeepSeek-R1**：當前推理邏輯與數學最強的開源模型（例如 `DeepSeek-R1 Distill 8B / 14B`）。
- **Llama 3.3 (70B)**：Meta 的旗艦開源模型，綜合英文能力極佳，但硬體資源要求高。
- **Gemma 3 (4B / 12B)**：Google 的輕量小模型，適合個人筆電或邊緣端順暢執行。
- **Phi-4**：微軟的小型高推理模型，適合家用 NAS 或本地 Copilot。

---

## 3. 本地硬體配置推薦

依 [[本地 AI 硬體分級與 Ollama 設定五大坑]]（2026-11）的分級改寫。速度為社群實測，僅供參考。

**估算規則**：4-bit 量化模型大約需要「參數量 × 0.6 GB」（9B ≈ 5.7 GB、27B ≈ 17.6 GB、35B ≈ 22.4 GB），還要另外留空間給 context。Mac 的統一記憶體預設大約只有 3/4 能給 GPU 用（16 GB 約 12 GB、32 GB 約 24 GB）。

| 記憶體 | 能跑的模型 | 適合做什麼 |
|---|---|---|
| 8–16 GB | Gemma 4 E4B（約 5 GB）、Qwen3.5 9B（約 5.7 GB）；gpt-oss-20b（約 12 GB，16 GB Mac 上很緊） | 改寫、翻譯、摘要、整理成表格；當 agent 容易出錯 |
| 24–32 GB（甜蜜點） | Qwen3.8 27B、Gemma 4 26B（MoE，較快）、Qwen3.6 35B-A3B（MoE） | 私人文件問答、批次分類、範圍清楚的 coding agent 小任務；24 GB 偏緊，32 GB 較穩 |
| 64 GB | 最強的還是 27B 等級，但可換 8-bit（約 29 GB）提升品質 | 開長 context（Ollama 在 ≥ 48 GB 時預設 256k）、跑長時間的 agent 任務 |
| 128 GB | gpt-oss-120b（約 63 GB）、Qwen3.8 Flash Next（125B） | 100B 以上的大模型，大約是一年前頂級雲端模型的水準；macOS 可用大約 96–107 GB |

**獨立顯示卡（看 VRAM）**：用同一條規則估算。12 GB VRAM（RTX 4070 等）適合 9B～14B 的 4-bit 模型；24 GB 以上 VRAM（RTX 4090 等）可以放下 27B 等級的 4-bit 模型，再加上中等長度的 context。放得下之後，還要留空間給 context，不要把記憶體吃到滿（有人在 16 GB 顯示卡硬塞 27B 導致當機）。

> [!NOTE]
> 本節原本以 Qwen 2.5、DeepSeek-R1 Distill、Gemma 3 等舊世代模型為例（32 GB 跑 8B／14B）。2026-11-26 依新來源改寫，舊模型的 `ollama run` 指令仍保留在第 2 節。

---

## 3.5 Context 預設值與安全設定（2026-11 補充）

- **預設 context 依顯示記憶體而定**：< 24 GB 為 4k、24～48 GB 為 32k、≥ 48 GB 為 256k。接 OpenClaw、Claude Code 這類 agent 時至少要拉到 **64k**，否則系統說明一放進去就爆，模型看起來會像「很笨」。
- **保持只聽本機**：Ollama 預設只綁本機；2026 年有 17.5 萬台被改成對外開放、沒有密碼的 Ollama 伺服器。需要遠端連線時改用 Tailscale 這類私人網路，並保持最新版。
- 硬體分級、MoE、chat template／KV cache 等坑，詳見 [[本地 AI 硬體分級與 Ollama 設定五大坑]]。

---

## 4. `ollama launch` 功能詳解：整合 Codex

Ollama 提供了啟動 OpenAI Codex 軟體載體的橋接指令，主要區分為兩類（另外關於 OpenCode 整合 Qwen3 的設定細節可參考 [[sources/01_AI_Tools/OPENCODE如何加QWEN3？.md|OPENCODE如何加QWEN3？]]）：

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
