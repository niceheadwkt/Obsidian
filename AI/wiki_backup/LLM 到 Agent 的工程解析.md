---
type: concept
tags: [AI概念, LLM, Agent, MCP, AgentSkill, CLI, Ollama]
sources: [
  "[[sources/03_AI_Concepts/LLM 到 Agent 的工程解析.md]]",
  "[[sources/03_AI_Concepts/Gemma 4 MCP 開發：本地與雲端計費.md]]"
]
created: 2026-06-11
updated: 2026-06-11
---

# 從 LLM 到 Agent Skill 的底層工程解析

本頁面從底層工程視角，剖析大語言模型 (LLM) 演進至智慧代理 (Agent) 與代理技能 (Agent Skill) 的架構堆疊，並結合本地 MCP 開發實務進行深入解析。

---

## 1. 核心概念解釋

大模型生態系的架構可層層堆疊如下：

```
┌──────────────────────────────────────────────┐
│             Agent Skill (SOP 說明書)         │
├──────────────────────────────────────────────┤
│          Agent (自主規劃靈魂：ReAct 等)        │
├──────────────────────────────────────────────┤
│  MCP (Type-C 接口)   <──>   Tool (執行手腳)  │
├──────────────────────────────────────────────┤
│   Context Window (記憶)  <──>  Tokenizer (翻譯)│
├──────────────────────────────────────────────┤
│              LLM (文字接龍大腦)              │
└──────────────────────────────────────────────┘
```

1. **LLM (大語言模型)**：底層基於 Transformer 結構，本質是「機率文字接龍」。模型接收數字並輸出數字，不直接認識文字。
2. **Tokenizer (分詞器)**：人類文字與模型數字之間的「翻譯官」。負責**編碼 (Encoding)**（將文字切分為 Token 並映射為 Token ID）與**解碼 (Decoding)**（將 Token ID 映射回文字）。一個 Token 大約等於 0.75 個英文單字或 1.5 ~ 2 個漢字。
3. **Context (上下文)**：模型每次處理任務時所接收的資訊總和（包括對話歷史、系統提示詞、工具回傳等），可視為臨時記憶體。**Context Window** 則限制了其能容納的最大 Token 數。
4. **Prompt (提示詞)**：給模型的指令。分為 **User Prompt**（使用者輸入的任務）與 **System Prompt**（開發者配置的人設與辦事規則）。
5. **Tool (工具/函數)**：模型的「外部感官與手腳」。LLM 本身無法感知世界，Tool 本質是**函數 (Function)**。模型只會輸出「想呼叫某工具」的文字指令與參數，真正執行工具的是背後的**開發平台/程式代碼**。
6. **MCP (Model Context Protocol)**：AI 界的「Type-C 統一標準接口」。MCP 讓工具開發者只需按照一套標準開發一次，即可無縫接入所有支援 MCP 的 AI 平台（如 Claude Desktop, VS Code 插件等），避免為每家 LLM 重寫接入代碼。
7. **Agent (智能體)**：具備「自主規劃與工具調用」能力的程式系統。常用的構建模式有 ReAct、Plan-and-Execute 等。它能反覆思考、決定下一步行動，直到解決使用者問題。
8. **Agent Skill (代理技能)**：給 Agent 閱讀的 **SOP 說明文檔**。它是一個以 Markdown 格式撰寫、檔名必須為大寫 `SKILL.md` 的文件，結構包含元數據層（Name & Description）與指令層（目標、步驟、判斷規則、格式與範例）。當使用者提問與元數據相關時，Agent 才會加載該 Skill 的指令層（**漸進式披露機制**，以節省 Token 成本）。

---

## 2. 為什麼越來越多人從網頁端轉向 CLI Agent？

像 **Claude Code** 這類的命令列 (CLI) Agent 正在成為開發者的新寵，核心優勢在於：
- **消除「冗長 Prompt」**：本地配置好的 `SKILL.md` 能讓 Agent 記住個人偏好與專案 SOP，無須每次手動輸入。
- **本地執行效率**：CLI Agent 能直接存取本地檔案系統 (FileSystem)、執行編譯、跑測試及 Git commit，比網頁端複製貼上更高效。
- **Token 節約**：藉由 Skill 的元數據過濾機制，僅在需要時讀取指令細節。

---

## 3. 本地 MCP 與 Agent 開發實務 (以 Gemma 4 為例)

當開發如「點餐 AI 助理 (Drink Ordering Agent)」等 MCP 應用時，為擺脫雲端 API Key 與高昂的 Token 費，通常會採用 **「本地 Gemma 4 (透過 Ollama) + 本地 MCP Server」** 架構：

### 本地與雲端計費對比
- **本地執行 (Ollama / LM Studio)**：無須 API Key，不計費，隱私性高，適合頻繁的 Tool Calling 測試。
- **雲端託管 (Google AI Studio / Groq)**：需要 API Key，按 Token 計費，但模型在工具呼叫的精準度上通常較高。

### Windows 本地虛擬環境配置陷阱
在 Windows PowerShell 部署本地 Streamlit 與 OpenAI SDK 連接 Ollama 時，需特別注意：
1. **虛擬環境路徑 (.\.venv\ vs .\venv\)**：
   許多工具（如 `uv`）建立的虛擬環境資料夾預設帶有小數點（`.venv`）。在寫死路徑時若少寫點號，會導致系統噴出 `WinError 2 (找不到指定的檔案)`。
2. **MCP 進程 Python 路徑**：
   在 Streamlit 呼叫 MCP 服務時，若 MCP 啟動參數 `command` 寫死為 `"python.exe"`，系統可能抓到全域 Python 而非虛擬環境的 Python，進而報出 `ModuleNotFoundError`。應將其修正為虛擬環境內的絕對路徑：
   ```python
   mcp_server_params = StdioServerParameters(
       command=r"C:\aiTest\mcp-drink-main\.venv\Scripts\python.exe", # 絕對路徑
       args=[r"C:\aiTest\mcp-drink-main\mcp_server.py"],
       env=None
   )
   ```
3. **優化建議**：與其在程式碼中寫死路徑，更好的做法是編寫讀取 `%APPDATA%\Claude\claude_desktop_config.json` 的邏輯，直接共用 Claude Desktop 的設定檔來啟動 MCP。
