---
type: source-summary
tags: [CI-CD, GitHub-Actions, Playwright, LLM-as-a-judge, VibeCoding, 品管, 自動化測試]
sources: ["[[AI/raw/2026-11-25T132408+0800-用 AI 寫程式你得懂的 CICD？新手一支影片看懂.md|用 AI 寫程式你得懂的 CI/CD？新手一支影片看懂（Gary Chen，YouTube，2026-11-18）]]"]
created: 2026-11-25
updated: 2026-11-25
---

# AI 開發的 CI/CD 品管防線與兩層驗證

Gary Chen 的 YouTube 影片（2026-11-18，約 14 分鐘），以記帳軟體案例拆解 AI 寫程式時代不可或缺的 CI/CD 自動化品管防線、GitHub Actions 雲端隔離檢查機制，以及超越傳統 CI 綠燈的「兩層防線」驗證策略。

> 來源：https://www.youtube.com/watch?v=aCvEYczBVSY 。片尾社群與實戰營宣傳未納入。

**一句話重點**：CI/CD 是 AI 寫程式的底線品管，再加實機驗證才完整

---

## 一、AI 開發的五步標準流程

| 步驟 | 動作 | 核心目的 |
| :---: | :--- | :--- |
| 1 | 開新分支（Branch） | 隔離新功能開發，避免污染 `main` 主線 |
| 2 | 推上 GitHub 開 PR | 宣告功能完成，申請合併進主線 |
| 3 | **CI（Continuous Integration，持續整合）** | 雲端自動跑檢查清單，確認新舊程式碼不相衝 |
| 4 | 合併（Merge）回 `main` | 全部綠燈通過後才合入正式主線 |
| 5 | **CD（Continuous Delivery / Deployment）** | 平台（Render／Vercel／Netlify）偵測主線更新，自動重新打包發布 |

> 持續交付（Delivery）需人工按確認才上線；持續部署（Deployment）則在通過檢查後完全自動發布。

---

## 二、CI 檢查清單的三道基本關卡

CI 本質上是一份可客製化的自動化檢查清單（通常放在 `.github/workflows/ci.yml`），由 GitHub Actions 或開發平台自動讀取執行，基本保底包含三關：

1. **Lint & Typecheck（`npm run lint` / `npm run typecheck`）**：
   - **Lint（風格與靜態規則檢查）**：清除 AI 留下的未用元件與冗餘程式碼，也能設規則封殺高風險寫法（例如禁止 `useEffect` 避免無限迴圈）。
   - **Typecheck（型別檢查）**：免啟動網站即可攔截資料型別錯置（例如誤把純文字「一百元」傳進數值加總）。
2. **Test（`npm run test`，自動功能測試）**：
   - 預先寫好標準驗收腳本（如模擬記帳、算總額、匯出報表與登入），防止開發新功能時意外破壞舊功能（避免打地鼠式修 Bug）。
3. **Build（`npm run build`，打包測試）**：
   - 將數百個開發檔案轉譯組裝成瀏覽器可讀的成品包，提前抓出組裝缺件或建置期錯誤，確保推上線後打得開。

---

## 三、為什麼要用 GitHub Actions（乾淨環境隔離）

本機電腦往往殘留舊套件、全域工具或暫存檔，AI 新功能用到未寫入安裝清單（如 `package.json`）的套件時，本機跑得過但上線必當機。

- **GitHub Actions 機制**：每次開 PR 即在雲端臨時建立一台**全新空白環境**，從頭下載專案、安裝依賴並依序跑完 Lint／Test／Build。
- **排錯流程**：PR 旁顯示通過比例（如 `3/3` 綠勾或 `2/4` 紅叉），點擊 Checks 分頁的 Details 查看報錯後，可讓 AI 透過 GitHub Connector 直接讀取錯誤日誌修正再重推。

---

## 四、進階關卡：Playwright 與 LLM as a judge

當產品變大或包含不確定性 AI 輸出時，可往上疊加進階檢查：

- **Playwright 自動化瀏覽器測試**：在雲端開啟真實瀏覽器模擬點擊與畫面渲染，確認無白屏或按鈕失效。
  - **原則**：只加在**流程已穩定且壞掉直接傷及核心體驗**的路徑（如登入、付款、報表匯出）；變動頻繁的早期原型不急著寫。
- **LLM as a judge（裁判模型評分）**：針對生成文字每次不同的 AI 功能（如 AI 理財顧問），準備約 20 題測試題庫，每次改動 Prompt 或邏輯後重跑一遍，將回答連同正確基準與評分標準交給裁判模型打分，低於門檻即擋下合併。

---

## 五、兩層防線心法：CI 全綠只是底線

- **底層防線（CI/CD 自動流水線）**：負責守住所有「事先定義好」的靜態規則、已知測試腳本與打包上線流程。
- **上層防線（獨立 AI 實機驗證）**：真實使用者不會完全照測試劇本操作，因此參考 `create verification skill` 做法，在合併前派另一批**未參與寫這段程式碼的獨立 AI** 像真人般實機點擊操作並錄下證據，確認玩不壞才放行。

---

## 我可以怎麼用

- **跨機與個人工具開發（如 Python 腳本／MCP Server）**：即使沒有上線網站，只要放上 GitHub 並加上輕量 `ci.yml`（跑語法檢查與關鍵 pytest 單元測試），就能在每次修改後自動確認相依套件清單（`requirements.txt`／`pyproject.toml`）無遺漏。
- **對照本知識庫工具的品管檢查**：`wiki_tool.py check` 與 `wiki_tool.py lint` 就像知識庫的專屬 `Lint + Test`，在入庫完畢或收工前執行以確保無斷鏈與格式缺漏。
- **AI 專案功能驗收與 ERP 驗證思維**：呼應「寫程式的人與驗收測試的人分離」原則，未來讓 Agent 改完程式後，可另開乾淨上下文驗證實機執行結果（如 CDP 唯讀抓頁面或比對 SQL 預期值），而非只看「程式有編譯過」。

---

## 關聯頁面

- [[軟體架構與發布自動化]]：CI/CD 基礎定義、ChatOps 與 Netlify／Mattermost 整合實務。
- [[Git GUI 與 GitHub 雙向同步實務]]：Git 分支、PR 與 GitHub 雙向同步基本操作。
- [[Claude Code 少叮嚀多設限：Opus 5.5 時代最佳實踐]]：指令、Hooks 與 CI 三層驗證點的設計理念。
- [[Chrome Skills 與瀏覽器自動化實務]]：Playwright 自動化操作與瀏覽器測試工具比較。
