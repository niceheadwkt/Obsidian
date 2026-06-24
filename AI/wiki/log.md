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
  - `[[LLM 到 Agent 的工程解析]]` (綜合概念頁面)
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

## [2026-06-14] ingest | 批次匯入第八批：母語式英文聽力與外語習得法 (KevinFeng)

- **來源文獻**：`SRC-056` 共 1 篇原始文章（位於 `raw/` 唯讀目錄下）。
- **新增 Wiki 頁面**：
  - `[[母語式英文聽力與外語習得法]]`
- **更新索引**：[index.md](file:///c:/Obsidian/AI/wiki/index.md) 已同步更新，追加此 Wiki 頁面與 1 筆文獻來源。
- **執行人**：Antigravity Agent

## [2026-06-14] ingest | 批次匯入第九批：國外旅遊實用英語情境與求助指南

- **來源文獻**：`SRC-057` 共 1 篇原始文章（位於 `raw/` 唯讀目錄下）。
- **新增 Wiki 頁面**：
  - `[[國外旅遊實用英語情境]]`
- **更新索引**：[index.md](file:///c:/Obsidian/AI/wiki/index.md) 已同步更新，追加此 Wiki 頁面與 1 筆文獻來源。
- **執行人**：Antigravity Agent

## [2026-06-15] ingest | 批次匯入第十批：NotebookLM 與 Claude 深度專題 (65篇)

- **來源文獻**：`SRC-058` 至 `SRC-122` 共 65 篇原始資料（含 62 篇 Markdown 文章及 3 篇 YAML 簡報樣式範本，位於 `raw/` 唯讀目錄下）。
- **新增 Wiki 頁面**：
  - `[[NotebookLM 進階應用與實戰指引]]`
  - `[[Claude 系統優化與 Token 節省指南]]`
  - `[[Claude Cowork 與 Agent Skill 實務]]`
  - `[[Claude Design 與前端美化實務]]`
  - `[[Claude 高階提示詞與應用場景]]`
- **更新索引**：[index.md](file:///c:/Obsidian/AI/wiki/index.md) 已同步更新，追加這 5 個新 Wiki 頁面與 65 筆文獻來源。
- **執行人**：Antigravity Agent

## [2026-06-18] ingest | 批次匯入第十一批：Antigravity 核心概念與 Remotion 影片工程

- **來源文獻**：`SRC-123` 與 `SRC-124` 共 2 篇原始資料（位於 `raw/` 唯讀目錄下）。
- **新增 Wiki 頁面**：
  - `[[Antigravity 核心概念與五層記憶系統]]`
  - `[[Antigravity 與 Remotion 影片生成實務]]`
- **更新索引**：[index.md](file:///c:/Obsidian/AI/wiki/index.md) 已同步更新，追加這 2 個新 Wiki 頁面與 2 筆文獻來源。
- **執行人**：Antigravity Agent

## [2026-06-18] lint | 知識庫完整健康檢查

- **描述**：執行了 `AI/wiki/` 知識庫的完整健康檢查與規範審查。
- **檢查範圍**：27 個 Wiki 頁面及對應之 124 篇原始文獻。
- **主要發現**：
  - 偵測到 7 處 Wiki 內部失效連結（包含 `從 LLM 到 Agent` 的名稱不符）。
  - 偵測到 6 處真正損壞的原始文獻連結（簡繁不一致、時間戳格式錯誤、結尾多餘單引號）。
  - 偵測到 64 處 sources 缺少 `raw/` 或 `sources/` 前綴。
  - 發現 13 個知識孤立頁面與 23 個未引用的原始文獻（代表知識庫缺口）。
  - 識別了 2 處潛在版本或指令矛盾。
- **報告產出**：已產出完整健康檢查報告 [health_check_report.md](file:///C:/Users/niceh/.gemini/antigravity-ide/brain/125d6655-6b58-4e6e-bbcc-e7c75c995c7a/health_check_report.md)。
- **執行人**：Antigravity Agent

## [2026-06-18] ingest | 批次匯入第十二批：Dify、辦公自動化、Agent術語與三大模型對比

- **來源文獻**：`SRC-010` (Dify.md)、`SRC-084` (三大工具付費版對比)、`SRC-106` (Claude in Excel)、`SRC-107` (Claude for Word) 以及 `SRC-125` (16個AI Agent術語)。
- **新增 Wiki 頁面**：
  - `[[Dify]]` (實體專頁)
  - `[[Claude 辦公自動化 (Excel & Word)]]` (概念專頁)
  - `[[AI 時代的 Agent 術語與核心概念]]` (概念專頁)
  - `[[三大 AI 付費版選用與效能橫向對比]]` (分析專頁)
- **更新索引**：[index.md](file:///c:/Obsidian/AI/wiki/index.md) 已同步更新，整理關聯並新增 4 個 Wiki 頁面與 1 筆文獻來源（SRC-125）。
- **執行人**：Antigravity Agent
## [2026-06-20] lint | 修復知識庫失效連結與路徑格式問題

- **描述**：全面修復並清理了 Wiki 知識庫中的所有失效連結與路徑前綴問題，確保知識鏈完整與健康。
- **修復內容**：
  - 修復 6 處完全損壞的原始文獻連結（如時間戳冒號 typo、檔名簡繁不一致、結尾多餘反單引號等）。
  - 修復 64 處 sources 前綴缺失問題，全部補齊 `raw/` 或 `sources/` 前綴。
  - 將未引用的文獻 `raw/投資理財專題報告：通膨與債券型基金投資分析.md` 作為 `SRC-130` 關聯至 `[[商業案例與投資思維專題]]`。
  - 修正了 `index.md` 中 `SRC-050`、`SRC-056`、`SRC-076`、`SRC-125` 的檔名與簡繁字元不一致問題。
- **結果**：最新 Advanced Lint 檢查結果為：失效連結 0，未引用來源 0。
- **儀表板更新**：重新執行並更新了 HTML 儀表板 [dashboard.html](file:///c:/Obsidian/AI/dashboard.html)。
- **執行人**：Antigravity Agent

## [2026-06-23] ingest | 批次匯入第十三批：美字心法、通膨與債券、Antigravity (n8n對比)、NotebookLM (RED模組)、雲端硬碟同步與 Git Gui、Warp 現代化終端機

- **來源文獻**：`SRC-131` 至 `SRC-137` 共 7 份原始文獻（包含 5 份 `raw/` 目錄下的文件，與從根目錄移入 `raw/` 的 `Claude Design.md` 及 `Warp Terminal.md`）。
- **新增 Wiki 頁面**：
  - `[[硬筆書法與美字練習心法]]` (新概念頁面)
  - `[[Warp 現代化終端機工具]]` (新實體頁面)
- **更新 Wiki 頁面**：
  - `[[商業案例與投資思維專題]]` (追加通膨對資產/投資/生活衝擊傳導及 AGG 基金特性)
  - `[[Antigravity 核心概念與五層記憶系統]]` (追加 n8n vs Antigravity、Vibe Coding 範式與 DOE 框架)
  - `[[NotebookLM 進階應用與實戰指引]]` (追加 RED AI 簡報模組、Canva 後製與 NanoBanana Pro 改圖流程)
  - `[[Git GUI 與 GitHub 雙向同步實務]]` (追加 Google 雲端硬碟同步模式建議與 Git GUI 私有庫 Token 驗證排障)
  - `[[Claude Design 與前端美化實務]]` (追加品牌自適應、工程交接及與 Figma / Canva 定位對比)
- **更新索引**：[index.md](file:///c:/Obsidian/AI/wiki/index.md) 已同步更新，關聯並整理這 7 筆新文獻來源。
- **執行人**：Antigravity Agent

## [2026-06-24] ingest | 批次匯入第十四批：Karpathy LLM Wiki 實務、跨平台螢幕擷取與 OCR、VS Code 巢狀 Git 衝突防範與排障

- **來源文獻**：`SRC-138` (Andrej Karpathy 方法的 LLM Wiki 知識庫.md)、`SRC-139` (跨平台螢幕擷取與智慧辨識（OCR／翻譯）操作全指南.md) 以及 `SRC-140` (VS_Code與GitHub雙向同步之環境衝突、防範配置與推送錯誤排除指南.md)。
- **新增 Wiki 頁面**：
  - `[[跨平台螢幕擷取與智慧辨識實務]]` (新概念頁面)
- **更新 Wiki 頁面**：
  - `[[個人知識管理系統構築]]` (整合 Karpathy 方法 LLM Wiki 的本地環境準備、Schema 定義、Agent 配置與運作維護)
  - `[[Git GUI 與 GitHub 雙向同步實務]]` (整合巢狀 Git / VS Code 誤判、外層 `.gitignore` 阻斷與 cache 刷新命令、命令列 rebase 合併與 Google Drive gc 鎖定排障、GitHub 網頁對比及 Hunk Header 解讀)
- **更新索引**：[index.md](file:///c:/Obsidian/AI/wiki/index.md) 已同步更新，新增 1 個 Wiki 頁面與 3 筆文獻來源。
- **執行人**：Antigravity Agent
