# Wiki 操作歷史日誌 (Changelog)

此檔案為追加寫入（Append-only）的操作日誌，用於記錄知識庫的演進歷史。每條日誌均採用統一的前綴格式，方便使用 Unix 命令列工具進行分析與篩選（例如 `grep "^## \[" log.md | tail -n 5`）。

格式規範：
`## [YYYY-MM-DD] <操作類型> | <操作主題/描述>`
- 操作類型包括：`setup`（系統初始化）、`ingest`（匯入資料）、`query`（高價值查詢歸檔）、`lint`（知識庫健康檢查與維護）。

---

## [2026-06-11] setup | 初始化 LLM Wiki 知識庫系統

- **描述**：成功搭建了 Karpathy 方法的 LLM Wiki 核心架構。
- **建立目錄**：
  - `sources/`（原始資料庫）
  - `wiki/`（編譯後 Wiki）
- **建立文件**：
  - `sources/README.md`
  - `wiki/README.md`
  - `wiki/index.md`
  - `wiki/log.md`
  - `schema.md` (Obsidian 規範)
  - `CLAUDE.md` (Agent 規範)
- **維護者**：Antigravity Agent

## [2026-06-11] ingest | 批次匯入第一批：AI 工具與 CLI (01_AI_Tools)

- **來源文獻**：`SRC-002` 至 `SRC-014` 共 13 篇原始文章。
- **新增 Wiki 頁面**：
  - `[[AI CLI 工具比較與選擇_摘要]]`
  - `[[Claude]]` (綜合實體頁面)
  - `[[Ollama]]` (綜合實體頁面)
  - `[[AI 工具與框架概覽]]` (綜合概念分析頁面)
- **更新索引**：[index.md](file:///c:/Obsidian/AI/wiki/index.md) 已同步更新。
- **執行人**：Antigravity Agent

## [2026-06-11] ingest | 批次匯入第二至五批：綜合資料編譯 (02_NotebookLM_Special 至 06_Networking_Systems)

- **來源文獻**：`SRC-015` 至 `SRC-041` 共 27 篇原始文章。
- **新增 Wiki 頁面**：
  - `[[NotebookLM 綜合指南]]` (綜合概念頁面)
  - `[[RAG 與 DeepSearch 概念綜述]]` (綜合概念頁面)
  - `[[從 LLM 到 Agent 的工程解析]]` (綜合概念頁面)
  - `[[個人知識管理系統構築]]` (綜合概念頁面)
  - `[[前端與系統開發常用技術]]` (綜合概念頁面)
  - `[[網路系統基礎]]` (綜合概念頁面)
- **更新索引**：[index.md](file:///c:/Obsidian/AI/wiki/index.md) 已同步更新，整理所有 41 篇文獻目錄。
- **執行人**：Antigravity Agent

## [2026-06-13] ingest | 批次匯入第六批：自動化、提示詞、Git 同步與商業思維

- **來源文獻**：`SRC-042` 至 `SRC-054` 共 13 篇原始文章（位於 `AI/raw/` 唯讀目錄下）。
- **新增 Wiki 頁面**：
  - `[[AI 第二大腦與 Claude Cowork 自動化]]`
  - `[[ChatGPT 影像生成提示詞指南]]`
  - `[[Git GUI 與 GitHub 雙向同步實務]]`
  - `[[商業案例與投資思維專題]]`
- **更新索引**：[index.md](file:///c:/Obsidian/AI/wiki/index.md) 已同步更新，追加這 4 個新 Wiki 頁面與 13 筆文獻來源。
- **執行人**：Antigravity Agent

## [2026-06-13] ingest | 批次匯入第七批：Claude 一桌三櫃專案管理工作流 (EP10)

- **來源文獻**：`SRC-055` 共 1 篇原始文章（位於 `raw/` 唯讀目錄下）。
- **新增 Wiki 頁面**：
  - `[[Claude 專案管理一桌三櫃工作流]]`
- **更新索引**：[index.md](file:///c:/Obsidian/AI/wiki/index.md) 已同步更新，追加此 Wiki 頁面與 1 筆文獻來源。
- **執行人**：Antigravity Agent
