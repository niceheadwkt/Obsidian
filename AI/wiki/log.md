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
  - `[[Claude（Anthropic）|Claude]]` (綜合實體頁面)
  - `[[Ollama]]` (綜合實體頁面)
  - `[[AI 工具與框架概覽]]` (綜合概念分析頁面)
- **更新索引**：[index.md](index.md) 已同步更新。
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
- **更新索引**：[index.md](index.md) 已同步更新，整理所有 41 篇文獻目錄。
- **執行人**：Antigravity Agent

## [2026-06-13] ingest | 批次匯入第六批：自動化、提示詞、Git 同步與商業思維

- **來源文獻**：`SRC-042` 至 `SRC-054` 共 13 篇原始文章（位於 `AI/raw/` 唯讀目錄下）。
- **新增 Wiki 頁面**：
  - `[[AI 第二大腦與 Claude Cowork 自動化]]`
  - `[[ChatGPT 影像生成提示詞指南]]`
  - `[[Git GUI 與 GitHub 雙向同步實務]]`
  - `[[商業案例與投資思維專題]]`
- **更新索引**：[index.md](index.md) 已同步更新，追加這 4 個新 Wiki 頁面與 13 筆文獻來源。
- **執行人**：Antigravity Agent

## [2026-06-13] ingest | 批次匯入第七批：Claude 一桌三櫃專案管理工作流 (EP10)

- **來源文獻**：`SRC-055` 共 1 篇原始文章（位於 `raw/` 唯讀目錄下）。
- **新增 Wiki 頁面**：
  - `[[Claude 專案管理一桌三櫃工作流]]`
- **更新索引**：[index.md](index.md) 已同步更新，追加此 Wiki 頁面與 1 筆文獻來源。
- **執行人**：Antigravity Agent

## [2026-06-14] ingest | 批次匯入第八批：母語式英文聽力與外語習得法 (KevinFeng)

- **來源文獻**：`SRC-056` 共 1 篇原始文章（位於 `raw/` 唯讀目錄下）。
- **新增 Wiki 頁面**：
  - `[[母語式英文聽力與外語習得法]]`
- **更新索引**：[index.md](index.md) 已同步更新，追加此 Wiki 頁面與 1 筆文獻來源。
- **執行人**：Antigravity Agent

## [2026-06-14] ingest | 批次匯入第九批：國外旅遊實用英語情境與求助指南

- **來源文獻**：`SRC-057` 共 1 篇原始文章（位於 `raw/` 唯讀目錄下）。
- **新增 Wiki 頁面**：
  - `[[國外旅遊實用英語情境]]`
- **更新索引**：[index.md](index.md) 已同步更新，追加此 Wiki 頁面與 1 筆文獻來源。
- **執行人**：Antigravity Agent

## [2026-06-15] ingest | 批次匯入第十批：NotebookLM 與 Claude 深度專題 (65篇)

- **來源文獻**：`SRC-058` 至 `SRC-122` 共 65 篇原始資料（含 62 篇 Markdown 文章及 3 篇 YAML 簡報樣式範本，位於 `raw/` 唯讀目錄下）。
- **新增 Wiki 頁面**：
  - `[[NotebookLM 進階應用與實戰指引]]`
  - `[[Claude 系統優化與 Token 節省指南]]`
  - `[[Claude Cowork 與 Agent Skill 實務]]`
  - `[[Claude Design 與前端美化實務]]`
  - `[[Claude 高階提示詞與應用場景]]`
- **更新索引**：[index.md](index.md) 已同步更新，追加這 5 個新 Wiki 頁面與 65 筆文獻來源。
- **執行人**：Antigravity Agent

## [2026-06-18] ingest | 批次匯入第十一批：Antigravity 核心概念與 Remotion 影片工程

- **來源文獻**：`SRC-123` 與 `SRC-124` 共 2 篇原始資料（位於 `raw/` 唯讀目錄下）。
- **新增 Wiki 頁面**：
  - `[[Antigravity 核心概念與五層記憶系統]]`
  - `[[Antigravity 與 Remotion 影片生成實務]]`
- **更新索引**：[index.md](index.md) 已同步更新，追加這 2 個新 Wiki 頁面與 2 筆文獻來源。
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
- **更新索引**：[index.md](index.md) 已同步更新，整理關聯並新增 4 個 Wiki 頁面與 1 筆文獻來源（SRC-125）。
- **執行人**：Antigravity Agent
## [2026-06-20] lint | 修復知識庫失效連結與路徑格式問題

- **描述**：全面修復並清理了 Wiki 知識庫中的所有失效連結與路徑前綴問題，確保知識鏈完整與健康。
- **修復內容**：
  - 修復 6 處完全損壞的原始文獻連結（如時間戳冒號 typo、檔名簡繁不一致、結尾多餘反單引號等）。
  - 修復 64 處 sources 前綴缺失問題，全部補齊 `raw/` 或 `sources/` 前綴。
  - 將未引用的文獻 `raw/投資理財專題報告：通膨與債券型基金投資分析.md` 作為 `SRC-130` 關聯至 `[[商業案例與投資思維專題]]`。
  - 修正了 `index.md` 中 `SRC-050`、`SRC-056`、`SRC-076`、`SRC-125` 的檔名與簡繁字元不一致問題。
- **結果**：最新 Advanced Lint 檢查結果為：失效連結 0，未引用來源 0。
- **儀表板更新**：重新執行並更新了 HTML 儀表板 [dashboard.html](../dashboard.html)。
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
- **更新索引**：[index.md](index.md) 已同步更新，關聯並整理這 7 筆新文獻來源。
- **執行人**：Antigravity Agent

## [2026-06-24] ingest | 批次匯入第十四批：Karpathy LLM Wiki 實務、跨平台螢幕擷取與 OCR、VS Code 巢狀 Git 衝突防範與排障

- **來源文獻**：`SRC-138` (Andrej Karpathy 方法的 LLM Wiki 知識庫.md)、`SRC-139` (跨平台螢幕擷取與智慧辨識（OCR／翻譯）操作全指南.md) 以及 `SRC-140` (VS_Code與GitHub雙向同步之環境衝突、防範配置與推送錯誤排除指南.md)。
- **新增 Wiki 頁面**：
  - `[[跨平台螢幕擷取與智慧辨識實務]]` (新概念頁面)
- **更新 Wiki 頁面**：
  - `[[個人知識管理系統構築]]` (整合 Karpathy 方法 LLM Wiki 的本地環境準備、Schema 定義、Agent 配置與運作維護)
  - `[[Git GUI 與 GitHub 雙向同步實務]]` (整合巢狀 Git / VS Code 誤判、外層 `.gitignore` 阻斷與 cache 刷新命令、命令列 rebase 合併與 Google Drive gc 鎖定排障、GitHub 網頁對比及 Hunk Header 解讀)
- **更新索引**：[index.md](index.md) 已同步更新，新增 1 個 Wiki 頁面與 3 筆文獻來源。
- **執行人**：Antigravity Agent

## [2026-06-26] ingest | 批次匯入第十五批：AI Agent 2.0、VoxCPM2 語音複製與六大工具橫向評比

- **來源文獻**：`SRC-141` 至 `SRC-148` 共 8 份原始文獻（位於 `raw/` 唯讀目錄下）。
- **新增 Wiki 頁面**：
  - `[[AI Agent 與 AntiGravity 2.0 基礎入門]]` (新概念頁面)
  - `[[AI 語音複製與 VoxCPM2 本地部署]]` (新概念頁面)
  - `[[AI 工具與任務場景橫向評比]]` (新概念頁面)
- **更新索引**：[index.md](index.md) 已同步更新，新增 3 個 Wiki 頁面與 8 筆文獻來源。
- **執行人**：Antigravity Agent

## [2026-07-09] ingest | 匯入第十六批：多專案共通規範與 Git 子模組文件結構

- **來源文獻**：`SRC-149` (多專案共通規範與文件管理結構指南.md，位於 `raw/` 唯讀目錄下)。
- **新增 Wiki 頁面**：
  - `[[多專案文件管理與 Git 子模組規範]]` (新概念頁面)
- **更新專案入口與索引**：
  - 更新專案根目錄 `README.md`，建立 Wiki 索引、行為規則與運作規範的雙向連結入口。
  - 更新 `index.md`，追加此文獻來源與新概念頁面，並建立系統配置與 AI 規範檔的歸檔導覽。
- **執行人**：Antigravity Agent

## [2026-07-09] ingest | 增量重整第一批：AI 工具與技術生態主題編譯

- **說明**：依據「批次增量重整」的安全策略，完成「主題 1：AI 工具與技術生態」的重新整理。
- **重新編譯與覆蓋頁面**：
  - `[[AI CLI 工具比較與選擇_摘要]]`
  - `[[Ollama]]` (實體頁面)
  - `[[Dify]]` (實體頁面)
  - `[[Warp 現代化終端機工具]]` (實體頁面)
  - `[[AI 工具與任務場景橫向評比]]`
  - `[[AI 工具與框架概覽]]`
- **更新索引**：[index.md](index.md) 已同步更新，更新這 6 個頁面的最後更新日期。
- **執行人**：Antigravity Agent

## [2026-07-09] ingest | 增量重整第二批：Git 版本控制與開發技術主題編譯

- **說明**：依據「批次增量重整」的安全策略，完成「主題 2：Git 版本控制與開發技術」的重新整理。
- **重新編譯與覆蓋頁面**：
  - `[[前端與系統開發常用技術]]`
  - `[[Git GUI 與 GitHub 雙向同步實務]]`
  - `[[多專案文件管理與 Git 子模組規範]]`
