# HG／QG 門禁系統新進人員教育訓練 工作筆記

## 上次做到哪 (2026-10-02)
- **需求**：針對 `D:\專業知識\HG` 專案，參考 HG、QG 系統，製作給新進員工使用的教育訓練文件（HTML 格式）。
- **輸出成果**：
  - HTML 版：[HG_QG門禁系統新進人員教育訓練.html](file:///D:/專業知識/HG/HG_QG門禁系統新進人員教育訓練.html)，共十四章，含架構圖、狀態碼、資料表、刷卡通訊、MQ、排程、異常處理手冊、自我測驗。
  - 壓縮檔：[HG_QG門禁系統新進人員教育訓練.zip](file:///D:/專業知識/HG/HG_QG門禁系統新進人員教育訓練.zip)，用來寄信。
  - Obsidian 版：[[HG_QG門禁系統新進人員教育訓練]]，圖表改用 Mermaid，常見問題改用 callout。
  - Outlook 草稿：主旨「HG／QG 門禁系統新進人員教育訓練教材（初稿）請協助檢視」，收件者為劉明峰（ch27159）、楊硯媚（ch26790），附件為 zip。**尚未寄出。**
- **資料來源**：`HG交接`、`KM`（異常處理要領、刷卡機設定要領、MQ 資料錯誤處理）、`.ods` 設定表；`erp.war/hg/system_features.md`；`erp.war/qg/(chatGPT)QG功能規格手冊.md`；`HGJJB02_cardOk核准判斷分析.md`；狀態碼取自 `hgjctb201VO`、`hgjctb206VO`。
- **CVS 查證結果**（qgStructs.xml 中三個沒有程式的頁面設定）：
  - `qgjjb02Copy` 在 1.4 版（2024/03/27，ch26793）加入；`qgjjb03Copy`、`qgjjb01B` 在 1.6 版（2024/05/08，ch26793）加入，提交說明都是空白。
  - 六個 QG 檔案（三支 JSP、三支 controller）在 CVS 中完全沒有紀錄，Attic 也沒有，表示從來沒有提交過。
  - HG 有名稱對應的檔案，而且仍在使用：`hgjjb01Approve`、`hgjjb02Copy`、`hgjjb03Copy`，以及 `hgjcb01Approve`、`hgjcb02Copy`、`hgjcb03Copy`。
  - 推斷是當初從 HG 複製設定過來，但沒有做完。
- **工具**：CVS 歷史查詢用暫存腳本，透過 `erp_cvs.py` 的 `Conn` 送出 `rlog`，並用 `get_server` 取回各版本內容比對（erp-cvs skill 本身只有 status／commit）。
- **處理原則**：交接資料中的帳號密碼，一律不寫進教材與筆記。

## 進度更新 (2026-10-02)
- 教材信件已寄給劉明峰、楊硯媚。
- `qgjjb02Copy`、`qgjjb03Copy`、`qgjjb01B` 三個頁面設定：已確認 QG 選單沒有用到，只是 `qgStructs.xml` 裡沒刪掉的殘留設定。目前保留，暫時不刪除。教材 HTML 版與 Obsidian 版的第五章已同步更新。
- (ZPJJB01) 每日工作記錄已寫入：20261002-001，0800～1100，3.0 HR，系統別 HG（教材製作）；20261002-002，1300～1500，2.0 HR，系統別 HG（erp-cvs 新增 log、cat）。

## 跨 Agent 技能共用整理 (2026-10-02 下午)
- 依 `AI/raw/CROSS_AGENT_SKILLS_SHARING_PLAN.md` 確認：skills 的實體檔案在 `~/.agents/skills`，以 GitHub Private Repo `niceheadwkt/erp-skills` 同步，不使用 chezmoi。
- 規劃書更新：
  - 技能清單改以 repo 的 README.md 為準（目前 10 個）。
  - 註明採用途徑三，途徑二標為未採用。
  - 雲端硬碟路徑改為 `G:/`。
  - 階段二、途徑一移除內嵌程式碼，改為說明並指向 repo。
  - `sanshiba-voice`、`finmind-agent` 確認不納入中央倉庫。
- repo commit `148b2fc`：
  - `setup-junctions.ps1` 補上 BOM（原本無 BOM，PowerShell 5.1 解析會出現 2 個錯誤）。
  - 只把含 `SKILL.md` 的資料夾當成技能，排除 `_home`。
  - 遇到實體資料夾時，先備份到 `~/.agents/skills-backup` 再建 Junction。
  - README 同步更新。
- `AI/scripts/bootstrap-skills.ps1`（Google Drive，不在 repo）改版：
  - 流程改為 `git clone` → 搬移含 `SKILL.md` 的實體技能（排除 `$excludeSkills`，目前為 `finmind-agent`）→ 複製 `_home` 檔案 → 執行 repo 內的 `setup-junctions.ps1`。
  - 移除 Google Drive 的 `claude_erp_rule` 遷移來源，補上 opencode。
  - 只做過語法檢查，**尚未實際執行**。

- **✅ 結案（2026-10-07）**：使用者決定教材不發布、不再後續修訂，本案結案；HTML 留在本機供參考（不提交 CVS）。

## 下一步
- 已結案，沒有待辦（以下為結案前紀錄，僅供參考）。
1. 等劉明峰、楊硯媚回覆。
2. 依回覆修正教材：控制主機 IP 與維護單位、排程清單（以 DF 現行設定為準）、MQ 處理步驟。
3. ~~考慮把 erp-cvs 的 `rlog` 查詢功能正式加進 skill。~~ 已完成（2026-10-02）：`erp_cvs.py` 新增唯讀指令 `log [-n 筆數]`、`cat <檔案> -r <版次> [-o 輸出檔]`，以及結束碼 5（`NOT_FOUND`），`SKILL.md` 也補上歷史查詢流程。查詢已刪除檔案（Attic）的分支，因為 zp、ds、ea、hg 都找不到可測試的檔案，還沒有實測。備份方式：依 `CROSS_AGENT_SKILLS_SHARING_PLAN.md`，skill 的實體檔案在中央倉庫 `~/.agents/skills`（`~/.claude/skills/*` 是 Junction，連回中央倉庫），以獨立 Git repo 同步到 `github.com/niceheadwkt/erp-skills`，**不要**用 chezmoi 管理 skills。本次修改已 commit `3650bea` 並 push。
4. （暫緩）QG 那三個殘留的頁面設定，已確認選單沒有用到，目前保留；以後若要整理 `qgStructs.xml`，可以直接刪除。
