# AI CLI 色彩配置 工作筆記

## 上次做到哪 (2026-10-05)
- **目的**：在 PowerShell 啟動不同 AI CLI 時，分頁自動換成專屬背景色，一眼就能分辨目前使用哪個 AI。
- **機制**：`~/Documents/PowerShell/ai-cli-colors.ps1` 用 OSC 4/10/11/12 跳脫序列暫時換色，離開（含 Ctrl+C）後以 OSC 104/110/111/112 還原；只在 Windows Terminal（有 `WT_SESSION`）作用。PS5 與 PS7 設定檔都會 dot-source 載入它。
- **四個 AI 的配色**：

| 指令 | 工具 | 背景 |
|---|---|---|
| `claude`、`claudea` | Claude Code | 淺米色 `#fdf6e3`（Solarized Light） |
| `agy`、`agya` | Antigravity | 淺藍色 `#e8f0fe`（One Half Light 調色盤） |
| `codex` | Codex | 深灰色 `#282c34`（One Half Dark） |
| `opencode` | OpenCode | 深藍綠色 `#002b36`（Solarized Dark） |

- **今日修正**：
  - 新增 `agy`、`agya` 的淺藍配色與包裝函式。
  - PS5 設定檔刪除舊的 `agya`、`claudea` 直接呼叫定義，改為只載入 `ai-cli-colors.ps1`，並補上 UTF-8 BOM。
  - `ai-cli-colors.ps1`、PS5 與 PS7 設定檔三個檔案都已納入 chezmoi，commit `df94d91` 已 push 到 dotfiles。
- **踩坑**：設定檔修改前就開著的 PowerShell 分頁，仍是舊函式定義，不會換色；要開新分頁或執行 `. $PROFILE`。
- Claude Code 主題 `custom:solarized-light` 只管文字色，背景色由終端機決定。

## 下一步
- 開新分頁實測 `claudea`、`agya` 換色效果；若淺藍與淺米色太接近，Antigravity 改淺綠或淺紫。
- 視需要為 `gemini`、`copilot` 也加上專屬配色。
