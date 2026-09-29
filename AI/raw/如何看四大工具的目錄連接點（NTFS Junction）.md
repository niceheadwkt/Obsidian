# 如何看四大工具的目錄連接點（NTFS Junction）

---

## 壹、常見問題與踩坑點：PowerShell 與 CMD 環境變數差異

### 1. 錯誤現象
在 PowerShell 中輸入以下指令時：
```powershell
dir %USERPROFILE%\.claude\skills
```
會產生以下報錯：
```text
dir : 找不到 'C:\Users\ch26788\%USERPROFILE%\.claude\skills' 路徑，因為它不存在。
位於 線路:1 字元:1
+ dir %USERPROFILE%\.claude\skills
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (C:\Users\ch2678...e\skills:String) [Get-ChildItem], ItemNotFoundException
    + FullyQualifiedErrorId : PathNotFound,Microsoft.PowerShell.Commands.GetChildItemCommand
```

### 2. 原因剖析
- **`%USERPROFILE%`** 是傳統 Windows 命令提示字元（CMD）的環境變數語法。
- **PowerShell** 不會自動解析 `%...%` 語法，而是將它視為普通的字串路徑，導致系統在當前路徑下嘗試尋找名為 `%USERPROFILE%` 的資料夾。
- 在 PowerShell 中，家目錄的標準寫法為 **`$HOME`**、**`~`** 或 **`$env:USERPROFILE`**。

---

## 貳、四大工具之全域技能目錄清單

| 工具名稱 | 全域技能預設載入路徑 |
| :--- | :--- |
| **Claude Code** | `~/.claude/skills` |
| **Codex** | `~/.codex/skills` |
| **Antigravity** | `~/.gemini/config/skills` |
| **OpenCode** | `~/.config/opencode/skills` |

所有工具的技能均透過 NTFS Junction 指向中央真相來源：`C:\Users\ch26788\.agents\skills\`。

---

## 參、檢視四大工具目錄連接點的三種方式

### 方法一：PowerShell 結構化表格（最推薦）

此方式能直接列出是否為 Junction，以及底層實際指向的實體路徑。

#### 1. 一次檢視四大工具所有技能連接點
在 PowerShell 中執行以下指令：
```powershell
$tools = @(
    @{ Name = "Claude Code";  Path = "$HOME\.claude\skills" },
    @{ Name = "Codex";        Path = "$HOME\.codex\skills" },
    @{ Name = "Antigravity";  Path = "$HOME\.gemini\config\skills" },
    @{ Name = "OpenCode";     Path = "$HOME\.config\opencode\skills" }
)

foreach ($t in $tools) {
    Write-Host "`n========== $($t.Name) ($($t.Path)) ==========" -ForegroundColor Cyan
    Get-ChildItem -Path $t.Path | Select-Object Name, LinkType, Target | Format-Table -AutoSize
}
```

#### 2. 單一工具快速查詢
```powershell
# 檢視 Claude Code
Get-ChildItem ~/.claude/skills | Select-Object Name, LinkType, Target

# 檢視 Codex
Get-ChildItem ~/.codex/skills | Select-Object Name, LinkType, Target

# 檢視 Antigravity
Get-ChildItem ~/.gemini/config/skills | Select-Object Name, LinkType, Target

# 檢視 OpenCode
Get-ChildItem ~/.config/opencode/skills | Select-Object Name, LinkType, Target
```

#### 3. 結果判讀
- **`LinkType`**：顯示為 **`Junction`** 即代表建立成功。
- **`Target`**：顯示該技能實際連向的中央目錄路徑（如 `C:\Users\ch26788\.agents\skills\erp-big5`）。

---

### 方法二：命令提示字元（CMD 風格）檢視 `<JUNCTION>` 標籤

CMD 的 `dir` 指令會直接印出 `<JUNCTION>` 標籤。

#### 1. 若目前人在 PowerShell 視窗中
透過 `cmd /c` 呼叫執行：
```powershell
cmd /c "dir %USERPROFILE%\.claude\skills"
cmd /c "dir %USERPROFILE%\.codex\skills"
cmd /c "dir %USERPROFILE%\.gemini\config\skills"
cmd /c "dir %USERPROFILE%\.config\opencode\skills"
```

#### 2. 若目前在純 CMD 視窗中
```cmd
dir %USERPROFILE%\.claude\skills
```

#### 3. 結果判讀
一般資料夾會顯示 `<DIR>`，連接點則會明確標示為 **`<JUNCTION>`** 並在中括號顯示目標：
```text
2026/09/18  15:02    <JUNCTION>     erp-big5 [C:\Users\ch26788\.agents\skills\erp-big5]
2026/09/18  15:02    <JUNCTION>     erp-conventions [C:\Users\ch26788\.agents\skills\erp-conventions]
```

---

### 方法三：Windows 檔案總管（GUI 圖形介面）

1. 按 `Win + R` 開啟「執行」對話框，輸入以下任一路徑並按 Enter：
   - `C:\Users\ch26788\.claude\skills`
   - `C:\Users\ch26788\.codex\skills`
   - `C:\Users\ch26788\.gemini\config\skills`
   - `C:\Users\ch26788\.config\opencode\skills`
2. **圖示特徵**：
   - 成功的 NTFS Junction 資料夾圖示左下角會帶有一個**小捷徑箭頭圖案**。
3. **內容屬性**：
   - 在任意技能資料夾上按右鍵選擇「內容」，在「類型」中會標記為相關連接屬性。

---

## 肆、穿透性讀取測試（驗證實際可用性）

可在 PowerShell 中直接透過連接點路徑讀取內容，確認檔案系統已打通：

```powershell
# 透過 Claude Code 入口讀取中央倉庫的 SKILL.md 前 10 行
Get-Content ~/.claude/skills/erp-big5/SKILL.md -Head 10

# 透過 Codex 入口讀取
Get-Content ~/.codex/skills/erp-big5/SKILL.md -Head 10
```

若能正常印出 YAML frontmatter 與說明文字，表示底層映射完全正常，各工具的 CLI 與 IDE 均可無縫共用。