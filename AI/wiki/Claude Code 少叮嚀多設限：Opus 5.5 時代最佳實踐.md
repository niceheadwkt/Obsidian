---
type: source-summary
tags: [Claude Code, CLAUDE.md, Opus 5.5, auto mode, deny規則, hooks, 沙盒, 驗證點, CI, Claude Code projects, 最佳實踐]
sources: ["[[AI/raw/2026-11-18T162924+0800-Claude Code設定大洗牌！進入Opus 5.5時代之後，為何CLAUDE.md愈短愈好？.md|Claude Code 設定大洗牌（數位時代）]]"]
created: 2026-11-20
updated: 2026-11-20
---

# Claude Code 少叮嚀多設限：Opus 5.5 時代最佳實踐

本頁整理《數位時代》2026-11-17 刊出、李先泰整理編輯的〈Claude Code 設定大洗牌！進入 Opus 5.5 時代之後，為何 CLAUDE.md 愈短愈好？〉（原文註明初稿為 AI 編撰）。內容主要來自 Anthropic Claude Code 開發者關係 Lydia Hallie 於 2026-11-12 的 AI Engineer 演講〈Rethinking Claude Code Best Practices〉。

**一句話重點**：對 AI 少叮嚀，對環境多設限，用驗證點取代人工盯場。

## 一、背景：人從盯一個 session 變成管幾十個

- Anthropic 每天合併的程式變更，從 2026 年 5 月約 2,500 筆增加到 9 月超過 3 萬筆，四個月成長十倍以上。
- 工程師同時管幾十個 session，每個跑數小時、自己驗證結果，甚至由一個 session 指揮其他 session。
- 年初 Opus 4.5 會提早停下來，大家在 `CLAUDE.md` 堆滿「IMPORTANT！」「絕對不要！」；沒有 auto mode，只能逐條按允許或整個關掉權限檢查。這些做法**只在當時是對的**。

## 二、「少」：CLAUDE.md 只留程式碼看不出來的事

- Opus 5.5 更懂意圖與程式碼，加驚嘆號的強硬指令不但沒必要，還可能讓模型偏離方向、工具呼叫變多、結果更差。
- 原則：**`CLAUDE.md` 只留程式碼看不出來的事**。例：某服務還連著一個程式碼沒直接引用的舊資料來源 → 留；用什麼技術、檔案放哪 → 模型看得出來，刪。
- 工具：`/doctor prompt-audit` 會檢查 `CLAUDE.md` 和技能檔，列出新模型不再需要的指示（需 v2.1.283 以上）。
- 光換成現行預設值（新模型＋auto mode），人在迴圈裡的工作就去掉大半。

## 三、「多」之一：安全靠 deny 規則與環境，不靠人按允許

- Anthropic 8 月實驗：1,053 名付費專業測試者面對明顯危險的指令，只攔下 13.6%；auto mode 分類器攔下 89%。
- 判準：**Claude 做錯一次，你收得回來嗎？**
  - 收得回來（程式寫錯可還原）→ 交給模型。
  - 收不回來（丟掉未提交的改動、把密碼讀進對話）→ 寫成 **deny 規則**，在分類器之前生效，一命中就擋。例如禁止讀 `.env`。
- **權限只管指令能不能跑，管不了它跑起來碰到什麼**：`npm test` 會被放行，但測試會執行第三方套件或臨時腳本，被動手腳就能讀 `.env` 外傳。所以還要框住環境：
  - 本機：用沙盒，由作業系統限制可讀檔案與可連網址，連子程序一起管。
  - 更推薦雲端 session：乾淨獨立機器，從 repo 重新複製，不帶本機未提交檔案與憑證。但推出去的東西收不回來，deny 規則與 auto mode 仍要留。

## 四、「多」之二：三層驗證點取代逐檔審查

同一句「把登入系統搬到新 API」可能有三種看似合理卻不同的結果，所以要設**驗證點**——任何能回答「過或沒過」的東西（測試、建置、截圖）。

