# 全方位 LoRA 訓練完整指南 (擴散模型與大型語言模型)

本指南提供擴散模型（如 SD 1.5、SDXL、Flux）與大型語言模型（如 Llama 3、Qwen、Mistral 等 LLM）進行 **LoRA (Low-Rank Adaptation)** 微調訓練的核心概念、實務流程與關鍵參數設定。

---

## 零、 什麼是 LoRA？（核心說明與原理）

### 1. 基本概念

**LoRA（Low-Rank Adaptation，低秩適應）** 是一種針對大型預訓練模型（如 LLM、Diffusion Model）的高效微調（Fine-tuning）技術。

傳統的微調需要對基礎模型的**全量參數**（通常高達數十億至數百億個權重）進行更新，這需要極大的顯示記憶體 (VRAM) 與儲存空間。而 LoRA 的核心原理是：

* **凍結 (Freeze)** 原有預訓練模型的全量權重 $W_0$。
* 在模型的特定層（如 Self-Attention 區域）外掛並訓練兩個小型的**低秩分解矩陣** $A$ 與 $B$。
* 最終的權重更新量表示為：$\Delta W = B \times A$，模型的實際輸出變為 $W = W_0 + \Delta W$。

### 2. 主要優勢

* **硬體需求極低**：訓練時只需計算與更新極少的參數，大幅降低 VRAM 需求（消費級顯示卡如 RTX 3090 / 4090 即可完成多數訓練）。
* **檔案輕巧**：基礎模型動輒數 GB 至數十 GB，而 LoRA 檔案通常僅有 **10MB \~ 500MB**。
* **模組化與靈活組合**：同一個基礎模型可以隨時切換或疊加不同的 LoRA（例如：基礎模型 + 特定領域知識 LoRA + 特定語氣 LoRA）。

---

## 一、 大型語言模型（LLM）LoRA 訓練

對 LLM 進行 LoRA 微調，主要用於調整模型的**對話風格**、**特定領域知識（RAG/Domain Adaptation）**、**指令遵從能力（Instruction Following）** 或 **特定格式輸出（如 JSON/Code）**。

### 1. 資料集準備與格式

LLM 訓練通常採用 `.json` 或 `.jsonl` 格式，常見的格式結構如下：

* **指令/對話格式 (Instruction / Chat Format)**：
  ```json
  [
    {
      "instruction": "請將以下句子翻譯成繁體中文。",
      "input": "Artificial Intelligence is transforming the world.",
      "output": "人工智慧正在改變世界。"
    }
  ]
  ```
* **多輪對話格式 (ShareGPT / Messages Format)**：
  ```json
  [
    {
      "messages": [
        {"role": "system", "content": "你是一位專業的客服助手。"},
        {"role": "user", "content": "請問如何申請退貨？"},
        {"role": "assistant", "content": "您好！請至個人帳戶的「訂單紀錄」點選「申請退貨」即可。"}
      ]
    }
  ]
  ```

### 2. 常見訓練工具

* **Unsloth**：目前極為受歡迎的高效微調庫，顯存佔用極低、訓練速度提升 2~5 倍，適合單機/Colab 操作。
* **LLaMA-Factory**：整合度極高、提供 WebUI 操作介面的開源框架，支援幾乎所有主流 LLM 架構。
* **Axolotl**：適合進階開發者的模組化微調工具，透過 YAML 配置檔進行彈性設定。

### 3. LLM 核心超參數建議

| 參數項目 | 建議設定值 | 說明 |
| :--- | :--- | :--- |
| **LoRA Rank ($r$)** | `8` 到 `64` | 對話/風格調優設 `8` \~ `16`；複雜邏輯/領域知識設 `32` \~ `64`。 |
| **LoRA Alpha** | `16` 到 `128` | 通常設為 Rank 的 1 至 2 倍（如 $r=32, \alpha=64$）。 |
| **Target Modules** | `q_proj, v_proj` (基本) 或 `all-linear` (完整) | 選擇套用 LoRA 的層。訓練 `all-linear` 能獲得更好的知識學習效果。 |
| **Learning Rate** | `1e-4` \~ `3e-4` | LLM 的 LoRA 學習率通常比傳統微調高。 |
| **Quantization (QLoRA)** | 4-bit (NF4) / 8-bit | 使用 QLoRA 可將 7B/13B 模型的訓練顯示記憶體需求降至 12GB\~16GB 內。 |
| **Max Sequence Length** | `2048` \~ `4096` | 單次輸入的最大 Token 數，長度越長顯存需求成倍增加。 |