- **更新索引**：[index.md](index.md) 已同步更新，更新這 3 個頁面的最後更新日期。
- **執行人**：Antigravity Agent

## [2026-07-09] ingest | 增量重整第三批：個人知識管理與 Obsidian 技巧主題編譯

- **說明**：依據「批次增量重整」的安全策略，完成「主題 3：個人知識管理與 Obsidian 技巧」的重新整理。
- **重新編譯與覆蓋頁面**：
  - `[[個人知識管理系統構築]]`
- **更新索引與健康度**：[index.md](index.md) 已同步更新，更新該頁面的最後更新日期；並透過反單引號包裹模擬範例，解決多個潛在的失效連結警報。
- **執行人**：Antigravity Agent

## [2026-07-09] ingest | 增量重整第四批：商業案例與投資思維主題編譯

- **說明**：依據「批次增量重整」的安全策略，完成「主題 4：商業案例與投資思維專題」的重新整理。
- **重新編譯與覆蓋頁面**：
  - `[[商業案例與投資思維專題]]`
- **更新索引與交叉連結**：[index.md](index.md) 已同步更新，更新該頁面的最後更新日期；並建立其與 `[[AI 工具與任務場景橫向評比]]`（良興企業落地案例）的別名交叉連結。
- **執行人**：Antigravity Agent

## [2026-07-09] ingest | 增量重整第五批：外語學習與出國旅遊情境主題編譯

- **說明**：依據「批次增量重整」的安全策略，完成「主題 5：外語學習與出國旅遊情境」的重新整理。
- **重新編譯與覆蓋頁面**：
  - `[[母語式英文聽力與外語習得法]]`
  - `[[國外旅遊實用英語情境]]`
- **更新索引與交叉連結**：[index.md](index.md) 已同步更新，更新這 2 個頁面的最後更新日期；並建立這兩個頁面之間的雙向概念連結，優化知識整合關係。
- **執行人**：Antigravity Agent

## [2026-07-09] ingest | 增量重整第六批：網路系統基礎與監視器串流主題編譯

- **說明**：依據「批次增量重整」的安全策略，完成「主題 6：網路系統基礎與監視器串流」的重新整理。
- **重新編譯與覆蓋頁面**：
  - `[[網路系統基礎]]`
- **更新索引與交叉連結**：[index.md](index.md) 已同步更新，更新該頁面的最後更新日期；並建立其與 `[[前端與系統開發常用技術]]` 的別名交叉連結。
- **執行人**：Antigravity Agent

## [2026-07-09] ingest | 增量重整第六批（終）：剩餘所有 Wiki 頁面批次編譯

- **說明**：完成 Obsidian 知識庫中剩餘 20 個概念與實體 Wiki 頁面的重新整理與編譯，實現全知識庫 Ingest 目標。
- **重新編譯與覆蓋頁面**：
  - `[[LLM 到 Agent 的工程解析]]`、`[[AI 第二大腦與 Claude Cowork 自動化]]` 等剩餘所有 20 個檔案。
- **更新索引與交叉連結**：[index.md](index.md) 索引已全量更新，所有頁面的最後更新日期同步更新為今日。透過細緻調整雙向連結結構，成功消除了全知識庫所有的孤立頁面，雙向連結健康度達到 100%。
- **執行人**：Antigravity Agent

## [2026-07-15] ingest | 建立 Google Tasks 與 Obsidian MCP 安裝與驗收指南

- **說明**：建立了 Google Tasks 與 Obsidian MCP 伺服器的完整建立、配置與功能驗收指南文檔。
- **新增 Wiki 頁面**：
  - `[[AI/raw/2026-07-15-Obsidian_MCP_安裝建立與功能驗收指南.md|Obsidian MCP 安裝建立與功能驗收指南]]`
  - `[[AI/raw/2026-07-15-Google_Tasks_MCP_安裝建立與功能驗收指南.md|Google Tasks MCP 安裝建立與功能驗收指南]]`
- **執行人**：Antigravity Agent

## [2026-07-20] ingest | 全量匯入第十七批：AI Agent與企業AI經濟學等48份原始文獻

- **說明**：完成 48 份未歸檔原始文獻的全量 Ingest。
- **新增 Wiki 頁面**：
  - `[[AI Agent 實戰與 MCP 伺服器整合]]`
  - `[[Chrome Skills 與瀏覽器自動化實務]]`
  - `[[Claude Code 與 Workspace Pro 實戰]]`
  - `[[生成式 AI 企業應用與成本經濟學]]`
  - `[[軟體架構與發布自動化]]`
  - `[[智慧裝置與日常應用技巧]]`
- **更新 Wiki 頁面**：
  - `[[AI Agent 與 AntiGravity 2.0 基礎入門]]`
  - `[[NotebookLM 進階應用與實戰指引]]`
  - `[[商業案例與投資思維專題]]`
  - `[[AI 工具與框架概覽]]`
- **更新索引**：[index.md](index.md) 索引已同步更新，錄入 SRC-150 至 SRC-197。
- **執行人**：Antigravity Agent

## [2026-07-21] lint | 收工維護與 .gitignore 優化

- **說明**：執行今日收工檢查，優化 Git 排除清單配置，並檢查今日變更。
- **更新檔案**：
  - 修改 `[[.gitignore]]`：排除 `node_modules/` 以解決 Google Drive 雲端環境中 Git status 掃描過慢的問題。
- **偵測到今日新增原始素材**：
  - `[[AI/raw/Google AI Studio 1.md|Google AI Studio 1.md]]`
  - `[[AI/raw/Google_Drive_Cross_PC_Setup_Guide.md|Google_Drive_Cross_PC_Setup_Guide.md]]`
- **執行人**：Antigravity Agent

## [2026-07-23] ingest | 匯入第十八批：三師爸 Claude 基本功系列 EP01-EP10 與 Matt Pocock Skills 評估

- **說明**：完成 12 份今日原始素材的 Ingest 彙整與 Wiki 新頁面編譯。
- **新增 Wiki 頁面**：
  - `[[Claude 基本功與個人 AI 工作流實戰]]`
- **更新索引與關聯連結**：[index.md](index.md) 索引已同步更新，錄入 SRC-198 至 SRC-209。
- **執行人**：Antigravity Agent

## [2026-07-23] lint | 收工維護與知識庫健康度檢查

- **說明**：執行今日收工檢查，跑 Lint 腳本確保全域無斷鏈與孤立頁面，維護知識圖譜一致性。
- **執行人**：Antigravity Agent

## [2026-08-07] ingest | 全量匯入第十九批：AI Agent 基本功、點餐系統與 Kimi 發展專題等 20 份文獻

- **來源文獻**：`SRC-210` 至 `SRC-229` 共 20 份原始文獻（位於 `raw/` 唯讀目錄下）。
- **新增 Wiki 頁面**：
  - `[[Kimi 與月之暗面 (Moonshot AI) 發展專題]]`
  - `[[AI Agent 基本功系列實踐指南 (EP01-EP07)]]`
  - `[[一沐日雲端點餐與 MCP 系統開發實務]]`
  - `[[深度學習與大語言模型架構全景]]`
- **更新 Wiki 頁面**：
  - `[[Claude 高階提示詞與應用場景]]`
  - `[[Claude Cowork 與 Agent Skill 實務]]`
  - `[[AI 工具與框架概覽]]`
  - `[[Git GUI 與 GitHub 雙向同步實務]]`
  - `[[生成式 AI 企業應用與成本經濟學]]`
  - `[[AI Agent 實戰與 MCP 伺服器整合]]`
- **更新索引**：[index.md](index.md) 已同步更新，整理所有 20 筆新文獻來源與 4 個新增 Wiki 頁面。
- **執行人**：Antigravity Agent

## [2026-08-14] ingest | 全量匯入第二十批：GitHub 開源工具、Wordwall、Google Spark 與 Qwen 3.8 等 5 份文獻

- **來源文獻**：SRC-230 至 SRC-234 共 5 份原始文獻（位於 
aw/ 唯讀目錄下）。
- **新增 Wiki 頁面**：
  - [[GitHub 開源工具與 AI Skills 入門指南]]
  - [[Wordwall 與教育科技的 AI Agent 自動化實務]]
  - [[Google Spark 與 GAS 雲端自動化實務]]
  - [[Qwen 3.8 本地模型部署與企業 ROI 實務]]
  - [[OpenCode 新版架構與模型最佳搭配指南]]
- **更新 Wiki 頁面**：
  - [[AI Agent 基本功系列實踐指南 (EP01-EP07)]]
  - [[AI Agent 與 AntiGravity 2.0 基礎入門]]
  - [[AI 工具與框架概覽]]
  - [[Claude Cowork 與 Agent Skill 實務]]
  - [[生成式 AI 企業應用與成本經濟學]]
- **更新索引**：[index.md](index.md) 已同步更新，整理所有 5 筆新文獻來源與 5 個新增 Wiki 概念頁面。
- **執行人**：Antigravity Agent

## [2026-08-14] lint | 知識庫全域健康檢查與孤立頁面關聯修復

- **檢查範圍**：全域 54 篇 Wiki 概念與實體頁面。
- **健康檢查結果**：
  - **斷鏈修復**：修正 [[OpenCode 新版架構與模型最佳搭配指南|OpenCode]]、[[Kimi 與月之暗面 (Moonshot AI) 發展專題|楊植麟]]、三師爸 等多處引用格式，確保雙括號鏈結 100% 精準對齊。
  - **孤立頁面修復**：為 [[深度學習與大語言模型架構全景]]、[[Kimi 與月之暗面 (Moonshot AI) 發展專題]] 與 [[一沐日雲端點餐與 MCP 系統開發實務]] 建立交叉入站鏈結，消除知識孤島。
  - **Frontmatter 結構**：所有 54 篇頁面之 YAML 元數據（標籤、來源、日期）均通過驗證。
