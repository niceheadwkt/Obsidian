# 原始資料庫 (Raw Sources)

此資料夾是您的個人知識庫之 **「不可變資料源 (Immutable Source of Truth)」**。

## 放置規範
- **用途**：放置所有您希望 AI 讀取、彙整、總結的原始文件。包括：
  - 網頁剪輯文檔（推薦使用 Obsidian Web Clipper 轉換為 Markdown）
  - 論文與報告（PDF、TXT）
  - 會議或 Podcast 逐字稿 (Transcripts)
  - 數據檔案與圖像
- **唯讀原則**：AI 代理在讀取此資料夾內的文件時，**絕對不會**對其內容進行任何修改或刪除。所有編譯與更新均會寫入至 `wiki/` 目錄。
- **命名建議**：使用清晰且具描述性的英文或中文檔名，例如 `2026-06-11-article-title.md`。

## 快速導入工具推薦
- **Obsidian Web Clipper**：瀏覽器套件，一鍵將網頁內容轉為 Markdown 格式並儲存。
- **附件自動下載**：建議在 Obsidian 的「檔案與鏈結 (Files and links)」設定中，將「附件資料夾路徑 (Attachment folder path)」設定為 `sources/assets/`。
