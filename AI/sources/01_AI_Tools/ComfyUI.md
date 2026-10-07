**ComfyUI** 是一個以節點式介面（Node-based GUI）為基礎的開源生成式 AI 工具，主要用於操作 Stable Diffusion、Flux 以及其他各類擴散模型（Diffusion Models）。

與傳統的表單式網頁介面（例如 Automatic1111 WebUI）不同，ComfyUI 讓使用者透過視覺化的「節點」與「連線」，自由組合圖片生成的每一個底層步驟。

## 核心特色

- **視覺化工作流程（Workflow）**：將模型的載入、提示詞（Prompt）、採樣器（Sampler）、VAE 解碼等步驟拆解成獨立節點，透過連線清楚掌握資料的流向。
    
- **高度靈活與複雜管線支援**：非常適合用來架設複雜的生成管線，例如同時結合 ControlNet、IP-Adapter、LoRA、圖像放大（Upscale）、FaceID 或動畫生成（AnimateDiff）。
    
- **卓越的效能與記憶體管理**：ComfyUI 對 VRAM（顯示卡記憶體）的優化非常出色，在執行高運算需求的大模型（如 Flux.1）時特別順暢。
    
- **工作流程隨圖存檔**：ComfyUI 產出的 PNG 圖片會將整組工作流程的參數與節點設定完整「內嵌」在中繼資料（Metadata）中。只要把圖片直接拖曳進介面，就能 100% 還原當時的生成環境。
    

## 適合的使用者

- **進階 AI 創作者**：希望完全掌控生成細節、自訂邏輯、不被既有介面框架限制的人。
    
- **效能導向者**：需要處理複雜工作流程或追求執行效率的使用者。
    

不過，對於剛接觸生成式 AI 的新手來說，它的學習曲線會比一般介面來得陡峭一些。

---
安裝與上手 **ComfyUI** 的過程比想像中直覺，特別是針對 Windows 使用者，官方提供了免手動配置 Python 環境的「可攜式版本（Portable）」讓你能迅速開箱。

以下是完整的安裝與基本操作指南：

## 一、 安裝方式（以 Windows 搭配 NVIDIA 顯示卡為例）

1. **下載可攜式版本**：
    
    - 前往 ComfyUI 的 GitHub 官方儲存庫（搜尋 `ComfyUI` 或前往 Releases 頁面）。
        
    - 下載 **`ComfyUI_windows_portable.7z`** 壓縮檔。
        
2. **解壓縮**：
    
    - 將壓縮檔解壓縮至你指定的硬碟目錄中（建議路徑不要有中文或特殊符號，並確保該磁碟有足夠空間存放模型）。
        
3. **啟動程式**：
    
    - 進入解壓縮後的資料夾，雙擊執行 **`run_nvidia_gpu.bat`**。
        
    - 首次執行會自動啟動內嵌的 Python 環境並開啟網頁介面（通常預設為 `[http://127.0.0.1:8188](http://127.0.0.1:8188)`）。
        

## 二、 放置必要模型（Checkpoints）

ComfyUI 本身安裝後並沒有內建大模型，你需要手動下載模型並放到正確的資料夾：

- **模型放置路徑**：`ComfyUI/models/checkpoints/`
    
- **支援格式**：常見的 `.safetensors` 格式模型（例如 SD 1.5、SDXL 或 Flux 模型都可以直接放入）。
    

## 三、 基本上手與介面導覽

當你開啟網頁介面後，畫面上會呈現一組**預設的文字生圖（Text-to-Image）工作流程**。由左至右主要包含以下核心節點：

1. **Load Checkpoint（載入模型）**：
    
    - 下拉選單中選擇你剛剛放進 `checkpoints` 資料夾的模型。
        
2. **CLIP Text Encode（提示詞節點）**：
    
    - **正向提示詞（Positive）**：輸入你希望畫面出現的元素。
        
    - **負向提示詞（Negative）**：輸入你希望排除的元素。
        
3. **KSampler（採樣器）**：
    
    - 核心運算單元。可調整採樣步數（Steps）、cfg、採樣方法（Sampler name）以及隨機亂數種子（Seed）。
        
4. **VAE Decode（VAE 解碼）**：
    
    - 將採樣後的潛在空間資料轉回一般圖像。
        
5. **Save Image（儲存圖片）**：
    
    - 生成完畢後自動輸出並儲存圖片。
        

### 執行生成步驟：

1. 確認節點連線正確。
    
2. 點擊右側控制面板（Menu）上的 **Queue Prompt** 按鈕（或使用快捷鍵 `Ctrl + Enter`）。
    
3. 觀察終端機（命令提示字元視窗）與介面上的進度條，完成後圖片就會顯示在右側的預存區域。
    

## 四、 建議安裝的必備外來擴充：ComfyUI-Manager

為了方便日後安裝其他創作者的工作流程或補齊缺少的節點，強烈建議安裝 **ComfyUI-Manager**：

1. 進入 `ComfyUI/custom_nodes/` 資料夾。
    
2. 在該目錄開啟命令提示字元（CMD），執行指令： `git clone [https://github.com/ltdrdata/ComfyUI-Manager.git](https://github.com/ltdrdata/ComfyUI-Manager.git)`
    
3. 重新啟動 ComfyUI，介面右側就會多出一个 **Manager** 按鈕，能直接在網頁上搜尋並安裝各種擴充與遺失的節點。

---
在 ComfyUI 中執行主流的 SDXL（Stable Diffusion XL）模型非常順暢，因為 SDXL 具備優秀的畫面細節與原生大尺寸解析度，是目前社群生態最豐富、資源也最多的選擇之一。