- **執行人**：Antigravity Agent

## [2026-09-16] setup | 建構跨電腦 (NB) 與跨 Agent (Antigravity/Claude Code/Codex) 全域規範同步體系

- **說明**：為解決跨辦公室與家裡 NB、以及三款主要 AI CLI/IDE（Antigravity、Claude Code、Codex）的全域運作規範一致性問題，建構基於 `chezmoi` 範本與 GitHub `dotfiles` 庫的動態同步架構。
- **更新 Wiki 頁面**：
  - `[[AI Agent 實戰與 MCP 伺服器整合]]`：擴充章節 2.2，記錄三方 Agent 規則路徑分發與 `{{ .chezmoi.homeDir }}` 跨裝置動態變數適配機制。
- **核心實作**：
  - Antigravity 規則：`dot_gemini/config/AGENTS.md.tmpl`
  - Claude Code 規則：`dot_claude/rules/global-rules.md.tmpl`
  - Codex 規則：`dot_codex/AGENTS.md.tmpl`
  - 家裡 NB 同步指令：`chezmoi update`
- **更新索引**：[index.md](index.md) 已同步更新最後維護日期。
- **執行人**：Antigravity Agent

## [2026-09-16] ingest | Google Flow 零門檻AI短片製造工具

- **來源文獻**：`SRC-235`（位於 `raw/` 唯讀目錄下）。
- **新增 Wiki 頁面**：
  - [[Google Flow AI短片製作實務]]
- **更新索引**：[index.md](index.md) 已同步更新，追加此 Wiki 頁面與 1 筆文獻來源。
- **執行人**：Antigravity Agent

## [2026-09-17] ingest | AI Agent 段考出題與教育科技自動化實務

- **來源文獻**：`SRC-236`（`AI Agent 教學應用：放大你的專業能力_輕鬆生成段考試卷.md`，三師爸直播逐字稿，位於 `raw/` 唯讀目錄下）。
- **更新 Wiki 頁面**：
  - `[[Wordwall 與教育科技的 AI Agent 自動化實務]]`：新增「多 Agent 段考出題自動化實戰」章節，涵蓋教材索引與舊卷格式建立流程、Bloom 認知層次難度控制、OMML 方程式與 Python 幾何繪圖，以及 AntiGravity／Codex／OpenCode 三家 Agent 出題實測比較與 Math Review Deck 互動複習網頁技能。
- **更新索引**：[index.md](index.md) 已同步更新該頁面說明、關聯來源數（2）與最後更新日期，並新增 `SRC-236` 至原始文獻目錄。
- **執行人**：Claude Code

## [2026-09-17] ingest | 全量匯入第二十三批：16 篇文獻（知識管理工具、Claude浮水印、GAS自動化、SQL/Node/React入門、ChatGPT提示詞更新、AI簡報與PPT編修、本地AI陪伴應用、OpenCode入門、教育Agent繪本應用、GCP數據工程、民生食安評測等）

- **來源文獻**：`SRC-237` 至 `SRC-252` 共 16 份原始文獻（位於 `raw/` 唯讀目錄下）。原規劃含 `sqlite 教學 - Google 搜尋.md` 一篇（純搜尋結果快照），經使用者決定直接刪除該檔案，故未列入 SRC 編號。
- **新增 Wiki 頁面**：
  - `[[民生消費品實測與食安評估]]`（台灣鮮乳市場實測、行銷迷思與選購指南）
  - `[[GCP 雲端排程與現代化數據工程實戰]]`（Cloud Scheduler、ETL/ELT 演進、dbt + BigQuery 實戰）
- **更新 Wiki 頁面**：
  - `[[個人知識管理系統構築]]`：新增第 5 節「五大筆記／知識工具橫向選型」（Notion/Obsidian/Heptabase/Gemini Notebook/Kuse AI）
  - `[[Claude（Anthropic）|Claude]]`：新增第 6 節「Claude 文字浮水印機制」
  - `[[智慧裝置與日常應用技巧]]`：新增第 4 節「台電 App 住宅用電分析」
  - `[[Google Spark 與 GAS 雲端自動化實務]]`：新增第四節「LINE AI 待辦機器人」零成本實戰案例
  - `[[前端與系統開發常用技術]]`：新增第 4～6 節（SQLite 資料庫入門、Discord 通訊協作平台、Node.js 與 React 全端基礎）
  - `[[ChatGPT 影像生成提示詞指南]]`：由 70 組更新為 120 組提示詞，新增第 4、5 節（靈感點子類、照片風格轉換類）
  - `[[Claude Design 與前端美化實務]]`：新增第 5、6 節（AI 改造原廠 PPT 四段指令、AI 簡報方法論 KH3R 法則）
  - `[[AI 語音複製與 VoxCPM2 本地部署]]`：新增第 6 節「桌面 AI 女友」本地陪伴應用趨勢
  - `[[OpenCode 新版架構與模型最佳搭配指南]]`：新增第五節「零基礎入門實戰：四階段工作流」
  - `[[Wordwall 與教育科技的 AI Agent 自動化實務]]`：新增第五節「生生有 Token」教案/簡報/繪本平台
- **Lint 修復**：修正 `SRC-235`（Google Flow）於 `index.md` 中登記檔名與實際檔案全形冒號後空格數不一致的問題。
- **更新索引**：[index.md](index.md) 已同步更新上述 12 個頁面之說明、關聯來源數與最後更新日期，並新增 `SRC-237` 至 `SRC-252`。
- **執行人**：Claude Code

## [2026-10-07] lint | Wiki 健康檢查與斷鏈修正

- **斷鏈修正（37 處）**：
  - 34 處 `[[sources/…]]` 指向的原始文獻實際已在 `raw/`，改為 `[[raw/…]]`（涉及 12 個頁面：AI Agent 基本功系列、Claude 基本功、Claude Cowork、Kimi 專題、一沐日點餐、深度學習架構、生成式 AI 成本、AI 工具概覽、Git GUI、Claude 高階提示詞等）。
  - `[[sources/chezmoi.md]]` → `[[AI/chezmoi.md]]`（chezmoi 筆記已於同日由根目錄移至 `AI/`）。
  - `[[Claude 專案管理一桌三櫃工作流]]` 的來源 `2026-06-13T211849` 版逐字稿已不存在，改指向現存最早版本 `2026-07-20T150840`。
  - 本檔 2026-09-17 紀錄中的 `[[OpenCode]]`、`[[楊植麟]]` 改為指向既有頁面的別名鏈結，`三師爸` 改為純文字（無對應頁面）。
  - `AI/chezmoi.md` 的 EP06 來源由不存在的 `2026-07-20T203320` 改為 `2026-07-28T083320`。
- **檢查結果**：
  - wiki 內已無斷鏈（`Wordwall` 頁表格內的 `\|` 別名為 Obsidian 合法寫法，非斷鏈）。
  - `raw/`、`sources/` 共 179 個斷鏈多為網頁剪藏 frontmatter 自動產生的作者／頻道鏈結（如 `[[數位時代 BusinessNext]]`），因兩者唯讀，不修改。
  - 無孤立頁面；`GCP 雲端排程與現代化數據工程實戰`、`智慧裝置與日常應用技巧`、`民生消費品實測與食安評估` 僅被 index／log 引用，建議日後與相關概念頁互相連結。
  - 除 wiki 內 `README.md` 外，所有頁面 frontmatter 皆具 tags／sources／created／updated。
- **執行人**：Claude Code

## [2026-10-07] ingest | 全球100大AI工具榜出爐！誰流量海放全場？有哪些隱形贏家？6大洞察一次看

- **來源**：`raw/2026-10-07T155412+0800-全球100大AI工具榜出爐！誰流量海放全場？有哪些隱形贏家？6大洞察一次看.md`（《數位時代》李先泰，2026-10-06，整理 a16z 第 7 版 Top 100 生成式 AI 消費應用榜）。剪藏後半段混入無關業配文（網銀國際《星城》），未納入。
- **新增頁面**：`[[a16z 第七版生成式 AI 應用榜與變現趨勢]]`（source-summary）：三張榜單與關鍵數字、六大洞察、隱形贏家分類表、新創四大破口；以 `[!WARNING]` 標註 ChatGPT 週活數 a16z（12 億）與 OpenAI 官方（超過 10 億）不一致。
- **更新頁面**：
  - `[[Claude（Anthropic）|Claude]]`：新增第 7 節「市場地位」（流量第三、付費訂戶與 Gemini 並駕齊驅、不放廣告、Max 方案占比 7.3%、7～8 月使用下滑警訊）。
  - `[[三大 AI 付費版選用與效能橫向對比]]`：新增第 6 節三家流量與付費數據對照表。
  - `[[生成式 AI 企業應用與成本經濟學]]`：新增第 7 節「消費端 AI 變現模式」，延伸閱讀加入新頁連結。
- **更新索引**：新增概念頁一列與 `SRC-253`，同步更新上述三頁說明、關聯來源數與日期。
- **執行人**：Claude Code

## [2026-10-08] ingest | Google Gemini 3 全能使用手冊！9大核心用法+17個最強功能實測

