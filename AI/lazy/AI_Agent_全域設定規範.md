# AI Agent 全域設定規範（可共用版）

> **本文件用途**：讓同一台電腦上的多個 AI Agent 共用同一套語音與同步設定。
> 適用於：Claude Code、ChatGPT Codex（APP）、OpenCode、Google Antigravity 等。
> 請將本文件內容分別放入各 Agent 的全域設定檔中（如 Claude Code 的 `~/.claude/CLAUDE.md`）。

---

## 一、語音回覆設定

### 核心工具：Edge-TTS

本環境統一使用 **Edge-TTS**（免費、微軟雲端語音合成）作為語音回覆的唯一工具。
不使用 SAPI 離線語音、不使用外部播放器視窗。

#### 安裝方式

```bash
# 在專案 .venv 中安裝
uv pip install --python .\.venv\Scripts\python.exe edge-tts
```

#### 基本用法（Python）

```python
import asyncio
import edge_tts

async def speak(text, voice="zh-TW-YunJheNeural", output="temp_speech.mp3"):
    """合成語音並儲存"""
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(output)
    print(f"語音已儲存：{output}")

# 執行
asyncio.run(speak("你好，歡迎使用語音回覆功能。"))
```

#### 常用聲音

| 聲音代碼 | 性別 | 風格 |
|----------|------|------|
| `zh-TW-YunJheNeural` | 男 | 穩重、適合教學（預設） |
| `zh-TW-HsiaoChenNeural` | 女 | 活潑、清晰 |
| `zh-TW-YunJheNeural` | 男 | 自然對話感 |
| `zh-TW-HsiaoYuNeural` | 女 | 溫柔、柔和 |

> 完整聲音清單：執行 `edge-tts --list-voices` 查看。

#### 行內播放（Windows PowerShell）

合成後直接播放，不開外部播放器：

```powershell
Add-Type -AssemblyName PresentationCore
$player = New-Object System.Windows.Media.MediaPlayer
$player.Open([System.IO.Path]::GetFullPath("temp_speech.mp3"))
$player.Play()
Start-Sleep -Seconds 5  # 依語音長度調整
$player.Close()
```

### 語音回覆規則

1. **觸發時機**：使用者說「用語音回答」「唸出來」「唸給我聽」「用語音講結論」時執行。
2. **講稿撰寫**：
   - 口語化、精簡（100–250 字）
   - 數字用中文（「五十頁」不要「50頁」）
   - 只講結論與下一步，細節留在文字回覆
3. **聲音選擇**：
   - 預設使用 `zh-TW-YunJheNeural`（男聲）
   - 使用者明確指定其他聲音時才切換
   - 使用者指名「用三師爸的聲音」→ 需另用 voice-clone 技能（VoxCPM2），不在本規範範圍
4. **播放方式**：一律行內播放，不開外部播放器視窗。
5. **語音結束後**：回報「語音已播放」即可，不重複文字內容。

---

## 二、多 Agent 自動同步設定

### 同步架構總覽

本電腦同時使用多個 AI Agent，設定檔需保持同步：

| Agent | 設定檔位置 | 同步工具 |
|-------|-----------|---------|
| Claude Code | `~/.claude/CLAUDE.md` | Chezmoi |
| ChatGPT Codex (APP) | App 內設定 | 手動同步（無自動工具） |
| OpenCode | `~/.config/opencode/` | 手動同步或 Chezmoi |
| Google Antigravity | App 內設定 | 手動同步（無自動工具） |

> **重要**：Claude Code 是唯一有完整自動同步機制的 Agent。其他 Agent 的設定變更後，需手動同步到對應位置。

### 同步工具：Chezmoi

Chezmoi 負責將 `~/.claude/` 內的設定檔同步到 Git repo，跨電腦時執行 `chezmoi update` 即可。

```bash
# 安裝 Chezmoi（Windows）
winget install --id chezmoi.chezmoi

# 初始化（首次）
chezmoi init mathruffian-dot

# 同步設定（換電腦時）
chezmoi update

# 新增被追蹤的檔案
chezmoi add ~/.claude/CLAUDE.md
chezmoi add ~/.claude/settings.json
```

### 同步流程：開工與收工

#### 開工（開始工作時）

當使用者說「開工」「我來了」「上次做到哪」時，自動執行：

1. 確認工作目錄是否在 Google Drive git repo 內
2. 讀取 Obsidian 工作筆記的「上次做到哪」+「下一步」
3. 執行 `git status` 檢查本地變動
4. 檢查遠端是否有新 commit（有則提醒，不自動 pull）
5. 回報結構化摘要

#### 收工（結束工作時）

當使用者說「收工」「下班」「結束」時，自動執行：

1. 專案 Git 同步（status → 建議 commit 訊息 → 等使用者確認 → push）
2. Claude 設定同步（`chezmoi status` → 變動則 commit + push）
3. 提醒未進 chezmoi 的敏感檔案（API key 等）
4. 更新 Obsidian 工作筆記
5. 回報 checklist

### 語音輸入的錯字處理

使用者常用語音輸入，轉文字後可能有同音錯字：

| 原文（語音轉出） | 實際意思 |
|------------------|---------|
| Call Desk | Codex |
| Cloud Call | Claude Code |
| Typeless | headless |

**處理原則**：
- 以「上下文善意還原」最合理的原意，不要逐字照字面理解。
- 明顯錯字直接順過，不用每個都提。
- 關鍵詞（檔名、路徑、指令）若沒把握，**先說出你的理解再往下做**。

---

## 三、各 Agent 設定檔放置位置

### Claude Code

```bash
# 全域設定
~/.claude/CLAUDE.md

# 技能目錄
~/.claude/skills/<skill-name>/SKILL.md

# 同步命令
chezmoi update
```

### ChatGPT Codex (APP)

```
App 內 → 設定 → 自訂指令（Custom Instructions）
```

將「語音回覆規則」與「多 Agent 同步」段落貼入 custom instructions。
Codex 無自動同步機制，設定變更後需手動更新。

### OpenCode

```bash
# 全域設定
~/.config/opencode/opencode.json

# 同步方式
# 可將設定目錄加入 Chezmoi 追蹤，或手動複製
```

### Google Antigravity

```
App 全域設定 → System Prompt / Custom Instructions
```

將本文件「一、語音回覆設定」段落貼入 system prompt。
Antigravity 無自動同步機制。

---

## 四、跨裝置同步注意事項

| 同步層 | 內容 | 工具 | 頻率 |
|--------|------|------|------|
| 自動 | 專案檔案 | Google Drive | 即時 |
| 自動 | Claude Code 設定 | Chezmoi | 換電腦時手動 `chezmoi update` |
| 半自動 | Obsidian 筆記 | Vault 同步 | 確認同步完成 |
| 手動 | GitHub repo | Git | `git pull` / `git push` |
| 手動 | 其他 Agent 設定 | 人工複製 | 設定變更時 |

### 換電腦 Checklist

- [ ] `chezmoi update`（同步 Claude Code 設定）
- [ ] 確認 `.venv` 已建立（`uv venv .venv --python 3.12`）
- [ ] 安裝核心套件（`uv pip install -r requirements-core.txt`）
- [ ] 檢查 API key 檔案是否存在（如 `~/.groq_api_key`）
- [ ] 手動同步其他 Agent 的 custom instructions

---

> **維護者**：三師爸 Sense Bar
> **最後更新**：2026-07-12
> **來源**：Claude Code 全域設定 + speak 技能實作經驗
