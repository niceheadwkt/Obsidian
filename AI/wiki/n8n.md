---
type: entity
tags: [n8n, No-Code, Low-Code, 工作流程自動化, Docker, 自架, API串接, 開源]
sources: ["[[AI/raw/2026-11-12T113821+0800-AI工作流程自動化實作（n8n＋LINE＋Gemini）課程重點整理.md|AI 工作流程自動化實作（n8n＋LINE＋Gemini）課程重點整理]]"]
created: 2026-11-12
updated: 2026-11-12
---

# n8n

**n8n** 是一個可高度擴充、以節點組成的**工作流程自動化平台**，屬於 No-Code／Low-Code 工具。在視覺化畫布上拖拉節點、拉線串接，就能把應用程式、資料庫、API 和 AI 模型串成自動執行的流程。官網：https://n8n.io

完整的入門實作請見 [[AI 工作流程自動化實作_n8n 課程總結]]。

---

## 核心概念

| 名詞 | 說明 |
| :--- | :--- |
| **Node（節點）** | 像積木，**一個節點只做一件簡單的小事**。內建數百種整合節點，例如 Google Workspace、GitHub、Slack、各種資料庫 |
| **Workflow（工作流）** | 用線把節點串起來，資料**由左往右**流動；節點的順序要先規劃好 |
| **Canvas（畫布）** | 設計工作流的區域 |
| **Trigger（觸發節點）** | 流程的起點，可以是手動、定時、Webhook 等 |
| **Credential（憑證）** | 串接外部服務時使用的驗證資訊，例如 Header Auth、OAuth |
| **Execution（執行紀錄）** | 每次執行的結果，會顯示 success 或 error |

### 萬用節點
- **HTTP Request**：沒有現成節點的服務，都能透過 API 串接，例如 LINE Messaging API、Gemini API。
- **Webhook**：讓外部系統主動呼叫 n8n。
- **Extract from File**：轉換資料格式，例如 XML 轉 JSON。
- **IF／Switch**：條件判斷與分支。

---

## 部署方式

| 方式 | 費用 | 說明 |
| :--- | :--- | :--- |
| n8n Cloud（官方） | 付費（約 20 歐起／月，以官網為準） | 環境由官方代管 |
| 其他雲端主機自架 | 通常較便宜 | 自己管理主機 |
| **本機 Docker 自架** | 免費 | `docker run -d -p 5678:5678 -v <路徑>:/home/node/.n8n docker.n8n.io/n8nio/n8n`，再開啟 `localhost:5678` |

**本機版的注意事項**
- 每次使用前，Docker Desktop 裡的容器要是**綠燈（執行中）**，啟動後等大約 5 秒暖機。
- 只啟動容器不需要網路；串接外部 API 時才需要。
- 自架可以讓資料留在內網，對企業的資料管控比較有利。

---

## 常用操作技巧
- 搜尋節點時只要輸入開頭幾個字母。
- 點兩下節點進入設定畫面，畫面分三欄：**左邊 Input、中間設定、右邊 Output**。
- 單一節點按「執行此步驟」測試，再回畫布按「執行工作流程」，確認每個節點都出現綠色勾勾。
- 可以 **Duplicate** 工作流或節點、**Rename** 節點，並從節點右邊的小白點拉出分支。
- JSON Expression 可以直接從 Input **拖拉欄位**，產生 `{{ $json.xxx }}` 的寫法。

---

## 與其他工具比較
- [[Dify]]：也有 Canvas 工作流，但重點在 LLM 應用、RAG 知識庫與 BaaS API；n8n 的重點是**跨系統的流程自動化**。
- AI Agent（例如 Antigravity、Claude Code）用自然語言就能產生類似的自動化流程，有人因此討論「n8n 會不會被取代」，見 [[Antigravity 核心概念與五層記憶系統]]。
- 其他介紹：[[AI 工具與框架概覽]] 的免安裝開源工具清單中也有提到 n8n。
