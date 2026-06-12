# 個人知識 Wiki (Compounded Wiki)

此資料夾是由 AI 代理程式 (LLM Agent) 自動生成與增量維護的 **「編譯後個人知識庫 (Persistent Compounding Wiki)」**。

## 核心概念
- **編譯一次，持續累積**：不同於每次提問都需要重新檢索原始文件的傳統 RAG 系統，這裡的頁面是經由 AI 將原始資料提取、融合並交叉鏈結後產生的精煉知識。
- **主動維護**：AI 代理會主動更新實體頁面、概念總結，並在發現新舊資料衝突時進行標記。
- **寫入權限**：**此目錄下的內容主要由 AI 寫入與維護**。雖然您隨時可以閱讀、點擊連結與查看 Obsidian 關係圖譜，但建議避免手動大範圍修改此處的結構，以免與 AI 代理的維護邏輯產生衝突。

## 目錄關鍵檔案
- [`index.md`](file:///c:/Obsidian/AI/wiki/index.md)：內容大綱與索引。AI 在每次導入新資料後會自動更新此索引。
- [`log.md`](file:///c:/Obsidian/AI/wiki/log.md)：編譯與查詢的 chronological 歷史日誌。

## 頁面命名與格式
- AI 會在每篇 Wiki 頁面頂部加上 YAML Frontmatter（包含建立日期、關聯原始文獻、標籤等）。
- 使用 `[[雙括號]]` 來建立頁面間的交叉引用，這在 Obsidian 中能渲染出完美的知識圖譜。
