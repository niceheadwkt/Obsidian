# bootstrap-skills.ps1
# 功能：跨 Agent（Claude、Codex、Antigravity、OpenCode）技能庫的新機一鍵冷啟動腳本
# 流程：git clone 中央倉庫 → 把各工具目錄中既有的實體技能搬進中央倉庫 → 複製 _home 檔案 → 執行 repo 內的 setup-junctions.ps1
# 注意：
#   - 本檔必須存成 UTF-8 with BOM，Windows PowerShell 5.1 才能正確解析中文
#   - setup-junctions.ps1 以 repo 內的版本為準，本腳本不再內嵌、也不會覆寫它
#   - 需要先安裝 Git，並能存取 Private Repo
$ErrorActionPreference = "Stop"

$repoUrl  = "https://github.com/niceheadwkt/erp-skills.git"
$userHome = [Environment]::GetFolderPath("UserProfile")
$ssot     = Join-Path $userHome ".agents\skills"

Write-Host "`n=== 開始執行 Agent 技能庫新機冷啟動 ===" -ForegroundColor Cyan

# 1. 取得中央倉庫
if (Test-Path (Join-Path $ssot ".git")) {
    Write-Host "中央倉庫已存在: $ssot（如需更新，請自行在該目錄執行 git pull）" -ForegroundColor Gray
} else {
    if (!(Get-Command git -ErrorAction SilentlyContinue)) {
        throw "找不到 git，請先安裝 Git for Windows 後再執行本腳本。"
    }
    if ((Test-Path $ssot) -and (Get-ChildItem $ssot -Force | Select-Object -First 1)) {
        throw "$ssot 已存在且不是空目錄，也不是 Git 倉庫。請先確認內容並手動移走後再執行，避免覆蓋。"
    }
    New-Item -ItemType Directory -Path (Split-Path $ssot -Parent) -Force | Out-Null
    git clone $repoUrl $ssot
    if ($LASTEXITCODE -ne 0) { throw "git clone 失敗，請確認網路與 GitHub 存取權限。" }
    Write-Host "已從 $repoUrl 取得中央倉庫" -ForegroundColor Green
}

# 2. 把各工具目錄中的實體技能搬進中央倉庫（中央倉庫已有同名技能時不搬，以 repo 版本為準）
$existingSources = @(
    (Join-Path $userHome ".gemini\config\skills"),
    (Join-Path $userHome ".claude\skills"),
    (Join-Path $userHome ".codex\skills"),
    (Join-Path $userHome ".config\opencode\skills")
)
# 刻意不納入中央倉庫、只留在原工具目錄的技能（2026-10-02 確認）
$excludeSkills = @("finmind-agent")
$migrated = @()
foreach ($src in $existingSources) {
    if (Test-Path $src) {
        Get-ChildItem -Path $src -Directory -Force | Where-Object {
            $_.Name -notmatch "^\." -and $_.Name -notin (@("synced", "_home") + $excludeSkills) -and $_.LinkType -ne "Junction" -and (Test-Path (Join-Path $_.FullName "SKILL.md"))
        } | ForEach-Object {
            $dest = Join-Path $ssot $_.Name
            if (!(Test-Path $dest)) {
                Copy-Item -Path $_.FullName -Destination $dest -Recurse -Force
                $migrated += $_.Name
                Write-Host "已把實體技能搬進中央倉庫: $($_.Name)（來源 $src）" -ForegroundColor Yellow
            }
        }
    }
}

# 3. 複製 _home 底下的檔案到家目錄（例如 erp-prod-web-executor 使用的 erp_web_client.py）
$homeSrc = Join-Path $ssot "_home"
if (Test-Path $homeSrc) {
    Get-ChildItem $homeSrc -File | ForEach-Object {
        $dest = Join-Path $userHome $_.Name
        if (!(Test-Path $dest)) {
            Copy-Item $_.FullName $dest
            Write-Host "已複製到家目錄: $($_.Name)" -ForegroundColor Green
        } elseif ((Get-FileHash $dest).Hash -ne (Get-FileHash $_.FullName).Hash) {
            Write-Host "家目錄的 $($_.Name) 和 repo 版本不同，未覆蓋，請自行確認。" -ForegroundColor DarkYellow
        }
    }
}

# 4. 執行 repo 內的 setup-junctions.ps1 建立 Junction
$ps1Path = Join-Path $ssot "setup-junctions.ps1"
if (!(Test-Path $ps1Path)) { throw "找不到 $ps1Path，中央倉庫內容不完整。" }
powershell -ExecutionPolicy Bypass -File $ps1Path
if ($LASTEXITCODE -ne 0) { throw "setup-junctions.ps1 執行失敗。" }

if ($migrated.Count -gt 0) {
    Write-Host "`n提醒：有 $($migrated.Count) 個技能是從本機工具目錄搬進來的（$($migrated -join '、')），" -ForegroundColor DarkYellow
    Write-Host "它們還沒進 Git。要共用的話，請到 $ssot 執行 git add、commit、push，並更新 README.md。" -ForegroundColor DarkYellow
}
Write-Host "`n=== 冷啟動完成 ===" -ForegroundColor Cyan