- **來源**：`raw/2026-10-08T130528+0800-Google Gemini 3 全能使用手冊！9大核心用法+17個最強功能實測 免費使用 分析Youtube 智慧體 谷歌全家桶 報告ppt 小白零基礎一個影片全學會！AI工具 AI賺錢 AI副業.md`（YouTube「盈夏AI輕創業」，2026-09-25）。匯入前已依使用者要求將原始檔與檔名轉為繁體，並依影片章節時間戳分段整理逐字稿。
- **新增頁面**：`[[Gemini 全能使用手冊與 Google 生態工作流]]`（source-summary）：呼叫入口、九大用法速覽表、Google 全家桶五服務整合細節、Gems 分享與 Deep Research 先審計畫等觀念、端到端工作流；以 `[!NOTE]` 標註模型版本與免費額度屬於快速變動資訊。片尾課程推銷未納入。
- **更新頁面**：
  - `[[AI 工具與框架概覽]]`：新增 7.2「Go Live 語音對話與 YouTube 提問側欄」，第 9 節補充 AI Studio TTS 語音生成。
  - `[[三大 AI 付費版選用與效能橫向對比]]`：第 3 節對比表後加入 Gemini 生態整合實操連結。
- **更新索引**：新增概念頁一列與 `SRC-254`，同步更新上述兩頁說明、關聯來源數與日期。
- **執行人**：Claude Code

## [2026-10-08] ingest | Gemini 對話：2026 銀髮經濟認知地圖

- **來源**：`raw/2026-10-08T150000+0800-Gemini 對話：2026銀髮經濟認知地圖.md`。原始網址為使用者的私人 Gemini 對話（https://gemini.google.com/app/a27da196512eb924），WebFetch 無法讀取，改經使用者已登入的 Chrome（CDP 9222）開新分頁擷取全文，整理為 Markdown 後存入 `raw/`；Gemini 的引用來源僅保留名稱。
- **新增頁面**：`[[2026 銀髮經濟認知地圖與樂齡數位課程商機]]`（source-summary）：全景認知地圖（市場、用戶、四大商業模式、四大黃金賽道）、智慧照護產品開發、樂齡社群營運、線上興趣課程、數位科技應用課程藍圖；以 `[!WARNING]` 標註內容為 AI 生成、市場數字未查證。
- **更新頁面**：
  - `[[Gemini 全能使用手冊與 Google 生態工作流]]`：關聯區加入本頁（影片 Deep Research 範例的實際追問紀錄）。
  - `[[商業案例與投資思維專題]]`：文末加入延伸閱讀連結。
- **更新索引**：新增概念頁一列與 `SRC-255`，更新商業案例頁日期。
- **執行人**：Claude Code

## [2026-10-08] ingest | AVA-GPT 對話：AVA_ERP MCP 工具建立標準流程

- **來源**：`raw/2026-10-08T140253+0800-AVA-GPT 對話：AVA_ERP MCP 工具建立標準流程.md`。原始網址為公司內部 AVA-GPT 對話（https://avagpt.chsteel.com.tw/c/c6d3e0b6-5fab-42ef-8a92-76ceba9c7fda），經使用者已登入的 Chrome（CDP 9222）擷取全文，移除模型思考內容與側邊欄後存入 `raw/`。
- **新增頁面**：`[[AVA_ERP MCP 工具建立標準流程]]`（source-summary）：AVA_ERP 四個會議室工具與用法、強制禁用政策、AVA-GPT 第 8 輪的兩階段標準流程與駕駛比喻；以 `[!WARNING]` 標註兩處錯誤（MCP 誤稱為 Model-Controller-Policy；工具定義應由 MCP 伺服器經 `tools/list` 宣告，而非管理員手寫），並補上修正後的七步驟流程與 FastMCP 示意範例。
- **更新頁面**：`[[AI Agent 實戰與 MCP 伺服器整合]]`：sources 加入本次來源，「實戰開發案例」加入本頁連結。
- **更新索引**：新增概念頁一列與 `SRC-256`，更新 MCP 頁說明、關聯來源數與日期。
- **執行人**：Claude Code

## [2026-10-08] ingest | 目前 2026 年最主流的 AI 發展趨勢

- **來源**：`raw/目前 2026 年最主流的 AI 發展趨勢.md`（原放在根目錄、未納入 git 的筆記，移入 `raw/`；未註明出處，格式與 Gemini Gems 選題助手產出一致）。
- **新增頁面**：`[[AI 工具應用內容趨勢與選題地圖]]`（source-summary）：三大主流內容方向、紅海與藍海、10 個選題與本庫既有頁面對照表（標示素材充足度），並列出三項知識缺口。
- **更新頁面**：`[[Gemini 全能使用手冊與 Google 生態工作流]]`：4.1 Gems 小節加入本頁作為選題助手產出實例。
- **更新索引**：新增概念頁一列與 `SRC-257`。
- **執行人**：Claude Code

## [2026-10-18] ingest | AI 越聰明，你越省力（三師爸 Sense Bar 直播）

- **來源**：`raw/2026-10-18T222039+0800-AI 越聰明，你越省力.md`。三師爸 Sense Bar 於 2026-10-18 之 YouTube 直播逐字稿（https://www.youtube.com/watch?v=Ysiva2yGEWE）。
- **新增頁面**：`[[AI 越聰明，你越省力_直播總結與學習卡]]`（source-summary）：AI 工具收斂分水嶺、AI 三代演進路徑（生成式 AI → AI Agent → Agent Bot）、Strata 架構本地 Agent 部署破局點、一條龍 AI 影音生成、Codex 視覺化動態教學、數學非選題命題排版與手寫考卷精準批改（200+ 題驗證，90%+ 準確率）、Google Drive 鏡像雙向同步與 Remote Control 架構、Claude Code 黃金四檔設定、10 張精選學習卡。
- **更新索引**：新增概念頁一列與 `SRC-258`。
- **執行人**：Antigravity Agent

## [2026-11-12] ingest | AI 工作流程自動化實作（n8n＋LINE＋Gemini）

- **來源**：`raw/2026-11-12T113821+0800-AI工作流程自動化實作（n8n＋LINE＋Gemini）課程重點整理.md`。經濟部產業發展署「AIUP 產發署人培專區」的線上課程（講師：李迦恩，共三章、3 小時 13 分），依 Vimeo 自動字幕整理；簡報上講師沒有念出的 API 網址與 JSON 範本，已依官方文件補充並標註。
- **新增頁面**：
  - `[[AI 工作流程自動化實作_n8n 課程總結]]`（source-summary）：Docker 本機架設 n8n、節點與工作流觀念、氣象 RSS 轉 JSON 推播 LINE（LINE Notify 已停止服務，改用 Messaging API）、Gemini 分支的提示詞設計，以及主幹與分支對照的驗證機制。
  - `[[n8n]]`（entity）：核心概念、萬用節點、三種部署方式比較、常用操作技巧，以及和 Dify、AI Agent 的比較。
- **更新頁面**：`[[AI 工具與框架概覽]]`（10.3 節的 n8n 改為連到新頁面）、`[[Dify]]`（新增第 5 節「相關工具比較」）。
- **更新索引**：新增概念頁一列、實體頁一列與 `SRC-259`。
- **執行人**：Claude Code

## [2026-11-16] ingest | 使用 Document AI 大規模自動擷取資料（Google Skills 技能徽章課程）

- **來源**：`raw/2026-11-13T112525+0800-使用 Document AI 大規模自動擷取資料（Google Skills 技能徽章課程）重點整理.md`。Google Skills 課程頁（course_templates/674）與各實驗室說明頁整理，未實際啟動實驗室；實驗室二頁面無法使用，只有課程卡片簡介。
- **新增頁面**：`[[Document AI 大規模資料擷取_課程總結]]`（source-summary）：課程結構（只有挑戰實驗室 GSP367 必修）、Form Parser 與專用剖析器、同步與非同步、textAnchor、Cloud Storage → Cloud Run → Document AI → BigQuery／Pub/Sub 管道、挑戰實驗室任務與排錯、ERP 單據擷取應用聯想（標為整理者補充）。
- **更新頁面**：`[[GCP 雲端排程與現代化數據工程實戰]]`（新增第 5 節 Document AI 擷取管道）、`[[跨平台螢幕擷取與智慧辨識實務]]`（加雲端 OCR 延伸連結）。
- **更新索引**：新增概念頁一列、更新兩列，新增 `SRC-260`。
- **執行人**：Claude Code

## [2026-11-16] ingest | 不能生成文字卻暴紅！ChatGPT 技術推手打造 AI 決策模型 Jev（數位時代）

- **來源**：`raw/2026-11-13T132312+0800-不能生成文字卻暴紅！ChatGPT技術推手打造AI決策模型Jev，為何讓開發者搶到當機？.md`。《數位時代》2026-09-21 李先泰整理（初稿為 AI 編撰）。剪輯檔後段夾帶另一篇無關文章（台灣數位安全發展協會 b-JADE 詐騙存證），依使用者同意不匯入。
- **新增頁面**：`[[Jev 與 System One 決策模型]]`（entity）：System One 定位、Choice／Score／機率判斷三種回答、真實機率與信心門檻、效能與價格、三大應用（取代分類器、Agent 監控、模型路由）、透過 Claude Code／Codex 的 TypeSafe skill 上手、使用注意、TypeSafe AI 公司背景。
- **更新頁面**：`[[生成式 AI 企業應用與成本經濟學]]`（新增 3.2 節「用決策模型擔任路由器：Jev」）。
- **更新索引**：新增實體頁一列、更新一列，新增 `SRC-261`。
- **執行人**：Claude Code

