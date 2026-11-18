---
type: source-summary
tags: [資安, 木馬, 網路釣魚, AMOS, Google-Cloud, Vertex-AI, Service-Account, 雲端帳單, Claude-Code, 數位時代]
sources: ["[[AI/raw/2026-11-05T134617+0800-我被駭了，差點一夕破產！Google Cloud遭盜刷3萬元，追查才發現Mac早被植入木馬.md|我被駭了，差點一夕破產！Google Cloud遭盜刷3萬元（數位時代，2026-11-04）]]"]
created: 2026-11-18
updated: 2026-11-18
---

# 假冒 Claude Code 官網木馬與雲端帳單盜刷事件

《數位時代》2026-11-04 刊出，原文為醫師林佑儒的第一人稱分享（原載於其 Facebook）。作者有資工碩士背景、用 Google Cloud 超過十年，某天凌晨帳號遭盜用、一小時被刷約新台幣 3 萬元；追查數日後，懷疑源頭是 8 個月前誤入假冒 Claude Code 的網站，Mac 被植入竊取憑證的木馬。文中攻擊鏈與「AI Agent 參與攻擊」皆為作者推測，非資安單位鑑識結論。

**一句話重點**：假 Claude Code 官網植入木馬，偷走憑證盜刷雲端帳單

## 一、事件時間軸

| 時間 | 發生什麼 |
|------|----------|
| 8 個月前（2 月） | 作者上網搜尋 Claude Code 安裝方式，點進 Google 搜尋第一名、仿得很像官網的 `claude-code-something.mssg.com`，推測下載了 `.dmg` 或 `.sh` 安裝檔，Mac 被植入木馬 |
| 之後某時 | 瀏覽器登入 Session／Cookie 疑遭竊取；因為不需要密碼，沒有觸發「新裝置登入」通知 |
| 攻擊前兩週 | Google Takeout 活動紀錄出現一筆美國 IP 操作；攻擊者逐一搜尋專案（每次間隔十幾分鐘），4 秒內啟用 17 個 AI 相關 API，再建立 Service Account、兩分鐘後建立並下載私鑰 |
| 攻擊當天凌晨 4 點 | 多個專案同時大量呼叫 Vertex AI（Gemini Flash、影片生成），來源 IP 顯示巴拿馬（推測是跳板） |
| 約 1 小時後 | 收到 Google「Early signal anomaly」異常費用警告（漲幅 1,000%） |
| 早上 6 點 | 作者登入 Logs Explorer 查看，發現陌生 Service Account；關閉所有帳單帳戶、撤下全部專案、關閉網站才止血 |
| 約 5 小時後 | 原本設定的每月 50 美元預算提醒信才寄到 |
| 當天傍晚 | Google 帳務團隊受理申訴，協商後減免大部分費用 |

作者觀察到攻擊者對常用專案「先搜尋再啟用 API」、對少用專案「直接建 Service Account」，懷疑有 AI Agent 自行推理再與人類協作，但僅為猜測。

## 二、排查過程：逐一排除四種可能

| 可能原因 | 檢查方式 | 結論 |
|----------|----------|------|
| API Key 或 Service Account 金鑰外洩 | 金鑰用完即刪、不存 `.env`、不上傳 GitHub；電腦沒裝 gcloud CLI、從未自建 Service Account | 找不到可用金鑰，可能性低 |
| AI Agent 工具執行惡意指令 | 翻查 Codex、Pi Coding Agent 的工具執行紀錄、`curl` 對外連線、PyPI 下載套件 | 沒有可疑指令 |
| Google 帳號密碼被盜 | 有開 2FA、新裝置登入幾秒就會通知、第三方授權 App 無 GCP 權限 | 可能性低 |
| 瀏覽器 Session／Cookie 被偷 | Google Takeout 匯出活動紀錄，發現建立 Service Account 當天有美國 IP 操作 | **最可能** |

順著第四點繼續查 Mac，找到 8 個月前建立的可疑檔案：