1. **指令層**：寫清楚「完成長什麼樣」，要求拆成任務、各配測試，並貼出實際輸出。
2. **hooks 層**：在改檔、標記完成、結束 session 等固定時機跑檢查；失敗就擋住，Claude 得回頭處理。
3. **CI 層**：每個 PR 跑同一套檢查，沒過 Claude 自己回去修。Claude Code 團隊另加：由不帶原 session 記憶的 Claude 審 PR，另一組 agent 複核找到的 bug。

人工審查量依風險決定：文件文案全綠可不看、一般變更一人審、高風險兩人審；自動合併不是預設。

## 五、下一步：連開 session 都交出去

- **Claude Code projects**（截至 11/16 公測，僅 Pro、Max、Ultra 個人方案）：主 session 拆工作、派工、追蹤，自己不寫程式。建議主 session 用擅長判斷的 Fable，動手的用 Opus 5.5。
- 注意：projects 派出的雲端 session **不套用 repo 設定檔的 deny 規則，也不跑 hooks**；要用這兩樣得在本機跑。
- 最佳實踐「搬了家」：導航→模型、核准→auto mode、限制→deny 規則與環境、把關→測試／hooks／CI、啟動→projects。人只剩開第一個 session 與驗收結果。
- 起手式：挑一件比平常大很多的任務，確認 CI 抓得到你在意的事，設好網路權限與機密，丟到雲端跑，看它卡在哪——卡住的地方就是下一件該交出去的事。

## 六、五個馬上能做的調整

1. 跑 `/doctor prompt-audit`，刪掉新模型不需要的指示。
2. `settings.json` 的 `permissions.deny` 加入 `Read` 規則，擋住讀檔工具與 `cat` 等它認得的指令；腳本自行開檔要靠沙盒，沙盒也管不到 MCP 伺服器與 hooks。
3. 用 TaskCompleted、Stop 等 hooks 擋完成時，失敗要回 **exit code 2**；回 1 只算一般錯誤，任務仍會被標成完成。
4. 下指令先寫「完成長什麼樣」，要求拆任務、配測試、貼實際輸出。
5. 雲端 session 的 API 金鑰設成 network secret，由代理伺服器附在請求上，模型看不到；單一 repo 雲端 session 會讀 repo 內 `.claude/settings.json` 的 deny 與 hooks，所以要 commit 進 repo。

## 我可以怎麼用

- **瘦身全域規範**：`~/.claude/CLAUDE.md` 與 `rules/` 下的規範有不少「一律」「禁止」「必須」的強硬語氣。可以跑一次 `/doctor prompt-audit`，把模型自己看得出來的部分刪掉，只留「程式碼看不出來的事」，例如 Google Drive 唯一正確路徑、zpq 的違規計次規則、ERP 檔案必須 Big5。
- **把「收不回來」的事改成 deny 規則**：例如 `%USERPROFILE%\.zpq\token` 目前只寫在 CLAUDE.md 叫 AI 不要讀，可改成 `permissions.deny` 的 `Read` 規則，由工具層直接擋。chezmoi 同步時一起帶到每台電腦。
- **用 hooks 當驗證點**：Wiki 入庫的 `wiki_tool.py check`、ERP 改檔後的 Big5 驗證，都是「過或沒過」的檢查，可以綁在 Stop hook，失敗回 exit code 2，讓 Claude 自己修到通過才收尾。
- **ERP 正式機仍要人在迴圈**：DAJJU1 上線、資料異動單屬於收不回來的動作，維持人工確認，不要交給自動模式。

## 關聯頁面

- [[Claude 系統優化與 Token 節省指南]]：CLAUDE.md 精簡規則與自我審查提示詞。
- [[Claude 高階提示詞與應用場景]]：Opus 4.7 字面化與「少即是多」提示心法。
- [[Claude（Anthropic）]]：Claude Code CLI 與模型版本。
- [[跨 Agent 技能共用：中央倉庫與 NTFS Junction]]：全域規則與技能的跨電腦同步方式。
- [[假冒 Claude Code 官網木馬與雲端帳單盜刷事件]]：憑證外洩的實際案例，對照 deny 規則與沙盒的必要性。