---

## 二、 擴散模型（Diffusion Model）LoRA 訓練

擴散模型（如 SD 1.5、SDXL、Flux）訓練 LoRA 主要用於**角色 (Character)**、**畫風 (Style)** 或 **特定物件/姿勢 (Object/Pose)**。

### 1. 資料集與標註 (Dataset & Tagging)

* **圖片數量與品質**：
  * **角色類**：約 15 \~ 30 張，包含多角度、表情與服裝變化。
  * **畫風類**：約 30 \~ 50 張，畫面構圖多變，風格需高度一致。
* **解析度要求**：
  * SD 1.5：$512 \times 512$ 以上。
  * SDXL / Flux：$1024 \times 1024$ 以上。
* **標註 (Captioning) 策略**：
  * **Danbooru Tag**（動漫/二次元）：使用逗號分隔，如 `1girl, blue hair, smiling, upper body`。
  * **自然語言**（寫實/Flux）：使用完整句子描述畫面光影、主體與背景細節。
  * **觸發詞 (Trigger Word)**：在所有標註開頭加上獨特標籤（如 `char_alex`），以便生成時呼叫。

### 2. 常見訓練工具

* **Kohya_ss (GUI)**：目前最主流且功能完整的圖形介面，支援 SD 1.5、SDXL 及部分 Flux 模型訓練。
* **OneTrainer**：開源訓練軟體，介面直觀，提供極度細緻的參數控制與即時預覽。

### 3. 擴散模型核心超參數建議 (以 SDXL / Kohya_ss 為例)

| 參數項目 | 建議設定值 | 說明 |
| :--- | :--- | :--- |
| **Network Rank ($r$)** | `16` 到 `64` | 一般設 `32` 或 `64`；數字越大表達能力越強，但檔案變大且易過擬合。 |
| **Network Alpha** | `8` 到 `32` | 通常設定為 Rank 的半分之一或相同數值（如 Rank=32, Alpha=16）。 |
| **Optimizer** | `AdamW8bit` / `Prodigy` | `Prodigy` 能自動調整學習率，對新手相對友善。 |
| **UNet Learning Rate** | `1e-4` \~ `5e-5` | 控制圖像特徵生成網路的主要學習速度。 |
| **Text Encoder LR** | `1e-5` 或 `0` | 若無需大幅修正模型對文字標籤的理解，可降低或設為 0。 |
| **Max Train Steps** | `1500` \~ `3000` 步 | 計算公式：$\text{總步數} = \frac{\text{圖片數} \times \text{重複次數}}{\text{Batch Size}} \times \text{Epochs}$ |

---

## 三、 測試與模型診斷

1. **輸出格式**：
   * LLM：產出包含 `adapter_model.bin` 或 `adapter_model.safetensors` 的資料夾。
   * 擴散模型：產出單一的 `.safetensors` 權重檔案。
2. **常見訓練問題處理**：
   * **過擬合 (Overfitting)**：
     * *LLM*：模型只會死記硬背訓練集的回答，失去通用對話與邏輯能力。
     * *擴散模型*：畫面出現嚴重雜訊、肢體崩壞或無法改變姿勢與背景。
     * *對策*：降低學習率、減少 Epochs，或增加資料集的多樣性。
   * **欠擬合 (Underfitting)**：
     * *LLM*：未能學會指定的回答風格或格式。
     * *擴散模型*：輸入觸發詞後效果不顯著或畫風未改變。
     * *對策*：提高 Learning Rate、增加訓練步數或提高 Rank。