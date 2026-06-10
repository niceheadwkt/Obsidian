將 Claude 加入 VS Code（Visual Studio Code）中，最常見且推薦的方式是使用 **Cline**（原名 Devins）或 **Continue** 這類強大的 AI 擴充功能，或者使用 Anthropic 官方支援的 **Sourcegraph Cody**。

以下為你整理最主流、好用的兩種完整安裝與設定步驟：

## 方法一：使用 Continue 擴充功能（最推薦，介面直覺）

**Continue** 是一個開源的 IDE 助理，可以完美對接 Claude 的 API，支援程式碼補全與側邊欄對話。

### 步驟 1：安裝 Continue 擴充功能

1. 打開 VS Code。
    
2. 點擊左側邊欄的 **Extensions（擴充功能）** 圖標（四個正方形的圖案）。
    
3. 在搜尋欄輸入 `Continue`。
    
4. 找到 **Continue**（由 Continue Dev 發行）並點擊 **Install（安裝）**。
    

### 步驟 2：獲取 Claude API Key

1. 前往 [Anthropic Console](https://console.anthropic.com/) 註冊或登入帳號。
    
2. 點擊 **Get API Keys**。
    
3. 建立一組新的 Key 並複製下來（請妥善保管，它只會顯示一次）。
    

### 步驟 3：在 VS Code 中設定 API

1. 安裝好 Continue 後，VS Code 左側邊欄會出現一個 **Continue 的圖標**（通常是一個大於符號 `>`），點擊它。
    
2. 在打開的 Continue 視窗底部，點擊 **齒輪圖標（Settings）**，這會打開一個 `config.json` 設定檔。
    
3. 在 `models` 欄位中加入 Claude 的設定。以下是標準的設定範例：
    

JSON

```
{
  "models": [
    {
      "title": "Claude 3.5 Sonnet",
      "provider": "anthropic",
      "model": "claude-3-5-sonnet-latest",
      "apiKey": "你的_CLAUDE_API_KEY_貼在這裡"
    }
  ]
}
```

4. 儲存檔案（Ctrl + S 或 Cmd + S），你就可以開始在側邊欄和 Claude 對話，或是選取程式碼按 `Ctrl/Cmd + I` 進行重構了！
    

## 方法二：使用 Cline 擴充功能（適合高階自動化開發）

如果你希望 Claude 不只能回答問題，還能**直接幫你建立檔案、修改專案目錄、執行 Terminal 指令**，那麼 **Cline** 是目前最強大的 Agent 工具。

### 步驟 1：安裝 Cline

1. 在 VS Code 的 **Extensions** 搜尋 `Cline`。
    
2. 點擊 **Install** 安裝。
    

### 步驟 2：設定 Claude API

1. 安裝完成後，點擊左側邊欄出現的 **Cline 圖標**（通常是一個機器人或魔杖圖案）。
    
2. 在 Cline 視窗的上方或設定內，將 **API Provider** 切換為 `Anthropic`。
    
3. 在 **Anthropic API Key** 欄位中，貼上你剛剛申請的 Claude API Key。
    
4. 在 **Model** 選擇 `claude-3-5-sonnet-latest`（此模型在程式開發表現最佳）。
    
5. 點擊 **Save**。
    

## 比較與選擇

|**擴充功能**|**特色**|**適合對象**|
|---|---|---|
|**Continue**|介面像 ChatGPT，側邊欄對話流暢，程式碼補全（Autocomplete）效果好。|喜歡傳統 AI 助理、想要輔助寫程式的人。|
|**Cline**|具備 Agent 能力，能自動讀寫檔案、執行終端機指令、自主分析專案。|想體驗「AI 自動幫我寫完一整套功能」的高階開發者。|

> ⚠️ **小提示**：使用上述兩種方法都需要準備 Anthropic 的 API Key。API 是採取「以量計費（Pay-as-you-go）」，新註冊帳號通常會贈送免費額度，額度用完後需要綁定信用卡儲值才能繼續使用。