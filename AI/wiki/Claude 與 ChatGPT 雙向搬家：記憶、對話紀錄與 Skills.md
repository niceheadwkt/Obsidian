---
type: source-summary
tags: [Claude, ChatGPT, Codex, 記憶轉移, AgentSkills, 資料匯出, 平台遷移, 數位時代]
sources: ["[[AI/raw/2026-09-29T114755+0800-換AI不用重教一次！Claude⇄ChatGPT雙向搬家，記憶、對話紀錄、Skills轉移教學一次看.md|換AI不用重教一次！Claude⇄ChatGPT雙向搬家（數位時代，2026-09-28）]]"]
created: 2026-11-18
updated: 2026-11-18
---

# Claude 與 ChatGPT 雙向搬家：記憶、對話紀錄與 Skills

《數位時代》蘇柔瑋整理（2026-09-28，初稿由 AI 協助編撰），參考《How to AI》電子報 Ruben Hassid 的流程並比對 Anthropic、OpenAI 官方文件，實測「Claude 轉 ChatGPT」與「ChatGPT 轉 Claude」兩個方向。介面與功能以 2026-09 為準，兩家都在分批改版，選單位置可能不同。

**一句話重點**：記憶、偏好、Skills 搬得走，完整對話紀錄搬不走

## 一、哪些能搬、怎麼搬

| 要搬的資料 | Claude → ChatGPT | ChatGPT → Claude |
|------------|------------------|------------------|
| 記憶與偏好 | 匯出 Claude 對話 → 濃縮成記憶檔 → 上傳 ChatGPT | Claude 內建記憶匯入工具 |
| Skills 與工作設定 | ChatGPT 桌面版「匯入」 | Skill 資料夾壓成 ZIP 手動上傳 |
| 操作裝置 | Claude 網頁版／桌面版；ChatGPT 網頁版（記憶檔）、桌面版（Skills） | 能登入 Claude 設定頁的裝置 |

搬家本質是**把個人背景、偏好與工作設定複製到新平台**；原本的對話紀錄不會出現在另一個 AI 裡。

## 二、Claude → ChatGPT：六步驟

1. **匯出 Claude 資料**：設定 → 隱私 → 匯出資料，可選起始時間；下載連結寄到信箱，**24 小時失效**。只能在網頁版或桌面版操作，iOS、Android 不行；Team／Enterprise 一般成員不能自行匯出，須由 Primary Owner 操作。
2. **取得完整對話檔**：信中下載的 `.json` 只是**索引清單**，不含對話內容；用記事本打開找到第一個 `https` 網址，貼到瀏覽器下載 `conversations-000.zip`，解壓得到 `conversations.json`（第二個 `light_metadata` 可略過）。
   > [!WARNING] 下載連結等於通行密鑰
   > 清單裡的兩組連結直接指向個人資料下載入口，不要轉傳，也不要貼進任何 AI 對話。
3. **濃縮成記憶檔**：開新 Claude 對話上傳 `conversations.json`，請它整理成 `Claude-to-ChatGPT.md`，章節為：
   - 核心背景（身分、工作、團隊、長期目標）
   - 回應指令（1,500 字元內、第一人稱，可直接貼進自訂指令）
   - 長期偏好（寫作風格、格式、禁用詞、明確糾正過的地方）
   - 進行中的專案（目的、最新狀態與日期、已確定的決策）
   - 衝突與過時資訊

   規則：只把使用者明確同意的內容列為決策、數字與狀態標日期、**排除密碼、API 金鑰與下載連結**、讀不到的檔案要說明不要假裝讀過。產出後先自己檢查、刪掉不想帶走的內容。
4. **放進 ChatGPT 記憶**：上傳到 ChatGPT 檔案庫（Library，網頁版，Free／Go／Plus／Pro／Business 可用），勾選後開始對話，請它把「核心背景」「長期偏好」一則一事實存進記憶、過時衝突的不存、最後列出存了哪些。
5. **語氣與格式放自訂指令**：把記憶檔的「回應指令」段貼到 設定 → 個人化 → 自訂指令。OpenAI 建議：明確規則放自訂指令，對話細節交給記憶。
6. **搬 Skills 與代理設定**：ChatGPT 桌面版 設定 → 匯入（或「一般」中的 Import other agent setup），支援 Claude Code、Claude Cowork、Cursor，可勾選指令、設定、Skills、專案、近期工作。匯入是在 ChatGPT 端新增一份，**不會刪除原工具內容**，部分設定可自動同步。

## 三、ChatGPT → Claude：兩步驟

1. **讓 ChatGPT 吐出記憶**：Claude 設定 → 記憶 → Start import（舊版介面在 設定 → 功能），複製 Claude 給的提示詞貼到 ChatGPT 執行，取得程式碼區塊結果。
   - 若 ChatGPT 回一堆「[unknown] 找不到相關記憶」，依序排查：確認記憶功能已開啟 → 到記憶設定頁看實際存了什麼 → 直接問「你記得我哪些事？」→ 追問「不要摘要，一條一條列出來」再「整理成程式碼區塊」。
   - 貼回前先刪掉過時、不正確或不想留的條目。