## [2026-11-17] ingest | AI 圍棋陪練上下集（數位時代「一天一 AI」）

- **來源**：`raw/2026-11-16T114023+0800-不會下圍棋，也能陪孩子練棋？她把AI設定成「圍棋家教」，看作業、出題都包了.md`（2026-11-09，上集）、`raw/2026-11-16T113459+0800-Claude把圍棋作業變遊戲！不會寫程式，也能做出5關兒童陪練.md`（2026-11-10，下集）。韋惟珊整理、讀者 Michelle 客座分享。兩個剪輯檔後段各夾帶一篇無關文章（b-JADE 詐騙存證、法國皇家 AI for Pets 徵件），沒有匯入。
- **新增頁面**：`[[AI 圍棋陪練：專案指示與成品小遊戲]]`（source-summary）：圍棋家教專案指示（角色、孩子進度、五個觸發詞情境）、拍照核對要點、Claude 成品 5 關遊戲的共用基本指令與關卡句型、試玩修正與可借用做法。
- **更新頁面**：`[[Claude（Anthropic）|Claude]]`（Artifacts 段補充成品設定、免費／付費差異與實作案例）、`[[Wordwall 與教育科技的 AI Agent 自動化實務]]`（關聯頁面）。
- **更新索引**：新增概念頁一列、更新 Claude 實體列，新增 `SRC-262`、`SRC-263`。
- **執行人**：Claude Code

## [2026-11-17] ingest | 用 Claude 一次整理出國行程！免費版製作旅遊網站（數位時代）

- **來源**：`raw/2026-11-16T113604+0800-用Claude一次整理出國行程！免費版製作旅遊網站，航班、地圖、記帳全都有.md`。《數位時代》蘇柔瑋 2026-11-16 整理（初稿為 AI 編撰）。剪輯檔的 `source` 網址（`article/93045/royalcanin_202611`）和內容不符，已在頁面註明。
- **新增頁面**：`[[Claude 成品製作旅遊行程網站]]`（source-summary）：免費版與 Pro 差異（連結分享、官方資料儲存、價格）、提示詞 6 欄位、先出規格再生成的 4 步驟、福岡六天五夜範例提示詞九段結構、使用限制。
- **更新頁面**：`[[Claude（Anthropic）|Claude]]`（同上一筆）。
- **更新索引**：新增概念頁一列，新增 `SRC-264`。
- **執行人**：Claude Code

## [2026-11-18] lint | 首次以 wiki-lint skill 健檢：反引號假連結與孤立頁修復

- **工具**：新增 `.claude/skills/wiki-ingest`、`.claude/skills/wiki-lint` 與檢查腳本 `AI/scripts/wiki_tool.py`（pending／check／lint／hubs），參考 Karpathy LLM Wiki gist 與 Fanko〈Claude＋Obsidian 第二大腦教學〉影片（素材尚未入庫）。
- **發現**：斷鏈 0、反引號包住的連結 82 處（23 頁，Obsidian 不當成連結）、孤立頁 5、frontmatter 問題 0、超過 120 天未更新 24 頁、raw 未匯入 28 篇。
- **已修復**：
  - 拆除 22 頁共 69 處指向既有頁面的反引號連結；`[[Gemini]]` 改指 `[[Gemini 全能使用手冊與 Google 生態工作流|Gemini]]`，`[[sources/Slack.md]]` 改為完整路徑。其餘 13 處為雙括號語法示範（如 `[[頁面名稱]]`），保留。
  - 孤立頁補回連：[[AI 越聰明，你越省力_直播總結與學習卡]]（自 [[Claude 基本功與個人 AI 工作流實戰]]、[[Wordwall 與教育科技的 AI Agent 自動化實務]]）、[[智慧裝置與日常應用技巧]]（自 [[2026 銀髮經濟認知地圖與樂齡數位課程商機]]、[[民生消費品實測與食安評估]]），另兩頁因反引號修復已有回連。孤立頁降為 0。
  - 健檢腳本的衝突統計改為只計含「衝突／矛盾」的警示；目前 2 處（a16z 用戶數、AVA-GPT 對 MCP 的誤釋），文中皆已寫明處理方式。
- **待決定**：24 頁自 2026-07 起未更新，其中 [[Claude 系統優化與 Token 節省指南]]、[[NotebookLM 綜合指南]]、[[Ollama]]、[[AI CLI 工具比較與選擇_摘要]] 含版本或價格等時效性資訊，建議有新素材時優先更新。
- **執行人**：Claude Code

## [2026-11-18] ingest | Claude＋Obsidian 第二大腦教學｜零基礎 7 步（Fanko AI 範式）

- **來源**：`raw/2026-11-18T074516+0800-Claude＋Obsidian 第二大腦教學｜零基礎 7 步，讓 AI 從陌生人變成最懂你的同事.md`。Fanko AI 範式 YouTube 影片（2026-11-17），含逐字稿與使用者附加的重點整理。首篇以 `wiki-ingest` skill 入庫並通過 `wiki_tool.py check` 評分。
- **新增頁面**：[[Claude＋Obsidian 第二大腦七步法]]（source-summary）：七步總覽（路由表、入口、入庫、地圖、品味、例行、客製）、各步要點與坑、可直接套用的提示詞，以及對照本知識庫進度的「我可以怎麼用」。
- **更新頁面**：[[AI 第二大腦與 Claude Cowork 自動化]]（新增「從零搭建的七步路徑」小節）、[[個人知識管理系統構築]]（LLM Wiki 段新增實作路徑與入庫 Skill 評分標準）、[[Claude Cowork 與 Agent Skill 實務]]（grill-me 段新增「先做順、再固化」的 Skill 建法）；三頁皆補上 sources。
- **更新索引**：新增概念頁一列、更新三列的來源數與日期，新增 `SRC-265`。
- **執行人**：Claude Code

## [2026-11-18] rename | Claude → Claude（Anthropic）

- **原因**：Windows 檔名不分大小寫，`AI/wiki/Claude.md` 會被 Claude Code 當成 `CLAUDE.md` 指令檔自動載入（約 9 KB），在 `AI/wiki` 目錄工作時平白佔用 Context。
- **處理**：以 `git mv` 改名為 [[Claude（Anthropic）]]，並將全 Vault 34 個檔案共 60 處 `[[Claude]]` 類連結改為 `[[Claude（Anthropic）|Claude]]`（保留原顯示文字；表格內使用 `\|` 跳脫；含 `AI/wiki_backup/`）。改名後 lint 斷鏈 0、孤立頁 0。
- **執行人**：Claude Code

## [2026-11-18] ingest | Agent Bot，一次搞懂基本原理（三師爸 Sense Bar 直播，兩篇合併）

- **來源**：`raw/2026-11-02T074859+0800-Agent Bot，一次搞懂基本原理.md`（YouTube J47Q77nFRUM）、`raw/2026-11-10T141555+0800-最新世代 AI Agent bot，一次搞懂基本原理.md`（YouTube 1MV-yuYLiV4，附使用者先前的重點整理）。兩檔為同一場 2026-11-02 直播，合併入庫。
- **新增頁面**：[[Agent Bot 基本原理與分層指揮架構]]（source-summary）：Agent Bot 定義與三家產品比較、AI 三階段、分層指揮架構、有自己電腦的意義、講者七種應用、建置前提，以及對照 ERP 與知識庫工作的「我可以怎麼用」。
- **更新頁面**：[[AI 越聰明，你越省力_直播總結與學習卡]]（三代演進段新增衝突警示與連結）、[[AI 時代的 Agent 術語與核心概念]]（新增 Agent Bot 詞條）；兩頁皆補上 sources。
- **待使用者決定的衝突**：Remote Control 能否取代 Agent Bot（10-18 與 11-02 直播說法不同）；舊頁「Dot（小巴）、GUACBOT」是否為 Dart 與 Grok Bot 的語音辨識誤寫。
- **更新索引**：新增概念頁一列、更新兩列，新增 `SRC-266`、`SRC-267`。
- **執行人**：Claude Code

## [2026-11-18] fix | 更正 Agent Bot 產品名稱誤寫

- **依據**：使用者確認 [[AI 越聰明，你越省力_直播總結與學習卡]] 中的「Dot（小巴）」「GUACBOT」為語音辨識誤寫，正確為 ChatGPT 的 Dart 與 Grok Bot（見 [[Agent Bot 基本原理與分層指揮架構]]）。
- **處理**：三代演進表第三代代表工具改為「Dart（ChatGPT）、Grok Bot」；「多端一致存取」段的「Dot 小巴」改為 Dart、Grok Bot；移除衝突警示中的產品名稱項，保留 Remote Control 一項待決定。
- **執行人**：Claude Code

## [2026-11-18] ingest | 別讓AI只做雜事！Anthropic主管公開「野心提示詞」3招（數位時代）

- **來源**：`raw/2026-11-04T133604+0800-別讓AI只做雜事！Anthropic主管公開「野心提示詞」3招，如何徹底釋放Claude極限？.md`。《數位時代》李先泰 2026-11-03 整理（初稿為 AI 編撰），原文為 Felix Rieseberg 2026-10-13 部落格。剪輯檔後段夾帶〈免費下載「會議紀錄整理師」〉（2026-09-17）一文，與主題無關，未匯入。
- **新增頁面**：[[Anthropic 野心提示詞：高度、深度、廣度三招]]（source-summary）：四方向與自我效能／目標設定理論、拉高度與 QBR 三階提示詞、挖深度四問提示詞與五技巧、拓廣度名詞換動詞與跨領域紅隊、適用前提，以及對照 ERP 工作的「我可以怎麼用」。
- **更新頁面**：[[Claude 高階提示詞與應用場景]]（新增第 7 節、於「紅隊安全測試」加衝突警示、補 sources，並修正 sources 第 5 行的 YAML 格式）、[[Agent Bot 基本原理與分層指揮架構]]（關聯頁面）。
- **待使用者決定的衝突**：角色扮演提示詞（「你是一位業界老手」）是否有效——舊頁推薦，Rieseberg 認為只換口吻、做法不變。
- **更新索引**：新增概念頁一列、更新一列，新增 `SRC-268`。
- **執行人**：Claude Code

