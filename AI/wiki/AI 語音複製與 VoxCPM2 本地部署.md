---
type: concept
tags: [語音複製, VoxCPM2, 本地部署, 語音合成, AI防詐]
sources: [
  "[[raw/2026-06-26T171715+0800-mathruffian-dotvoxcpm2-voice-cloner VoxCPM2 voice cloner with auto GPU detection (CUDAXPUCPU) and Ultimate Cloning support.md]]",
  "[[raw/2026-06-26T181709+0800-Anti gravity EP08：Agent代理 複製你的聲音_別再付費買 AI 語音了！一行指令免費複製你的聲音.md]]"
]
created: 2026-06-26
updated: 2026-07-09
---

# AI 語音複製與 VoxCPM2 本地部署

**AI 語音複製與 VoxCPM2 本地部署** 旨在介紹基於開源語音合成模型 **VoxCPM2** 的聲音複製（Voice Cloning）技術、本地端部署流程，以及如何透過 AI Agent 進行自然語言語音合成。此技術不僅能免去昂貴的雲端語音服務費用，亦可作為 AI 資訊素養中防範語音詐騙的教學教材。

---

## 1. VoxCPM2 核心特色

**VoxCPM2** 是一款功能強大的開源語音合成（TTS）與複製模型，採用 **Apache-2.0** 授權，完全支援商業用途。其主要特色如下：

*   **自動偵測與適應 GPU**：系統能自動識別 NVIDIA CUDA、Intel Arc XPU 或純 CPU 模式，並調配最佳推理硬體。
*   **極致克隆 (Ultimate Cloning)**：同時吃入「參考音檔」與該音檔對應的「逐字稿」，藉此精準複製說話者的語氣、語調與節奏起伏。
*   **自然語言/Agent 驅動**：傳統語音複製需要繁複的 Web UI 點擊；本專案設計為 **AI Agent 工具包**。使用者只需完成一次性錄音，後續即可透過自然語言指示 Agent（如 AntiGravity、Claude Code）自動調用腳本進行配音。
*   **零雲端費用**：所有模型推理、合成工作均在本地端運算完成，無需綁定付費的 API 密鑰（API Key）。

---

## 2. 系統需求與部署流程

本專案經過優化打包，可在本地端一鍵安裝部署：

### 💻 系統需求
*   **作業系統**：Windows 10/11（Linux/Mac 使用者可自行修改安裝指令）。
*   **依賴環境**：Python 3.10–3.12（安裝腳本會自動調用 `uv` 套件管理器建立虛擬環境）。
*   **儲存空間**：約 5GB 的硬碟空間（用於存放模型權重檔）。
*   **顯卡效能**：
    *   **NVIDIA GPU**（CUDA 12+，約 8GB VRAM 以上）：推速極快，RTF（生成時間倍率）可達 `~0.3`。
    *   **Intel Arc GPU**（XPU，約 8GB VRAM 以上）：需要套用自動 patch，RTF 約 `~2.0`。
    *   **無獨立顯卡（CPU 模式）**：RTF 約 `~8.0`，速度較慢，但文書筆電仍可正常運作。

### ⚙️ 一鍵安裝步驟
1.  **拉取專案**：在 AI Agent（如 AntiGravity 2.0）中輸入 GitHub 儲存庫網址：
    `https://github.com/mathruffian-dot/voxcpm2-voice-cloner`
    並指示 Agent 進行下載安裝。
2.  **雙擊執行安裝**：雙擊專案目錄下的 `install.bat`（或執行 `install.ps1`），系統將自動以 `uv` 安裝依賴套件、偵測 GPU 硬體並拉取對應的 PyTorch 版本。
3.  **Intel Arc XPU 補丁機制**：由於官方模型尚未原生支援 Intel Arc，本專案在安裝時會自動套用 XPU 補丁。若後續升級套件導致補丁失效，可手動執行以下指令重新套用：
    ```powershell
    .\patches\repatch_xpu.ps1
    ```

---

## 3. 語音克隆與操作實務

錄音工作使用網頁 UI 進行，而生成與調用則完全交由 Agent 操作：

### 🎙️ 錄製參考音（人類操作）
*   **方法 A（推薦網頁 UI）**：雙擊 `start.bat` 啟動 `app.py` 錄音介面。在瀏覽器中為聲音命名（例如：`王老師`），跟讀網頁上提供的示範稿並儲存。
*   **方法 B（終端機命令）**：執行以下指令進行命令列錄音：
    ```powershell
    .\.venv\Scripts\python.exe record.py --voice 我的聲音
    ```

### 🤖 生成與應用（Agent 自然語言驅動）
錄音成功存入 `voices/` 目錄後，即可在專案對話中直接向 AI Agent 下達指令：

> 💬 **指令範例**：
> 「用王老師的聲音說：『同學們早安，今天我們來上數學課。』」

Agent 將自動調用 `clone.py` 與對應的聲音特徵，將音檔生成於 `output/cloned_voice.wav`。

### 📂 專案目錄結構

*   `app.py`：網頁錄音 UI。
*   `clone.py`：文字轉克隆語音工具（Agent 呼叫）。
*   `dialogue.py`：多聲音角色對話生成工具。
*   `install.bat` / `install.ps1`：環境自動建置腳本。
*   `voices/`：存放已錄製的本地聲音特徵（已加入 `.gitignore` 避免外洩）。
*   `output/`：生成之語音 WAV 檔輸出目錄。

---

## 4. 進階實務與多重場景

*   **多角色對話 (Dialogue)**：利用 `dialogue.py` 腳本，Agent 能同時調用兩個以上的聲音（例如：老師與助教小克），根據一段文字劇本自動分段生成語音，最後合併為單一的對話音檔。
*   **教學影片配音**：可將此工具與 [[Antigravity 與 Remotion 影片生成實務]] 等影片生成框架串接。老師僅需提供講義 PPT，Agent 便能以老師複製的聲音錄製旁白，全自動生成高質感的教學解題影片。
*   **多元語言與閩南語支援**：VoxCPM2 支援多種本土語言。在使用閩南語合成時，為了獲得更準確的語音腔調，建議將提示文字轉為**台羅文字 (Tâi-lô)** 後再進行合成，可避免 AI 將中文字夾雜國語發音。
*   **全新聲音創建**：除複製真人聲音外，亦可向 Agent 描述特定的語音特徵（例如：「一隻可愛、聲音細柔的黑貓小克」），讓系統隨機合成並儲存全新的語音。

---

## 5. AI 資訊素養與防詐警告

> [!CAUTION]
> 聲音複製技術極易被不法分子用於電話詐騙（例如模仿親友聲音要求匯款）。
> *   **道德規範**：切勿在未取得當事人明確授權的前提下，複製或使用任何人的聲音。
> *   **教育宣導**：此工具非常適合作為學校 AI 素養課程的教材，讓學生親自體驗「只要錄音一分鐘，AI 就能模仿說出任意話語」，藉此提升對不明來電的警覺性（確認安全暗號或以其他管道雙重驗證）。
