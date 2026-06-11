# Obsidian LLM Wiki 知識庫倉庫

本倉庫是一個基於 Andrej Karpathy 提出的 **LLM Wiki** 模式搭建的個人編譯型知識庫。它將 Obsidian 的本地雙向連結特性與 LLM 的自動化整理、維護能力相結合，實現知識的持續沉澱與複利。

## 知識庫目錄架構
- **`AI/sources/`**：原始資料庫。放置所有 Immutable（不可變）的原始文件（如剪輯文章、PDF、逐字稿等）。
- **`AI/wiki/`**：核心 Wiki。由 AI 代理自動編譯、交叉參考並維護的 Markdown 頁面。
- **`AI/schema.md`**：Wiki 運作規範文件。定義了 Wiki 的格式、命名標準與 AI 代理的工作流程。
- **`CLAUDE.md`**：專案根目錄的 AI 指令檔。任何 AI 代理（如 Claude Code 或 Antigravity）啟動時，都會讀取並遵守此規則。

## 快速開始
1. **使用 Obsidian 開啟**：將本專案的 `AI/` 資料夾作為獨立的 Vault 載入至 Obsidian 軟體中。
2. **放置原始資料**：將您要整理的文章或 PDF 存入 `AI/sources/`。
3. **呼叫 AI 代理進行編譯**：在終端機啟動您的 AI 代理，輸入指令，例如：
   > 「幫我匯入 sources 中新加的文章，並更新對應的 Wiki 概念頁面。」
4. **瀏覽成果**：在 Obsidian 中開啟關聯圖譜 (Graph View)，享受自動連結、編譯後的知識網路。

---

## 常用 Git 指令
```bash
# 提交與推送變更
git add .
git commit -m "update wiki"
git push origin main
```