## [2026-11-18] ingest | 1 年雲端 AI 預算 3 個月燒光！企業為何要搶回主權 AI？（數位時代未來商務）

- **來源**：`raw/2026-10-14T212236+0800-1 年雲端 AI 預算 3 個月燒光！企業為何要搶回主權 AI？拆解 token 帳單三層陷阱｜未來商務.md`。《數位時代》未來商務陳祈安 2026-10-13 整理（初稿為 AI 編撰），Podcast〈數位關鍵字 EP250〉黃亮崢對談 APMIC 吳柏翰。價格與評測數字為業者 2026-07 說法。
- **新增頁面**：[[主權 AI 與 token 帳單三層陷阱]]（source-summary）：主權同心圓、token 帳單三層陷阱與三種控制權、蒸餾小模型與知識分層成本分流、FinLLM 產業公版與 RAG 切塊漏讀對策、工廠或宮殿、企業第一步，以及對照 ERP 的「我可以怎麼用」。
- **更新頁面**：[[生成式 AI 企業應用與成本經濟學]]（新增 2.2 節）、[[Qwen 3.8 本地模型部署與企業 ROI 實務]]（補「地端不是零成本」說明）、[[RAG 與 DeepSearch 概念綜述]]（新增切塊漏讀的限制與對策）；三頁皆補上 sources。
- **衝突**：無。
- **更新索引**：新增概念頁一列、更新三列，新增 `SRC-269`。
- **執行人**：Claude Code

## [2026-11-18] ingest | 我被駭了，差點一夕破產！Google Cloud遭盜刷3萬元（數位時代）

- **來源**：`raw/2026-11-05T134617+0800-我被駭了，差點一夕破產！Google Cloud遭盜刷3萬元，追查才發現Mac早被植入木馬.md`。《數位時代》2026-11-04 刊出，醫師林佑儒第一人稱分享（原載 Facebook）。攻擊鏈與 AI Agent 參與皆為作者推測。無夾帶無關文章。
- **新增頁面**：[[假冒 Claude Code 官網木馬與雲端帳單盜刷事件]]（source-summary）：事件時間軸、四種可能原因排查、AMOS 類木馬檔案與 LaunchDaemons 自動執行、預算提醒不停機與 Hard Cap 限制、四個教訓，以及對照本機憑證、Windows 自動執行項目、雲端支出上限與 ERP 權限稽核的「我可以怎麼用」。
- **更新頁面**：[[GitHub 開源工具與 AI Skills 入門指南]]（資安防坑段新增實例）、[[主權 AI 與 token 帳單三層陷阱]]（「我可以怎麼用」補憑證被盜導致帳單失控、關聯頁面）、[[Claude（Anthropic）]]（Claude Code 安裝段新增「只從官方網址安裝」警示）；三頁皆補上 sources。
- **衝突**：無。
- **更新索引**：新增概念頁一列，新增 `SRC-270`。
- **執行人**：Claude Code

## [2026-11-18] ingest | ChatGPT、Claude對話會被拿去訓練嗎？9個隱私關卡＋關閉AI訓練設定（數位時代）

- **來源**：`raw/2026-09-17T132941+0800-ChatGPT、Claude對話會被拿去訓練嗎？9個隱私關卡＋關閉AI訓練設定.md`。《數位時代》李先泰 2026-09-16 整理（初稿為 AI 編撰）。原文「9 個隱私關卡」為互動卡片，剪輯檔未抓到，僅整理前言與「4 個設定」，並於頁面註明缺漏；文末資料來源中的事件僅列為延伸線索。
- **新增頁面**：[[ChatGPT 與 Claude 對話隱私與關閉訓練設定]]（source-summary）：Buckmaster 事件起因、是否被訓練取決於方案／設定／回饋、關訓練／關記憶／刪對話三者差異表、四個立即可調設定、延伸線索，以及對照 ERP 資料分級與帳號設定檢查表的「我可以怎麼用」。
- **更新頁面**：[[Claude（Anthropic）]]（Claude Code 運作機制補個人方案依模型改善開關而定）、[[Claude 高階提示詞與應用場景]]（記憶設定段新增「暫停記憶不等於清除」提示）、[[假冒 Claude Code 官網木馬與雲端帳單盜刷事件]]（關聯頁面）；前兩頁補上 sources。
- **衝突**：無（舊頁「API 與商業版不納入訓練」與本文「企業方案預設不訓練」一致）。
- **更新索引**：新增概念頁一列，新增 `SRC-271`。
- **執行人**：Claude Code

## [2026-11-18] ingest | 換AI不用重教一次！Claude⇄ChatGPT雙向搬家（數位時代）

- **來源**：`raw/2026-09-29T114755+0800-換AI不用重教一次！Claude⇄ChatGPT雙向搬家，記憶、對話紀錄、Skills轉移教學一次看.md`。《數位時代》蘇柔瑋 2026-09-28 整理（初稿由 AI 協助編撰），參考 Ruben Hassid《How to AI》與兩家官方文件。略過文中課程廣告與延伸閱讀連結。
- **新增頁面**：[[Claude 與 ChatGPT 雙向搬家：記憶、對話紀錄與 Skills]]（source-summary）：可搬資料對照、Claude→ChatGPT 六步驟（匯出索引檔、記憶檔提示詞、檔案庫／記憶／自訂指令、桌面版匯入）、ChatGPT→Claude 兩步驟與排查、Codex Skills 搬到 Claude、六項限制與 Codex CLI /import，以及對照本機規則檔與 chezmoi 的「我可以怎麼用」。
- **更新頁面**：[[Claude 高階提示詞與應用場景]]（記憶匯入改為 2026-09 新版位置並註明舊路徑、連到新頁）、[[Claude Cowork 與 Agent Skill 實務]]（新增 2026-09 統一介面說明、跨平台搬 Skill）、[[LLM 到 Agent 的工程解析]]（Skill 檔名衝突警示）、[[ChatGPT 與 Claude 對話隱私與關閉訓練設定]]（關聯頁面）；前三頁補上 sources。
- **待使用者決定的衝突**：Skill 說明檔名——本文說搬到 Claude 要改小寫 `skill.md`，[[LLM 到 Agent 的工程解析]] 說必須為大寫 `SKILL.md`。
- **更新索引**：新增概念頁一列，新增 `SRC-272`。
- **執行人**：Claude Code

## [2026-11-18] ingest | AI Agents 時代下的教學簡報完全體：HTML 簡報（三師爸直播）

- **來源**：`raw/2026-09-17T150844+0800-AI Agents 時代下的教學簡報完全體：HTML 簡報_別再被傳統簡報軟體綁架！帶你看見未來教學簡報的完全體。.md`（YouTube ZNdaQJOu8AU）。三師爸 Sense Bar 2026-05-24 直播逐字稿，檔尾附 2026-09-17 AI 摘要；以逐字稿為準，略過開場收音測試、贊助致謝與回饋問卷段落。
- **新增頁面**：[[HTML 簡報：AI Agent 時代的教學簡報完全體]]（source-summary）：HTML 與 Markdown 依讀者分工、人的注意力是稀缺資源、四大優勢、AI 生圖取代 Emoji 三種做法與成本、Firebase 文字雲與滑桿互動、打包成 Skill、直播問答，以及對照 ERP 文件與教學的「我可以怎麼用」。
- **更新頁面**：[[Claude 基本功與個人 AI 工作流實戰]]（自動化備課段補 HTML 簡報替代做法）、[[AI 工具與任務場景橫向評比]]（簡報任務 Claude 一列加連結）、[[Claude Cowork 與 Agent Skill 實務]]（「先做順、再固化」補實例）；前兩頁補上 sources。
- **衝突**：無。
- **更新索引**：新增概念頁一列，新增 `SRC-273`。
- **執行人**：Claude Code

## [2026-11-18] fix | 解決 Skill 主檔名衝突

- **依據**：使用者確認 Skill 主檔名為大寫 `SKILL.md`。
- **處理**：[[Claude 與 ChatGPT 雙向搬家：記憶、對話紀錄與 Skills]] 與 [[LLM 到 Agent 的工程解析]] 的衝突警示改為「衝突已解決」說明，註明《數位時代》「改小寫 `skill.md`」之說有誤；[[Claude Cowork 與 Agent Skill 實務]] 跨平台搬 Skill 段改為「主檔名維持 `SKILL.md`，不需改名」。
- **執行人**：Claude Code

## [2026-11-18] ingest | SogaType 語音輸入操作踩坑與排錯實戰全紀錄

