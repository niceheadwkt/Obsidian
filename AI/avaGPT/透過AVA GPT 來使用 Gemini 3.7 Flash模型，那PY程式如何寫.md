透過企業級 AI 平台（如 **AVA GPT / AVA AI Gateway**）呼叫底層模型時，通常都是採用 **OpenAI 相容標準（OpenAI-Compatible API）** 介面進行對接。

這代表你可以直接使用 Python 官方的 `openai` 套件或標準 `requests` 庫，只需要將 **`base_url`（API 端點網址）** 指向內部的 AVA GPT 服務，並指定模型名稱與 API Key 即可。

---

### 前置準備

1. **安裝 SDK**（若使用官方套件）：
    
    bash
    
    複製程式碼
    
    `pip install openai requests`
    
2. **確認三項連線資訊**：
    - **`base_url`**：AVA GPT 服務的 API 網址（例如：`https://<your-ava-gpt-domain>/v1` 或內網 IP/URL）
    - **`api_key`**：你在 AVA GPT 平台上取得的 API Key / Token
    - **`model`**：平台上註冊的模型識別名稱（例如 `gemini-3.7-flash` 或 `gemini-2.0-flash` 等）

---

### 方法一：使用 `openai` Python SDK（推薦）

這是最簡潔且支援完整功能（如非同步、串流等）的寫法：

python

複製程式碼

‵‵‵
import os
from openai import OpenAI

# 1. 初始化 Client，指向 AVA GPT 的 API 網址
client = OpenAI(
    api_key=os.environ.get("AVA_API_KEY", "your-ava-api-key-here"),
    base_url="https://<your-ava-domain>/v1"  # 請替換為你內部 AVA GPT 的 API base_url
)

def chat_with_gemini(prompt: str):
    try:
        response = client.chat.completions.create(
            # 指定 AVA GPT 上的 Gemini 模型名稱
            model="gemini-3.7-flash",  
            messages=[
                {"role": "system", "content": "你是一個專業且友善的繁體中文 AI 助手。"},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=2048,
        )
        
        # 取得回覆內容
        reply = response.choices[0].message.content
        return reply

    except Exception as e:
        print(f"呼叫發生錯誤: {e}")
        return None

if __name__ == "__main__":
    user_prompt = "請用 Python 寫一個計算費氏數列的函式，並加上詳細註解。"
    result = chat_with_gemini(user_prompt)
    print("=== AI 回覆 ===")
    print(result)
‵‵‵

### 方法二：支援即時打字效果（Streaming 串流輸出）

處理長文本或對話時，開啟串流可以大幅降低等待時間：

python

複製程式碼

`import os from openai import OpenAI  client = OpenAI(     api_key=os.environ.get("AVA_API_KEY", "your-ava-api-key-here"),     base_url="https://<your-ava-domain>/v1" )  response = client.chat.completions.create(     model="gemini-3.7-flash",     messages=[         {"role": "user", "content": "請列出五個適合初學者的 Python 專案主題與說明。"}     ],     stream=True  # 開啟串流 )  print("=== AI 即時回覆 ===") for chunk in response:     content = chunk.choices[0].delta.content     if content:         print(content, end="", flush=True) print()`

---

### 方法三：使用原生 `requests`（免安裝額外 AI 套件）

如果你在較輕量或受限的伺服器環境中，可直接用標準 HTTP POST 請求：

python

複製程式碼

`import requests import json  AVA_BASE_URL = "https://<your-ava-domain>/v1/chat/completions" AVA_API_KEY = "your-ava-api-key-here"  headers = {     "Content-Type": "application/json",     "Authorization": f"Bearer {AVA_API_KEY}" }  payload = {     "model": "gemini-3.7-flash",     "messages": [         {"role": "system", "content": "你是一個技術顧問。"},         {"role": "user", "content": "請說明 REST API 與 GraphQL 的主要差異。"}     ],     "temperature": 0.7 }  response = requests.post(AVA_BASE_URL, headers=headers, json=payload, timeout=60)  if response.status_code == 200:     data = response.json()     answer = data["choices"][0]["message"]["content"]     print("AI 回覆內容：\n", answer) else:     print(f"請求失敗，狀態碼：{response.status_code}")     print("錯誤訊息：", response.text)`

---

### ⚠️ 常見注意事項與除錯建議

1. **模型名稱確認（Model ID）**：
    - 各企業平台在註冊模型時的命名代碼可能略有差異（例如 `gemini-3.7-flash`、`gemini-2.0-flash`、`gemini-flash` 或 `google/gemini-3.7-flash`）。
    - 若回傳 `404 Not Found` 或 `Model not found`，建議先向平台管理員確認 AVA GPT 後台該模型確切的 **Model Name**。
2. **網址路徑格式**：
    - `OpenAI(base_url=...)` 結尾通常需包含 `/v1`，但**不要**帶有結尾斜線（例如 `https://ava-gpt.company.com/v1`）。
    - 原生 `requests` 的完整 URL 則為 `https://ava-gpt.company.com/v1/chat/completions`。
3. **內網與 VPN**：
    - 若 AVA GPT 為內部私有化部署，請確認執行程式的機器已連上公司內網（Intranet）或 VPN。