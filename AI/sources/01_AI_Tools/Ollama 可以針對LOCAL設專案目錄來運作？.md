---
tags:
- AI工具
- Claude
- Cursor
- Ollama
- RAG
- 知識庫
---
可以，但要看你說的「設專案目錄來運作」是指哪一種需求。

### 1. Ollama 本身沒有「切換專案目錄」的概念

和一些 AI 開發工具（例如 Claude Code、Cursor、Aider）不同，**Ollama 只是模型服務器**，它負責：

- 下載模型
- 啟動模型
- 提供 API
- 執行推論

例如：

```
ollama run qwen3
```

它不會自動知道：

- 目前是哪個專案
- 哪個資料夾是工作區
- 要讀取哪些檔案

因此 Ollama 沒有類似：

```
ollama --project ./myapp
```

這種功能。

---

### 2. 可以從專案目錄啟動客戶端

通常做法是：

```
cd my-project
```

然後由前端工具讀取當前資料夾，再透過 Ollama 呼叫模型。

例如：

- Aider
- [Open WebUI](https://openwebui.com?utm_source=chatgpt.com)
- [Continue.dev](https://continue.dev?utm_source=chatgpt.com)
- [AnythingLLM](https://anythingllm.com?utm_source=chatgpt.com)
- [OpenCode AI](https://opencode.ai?utm_source=chatgpt.com)

這些工具會：

1. 掃描目前專案目錄
2. 讀取程式碼
3. 呼叫本機 Ollama
4. 讓模型理解整個專案

例如：

```
cd ~/projects/myappaider --model ollama/qwen3
```

這時候專案目錄就是 `myapp`。

---

### 3. 如果是要讓模型固定讀取某個資料夾

可以自行指定：

```
python app.py
```

```
project_path = "/home/user/project"files = load_project(project_path)response = ollama.chat(    model="qwen3",    messages=[        {            "role":"user",            "content": f"分析這些檔案:\n{files}"        }    ])
```

也就是：

- 專案目錄由你的程式管理
- Ollama 只負責推論

---

### 4. 若你是在做 RAG 專案

很多人會建立：

```
my-project/├── docs/├── src/├── data/└── vector_db/
```

然後：

1. 掃描專案目錄
2. 建立向量資料庫
3. 使用 Ollama Embedding
4. 使用 Ollama Chat

像：

- [LangChain](https://www.langchain.com?utm_source=chatgpt.com)
- [LlamaIndex](https://www.llamaindex.ai?utm_source=chatgpt.com)
- [Haystack](https://haystack.deepset.ai?utm_source=chatgpt.com)

都能做到「以某個資料夾作為知識庫」。

---

如果你的意思是：

> 「像 Claude Code 一樣，進入某個專案目錄後，讓 Ollama 只針對該專案程式碼工作」

那答案是：

**單純 Ollama 不行，但搭配 Aider、Continue、OpenCode AI 或 Open WebUI 都可以達成，而且這也是目前最常見的本機開發模式。**