- **來源**：`raw/2026-09-20T174500+0800-SogaType語音輸入操作踩坑與排錯實戰全紀錄.md`。使用者 2026-09-20 個人排錯紀錄（ROG Zephyrus G14、Windows 11、SogaType v0.9.1）。原文中的登入帳號、裝置 ID 與本機路徑未寫入 Wiki。
- **新增頁面**：[[SogaType 語音輸入 Windows 排錯紀錄]]（source-summary）：SogaType 收音／熱鍵／輸出機制、四個坑（麥克風端點停用、F 鍵多媒體鍵、Ctrl+Space 衝突、UIPI 擋模擬貼上）、F9 翻譯模式、最佳實務，以及對照 Claude Code 語音輸入與自動化工具的「我可以怎麼用」。
- **更新頁面**：[[AI Agent 實戰與 MCP 伺服器整合]]（全域設定「語音輸入錯字正規化」加連結、補 sources）。
- **略過**：`raw/2026-09-17T132524+0800-Gmail技巧大全：139個收件匣整理、排程寄信與自動分類設定.md` 剪輯失敗（內文僅「`後綴詞` 產」），未匯入，待使用者重新剪輯。
- **衝突**：無。
- **更新索引**：新增概念頁一列，新增 `SRC-274`。
- **執行人**：Claude Code

## [2026-11-18] ingest | NoType 專案深度分析與演進建議書

- **來源**：`raw/NoType 專案深度分析與演進建議書.md`。使用者自製語音輸入工具 NoType（`C:\aiTest\NoType`）的技術分析文件，無日期。
- **新增頁面**：[[NoType 語音輸入專案分析與演進建議]]（analysis）：與 SogaType 八面向對比、現有優勢、熱鍵／UIPI／前景視窗感知／記憶體直傳四項改善、Whisper prompt＋LLM 兩層台灣詞庫、資料庫選型（結論：現階段用 JSON 雙軌）、三階段藍圖，以及對照 ERP 專有名詞與技術選型的「我可以怎麼用」。
- **更新頁面**：[[SogaType 語音輸入 Windows 排錯紀錄]]（最佳實務熱鍵段加衝突警示、關聯頁面）。
- **待使用者決定的衝突**：`Alt+Space` 能否當語音輸入熱鍵——SogaType 紀錄建議可用，NoType 建議書指出會觸發 Windows 系統選單導致貼空。
- **更新索引**：新增概念頁一列，新增 `SRC-275`。
- **執行人**：Claude Code

## [2026-11-18] query | AI Token 用量比較：Desktop 與 CLI 深度分析

- **操作主題**：整理並深度擴充 AI Token 用量在 Desktop（桌面 GUI）與 CLI（命令列 TUI）之比較與架構分析。
- **新增頁面**：[[AI Token用量比較_Desktop與CLI深度分析]]（analysis 類型）。
- **核心內容**：剖析系統前置開銷、MCP 稅（MCP Tax）、Unix 管線源頭過濾、對話歷史膨脹與計費模型衝擊，並提供調優實踐手冊與決策矩陣。
- **更新索引**：[index.md](index.md) 同步更新。
- **執行人**：Antigravity Agent
## [2026-11-18] ingest | 副總統親臨高喊生技護體神山！藥華藥前8月營收超車去年整年，為何股價不漲反跌？（理財周刊）

- **來源**：`raw/2026-09-22T162903+0800-副總統親臨高喊生技護體神山！藥華藥前8月營收超車去年整年，為何股價不漲反跌？.md`。《理財周刊》投研部 2026-09-18 個股分析。略過廣告橫幅、推薦文章元件與延伸閱讀連結。
- **更新頁面**：[[商業案例與投資思維專題]]（新增第 5 節「個股案例：藥華藥（6446）」：股價反跌原因、財報表、自建通路與 MPN 營運槓桿、波多黎各產能、六大風險；補上「我可以怎麼用」段落與 sources）。非 AI 主題，擴充既有投資頁，未另開新頁。
- **衝突**：無。
- **更新索引**：更新概念頁一列（來源數 10 → 11），新增 `SRC-276`。
- **執行人**：Claude Code

## [2026-11-18] ingest | Claude 訂閱方案、Claude Code 安裝教學、Claude 操作模式（Desktop 與 CLI 登入及額度比較）

- **來源**：`raw/2026-06-15T153635+0800-Claude 2026最新訂閱方案｜Claude ai免費版功能有什麼？Agent SDK費用怎麼算？.md`、`raw/2026-06-15T160222+0800-Claude Code安裝教學｜Desktop App、終端機2種方式怎麼裝？不懂程式也能秒上手.md`、`sources/01_AI_Tools/Claude 操作模式與功能介紹.md`。
- **更新頁面**：[[AI Token用量比較_Desktop與CLI深度分析]]（新增第 1 節「登入方式與額度歸屬」：兩種登入方式對照、互動式／程式化兩額度池與 API Key 按量計費、快速判斷表、雲端推理架構；原第 1–5 節順延為第 2–6 節；補 sources、一句話重點與「我可以怎麼用」）；[[Claude 系統優化與 Token 節省指南]]（新增延伸閱讀回連）。
- **衝突**：原第 3 節（計費模式）將 CLI 歸為「API 計費為主」，與訂閱帳號登入 CLI 共用訂閱額度的事實不符，已加 `> [!WARNING]` 標註，表格 CLI 欄限定為 API Key 情境。〈Claude 操作模式與功能介紹〉模型名稱已過時，加註說明。
- **更新索引**：頁面列來源數 4 → 7、描述補登入與額度池；`SRC-003`、`SRC-082`、`SRC-115` 加註關聯頁面。
- **執行人**：Claude Code

## [2026-11-18] ingest | 2026老人健保補助、敬老卡點數（數位時代）

- **來源**：`raw/2026-10-06T091411+0800-2026老人健保補助｜22縣市資格、免申請、排富門檻一次看.md`（《數位時代》2026-09-08，初稿為 AI 編撰；略過文後 AWS 高雄 AI 創新日業配文與熱門文章清單）、`raw/2026-10-06T091350+0800-敬老卡點數｜22縣市最新額度、用途一次看，用不完會歸零嗎？.md`（《數位時代》2026-10-05；剪輯失敗，內文僅「縣內公車、客運、台鐵」，只採用 frontmatter 摘要並於頁面註明缺漏）。
- **更新頁面**：[[2026 銀髮經濟認知地圖與樂齡數位課程商機]]（依使用者指示併入：新增第 6 節「長者福利實務」——老人健保補助法源、826 元上限計算、免申請機制、22 縣市三類資格表、離島與新北細節、注意事項；敬老卡 2026-10 調整摘要；新增第 7 節「我可以怎麼用」；原第 6 節順延為第 8 節；補 tags 與 sources）。
- **衝突**：無。
- **更新索引**：更新概念頁一列（來源數 1 → 3），新增 `SRC-277`、`SRC-278`。
- **執行人**：Claude Code

## [2026-11-18] update | 補齊敬老卡 22 縣市額度表

- **依據**：使用者要求補齊。raw 剪輯不完整，改依原文網頁（bnext.com.tw/article/92501，2026-10-05，林育萱整理，初稿為 AI 編撰）重新讀取，用途欄以改寫方式摘要。略過頁面下方贊助文章。
- **處理**：[[2026 銀髮經濟認知地圖與樂齡數位課程商機]] 第 6.2 節改寫：10 月五縣市調整表、22 縣市額度／用途／年齡表、點數歸零規則（台北、台中、台東月底歸零；高雄季末歸零）、使用率數據；第 7 節補兩點用法。索引描述同步更新。
- **執行人**：Claude Code

## [2026-11-18] ingest | 超強做動畫技能：全 Agent 通用（三師爸直播）

- **來源**：`raw/2026-10-27T220731+0800-超強做動畫技能_全agent通用_說明欄附上github repo.md`（YouTube vN-VWqVojRs）。三師爸 Sense Bar 2026-10-18 直播逐字稿。直播中的工具消息（Argon 額度、Gemini 桌面版、DeepSeek 新版）為口述未查證，僅簡短記錄。
- **新增頁面**：[[claude-motion-explainer 科普解說動畫技能]]（source-summary）：技能目的與定位、Roadster 三招原理解說實例、現場修改（粗體、三色主題、加圖片影片、Breeze／Edge TTS）、Colab 四倍速生成與隱私處理、直播觀點，以及對照 ERP 教學動畫的「我可以怎麼用」。
- **更新頁面**：[[Antigravity 與 Remotion 影片生成實務]]（關聯頁面補後續發展、補 sources）、[[AI 語音複製與 VoxCPM2 本地部署]]（新增旁白 TTS 選擇、補 sources）、[[HTML 簡報：AI Agent 時代的教學簡報完全體]]（關聯頁面）。
- **略過（剪輯不完整，待重新剪輯）**：`raw/2026-10-23T205650+0800-不用 本地顯卡_付費生成 AI 的兩種方式_全攻略附 Repo.md`、`raw/2026-10-23T213411+0800-AI 生成影片，直播創造新角色人物資產.md`（皆僅影片連結、無逐字稿）、`raw/2026-11-04T084754+0800-ChatGPT做LINE貼圖、月曆、菜單怎麼下指令？30組生活生圖提示詞一次看.md`（內文僅數字）。
- **衝突**：無。
- **更新索引**：新增概念頁一列，新增 `SRC-279`。
- **執行人**：Claude Code

## [2026-11-18] ingest | 【下集】AI 影片原理全公開：MiniMax-H3 本機實測（三師爸）

