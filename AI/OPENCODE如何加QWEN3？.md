如果你已經安裝 OpenCode，最簡單的方法是直接讓它使用 Ollama 裡的 Qwen3。

### 方法 1：官方推薦（最快）

先拉模型：

```
ollama pull qwen3
```

或 Coding 專用版：

```
ollama pull qwen3-coder:30b
```

然後啟動 OpenCode：

```
ollama launch opencode --model qwen3
```

或

```
ollama launch opencode --model qwen3-coder
```

Ollama 官方文件就是這樣整合 OpenCode 的。

---

### 方法 2：修改 opencode.json

OpenCode 的設定檔通常在：

Linux/macOS：

```
~/.config/opencode/opencode.json
```

加入類似：

```
{  "provider": {    "ollama": {      "models": {        "qwen3": {          "name": "qwen3"        }      }    }  }}
```

如果是 Coding：

```
{  "provider": {    "ollama": {      "models": {        "qwen3-coder": {          "name": "qwen3-coder:30b"        }      }    }  }}
```

OpenCode 支援透過 Ollama API 直接掛本機模型。

---

### 方法 3：指定 Context Window（很重要）

很多人遇到：

- 不會用工具
- 一直問「你要我做什麼？」
- 看不懂專案結構
- Plan Mode 壞掉

其實是 Ollama 預設 Context 太小（常見只有 4K）。OpenCode 官方建議至少 64K Context。

例如：

```
export OLLAMA_CONTEXT_LENGTH=65536
```

或：

```
export OLLAMA_CONTEXT_LENGTH=128000
```

之後重啟：

```
ollama serve
```

再開：

```
opencode
```

不少使用者回報把 Context 拉到 64K~128K 後，工具呼叫與專案理解能力才正常。

---

### 我比較推薦的組合

如果你的機器有：

- 16GB RAM → `qwen3:8b`
- 32GB RAM → `qwen3:14b`
- 48GB 以上 RAM → `qwen3-coder:30b`

寫程式的效果通常：

```
qwen3-coder:30b    >qwen3:30b    >qwen3:14b    >qwen3:8b
```

其中 `qwen3-coder:30b` 是目前 Qwen 系列專門做 Agent/Coding 的版本，比一般 Qwen3 更適合 OpenCode。

如果你告訴我你的設備（Windows/Linux/macOS、RAM 幾 GB、CPU 或 GPU 型號），我可以直接給你一份最佳化的 OpenCode + Ollama + Qwen3 設定檔。