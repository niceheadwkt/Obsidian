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
