---
title: "Claude Code快捷鍵+指令大全！13大類速查不用背，從Ctrl+C到多Agent協作一次整理"
source: "https://www.bnext.com.tw/article/90925/claude-code-slash-commands-shortcuts-complete-guide"
author:
  - "[[數位時代 BusinessNext]]"
published: 2026-05-14
created: 2026-06-15
description: "多數人只把 Claude Code 當成「輸入需求、等待回覆」的聊天助手，善用快捷鍵與確定性指令，能比自然語言互動更快、更精準。"
tags:
  - "clippings"
---
多數人使用 Claude Code 的方式很單純：輸入需求、等待回覆、不滿意就重來。但事實上，從壓縮對話、倒帶操作、切換模型，到安全審查、排程工作、管理記憶體，許多你以為要手動處理的事，Claude Code 都有對應的斜線指令可以直接觸發。

以下內容整理自 Claude Code 官方文件，將官方整理的內建指令以及快捷鍵依應用情境分類，方便大家查找與上手，快收藏起來吧！

## 在 Claude Code 會幫你處理事情的前提下，還有必要了解指令嗎？

答案是：有，但理由變了。以前學指令是因為「不知道指令就做不到」，現在的理由是 **效率與精準度** 。

掌握最新AI、半導體、數位趨勢！訂閱《數位時代》日報及社群活動訊息

**指令比對話快。** `/compact` 一秒執行完，用對話說「幫我壓縮目前的上下文，重點保留認證邏輯」，Claude 要先理解意圖、確認、再執行，而直接使用指令可以省下更多的溝通成本。

**指令觸發的是確定性行為。** `/rewind` 就是倒帶，不會因為措辭模糊而執行到一半。用對話請 Claude「回到剛才那個版本」，有可能它理解的「剛才」跟你的不一定一樣。

**部分指令無法用對話替代。** `/tui fullscreen` 、 `/terminal-setup` 、 `/setup-bedrock` 這類改變 CLI 本身設定的指令，系統必須由使用者明確輸入指令來觸發，無法靠存在模糊空間的口語要求來執行。

快捷鍵處理的則是「對話做不到的事」：你沒辦法對 Claude 說「幫我把選取範圍向右延伸」或「把這段提示送到外部編輯器」，這些操作只存在於介面層，Claude 根本無法透過回覆執行。另外，快捷鍵裡有幾個高頻操作（ `Ctrl+C` 中斷、 `Ctrl+R` 搜尋歷史、 `Shift+Tab` 切換權限模式），一旦熟悉這些快捷鍵，在操作上就能更流暢。

## Claude Code 指令大全

下面先提供2張可以直接存下來參考的圖：

