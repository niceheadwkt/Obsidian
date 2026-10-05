# EA 通報批次（eajcNotifyBatch／eajcSumNotifyBatch）工作筆記

## 上次做到哪 (2026-09-30)
- **起因**：正式機 115/09/29 11:40:51 發出「NA202609221656（中秋節／教師節連假通報）之啟動日期時間 202609290715 已過期，尚未啟動!」。
- **查證結果**（正式機唯讀 SQL）：
  - 啟動確認在 09/22 17:00:49，時機正常；09/25～09/28 八個時段都正常執行，只有 09/29 07:15 沒啟動。
  - `db.tbdqlog`：排程 07:15:00 有 A、B（觸發、進入佇列），C 到 11:40:51 才出現，卡在 `scheduleQueue` 約四小時二十五分。
  - 佇列被 FFRPDAILY05、ZTCCR00010、ZTCHR00030 三個長時間批次佔滿（有 C 沒 D、也沒 F 逾時），直到 11:37～11:40 ERP43／ERP12 連線被拒（G）才被判定失敗釋放；失敗通知網址 `dqjjNotify.jsp` 也無效（FileNotFoundException）。
  - 程式規定啟動時間要和執行當下同一分鐘，因此判定過期。
- **DQ 狀態碼**（反編譯 dq.jar 取得）：A 觸發、B 進佇列、C 派到 AP、D AP 回報完成、E 移出佇列、F 逾時、G 錯誤、H 發失敗通知、I 人工停止。
- **程式修改並 CVS commit**：
  - [eajcNotifyBatch.java](file:///D:/CHSBrowser_erp/erpHome/yl.ear/erp.war/ea/src/com/chsteel/ea/eajcNotifyBatch.java) 1.8 → **1.9**：新增 `checkAndStart()`，容許延遲至 `NtfDateTimeEnd`（空白時 +60 分），已啟動不重發，過期同時通知確認人；修正 `run()` 排序欄位 `StartDateTime` 不存在。
  - [eajcSumNotifyBatch.java](file:///D:/CHSBrowser_erp/erpHome/yl.ear/erp.war/ea/src/com/chsteel/ea/eajcSumNotifyBatch.java) 1.4 → **1.5**：新增 `checkAndSum()`，容許延遲 60 分，已彙總不重跑，回報通報未發出（`StartSW<>'Y'`）不彙總。
  - 無需求單，註解標記為「20260930 改良(26788)」。
- **文件**：
  - [EA通報過期未啟動_NA202609221656.md](file:///D:/temp/EA通報過期未啟動_NA202609221656.md)（問題、影響、關鍵處理、研判及日後對應）
  - [EA通報批次修改方向_eajcNotifyBatch_eajcSumNotifyBatch.md](file:///D:/temp/EA通報批次修改方向_eajcNotifyBatch_eajcSumNotifyBatch.md)（原因、修改方向、程式碼、測試案例）
- **DAJJU1**：測試機上線申請已填兩支的上線說明（尚未由使用者送出）。另建 `erp-dajju1` 技能供 AI 代填上線說明，只填不送。
- **ZPJJB01**：正式機 09/30 序號 001 已代填（0800～1130，系統別 EA，計劃類別 Q0909），待使用者按「新增」。
- **ERP 技能私人 repo（erp-skills）**：
  - GitHub 私人 repo：https://github.com/niceheadwkt/erp-skills （2026-09-30 建立；匿名存取回 404，已確認為 Private）
  - 本機位置：`C:/Users/ch26788/.agents/skills`（中央倉庫，本身就是 git repo，commit `af090c7`，42 個檔案）。
  - 由 `setup-junctions.ps1` 以 Junction 連到 `~/.claude/skills`、`~/.codex/skills`、`~/.gemini/config/skills`、`~/.config/opencode/skills`。
  - `erp-cvs`、`erp-dajju1` 已從 `~/.claude/skills` 搬進中央倉庫，原路徑改為 junction，技能呼叫路徑不變。
  - 內容：db-data-migration-and-analysis、erp-big5、erp-conventions、erp-cvs、erp-dajju1、erp-prod-web-executor、erp-reference，以及通用的 find-skills、mermaid-syntax-guard、pdf。
  - `_home/erp_web_client.py`：`%USERPROFILE%\erp_web_client.py` 的副本（erp-prod-web-executor 使用），兩邊改動要手動同步。
  - **不在 repo 內**：CVS 密碼檔 `%USERPROFILE%\.erp_cvs.dpapi`（DPAPI 加密，只能在本機本帳號解開；新電腦用 `setpw` 重設）。
  - 推送走 Git Credential Manager；`gh` CLI 沒有登入（登入沒有成功，平常同步用 git 即可）。
  - **dotfiles（chezmoi，niceheadwkt/dotfiles）是公開 repo，ERP 技能與公司內部資訊一律不可放進去。** `.claude.json` 也不 commit。
  - 新電腦安裝：clone 到 `%USERPROFILE%\.agents\skills` → 執行 `setup-junctions.ps1` → 複製 `_home\erp_web_client.py` 到 `%USERPROFILE%\`。
  - 日常同步：改完技能在 `~/.agents/skills` 執行 `git add -A`、`git commit`、`git push`；另一台電腦 `git pull`，有新技能再跑 `setup-junctions.ps1`。
  - 注意：`setup-junctions.ps1` 遇到目標目錄有同名實體資料夾會直接刪除（沒有備份），執行前先確認。

- **測試機驗證（2026-09-30 13:25）**：
  - 方式：本機用 `ihjcDsCom` 直連測試 DB（testdb.chsteel.com.tw:50000/idbyl），呼叫 1.9／1.5 的 `doByStartDateTime()`；測試專用通報項目 `NA209909300001`，廠區設不存在的 ZZ。測完已刪除測試資料（N10／N11／NotifyFactory 皆 0 筆）。測試程式在 scratchpad（對話結束即清除）。
  - 通過：準時、容許內延遲、超過回報迄（通知 EASYSMGR＋確認人）、重複觸發略過、NtfDateTimeEnd 空白退回 +60 分、尚未到彙總時間、回報未發出不彙總、彙總超過容許。
  - **未驗證**：案例 6 彙總報表產出（本機缺 `config/yl/zp/zpCommonConfig.ini`，報表失敗）；DW 訊息實際寫入 `tbdw11`（本機執行時沒有寫進去）。發訊息次數是從 log 的 `dwjc111` 呼叫次數推得。
  - 若要在本機完整跑，工作目錄須設為 `erp.war`（有 `erp.ini` 與 `config/yl/`），但會寫 log／報表檔到 CVS 工作目錄、報表可能上傳 FTP、並真的發訊息給測試機 18 位 (ALL) 人員。
  - 使用者決定不再測試，直接準備上正式機。

## 下一步
- DAJJU1 送出上正式機（送出前確認上線類別與需求單號）。
- 上線後第一次有通報時，用正式機唯讀查詢確認：`tbeaNotify11` 的 StartSW／SumSW 有變 Y、報表 K0R00400 有發出、`tbdw11.ACTIVITYNAME` 有通報訊息且過期訊息格式正確。
- 通知業務單位（25346／M9）09/29 07:15 通報沒發出，由他們決定是否人工補通知。
- 請 DQ 管理者：查三個批次卡住原因、替長時間批次設定逾時、修正失敗通知網址；請機房確認 09/29 11:37～11:40 ERP43／ERP12 重啟原因。
- `eaNtfS_*` 彙總排程在 `tbdqlog` 查不到紀錄，待確認記錄位置。
- ZPJJB01 按「新增」後確認工作時數是 3.5 HR。
- 其他電腦要用 ERP 技能時，照 erp-skills 的 README 安裝；以後新增或修改技能一律放 `~/.agents/skills`，完成後 push 到 erp-skills。