```
~/.mainhelper
~/.pass
~/.id
/Library/LaunchDaemons/com.finder.helper.plist   # 內容：/bin/bash ~/.agent
```

`.plist` 讓系統開機自動執行 `~/.agent`（調查時已被刪除，無法分析）；特徵與 **AMOS（Atomic macOS Stealer）** 相符，這是專偷密碼、瀏覽器 Cookie 與登入憑證的 macOS 竊密程式。向 Google 調閱搜尋紀錄後，發現 `.plist` 建立前約兩分鐘，作者剛好造訪了上述假冒網站。

## 三、為什麼一般防護都沒擋住

- **2FA 與登入通知擋不住偷 Session**：攻擊者拿的是已登入的 Cookie，不是帳密，不算「新裝置登入」。
- **預算提醒不會停機**：Google Cloud 的預算設定只發通知，不會自動停止服務，且當天延遲約 5 小時才寄出。新推出的 **Hard Cap（硬性支出上限）** 只適用部分服務，無法涵蓋整個專案。
- **平常不看 Credentials 頁**：陌生 Service Account 潛伏兩週沒被發現。
- **技術背景不等於安全**：作者自認謹慎，卻在新工具爆紅、急著安裝時點了搜尋第一名的假網站。

## 四、作者的四個教訓

1. **Mac 也要裝防毒**：事後測試，Avast Free、Malwarebytes 等免費防毒都能偵測出這個木馬。成本低、出事損失大，像打疫苗。
2. **檢查電腦是否有可疑檔案**：可請 AI 教你找；先斷網、不要執行可疑檔案。
3. **設定費用提醒與支出上限**：自架網站、部落格用雲端服務時務必設定，支援的服務就開硬性上限。
4. **API Key 管理**：不用就撤銷（Revoke）、定期更換。

## 我可以怎麼用

- **AI 工具只從官方網址安裝**：Claude Code、Codex 等 CLI 一律從官方文件取得安裝指令（如 [[Claude（Anthropic）]] 記錄的 `irm https://claude.ai/install.ps1 | iex`），不要點搜尋結果的第一名或廣告；`irm ... | iex` 這類「下載即執行」指令，先核對網域再貼上。
- **盤點本機憑證存放**：zpq 的 token、各家 API Key、chezmoi 管理的設定檔，確認沒有明文放進 Git 或雲端硬碟同步資料夾；收工流程的「敏感資訊檢查」就是為這種情境設計。
- **定期檢查 Windows 自動執行項目**：Windows 對應 LaunchDaemons 的是「工作排程器」、登錄檔 Run 機碼與啟動資料夾；可用 `Get-ScheduledTask`、`Get-CimInstance Win32_StartupCommand` 列出，看到不認得的就查。
- **雲端帳號設支出上限**：GCP（[[GCP 雲端排程與現代化數據工程實戰]]）、Anthropic Console、OpenAI 等 API 帳號，都設定預算提醒並開啟支援的硬性上限；記得「提醒不等於停機」。
- **用 AI Agent 時保留執行紀錄**：作者能排除「Agent 執行惡意指令」，靠的是工具執行紀錄還在；Claude Code 的對話紀錄與 hooks 日誌也值得保留一段時間。
- **對照 ERP 權限管理**：攻擊者先建「看起來正常的服務帳號」潛伏兩週才出手，和 ERP 的權限稽核同理——定期比對系統帳號清單、找出沒人認領的帳號與金鑰。

## 關聯頁面
- [[GitHub 開源工具與 AI Skills 入門指南]]（安裝外部工具的資安風險）
- [[主權 AI 與 token 帳單三層陷阱]]（雲端 AI 帳單失控）
- [[Claude（Anthropic）]]（Claude Code 官方安裝方式）
- [[AI CLI 工具比較與選擇_摘要]]
- [[GCP 雲端排程與現代化數據工程實戰]]
- [[ChatGPT 與 Claude 對話隱私與關閉訓練設定]]（瀏覽器擴充套件與分享連結的隱私風險）