![#0 Claude Code指令大全](https://image-cdn.learnin.tw/bnextmedia/image/album/2026-05/a6ch-1778660938.png?w=1200&output=webp)

圖／ ChatGPT生成

![#2 Claude Code指令大全](https://image-cdn.learnin.tw/bnextmedia/image/album/2026-05/zjtm-1778660940.png?w=1200&output=webp)

圖／ ChatGPT生成

### 一、對話與上下文管理

| 指令 | 說明 |
| --- | --- |
| `/btw <問題>` | 提出側邊問題， **不寫入對話歷史** ，不汙染主線 |
| `/compact [焦點說明]` | 壓縮對話歷史釋放上下文，可指定保留重點（例： `/compact 保留認證邏輯討論` ） |
| `/context [all]` | 視覺化上下文使用量，標出記憶體膨脹點與最佳化建議；傳入 `all` 展開每項細節 |
| `/clear [名稱]` | 清空上下文開啟新對話，舊對話仍可用 `/resume` 取回；可傳名稱供日後辨識。別名： `/reset` 、 `/new` |
| `/recap` | 按需生成目前工作階段的單行摘要 |
| `/export [檔名]` | 匯出對話為純文字；不帶檔名則開啟複製／儲存對話框 |
| `/copy [N]` | 複製最後一個回覆； `/copy 2` 複製倒數第二個；有程式碼區塊時出現互動選擇器，按 `w` 可寫入檔案 |

### 二、程式碼變更與版本追蹤

| 指令 | 說明 |
| --- | --- |
| `/diff` | 互動式差異檢視器：左右鍵切換 git diff／每回合變更，上下鍵瀏覽檔案 |
| `/rewind` | 將對話和程式碼倒帶到上一個 checkpoint，或從選定訊息重新摘要。別名： `/checkpoint` 、 `/undo` |
| `/branch [名稱]` | 在此時刻建立對話分支，用於實驗不同方向。別名： `/fork` |
| `/add-dir <路徑>` | 為本次工作階段新增額外工作目錄（僅授予檔案存取，不套用 `.claude/` 配置） |
| `/security-review` | 分析目前分支待處理變更，偵測注入、驗證、資料洩露等安全風險 |
| `/review [PR]` | 在目前工作階段本地審閱 pull request；深度雲端審閱請用 `/ultrareview` |

### 三、任務規劃與自動化

| 指令 | 說明 |
| --- | --- |
| `/plan [描述]` | 進入 Plan Mode，Claude 先擬計畫再動手；可帶描述立即開始，例： `/plan fix the auth bug` |
| `/ultraplan <提示>` | 在 ultraplan 工作階段草擬計畫，可在瀏覽器中檢視，再遠端執行或發回終端機 |
| `/goal [條件\|clear]` | 設定持續目標，Claude 跨回合持續工作直到條件達成； `clear` 等可提前移除 |
| `/schedule [描述]` | 建立、更新、列出或執行雲端例行工作，對話式引導設定。別名： `/routines` |
| `/autofix-pr [提示]` | 產生網頁工作階段監視目前分支 PR，在 CI 失敗或審閱評論時自動推送修復；需 `gh` CLI |

### 四、並行執行與 Agent 管理

| 指令 | 說明 |
| --- | --- |
| `/agents` | 管理 agent 配置，也是 Agent 管理員入口 |
| `/tasks` | 列出並管理目前工作階段背景執行的工作。別名： `/bashes` |
| `/background [提示]` | 將目前工作階段分離為背景 agent 執行，釋放終端機；可傳入額外指示。別名： `/bg` |
| `/stop` | 停止目前附加的背景工作階段；記錄與 worktree 保留。若只分離不停止請用 `/exit` 或 `←` |

### 五、工作階段管理

| 指令 | 說明 |
| --- | --- |
| `/rename [名稱]` | 重新命名目前工作階段；不帶名稱則從對話歷史自動生成 |
| `/resume [工作階段]` | 按 ID 或名稱繼續對話，或開啟工作階段選擇器。別名： `/continue` |
| `/desktop` | 將目前工作階段移至 Claude Code 桌面應用繼續。僅限 macOS 和 Windows。別名： `/app` |
| `/teleport` | 將網頁版 Claude Code 工作階段拉入此終端機；需 claude.ai 訂閱。別名： `/tp` |
| `/remote-control` | 讓此工作階段可從 claude.ai 遠端控制。別名： `/rc` |
| `/remote-env` | 配置以 `--remote` 啟動的網頁工作階段的預設遠端環境 |
| `/sandbox` | 切換 sandbox 模式（僅限支援平臺） |

### 六、模型與效能設定

| 指令 | 說明 |
| --- | --- |
| `/model [模型]` | 切換 AI 模型；支援的模型可用左右鍵調整努力程度，變更立即生效 |
| `/effort [low\|medium\|high\|xhigh\|max\|auto]` | 調整模型努力程度； `max` 僅限本次工作階段；不帶引數開啟互動滑桿 |
| `/fast [on\|off]` | 切換快速模式 |

### 七、介面與個人化

| 指令 | 說明 |
| --- | --- |
| `/config` | 開啟設定介面，調整主題、模型、輸出樣式等。別名： `/settings` |
| `/theme` | 更換色彩主題，含自動跟隨終端機深淺色、色盲無障礙（daltonized）、ANSI 及自訂主題 |
| `/color [顏色\|default]` | 設定本次工作階段提示列顏色；不帶引數隨機選色 |
| `/tui [default\|fullscreen]` | 切換終端機 UI 渲染器（ `fullscreen` 啟用無閃爍 alt-screen）；不帶引數列印目前渲染器 |
| `/focus` | 切換焦點檢視，僅顯示最後提示、單行工具摘要和最終回應。僅限全螢幕渲染 |
| `/scroll-speed` | 互動調整滑鼠滾輪捲動速度；僅限全螢幕渲染，JetBrains IDE 終端機不支援 |
| `/keybindings` | 開啟或建立快捷鍵配置檔案 |
| `/statusline` | 配置狀態列顯示內容；不帶引數從 shell 提示自動配置 |
| `/terminal-setup` | 配置 Shift+Enter 等快捷鍵（僅在需要的終端機中顯示，如 VS Code、Cursor、Warp、Zed） |

### 八、記憶體與權限管理

| 指令 | 說明 |
| --- | --- |
| `/memory` | 編輯 `CLAUDE.md` 記憶體檔案、啟用／停用自動記憶體、檢視自動記憶體項目 |
| `/permissions` | 管理工具的允許、詢問、拒絕規則；可檢視最近 Auto Mode 拒絕紀錄。別名： `/allowed-tools` |
| `/init` | 用 `CLAUDE.md` 初始化專案；設定 `CLAUDE_CODE_NEW_INIT=1` 可進入互動式引導流程 |

### 九、外部整合

| 指令 | 說明 |
| --- | --- |
| `/mcp` | 管理 MCP 伺服器連線與 OAuth 驗證 |
| `/ide` | 管理 IDE 整合並顯示連線狀態 |
| `/chrome` | 配置 Claude in Chrome 設定 |
| `/install-github-app` | 為存放庫設定 Claude GitHub Actions 整合 |
| `/install-slack-app` | 安裝 Claude Slack 應用程式（開啟瀏覽器完成 OAuth） |
| `/voice [hold\|tap\|off]` | 切換語音聽寫模式；需 Claude.ai 帳戶 |
| `/web-setup` | 用本地 `gh` CLI 認證將 GitHub 帳號連接至網頁版 Claude Code |
| `/setup-bedrock` | 互動式精靈配置 Amazon Bedrock 驗證、區域與模型（需設定 `CLAUDE_CODE_USE_BEDROCK=1` ） |
| `/setup-vertex` | 互動式精靈配置 Google Vertex AI 驗證、專案與區域（需設定 `CLAUDE_CODE_USE_VERTEX=1` ） |

### 十、Skills 與 Plugins

| 指令 | 說明 |
| --- | --- |
| `/skills` | 列出可用 skills；按 `t` 依 token 計數排序；按 `Space` 隱藏 skill |
| `/plugin` | 管理 Claude Code plugins |
| `/reload-plugins` | 重新載入所有作用中的 plugins 套用變更，無需重啟 |

### 十一、診斷、費用與帳戶

| 指令 | 說明 |
| --- | --- |
| `/doctor` | 診斷並驗證 Claude Code 安裝與設定；按 `f` 可讓 Claude 自動修復問題 |
| `/heapdump` | 將 JS 堆快照與記憶體分解寫入 `~/Desktop` ，用於診斷高記憶體使用 |
| `/usage` | 顯示工作階段成本、方案使用限制與活動統計。 `/cost` 、 `/stats` 為別名 |
| `/extra-usage` | 配置額外使用量，在達到速率限制時繼續工作 |
| `/status` | 開啟設定介面的狀態標籤（版本、模型、帳戶、連線），Claude 回覆中也可使用 |
| `/insights` | 產生報告，分析工作階段的專案領域、互動模式與摩擦點 |
| `/privacy-settings` | 檢視與更新隱私設定（僅限 Pro／Max） |
| `/upgrade` | 開啟升級頁面 |
| `/login` / `/logout` | 登入／登出 Anthropic 帳戶 |
| `/passes` | 分享一週免費 Claude Code 通行證（帳戶符合資格時顯示） |

### 十二、團隊協作

| 指令 | 說明 |
| --- | --- |
| `/team-onboarding` | 從過去 30 天使用歷史產生團隊入職 Markdown 指南；Pro／Max／Team／Enterprise 可取得分享連結 |

### 十三、其他

| 指令 | 說明 |
| --- | --- |
| `/help` | 顯示說明與可用命令 |
| `/powerup` | 以互動式課程（附動畫演示）探索 Claude Code 功能 |
| `/release-notes` | 在互動式版本選擇器中檢視變更日誌 |
| `/feedback` | 提交意見反應或回報問題。別名： `/bug` |
| `/mobile` | 顯示 QR Code 下載 Claude 行動應用。別名： `/ios` 、 `/android` |
| `/radio` | 在瀏覽器開啟 Claude FM lo-fi 廣播；無瀏覽器時列印串流 URL（Bedrock／Vertex／Foundry 不支援） |
| `/stickers` | 訂購 Claude Code 貼紙 |
| `/exit` | 結束 CLI。別名： `/quit` |

## Claude Code 常用快捷鍵

![#1 Claude Code指令大全](https://image-cdn.learnin.tw/bnextmedia/image/album/2026-05/tsd8-1778660939.png?w=1200&output=webp)

圖／ ChatGPT生成

| 快捷鍵 | 動作 | 說明 |
| --- | --- | --- |
| `Ctrl+C` | `app:interrupt` | 取消目前操作（ **無法重新綁定** ） |
| `Ctrl+D` | `app:exit` | 結束 Claude Code（ **無法重新綁定** ） |
| `Ctrl+T` | `app:toggleTodos` | 顯示／隱藏工作清單 |
| `Ctrl+O` | `app:toggleTranscript` | 切換詳細逐字稿檢視 |
| `Ctrl+J` | `chat:newline` | 插入換行，不送出 |
| `Escape` | `chat:cancel` | 取消目前輸入 |
| `Ctrl+L` | `chat:clearInput` | 強制全螢幕重繪並保留輸入；全螢幕模式下兩秒內按兩次執行 `/clear` |
| `Cmd+K` | `chat:clearScreen` | 全螢幕模式下兩秒內按兩次執行 `/clear` |
| `Ctrl+G` / `Ctrl+X Ctrl+E` | `chat:externalEditor` | 在外部編輯器開啟輸入內容 |
| `Ctrl+S` | `chat:stash` | 暫存目前提示 |
| `Ctrl+_` / `Ctrl+Shift+-` | `chat:undo` | 復原上一個動作 |
| `Shift+Tab` | `chat:cycleMode` | 循環切換權限模式（Windows 無 VT 模式時預設為 `Meta+M` ） |
| `Meta+P` | `chat:modelPicker` | 開啟模型選擇器 |
| `Meta+O` | `chat:fastMode` | 切換快速模式 |
| `Meta+T` | `chat:thinkingToggle` | 切換延伸思考模式 |
| `Ctrl+X Ctrl+K` | `chat:killAgents` | 終止本工作階段所有背景子 agent |
| `Ctrl+R` | `history:search` | 開啟歷史搜尋 |
| `↑` | `history:previous` | 上一筆歷史記錄 |
| `↓` | `history:next` | 下一筆歷史記錄 |

> 延伸閱讀：  
> [Claude、ChatGPT語音輸入這樣用！5步驟說清任務＋評估標準，讓AI幫你生出最強提示詞](https://www.bnext.com.tw/article/90920/ai-prompt-tips)  
> [ChatGPT Image 2.0指令大全！40組提示詞一次整理，LINE貼圖、簡報封面、插畫菜單全搞定](https://www.bnext.com.tw/article/90908/chatgpt-image-2-prompt-guide-complete)

資料來源： [Anthropic 1](https://code.claude.com/docs/zh-TW/commands) 、 [Anthropic 2](https://code.claude.com/docs/en/keybindings)

本文初稿為AI編撰，整理．編輯/ 黃若彤