2. **存進 Claude**：貼進「Paste results below to add to Claude's memory」→ Add to memory。畫面不會即時更新。
   - 記憶匯入仍是**實驗功能**，不一定完整吸收。
   - Claude 記憶**聚焦工作相關主題**，與工作無關的個人細節可能不保留；一定要留的用「Tell Claude what to change or remove」補，或直接在對話中說。
   - 驗收：開新對話問「你目前對我有哪些了解？」

## 四、Codex Skills 搬到 Claude

- 兩邊都是「Skill 資料夾＋說明檔」結構，以指令與參考資料為主的 Skill 通常可沿用；用到 Codex 專屬工具、MCP、`agents/openai.yaml` 或特定執行環境的需另外調整。
- Codex 個人 Skills 在使用者主目錄 `.agents/skills`，專案 Skills 在專案內 `.agents/skills`。
- 每個 Skill 資料夾**各自壓成 ZIP，最外層是資料夾**（說明檔與參考資料放在資料夾內），到 Claude「Customize → Skills → ＋ → Create skill → Upload a skill」上傳。
- Claude Skills 開放 Free／Pro／Max／Team／Enterprise，須先啟用程式碼執行；Enterprise 要管理員先在 Organization settings → Skills 開啟。

> [!NOTE] 衝突已解決（2026-11-18）
> 本文說搬到 Claude 前要把 `SKILL.md` 改名為小寫 `skill.md`，**此說有誤**。經使用者確認，Skill 主檔名為大寫 `SKILL.md`（與 [[LLM 到 Agent 的工程解析]] 一致），Codex 搬到 Claude 時檔名維持不變即可。

## 五、限制與補充

| 限制 | 說明 |
|------|------|
| 手機無法匯出 Claude 資料 | 只能用網頁版或桌面版 |
| 公司帳號需管理者 | Team／Enterprise 只有 Primary Owner 能匯出 |
| Claude 記憶匯入會篩選 | 不一定全部保留 |
| ChatGPT 記憶介面因地區而異 | 新功能分批推出 |
| Claude 介面整合中 | 2026-09-16 起 Chat、Cowork、Artifacts 逐步整合為統一介面，由 Claude 自動判斷能力，不再手動切換 Cowork 分頁；先從 Pro、Max 分批推出，設定位置可能再調整 |
| 對話紀錄無法重現 | 只複製設定，不搬完整對話 |

- **Claude Code → Codex CLI**：在 Codex CLI 輸入 `/import`，可匯入 Claude Code 設定與近 30 天內最多 50 則對話；claude.ai 網頁版聊天紀錄不在範圍內。

## 我可以怎麼用

- **你的「記憶」本來就在本機**：全域規則（`~/.claude/rules/`）、CLAUDE.md、Skills 都是 Markdown 檔：全域規則用 chezmoi 跨電腦同步（見 [[AI Agent 實戰與 MCP 伺服器整合]]），Skills 則放在 `~/.agents/skills` 私人 Git repo、用 Junction 分給四個工具（見 [[跨 Agent 技能共用：中央倉庫與 NTFS Junction]]）。換到 Codex 時，這套檔案比平台內建記憶更好搬；平台記憶只當補充。
- **跨 Agent 共用 Skills**：自己的 skill 已採資料夾＋`SKILL.md` 結構，Codex 與 Claude Code 都讀得懂；放進 `.agents/skills` 或用目錄連接點共用，比每次 ZIP 上傳省事。網頁版 Claude 才需要 ZIP 上傳。
- **借用「記憶檔」提示詞做年度整理**：第三步的五章節提示詞（核心背景、回應指令、長期偏好、進行中專案、衝突與過時資訊）也適合拿來整理自己的 CLAUDE.md 或 Obsidian 工作筆記，順便找出過時規則。
- **匯出資料要當機密處理**：`conversations.json` 可能含 ERP 討論、SQL 與公司內部資訊，存放在本機非同步資料夾、用完刪除；下載連結不要貼進任何 AI（呼應 [[ChatGPT 與 Claude 對話隱私與關閉訓練設定]]）。
- **公司帳號先問管理者**：若改用 Team／Enterprise，個人無法自行匯出，搬家前先確認誰是 Primary Owner。

## 關聯頁面
- [[Claude 高階提示詞與應用場景]]（ChatGPT／Gemini → Claude 記憶轉移）
- [[Claude Cowork 與 Agent Skill 實務]]
- [[ChatGPT 與 Claude 對話隱私與關閉訓練設定]]
- [[LLM 到 Agent 的工程解析]]（Agent Skill 結構）
- [[AI Agent 實戰與 MCP 伺服器整合]]（跨電腦／跨 Agent 同步）
- [[Antigravity 核心概念與五層記憶系統]]（Antigravity 的記憶轉移）
- [[跨 Agent 技能共用：中央倉庫與 NTFS Junction]]（本機跨 Agent 共用 Skills）
