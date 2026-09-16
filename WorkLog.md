# 工作筆記

**更新日期**：2026-09-16

## 上次做到哪
- **多 Agent 全域規範與跨電腦同步體系建立 (chezmoi & GitHub)**：
  - 將 Antigravity、Claude Code、Codex 三大工具的全域規範統一（包含開工、收工、Edge-TTS 語音播報、語音輸入錯字校正）。
  - 使用 `chezmoi` 範本（`{{ .chezmoi.homeDir }}`）管理三方規則與 PowerShell Profile，相容公司電腦與家裡筆電（NB）。
  - 將變更全數推送到 GitHub `niceheadwkt/dotfiles`，家裡 NB 只需執行 `chezmoi update` 即可完成同步。
  - 完成《AI Agent 基本功 EP06 跨 Agent、跨電腦協作同一個專案》重點精華摘要，已整理追加至 `chezmoi.md` 與對應原始文獻中。
- **工安稽查單號 1150504015 誤植資料刪除案 (RQ11508035)**：
  - 完成 `HGJJG01` 全系統關聯資料表探索與異動申請表 ODT 產出。

## 相關筆記連結
- [[chezmoi]]
- [[AI/wiki/AI Agent 實戰與 MCP 伺服器整合]]
- [[HGJJG01_稽查單號_1150504015_資料關聯與刪除計畫]]

## 下一步
- 回到家裡筆電執行 `chezmoi update` 驗證三方 AI CLI / IDE 規則是否順暢生效。
- 待工安稽查單號 1150504015 ODT 申請表內部簽核後，於維護時段至正式機執行備份與刪除。
