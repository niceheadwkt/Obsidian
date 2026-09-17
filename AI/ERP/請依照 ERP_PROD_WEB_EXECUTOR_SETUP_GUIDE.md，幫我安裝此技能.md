  已依照指南 ERP_PROD_WEB_EXECUTOR_SETUP_GUIDE.md，為您完成 erp-prod-web-executor（正式機 Web 查詢技能） 的完整安裝與配置！
  ──────
  ### 一、已完成的安裝項目與檔案清單

  1. Python 依賴套件：
      • 已成功安裝 websocket-client（用於與瀏覽器 CDP 遠端調試埠 9222 進行即時 WebSocket 通訊）。
  2. 桌面 AI 連線模式啟動捷徑：
      • Chrome 捷徑：啟動正式機ERP(AI連線模式.bat)
      • Edge 捷徑：啟動正式機ERP(Edge連線模式.bat)
  3. 通用橋接腳本：
      • 檔案路徑：erp_web_client.py
      • 具備：
          • 唯讀安全守門：嚴格限制僅允許 SELECT / WITH 查詢，阻擋任何寫入語法。
          • 智慧雙軌輸出：≤20 筆直接呈現在對話中；>20 筆自動轉存至 D:\temp\query_results\ 並僅預覽前 3 筆以極致節省 Token。

  4. Antigravity CLI Skill 註冊檔：
      • 配置路徑：SKILL.md

  ──────
  ### 二、日常使用 SOP

    flowchart LR
        A[1. 雙擊桌面捷徑開啟瀏覽器] --> B[2. 輸入帳密登入正式機 ERP] --> C[3. 在 Antigravity CLI 用自然語言查詢]

  1. 啟動瀏覽器：雙擊桌面上的 啟動正式機ERP(AI連線模式).bat（或 Edge 版本）。
  2. 登入 ERP：在該瀏覽器視窗中登入正式機帳號密碼。
  3. 開始查詢：在對話中直接使用自然語言指示，例如：
      • 「幫我查正式機 db.tbeaWorkDoc 最近 5 筆資料」
      • 「查詢正式機員工 26788 的請假記錄」
      • 「執行正式機查詢：SELECT * FROM db.tbeaRE00 WHERE formNo = '26S01M462262081511'」*
