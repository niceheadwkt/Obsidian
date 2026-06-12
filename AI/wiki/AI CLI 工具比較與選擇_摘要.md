---
type: source-summary
tags: [AI工具, CLI, Gemini, Claude, OpenAI, Aider]
sources: ["[[sources/01_AI_Tools/AI CLI 工具比較與選擇.md]]"]
created: 2026-06-11
updated: 2026-06-11
---

# AI CLI 工具比較與選擇 (文獻摘要)

本篇摘要整理自原始文獻 `AI CLI 工具比較與選擇.md`，系統性梳理了 2026 年主流的 AI 命令行介面 (CLI) 工具之核心功能、免費方案及選擇策略。

## 1. 主流 AI CLI 工具核心對比

| 工具名稱 | 開發商/社群 | 核心強項 | 免費額度 | 適合對象與場景 |
| :--- | :--- | :--- | :--- | :--- |
| **Gemini CLI** | Google | 100 萬超大上下文、連網搜尋、MCP 協議、Shell 模式 | 每日 1,000 次 (最慷慨) | 預算有限、需要處理大型專案與查詢最新資訊者 |
| **Claude Code** | Anthropic | 強大邏輯推理、Agent 自動化 (Git 提交、跑測試、修 Bug) | 需 API Key 或 Pro 訂閱 (特定開源維護者免費) | 追求極致自動化與重構效率的資深工程師 |
| **Codex CLI** | OpenAI | 雲端沙盒 (Sandbox) 安全執行、語音輸入、GPT-5.3 | 包含在 ChatGPT Plus | 重視系統安全、需執行不確定腳本者 |
| **Aider** | 開源社群 | 本地模型支援 (Ollama)、Git 自動提交、雙向同步編輯 | 工具免費，API 費另計 (搭配 Ollama 則全免費) | 隱私至上、偏好開源方案或完全本地運行者 |

## 2. 免費使用 AI CLI 的三種途徑

1. **官方直接提供 (有額度限制)**：
   - **Gemini CLI (首選)**：每天免費 1,000 次請求。
   - **GitHub Copilot CLI (基礎層)**：每月 50 次 Agent 模式，2,000 次代碼補全。
2. **開源工具 + 本地模型 (100% 免費 & 隱私)**：
   - **Aider / Continue CLI + Ollama**：在本地執行 `Llama 3.3` 或 `DeepSeek-R1`。完全離線，無 Token 費用，適合公司內部敏感代碼。
3. **特定身份福利 (隱藏版)**：
   - **學生專案**：GitHub Student Pack 提供免費 Copilot。
   - **開源維護者**：Claude Code 提供給 5,000+ Stars 或 100萬+ npm 下載量的作者 6 個月免費 Claude Max。
   - **新創補助**：Anthropic/Google 常提供 $1,000 ~ $10,000 的 API 試用金。

## 3. 實戰指引：以 GitHub Copilot CLI 產製文件為例

- **安裝指令**：Windows 使用 `winget install GitHub.Copilot`；macOS 使用 `brew install copilot-cli`。
- **初始化**：於專案目錄執行 `copilot init` 建立並配置 `.github/copilot-instructions.md`。
- **產製文件**：
  - 單次指令：`copilot -p "根據現有程式碼生成完整的 README.md"`
  - 互動模式：輸入 `copilot` 進入對話，例如要求「產製 `SYSTEM_ARCHITECTURE.md`，包含模組關係圖」。
- **Windows 權限脫困**：
  - 若在 Windows 環境下遇到 `Permission denied` 或程序卡死，建議使用**「系統管理員身份」**開啟 PowerShell，並在卡住時按 `Esc` 退出選取模式，或按 `Ctrl + C` 強制終止。

---

> [!NOTE]
> 關聯實體頁面：
> - 關於本地運行的引擎，請參閱 [[Ollama]]。
> - 關於 Anthropic 的核心工具，請參閱 [[Claude]]。
