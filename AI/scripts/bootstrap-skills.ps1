# bootstrap-skills.ps1
# 功能：跨 Agent（Claude、Codex、Antigravity、OpenCode）技能庫新機一鍵冷啟動萬能腳本
# 特點：自動建立中央庫、安全遷移現有目錄實體技能、生成含 UTF-8 BOM 之 setup-junctions.ps1、一鍵建立四大工具 Junction
$ErrorActionPreference = "Stop"

$userHome = [Environment]::GetFolderPath("UserProfile")
$ssot     = Join-Path $userHome ".agents\skills"

Write-Host "`n=== 開始執行 Agent 技能庫新機一鍵冷啟動 ===" -ForegroundColor Cyan

# 1. 建立中央真相來源 (SSOT) 目錄
if (!(Test-Path $ssot)) {
    New-Item -ItemType Directory -Path $ssot -Force | Out-Null
    Write-Host "已建立中央技能庫: $ssot" -ForegroundColor Green
} else {
    Write-Host "中央技能庫已存在: $ssot" -ForegroundColor Gray
}

# 2. 安全掃描並遷移現有工具目錄中的實體技能（避免直接建立 Junction 時覆蓋舊檔案）
$existingSources = @(
    (Join-Path $userHome ".gemini\config\skills"),
    (Join-Path $userHome "我的雲端硬碟\claude_erp_rule\chs-erp\skills"),
    (Join-Path $userHome ".claude\skills"),
    (Join-Path $userHome ".codex\skills")
)
foreach ($src in $existingSources) {
    if (Test-Path $src) {
        Get-ChildItem -Path $src -Directory | Where-Object {
            $_.Name -notmatch "^\." -and $_.Name -notin @(".system", "synced", ".trash") -and $_.LinkType -ne "Junction"
        } | ForEach-Object {
            $dest = Join-Path $ssot $_.Name
            if (!(Test-Path $dest)) {
                Copy-Item -Path $_.FullName -Destination $dest -Recurse -Force
                Write-Host "已安全遷移既有實體技能至中央庫: $($_.Name)" -ForegroundColor Yellow
            }
        }
    }
}

# 3. 寫入具備 UTF-8 BOM 之 setup-junctions.ps1 腳本
$innerScript = @'
# setup-junctions.ps1
# 功能：自動將 ~/.agents/skills 下的所有技能以 Junction 連結至各大 Agent 工具目錄
# 注意：此檔案必須儲存為 UTF-8 with BOM 格式以供 PowerShell 5.1 正常解析
$ErrorActionPreference = "Stop"

$userHome   = [Environment]::GetFolderPath("UserProfile")
$ssotPath   = Join-Path $userHome ".agents\skills"
$clientDirs = @(
    (Join-Path $userHome ".gemini\config\skills"),
    (Join-Path $userHome ".claude\skills"),
    (Join-Path $userHome ".codex\skills"),
    (Join-Path $userHome ".config\opencode\skills")
)

foreach ($dir in $clientDirs) {
    if (!(Test-Path $dir)) {
        New-Item -ItemType Directory -Path $dir -Force | Out-Null
    }
}

$skills = Get-ChildItem -Path $ssotPath -Directory | Where-Object {
    $_.Name -notmatch "^\." -and $_.Name -notin @(".system", "synced", ".trash")
}

foreach ($s in $skills) {
    $skillName = $s.Name
    $sourceDir = $s.FullName

    foreach ($clientDir in $clientDirs) {
        $destDir = Join-Path $clientDir $skillName

        if (Test-Path $destDir) {
            $item = Get-Item $destDir
            if ($item.LinkType -eq "Junction") {
                [System.IO.Directory]::Delete($destDir)
            } else {
                Remove-Item -Path $destDir -Recurse -Force
            }
        }

        New-Item -ItemType Junction -Path $destDir -Target $sourceDir | Out-Null
        Write-Host "已建立 Junction: $skillName -> $clientDir" -ForegroundColor Green
    }
}

Write-Host "`n所有 Agent 技能已成功關聯至中央庫！" -ForegroundColor Cyan
'@

$ps1Path = Join-Path $ssot "setup-junctions.ps1"
[System.IO.File]::WriteAllText($ps1Path, $innerScript, [System.Text.Encoding]::UTF8)
Write-Host "已寫入關聯腳本: $ps1Path (UTF-8 with BOM)" -ForegroundColor Green

# 4. 呼叫腳本建立 Junction
powershell -ExecutionPolicy Bypass -File $ps1Path
