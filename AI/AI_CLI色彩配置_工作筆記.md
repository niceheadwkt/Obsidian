# AI CLI 色彩配置 工作筆記

## 上次做到哪 (2026-10-06 晚，電腦 `weng`)
- **同步到第二台電腦**：`weng` 原本完全沒有套用色彩配置（chezmoi 落後遠端 8 個 commit，PS5 設定檔仍是舊的 `agya`／`claudea` 直接定義）。
  - `chezmoi git -- pull --ff-only` 快轉到 `e4619c1`，`chezmoi diff` 確認後 `chezmoi apply`。
  - 該批 commit 也移除了 `dot_claude.json`（停止同步 `.claude.json`），本機檔案不受影響。
  - `weng` 未安裝 PS7（無 `pwsh`），PS7 設定檔已部署但用不到。
- **踩坑：OneDrive 重新導向「文件」**：`weng` 的 `$PROFILE` 實際在 `C:\Users\niceh\OneDrive\文件\WindowsPowerShell\Microsoft.PowerShell_profile.ps1`，而 chezmoi 管的是 `~\Documents\WindowsPowerShell\...`，apply 後 PowerShell 仍讀不到。
  - 解法：OneDrive 那份改成只 dot-source `~\Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1`（UTF-8 BOM），原檔備份為 `...profile.ps1.bak-20261006`。之後設定一律以 chezmoi 那份為準。
  - ✅ 新分頁實測，`claude`、`agy` 等配色皆正常。
- **安裝 Codex CLI**：`npm install -g @openai/codex`，版本 `codex-cli 0.160.1`，位置 `%APPDATA%\npm\codex.ps1`；換色函式免另設，深灰背景正常。
- **踩坑：Codex 不可在系統管理員終端機執行**：會出現 `start the Windows daemon from a non-elevated terminal; shared clients must not inherit administrator privileges`。
  - 原因：Codex 的背景 daemon 為多個 client 共用，若以管理員啟動，之後一般權限的 client 連上就等於借到管理員權限（權限提升），因此 Codex 主動拒絕。
  - 解法：用一般權限開 Windows Terminal（WT 設定檔本身沒有 `elevate`，是捷徑／右鍵以管理員開啟所致）；臨時需要可用 `codex --no-daemon`。
  - 原則：AI CLI 一律用一般權限執行（最小權限原則），需要管理員的操作另開分頁手動做。
- **踩坑：McAfee 封鎖 Codex 自動更新（誤判）**：19:37 McAfee 跳出「已阻擋威脅 Real Protect-PSFL!A9CD92EAEB70，已封鎖」。
  - 查證：PowerShell/Operational 事件 4100 顯示 `ScriptContainedMaliciousContent`，宿主指令為 `powershell.exe -NoLogo -NoProfile -NonInteractive -ExecutionPolicy Bypass -Command try { Invoke-Expression ([Console]::In.ReadToEnd()) } ...`。
  - 該字串位於 `codex.exe` 內，旁邊是 `app-server-daemon`、`standalone Codex updater` 與 `https://chatgpt.com/codex/install.ps1`：Codex 背景 daemon 下載官方安裝腳本後直接 `Invoke-Expression` 執行。
  - 原因：「下載後不落地直接 IEX + Bypass 執行原則」是無檔案型（fileless）惡意程式手法，McAfee 行為偵測因此誤判（PSFL 推測為 PowerShell FileLess）。
  - 影響：只有自動更新失敗，`codex.exe` 未被隔離，Codex 可正常使用。
  - 處置：**不要**加入 McAfee 例外（等於放行所有 PowerShell 下載即執行的腳本）；改為手動更新 `npm install -g @openai/codex@latest`。之後再跳同名通知按「完成」即可。
- **發現：Codex 沙盒會建立本機帳號群組並改 ACL**：清 `.git/worktrees/organize-documentation-files` 殘留目錄時，在 ACL 看到 `weng\CodexSandboxUsers`。
  - 安裝 Codex 後多了本機群組 `CodexSandboxUsers`（描述：Codex sandbox internal group (managed)），成員為 `CodexSandboxOffline`、`CodexSandboxOnline` 兩個沙盒帳號（應由 `codex-windows-sandbox-setup.exe` 建立）。
  - 權限只有 `ReadAndExecute`（唯讀＋執行），不能寫入或刪除。
  - 出現位置：`~\.codex`、`~\Documents` 為直接設定；Obsidian 專案（含 `.git`、`AI`）為從上層 `我的雲端硬碟` 繼承；`~` 本身沒有。
  - 與 worktree 刪不掉無關，真正原因是該目錄帶 `ReadOnly` 屬性（已清屬性後刪除並 `git worktree prune`）。
  - 之後遇到奇怪的權限問題，可先檢查是否與這些沙盒群組／ACL 有關；若日後移除 Codex，需另外清除這些本機帳號、群組與 ACL。

## 先前紀錄 (2026-10-06 早)
- **agy 配色字體太淡**：在淺藍背景上，agy 用白色顯示的工具參數，例如 `Bash(...)` 括號裡的指令，幾乎看不見。調整 `ai-cli-colors.ps1` 的 agy 調色盤：
  - 白(7) `fafafa` → `5c6370`，亮白(15) `ffffff` → `383a42`
  - 亮黃(11) `e4c07a` → `b07d00`，`Bash`、`ManageTask` 等工具名稱比較清楚
- 已用 `chezmoi re-add` 同步，commit `e4619c1` 已 push 到 dotfiles。
- 新開的 PowerShell 分頁才會套用；**✅ 已實測，白字和黃字都清楚了**。

## 先前紀錄 (2026-10-05)
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
- ~~chezmoi 原始碼目錄有未追蹤的 `dot_agents/skills/setup-junctions.ps1`~~ → ✅ 已於 dotfiles commit `40b7e1b` 停止以 chezmoi 管理，改由 erp-skills repo 管理（2026-10-07 收工確認 chezmoi 工作區乾淨）。
- ~~`weng` 的 Google Drive 模式需確認~~ → ✅ 已確認 `weng` 為**鏡像（雙向同步）模式**（`G:\` 只有指向 C 槽的 `我的雲端硬碟.lnk`，DriveFS 的 `mirror_sqlite.db` 持續寫入），決定維持現狀。全域規範三份模板（Claude／Codex／Gemini）改用 chezmoi `{{ if eq .chezmoi.hostname "weng" }}` 依電腦區分路徑，dotfiles commit `f52ba16`。
  - 踩坑：部署出去的規範檔是 CRLF，模板用 `{{- ... }}` 會吃掉前一行的換行而改到無關行，要改用 `{{ ... -}}`。
- 其他電腦若「文件」也被 OneDrive 重新導向，比照 `weng` 的作法處理 `$PROFILE`。
- Codex 自動更新會被 McAfee 擋，記得定期手動 `npm install -g @openai/codex@latest`。
- 若淺藍與淺米色太接近，Antigravity 可以改成淺綠或淺紫。
- 視需要為 `gemini`、`copilot` 也加上專屬配色。
