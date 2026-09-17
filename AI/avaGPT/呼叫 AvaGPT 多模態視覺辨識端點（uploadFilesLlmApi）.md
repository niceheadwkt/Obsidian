  呼叫 AvaGPT 多模態視覺辨識端點（uploadFilesLlmApi）的核心技術規格與完整 Python 呼叫範例如下：
  ──────
  ### 一、API 核心規格

| 項目                      | 說明                                                                                                         |
| ----------------------- | ---------------------------------------------------------------------------------------------------------- |
| 請求端點 (URL)              | https://avagpt.chsteel.com.tw/ava/backend/file/uploadFilesLlmApi                                           |
| HTTP 方法                 | POST                                                                                                       |
| 請求格式                    | multipart/form-data（由 requests 的 files 參數自動組裝，切勿手動指定 Content-Type）                                         |
| 必要 Headers              | Origin: https://avagpt.chsteel.com.twapi-key: ak_...                                                       |
| 支援檔案格式                  | .jpg, .jpeg, .png, .gif, .webp, .pdf                                                                       |
| 支援多模態模型 (model_list_id) | • "12"：caf-azure-gpt-4o• "75"：openai/gpt-4.1 (OpenRouter)• "1"：gpt-4o (OpenAI)• "67"：caf-azure-gpt-4o-mini |
  ──────
  ### 二、完整 Python 呼叫程式碼

  這是一份可以直接獨立執行的最小範例腳本：
    import os
    import sys
    import requests

    # 避免 Windows 終端輸出簡體字或 Emoji 報錯
    if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    # ============================
    # 1. 連線設定
    # ============================
    BASE_URL = "https://avagpt.chsteel.com.tw"
    API_KEY = "ak_xpPY9id4YhRacNYx0dlnhw8JERfckxtZIsxbbWPHIk"
    URL = f"{BASE_URL}/ava/backend/file/uploadFilesLlmApi"

    HEADERS = {
        "Origin": BASE_URL,
        "api-key": API_KEY,
        # 注意：絕對不要加 "Content-Type": "application/json"，
        # requests 在帶入 files 參數時會自動設定 multipart/form-data 及 boundary
    }

    # 支援的副檔名與 MIME 類型映射表
    MIME_MAP = {
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".gif": "image/gif",
        ".webp": "image/webp",
        ".pdf": "application/pdf",
    }

    def call_ava_vision(image_path: str, prompt: str = "請描述這張圖片的內容", model_list_id: str = "12"):
        """
        呼叫 Ava 多模態視覺辨識 API

        :param image_path: 圖片或 PDF 本機檔案路徑
        :param prompt: 針對圖片的提問或指令
        :param model_list_id: 模型 ID，預設 "12" (caf-azure-gpt-4o) 或 "75" (gpt-4.1)
        """
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"找不到檔案: {image_path}")

        # 1. 取得副檔名與 MIME 類型
        ext = os.path.splitext(image_path)[1].lower()
        mime = MIME_MAP.get(ext)
        if not mime:
            raise ValueError(f"不支援的副檔名: {ext}，僅支援: {list(MIME_MAP.keys())}")

        filename = os.path.basename(image_path)

        # 2. 讀取二進位檔案資料
        with open(image_path, "rb") as f:
            file_bytes = f.read()

        # 3. 組裝 multipart/form-data
        # 檔案欄位名稱固定為 'files'，格式為 (檔名, 二進位資料, MIME 類型)
        files = [("files", (filename, file_bytes, mime))]

        # 表單額外欄位
        data = {
            "message": prompt,              # 提示詞 / 提問
            "model_list_id": model_list_id,  # 指定模型 ID
        }

        print(f"正在上傳: {filename} ({len(file_bytes):,} bytes)")
        print(f"使用模型 ID: {model_list_id}")
        print(f"提問內容: {prompt}")

        # 4. 發送 POST 請求
        resp = requests.post(URL, headers=HEADERS, files=files, data=data, timeout=120)

        # 5. 解析回應結果
        if resp.status_code != 200:
            print(f"HTTP 請求錯誤: {resp.status_code} - {resp.text}")
            return

        body = resp.json()

        # Ava API 規範：code == 0 表示成功
        if body.get("code") == 0:
            data_block = body.get("data", {})
            answer = data_block.get("response", data_block)

            print("\n=== AI 視覺辨識回應 ===")
            print(answer)

            # Token 使用統計
            p_tok = data_block.get("prompt_token")
            c_tok = data_block.get("completion_token")
            t_tok = data_block.get("total_token")
            if t_tok is not None:
                print(f"\n[Token 統計] Prompt: {p_tok}, Completion: {c_tok}, Total: {t_tok}")

            return answer
        else:
            err_msg = body.get("message") or body.get("data")
            print(f"\n❌ 呼叫失敗 (code={body.get('code')}): {err_msg}")
            return None

    # ============================
    # 執行測試
    # ============================
    if __name__ == "__main__":
        # 範例呼叫：
        test_image = "test.png"  # 請替換為您的圖片路徑
        if os.path.exists(test_image):
            call_ava_vision(
                image_path=test_image,
                prompt="請辨識這張圖片中的表格內容，並轉為繁體中文 Markdown 表格",
                model_list_id="12"  # 12 代表 caf-azure-gpt-4o
            )
        else:
            print(f"請放置測試圖片 {test_image} 後再執行。")
  ──────
  ### 三、關鍵細節與避坑指南

  1. files 欄位命名必須為 "files"：
      • API 後端接收 multipart 的檔案鍵值名稱固定是 "files"，格式必須是：
        files = [("files", (filename, file_bytes, mime))]

  2. 切勿手動加上 Content-Type Header：
      • 若在 HEADERS 加上 "Content-Type": "application/json"，會覆蓋掉 requests 原本要帶入的 multipart/form-data; boundary=...，造成後端無法解析檔案。
  3. 選擇有 Vision 能力的模型：
      • 純文字模型（如 16: gpt-3.5-turbo）無法做圖片辨識。推薦使用：
          • 12：caf-azure-gpt-4o（公司內部 Azure 部署，速度快且辨識精準）
          • 75：openai/gpt-4.1（OpenRouter）
          • 1：gpt-4o（OpenAI 原生）

  4. 專案現有實作參考：
      • CLI 實作範例可見：ava_api_example.py:152-206 的 upload_image()
      • MCP Tool 實作範例可見：mcp_server.py:138-187 的 ava_vision()