  ### 一、問題修復摘要

  1. 修復 pipeline.py 的 scalar_subquery 錯誤
      • 原因：原本在取得上週價格進行 WoW 計算時，誤將 session.execute(...) 包在子查詢外層，導致呼叫 ChunkedIteratorResult.scalar_subquery() 拋出 AttributeError。
      • 修正：將子查詢改為直接對 SQLAlchemy select 陳述式呼叫 scalar_subquery()，正確取得前一週價格字典。
  2. 修復新版 Starlette / FastAPI 的 TemplateResponse 呼叫相容性
      • 影響檔案：
          • app.py（dashboard 視圖）
          • prices.py（price_list 與 price_detail 視圖）
          • summaries.py（summary_list 與 summary_detail 視圖）
      • 原因：新版 Starlette 中 TemplateResponse 的第一個參數已改為 request，原本傳入字典 context 會被當成 template name 快取 key，觸發 TypeError: unhashable type: 'dict'。
      • 修正：一律採用標準關鍵字參數 templates.TemplateResponse(request=request, name=..., context=...)。

  ──────
  ### 二、單元測試驗證

  執行完整的 Pytest 測試套件：

    uv run --with pytest --with httpx pytest

  • 測試結果：25 passed, 2 skipped（全部通過，無任何報錯）。
  ──────
  ### 三、fastmarkets-v2 ingest 匯入執行結果

  重新執行批次匯入指令：

    uv run fastmarkets-v2 ingest

  • 執行結果：完成: 1 檔, 新聞 0 篇, 價格 0 筆, 失敗 5 篇
  • 失敗診斷：
      • 程式碼管線與資料庫寫入皆正常運作無崩潰。
      • 提取的 5 篇新聞在呼叫 Ava GPT API（專家 28999566-b676-4449-aa41-0077857ace8a）進行摘要時，內部 Ava 伺服器回傳：
        {"error": "Upstream service error: No API key was provided. Please pass a valid API key. Learn how to create an API key at https://ai.google.dev/gemini-api/docs/api-key."}

      • 此為 Ava GPT 後端平台未設定或過期 Google Gemini API Key 所致（透過 mcp_server.py 確認 Web Gateway 正常，但後端 RAG 推論回傳 500）。待 Ava 伺服器金鑰補齊後，管線即可自動完成新聞摘要生成。