以下是針對 SDXL 在 ComfyUI 中的模型選擇、解析度設定與基礎工作流程重點：

## 一、 常見的主流 SDXL 模型選擇

社群上有許多基於 SDXL 微調出類拔萃的開源模型（通常可至 Civitai 下載 `.safetensors` 格式），常見的有：

- **真實攝影類**：`Juggernaut XL`、`RealVisXL` 等，光影與人像寫實度極佳。
    
- **二次元/動漫類**：各種基於 SDXL 或 Pony 架構的二次元微調模型，線條與構圖表現優異。
    
- **模型放置位置**：將下載好的檔案放入 `ComfyUI/models/checkpoints/` 目錄中。
    

## 二、 SDXL 的關鍵設定與注意事項

1. **原生解析度**：
    
    - SDXL 是以 **$1024 \times 1024$** 像素為基礎訓練的。
        
    - 建議生成尺寸保持在 100 萬像素左右的比例，例如正方形 $1024 \times 1024$，或是長寬比合適的配置（如 $896 \times 1152$、$1152 \times 896$、$1344 \times 768$ 等）。切勿使用 SD 1.5 時代的 $512 \times 512$，否則畫面容易出現嚴重疊影或結構錯亂。
        
2. **採樣設定（KSampler）**：
    
    - **步數（Steps）**：建議設定在 **20 至 30 步** 左右。
        
    - **採樣器與調度器（Sampler / Scheduler）**：推薦使用 `dpmpp_2m` 搭配 `karras`，或是 `euler` 搭配 `normal`，能兼顧速度與畫質。
        
3. **雙文字編碼器（Dual CLIP）**：
    
    - SDXL 同時使用兩個 CLIP 模型（CLIP L 與 CLIP G）來解析提示詞。在 ComfyUI 的標準 `CLIP Text Encode` 節點中，系統會自動處理這部分，你只需要像平常一樣輸入正向與負向提示詞即可。
        

## 三、 標準的 SDXL 執行工作流程

當你在 ComfyUI 載入預設工作流程後，針對 SDXL 只需要調整以下幾個環節：

1. **Load Checkpoint 節點**：
    
    - 下拉選單切換為你剛下載的 SDXL 模型（例如 `juggernautXL_...safetensors`）。
        
2. **Empty Latent Image 節點**：
    
    - 將 Width 與 Height 調整為 **1024**（或符合比例的 1024 級距解析度）。
        
3. **提示詞與採樣**：
    
    - 在正向提示詞輸入畫面描述（SDXL 對自然語言的理解能力很好，可以用詳細的短句描述主體、背景與光影）。
        
    - 點擊 **Queue Prompt** 即可開始運算。
        

> **關於 Refiner（精煉模型）**：
> 
> 早期官方建議 SDXL 搭配 Base 與 Refiner 兩個模型串接。但目前社群主流的微調模型（如 Juggernaut 等）多數已經是「單兵作戰（Standalone）」的完整模型，**不需要**額外接 Refiner，直接透過單一模型就能產出高品質的圖片。


---

## 執行 **Flux** 模型的需求與設定指南

**Flux** 是由 Black Forest Labs 開發的頂尖生成式 AI 模型（包含 Schnell 與 Dev 兩種版本），具備極為強悍的文字理解能力與寫實細節表現。然而，它對硬體資源（特別是 VRAM 顯示卡記憶體）的要求也相對高。

### 一、 核心檔案結構與放置路徑

與傳統的單一 Checkpoint 檔案不同，Flux 將模型拆分為多個元件。在 ComfyUI 中執行 Flux，需要下載並放置以下三類檔案：

- **UNET 主模型**：放置於 `ComfyUI/models/unet/`
    
    - 例如 `flux1-dev.safetensors` 或 `flux1-schnell.safetensors`。
        
- **文字編碼器（Text Encoders）**：放置於 `ComfyUI/models/clip/`
    
    - 包含 **CLIP L** (`clip_l.safetensors`) 與 **T5-XXL** (`t5xxl_fp16.safetensors` 或低記憶體版 `t5xxl_fp8.safetensors`)。
        
- **VAE 解碼器**：放置於 `ComfyUI/models/vae/`
    
    - 官方的 `ae.safetensors`。
        

### 二、 硬體與記憶體最佳化建議

- **VRAM 需求**：標準版需要 16GB 以上的顯示卡記憶體才能順暢運行。若是 12GB 或更低 VRAM 的顯示卡，強烈建議使用 **FP8 量化版** 或 **GGUF 格式** 的 Flux 模型與 T5 編碼器，並在啟動批次檔中調整記憶體配置參數來避免 Out of Memory (OOM)。
    
- **量化版本選擇**：社群提供的 FP8 或 Q4/Q5/Q8 GGUF 版本能在幾乎不犧牲畫質的前提下，大幅降低硬體門檻。
    

### 三、 執行工作流程要點

- **雙編碼載入（DualCLIPLoader）**：必須同時載入 `clip_l` 與 `t5xxl`，讓模型能精確解析冗長且複雜的提示詞。
    
- **採樣設定（ModelSamplingFlux）**：Flux 需要專屬的採樣設定節點。如果是 Schnell 版本，步數（Steps）設為 4 步即可；如果是 Dev 版本，建議設為 20 至 25 步。
    
- **引導係數（CFG Scale）**：Flux 對 CFG 的敏感度與傳統模型不同，Schnell 通常設為 1.0（不需額外引導），Dev 則建議維持在 3.0 至 3.5 左右，以確保最佳的畫面細節與穩定度。
    

透過正確的元件配置與量化模型，即使是中階顯示卡也能在 ComfyUI 中順利駕馭 Flux 的頂級畫質。