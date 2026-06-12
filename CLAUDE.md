# LLM Wiki Repository Instructions (CLAUDE.md)

Welcome to the Obsidian LLM Wiki Repository. This repository is configured to be maintained as an LLM-driven compounding knowledge base, as described in Andrej Karpathy's LLM Wiki pattern.

## 核心規則 (Core Rules)
- **語言限制**：所有生成的檔案、內容、修改及對使用者的回覆，**必須全部使用繁體中文 (Traditional Chinese)**。
- **Wiki 目錄定義**：
  - 原始資料庫：[AI/sources/](file:///c:/Obsidian/AI/sources)（不可變、唯讀）。
  - 編譯後 Wiki：[AI/wiki/](file:///c:/Obsidian/AI/wiki)（由 AI 全權寫入、維護）。
  - 運作規範：[AI/schema.md](file:///c:/Obsidian/AI/schema.md)（所有 Agent 的行為準則）。
- **交叉鏈結**：Wiki 內部頁面之間必須使用 Obsidian 的 `[[雙括號]]` 語法建立關聯，以便渲染知識圖譜。
- **YAML Frontmatter**：每個 Wiki 頁面頂部都必須有正確的 YAML 元數據（標籤、關聯原始文獻、建立與更新日期等）。

## 核心操作命令與工作流 (Key Workflows)
在協助使用者時，您需要自動識別並執行以下工作流：

1. **資料匯入 (Ingest)**：
   - 使用者將原始檔案放置於 `AI/sources/` 中。
   - 讀取檔案，提煉核心概念與關鍵實體。
   - 與使用者核對摘要重點。
   - 在 `AI/wiki/` 建立文獻總結頁面，並建立/更新關聯的概念與實體頁面（使用 `[[雙括號]]` 引用）。
   - 更新索引檔 [AI/wiki/index.md](file:///c:/Obsidian/AI/wiki/index.md)。
   - 在歷史日誌 [AI/wiki/log.md](file:///c:/Obsidian/AI/wiki/log.md) 中追加一筆：`## [YYYY-MM-DD] ingest | 標題`。

2. **知識查詢 (Query)**：
   - 讀取 [AI/wiki/index.md](file:///c:/Obsidian/AI/wiki/index.md) 定位相關頁面。
   - 閱讀對應 Wiki 頁面與原始資料，給出有引用來源的回答。
   - 若回答具備深度整理價值，主動建議或直接將其整理為新的 Wiki 頁面，並更新索引與日誌。

3. **健康檢查 (Lint)**：
   - 檢查斷鏈（指向不存在頁面的鏈結）。
   - 找出無任何入站鏈結的孤立頁面。
   - 識別新舊資料衝突，並使用 `> [!WARNING]` 警示。
   - 推薦需要擴充的主題。

詳細運作規範與格式範例，請務必先閱讀並遵守 [AI/schema.md](file:///c:/Obsidian/AI/schema.md)。
