---
tags:
- AI工具
- Gemma
- Ollama
- Qwen
- RAG
- 智能體
- 知識庫
- 網路
---
如果你的目標是在本機（Local）執行大型語言模型（LLM），目前主流方案大致可以分成「開源模型」與「本地推理框架」兩個層面來看。

## 一、主流可本地執行的 LLM 模型

### 1. Meta 的 Llama 系列

目前最熱門的開源模型之一。

#### Llama 3.3 70B

**優點**

- 綜合能力非常強
- 英文推理、程式撰寫能力佳
- 社群資源豐富
- 支援量化後本地部署

**缺點**

- 70B 需要大量記憶體
- 完整運行建議 48GB~64GB VRAM
- 中文能力不如部分中文優化模型

**適合**

- 企業私有化部署
- AI Agent
- 程式開發助手

---

### 2. Alibaba Group 的 Qwen 系列

目前中文能力最強的開源模型之一。

#### Qwen3 8B / 32B / 72B

**優點**

- 中文能力極佳
- 英文表現也不錯
- 支援長上下文
- 工具呼叫（Tool Calling）成熟
- Agent 生態完整

**缺點**

- 超大型版本資源需求高
- 某些推理任務略遜於頂級推理模型

**適合**

- 中文客服
- 文件分析
- RAG知識庫

---

### 3. Mistral AI 的 Mistral 系列

#### Mistral Small / Ministral / Mixtral

**優點**

- 同參數量下效率高
- 推理速度快
- MoE 架構節省資源

**缺點**

- 中文能力普通
- 中文資料相對較少

**適合**

- 英文聊天
- 技術文件
- 輕量部署

---

### 4. DeepSeek 的 DeepSeek 系列

#### DeepSeek-R1

近年最受關注的推理模型。

**優點**

- 數學推理極強
- 程式能力優秀
- 接近部分商業模型表現
- 開源權重

**缺點**

- 大模型版本資源需求高
- 回答較冗長
- 中文表達有時較機械

**適合**

- 程式開發
- 推理任務
- 研究用途

---

### 5. Google 的 Gemma 系列

#### Gemma 3 4B / 12B / 27B

**優點**

- 小模型表現突出
- 硬體需求低
- 部署容易

**缺點**

- 超長對話能力較弱
- 推理能力不及大型模型

**適合**

- 個人電腦
- 筆電部署
- 邊緣設備

---

### 6. Microsoft 的 Phi 系列

#### Phi-4

**優點**

- 小而強
- 推理能力超越許多同級模型
- 記憶體需求低

**缺點**

- 長文處理有限
- 多語言能力一般

**適合**

- 本地 Copilot
- 小型 AI 助理

---

## 二、主流本地執行框架

模型本身需要搭配推理框架。

### 1. [Ollama](https://ollama.com?utm_source=chatgpt.com)

目前最受歡迎。

**優點**

- 安裝最簡單
- 一行指令下載模型
- API相容性佳
- Windows / Linux / Mac 支援

**缺點**

- 進階調校能力有限
- 多 GPU 管理較弱

範例：

```
ollama run qwen3:8b
```

---

### 2. [LM Studio](https://lmstudio.ai?utm_source=chatgpt.com)

GUI 最友善。

**優點**

- 無需指令列
- 支援 GGUF
- OpenAI API 模式

**缺點**

- 自動化能力較弱

適合：

- 一般使用者
- 測試模型

---

### 3. [vLLM](https://vllm.ai?utm_source=chatgpt.com)

企業部署主流方案。

**優點**

- 吞吐量高
- 多使用者併發佳
- OpenAI API相容

**缺點**

- 安裝較複雜
- 需要 Linux 環境較佳

---

### 4. llama.cpp

本地部署核心技術之一。

**優點**

- CPU即可執行
- 支援GGUF量化
- 資源利用率高

**缺點**

- CLI較複雜
- 初學者門檻較高

---

## 三、依硬體推薦

### 16GB RAM 電腦

推薦：

- Qwen3 4B
- Gemma 3 4B
- Phi-4 Mini

體驗：

- 基本聊天流暢
- 程式輔助可用

---

### 32GB RAM

推薦：

- Qwen3 8B
- Gemma 3 12B
- Llama 3.1 8B
- DeepSeek-R1 Distill 8B

體驗：

- 非常適合個人使用
- 可建立私有知識庫

---

### RTX 4070 / 5070（12GB VRAM）

推薦：

- Qwen3 14B Q4
- DeepSeek-R1 Distill 14B
- Llama 3.1 8B

體驗：

- 推理速度佳
- Agent 專案可用

---

### RTX 4090 / 5090（24GB+ VRAM）

推薦：

- Qwen3 32B
- DeepSeek-R1 32B
- Llama 70B（量化）

體驗：

- 接近商業級部署
- 可同時跑 [[RAG]] 與 Agent

---

## 2026 年較推薦的組合

|用途|推薦模型|部署方式|
|---|---|---|
|中文聊天|Qwen3 8B|Ollama|
|程式開發|DeepSeek-R1 Distill 14B|Ollama / LM Studio|
|文件分析|Qwen3 32B|vLLM|
|AI Agent|Qwen3 32B|vLLM|
|筆電本機|Gemma 3 4B|LM Studio|
|高階工作站|DeepSeek-R1 32B|vLLM|
|家用 NAS|Phi-4|Ollama|

如果你能提供你的硬體規格（CPU、RAM、顯卡型號與 VRAM），我可以直接幫你列出「能順跑哪些模型、預估 Tokens/s、以及最佳量化版本（Q4/Q5/Q8）」的建議清單。