- **來源**：`raw/2026-11-01T200728+0800-【下集】AI 影片原理全公開：MiniMax-H3 本機實測，踩過的坑全部告訴你.md`（YouTube ZBQXXOVZK8M）。三師爸 Sense Bar 2026-10-10 影片下集逐字稿；上集不在素材中。
- **新增頁面**：[[MiniMax-H3 本機 AI 短片製作原理與踩坑]]（source-summary）：整體流程、角色一致性三層、首幀三家實測與 Blender 排空間、BreezyVoice 選字配音與 H3 對嘴、DMAD 加速與放大比較、十項試過的做法、音效配樂混音、審核分工、商用授權表，以及「我可以怎麼用」。
- **更新頁面**：[[AI 語音複製與 VoxCPM2 本地部署]]（台詞先轉簡體、BreezyVoice 與 Breeze TTS 2 授權）、[[claude-motion-explainer 科普解說動畫技能]]（Breeze TTS 授權待確認警示、關聯頁面）、[[Google Flow AI短片製作實務]]（開頭相關主題加連結）；前一與末頁補 sources。
- **待使用者確認**：動畫技能使用的是 Breeze TTS 2（不可商用）還是 BreezyVoice（可商用）。
- **更新索引**：新增概念頁一列，新增 `SRC-280`。
- **執行人**：Claude Code

## [2026-11-18] ingest | 全方位 LoRA 訓練完整指南、Open Pose & Costume

- **來源**：`raw/全方位 LoRA 訓練完整指南 (擴散模型與大型語言模型).md`（無作者、無日期的技術整理）；`raw/2026-11-05T131048+0800-Open Pose & Costume 收錄超過 5,800 張參考圖，人物、姿勢、服裝都有，讓你 AI 生圖更容易.md`（電腦王阿達 2026-11-04，剪輯僅含 frontmatter 摘要與一句授權提醒）。
- **新增頁面**：[[LoRA 微調訓練指南]]（concept）：LoRA 原理與優勢、LLM 資料格式／工具／參數、擴散模型資料集與標註／工具／參數、輸出與過擬合欠擬合診斷，以及對照 ERP 知識（微調 vs RAG）與 AI 短片角色的「我可以怎麼用」。
- **更新頁面**：[[ChatGPT 影像生成提示詞指南]]（防錯段新增 Open Pose & Costume 參考圖庫、補 sources）、[[MiniMax-H3 本機 AI 短片製作原理與踩坑]]（角色 LoRA 與參考圖連結、補 sources）、[[Qwen 3.8 本地模型部署與企業 ROI 實務]]（關聯頁面）。Open Pose & Costume 內容過短，未另開新頁。
- **衝突**：無。
- **更新索引**：新增概念頁一列，新增 `SRC-281`、`SRC-282`。
- **執行人**：Claude Code

## [2026-11-18] ingest | 跨 Agent 技能共用整合實施規劃書、如何看四大工具的目錄連接點

- **來源**：`raw/CROSS_AGENT_SKILLS_SHARING_PLAN.md`（使用者規劃書，最後更新 2026-10-06）、`raw/如何看四大工具的目錄連接點（NTFS Junction）.md`（使用者操作說明）。
- **新增頁面**：[[跨 Agent 技能共用：中央倉庫與 NTFS Junction]]（analysis）：建倉前五項問題、中央倉庫＋Junction＋私人 Git repo 架構與定案理由、兩支腳本行為、六項踩坑、檢視連接點三法與驗證清單，以及日常維護與收工檢查的「我可以怎麼用」。
- **更新頁面**：[[AI Agent 實戰與 MCP 伺服器整合]]（2.2 節加衝突警示、補 sources）、[[AI Agent 基本功系列實踐指南 (EP01-EP07)]]（EP06 加衝突警示、補 sources）、[[Claude 與 ChatGPT 雙向搬家：記憶、對話紀錄與 Skills]]（見下方 fix、關聯頁面）。
- **衝突**：兩篇舊頁寫「Agent Skills 用 chezmoi 同步」，新規劃書定案為私人 Git repo、技能不用 chezmoi。依使用者同意，以警示框標註並保留原文。
- **fix**：[[Claude 與 ChatGPT 雙向搬家：記憶、對話紀錄與 Skills]] 的「我可以怎麼用」原寫「Skills 用 chezmoi 跨電腦同步」為 Claude Code 先前誤寫，已更正為「全域規則用 chezmoi、Skills 用私人 Git repo＋Junction」。
- **更新索引**：新增概念頁一列，新增 `SRC-283`、`SRC-284`。
- **執行人**：Claude Code

## [2026-11-18] ingest | ERP 畫面擷取含滑鼠提示、Mattermost CI/CD、AI 音樂生成、NotebookLM 與 Napkin AI 課程

- **來源**：`raw/ERP畫面擷取含滑鼠提示_操作說明.md`（使用者 2026-10-22 操作說明；範例截圖未匯入）、`raw/mattermost_ci_cd_integration_guide.md`、`raw/ai_music_generation_guide.md`（皆無作者、無日期技術整理）、`raw/搞懂NotebookLM與Napkin AI-提升你的知識管理力.md`（臺南市 e 學補給站課程筆記，巨匠電腦蘇世榮講師）。
- **新增頁面**：[[AI 音樂生成：Suno 與 YuE2]]（concept；YuE2 範例程式碼標註未經驗證）、[[NotebookLM 與 Napkin AI 知識管理課程]]（source-summary）。
- **更新頁面**：[[跨平台螢幕擷取與智慧辨識實務]]（新增第 6 節擷取含滑鼠提示畫面，`Win+Shift+S` 處註明不適用）、[[軟體架構與發布自動化]]（新增 1.1 節 ChatOps：Mattermost 與 CI/CD 整合）、[[NotebookLM 進階應用與實戰指引]]、[[NotebookLM 綜合指南]]、[[MiniMax-H3 本機 AI 短片製作原理與踩坑]]、[[a16z 第七版生成式 AI 應用榜與變現趨勢]]（皆加回連）；擴充頁補 sources。
- **衝突**：無。
- **更新索引**：新增概念頁兩列，新增 `SRC-285`～`SRC-288`。
- **執行人**：Claude Code

## [2026-11-20] ingest | Claude Code 設定大洗牌（Opus 5.5 時代 CLAUDE.md 愈短愈好）、Google AI Pro 八種隱藏工具

- **來源**：`raw/2026-11-18T162924+0800-Claude Code設定大洗牌！進入Opus 5.5時代之後，為何CLAUDE.md愈短愈好？.md`（數位時代，李先泰，2026-11-17，內容來自 Lydia Hallie 2026-11-12 演講）；`raw/2026-11-19T143623+0800-買了Google AI Pro只會用Gemini聊天？這8種隱藏AI工具，幫你把訂閱費用好用滿.md`（數位時代，蘇柔瑋，2026-11-18）。後者剪輯檔後半段為亞馬遜跨境電商高峰會業配文，已略過。
- **新增頁面**：[[Claude Code 少叮嚀多設限：Opus 5.5 時代最佳實踐]]（source-summary）：CLAUDE.md 只留程式碼看不出來的事、deny 規則與沙盒、三層驗證點、projects 派工、五項調整與對照使用者全域規範的「我可以怎麼用」；[[Google AI Pro 訂閱權益與八大工具選用]]（source-summary）：八工具對照、額度與 AI 點數規則、選用建議。
- **更新頁面**：[[Claude 系統優化與 Token 節省指南]]（第 4 節加衝突警示、延伸閱讀加連結）、[[Claude（Anthropic）]]（第 3 節後加說明框）、[[Gemini 全能使用手冊與 Google 生態工作流]]、[[Google Flow AI短片製作實務]]（補 Pro 每月 1,000 點）、[[NotebookLM 綜合指南]]（改名 Gemini Notebook）、[[Antigravity 核心概念與五層記憶系統]]（關聯頁面）。
- **衝突**：舊頁「CLAUDE.md 應寫入建置與測試指令」vs 新頁「只留程式碼看不出來的事」，以警示框標註，待使用者決定。
- **更新索引**：新增概念頁兩列，新增 `SRC-289`、`SRC-290`。
- **執行人**：Claude Code

## [2026-11-20] fix | Claude 系統優化與 Token 節省指南：更正 12 條規則

- **原因**：第 4 節「12 條優化核心規則（精華）」列的三條（只寫建置／測試指令、單一事實來源、100 行以內）在來源 `raw/2026-06-15T160238+0800-CLAUDE.md這樣寫才對！12條規則一次整理…` 中查無出處；同日 ingest 時依此加的衝突警示前提也不成立。
- **更正**：[[Claude 系統優化與 Token 節省指南]] 第 4 節改寫為 4.1 前提（時間與模型、演進來源、測試條件、結果、適用範圍、附帶發現）、4.2 原文 12 條行為規則、4.3 依 [[Claude Code 少叮嚀多設限：Opus 5.5 時代最佳實踐]] 新原則的刪／搬家／改寫對照（註明為 Claude Code 推論），衝突警示改為「12 條實測（Opus 4.x）vs Opus 5.5 時代少叮嚀」。
- **執行人**：Claude Code

## [2026-11-20] fix | Claude 系統優化與 Token 節省指南：自我審查提示改回原文

- **原因**：第 4 節「規則自我審查 Prompt 範本」的 5 個條件被改寫過，第 5 條「只寫建置／測試指令」在來源 `raw/2026-06-15T154927+0800-CLAUDE.md規則越加越爛？…` 中查無出處。
- **更正**：改為 4.4 節，換成原文自我修正提示（5 個篩選條件＋三項輸出）、補上「收到報告後怎麼刪」五步驟、「setup-audit 每週一 9 點排程」提示詞與使用前提，並以 TIP 連到 [[Claude Code 少叮嚀多設限：Opus 5.5 時代最佳實踐]] 的 `/doctor prompt-audit`。
- **執行人**：Claude Code
