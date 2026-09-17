# Ava GPT MCP 整合工具說明文件

本文件為 **Google Antigravity** 與內部 **Ava GPT (中鋼 Ava API)** 整合工具之說明文件。

完整技術指南請參閱：[`docs/mcp_server_guide.md`](file:///C:/aiTest/fastmarkets-daily-v2/docs/mcp_server_guide.md)

---

## 快速速查

- **MCP 伺服器程式碼**：[`mcp_server.py`](file:///C:/aiTest/fastmarkets-daily-v2/mcp_server.py)
- **環境設定檔**：[`.env`](file:///C:/aiTest/fastmarkets-daily-v2/.env)
- **全域設定檔**：[`~/.gemini/config/mcp_config.json`](file:///C:/Users/ch26788/.gemini/config/mcp_config.json)

---

## 核心工具一覽

| 工具名稱                 | 主要功能            | 參數                                                                |
| :------------------- | :-------------- | :---------------------------------------------------------------- |
| `ava_health_check`   | 系統健康檢查與連線延遲診斷   | 無                                                                 |
| `ava_chat`           | 專家知識庫問答 (RAG)   | `prompt`, `expert_id` (選填), `timeout` (選填)                        |
| `ava_vision`         | 圖片多模態辨識與圖表判讀    | `image_path`, `prompt` (選填), `model_list_id` (選填), `timeout` (選填) |
| `ava_list_models`    | 查詢可用模型清單        | `mode_type` (選填，預設 `"search"`)                                    |
| `ava_summarize_news` | 鋼鐵新聞結構化 JSON 摘要 | `article_text`                                                    |

---

## 如何在對話中呼叫

直接在對話框向 Agent 提出需求即可：
- 「請呼叫 Ava GPT 查詢...」
- 「請使用 Ava 視覺模型分析圖片 `C:/path/to/image.png`」
- 「列出 Ava GPT 目前所有可用的 AI 模型」
