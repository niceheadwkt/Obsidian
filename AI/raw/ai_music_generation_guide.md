# AI 音樂生成雙雄解析：Suno 與 YuE2 完全指南

在當前 AI 音訊與音樂生成領域，**Suno** 與 **YuE2** 分別代表了**商業化雲端體驗**與**開源深度可控技術**的代表性工具。本文件整理兩者的核心架構、 Prompt/標籤語法、技術原理及開發/創作工作流對比。

---

## 一、 Suno：商業級端到端音樂生成平台

### 1. 核心定位與優勢
* **定位**：商業化雲端一站式 AI 音樂生成服務（支援 Web / App）。
* **優勢**：
  * **零門檻**：只需文字描述或自訂歌詞，數秒內輸出包含人聲、編曲與混音的完整歌曲。
  * **語言適應性高**：支援中文、英文、日文及多國語言歌詞演唱。
  * **風格豐富**：涵蓋 POP、Rock、EDM、Jazz、Synthwave、Hip-Hop 等主流與小眾音樂類型。

---

### 2. Style Prompt（風格提示詞）撰寫公式

Suno 的 Prompt 應盡量使用**英文關鍵詞**，並採用 **四要素公式**：

$$\text{Style Prompt} = \text{[曲風 Genre]} + \text{[情感/時代 Mood/Era]} + \text{[人聲特色 Vocals]} + \text{[樂器與混音 Instrumentation]}$$

#### 範例對比：
* ❌ **不佳提示**：`A very beautiful quiet sad song about night` (抽象且模糊)
* ✅ **優質提示**：`Indie Acoustic Folk, melancholic night vibe, warm fingerpicking acoustic guitar, soft whisper male vocals, subtle cello, 80 BPM, clean mix`

---

### 3. 歌詞結構標籤 (Meta Tags) 實務

在 Custom 模式下，透過控制段落標籤可精準導引 Suno 的動態演進與配器表現：

```text
[Intro - Acoustic Guitar & Slow Piano]

[Verse 1 - Soft Female Vocal]
夜幕低垂 城市的光點閃爍
走在熟悉的街頭 尋找失落的夢

[Pre-Chorus - Drum Layering, Building Tension]
心中的聲音 越來越清楚
積蓄的能量 即將噴發

[Chorus - Explosive Synthwave, Full Band, Layered Harmonies]
爆發這夜的狂熱 讓音樂帶走所有的重負
黑夜過後 就是曙光

[Guitar Solo - Fast Melodic Shred, High Energy]

[Bridge - Ambient, Vocal Echo, Piano Only]
若一切重來 我是否依然
選擇這條 孤獨的漫漫長路

[Chorus - Maximum Energy, Double Kick Drum]
爆發這夜的狂熱 讓音樂帶走所有的重負
黑夜過後 就是曙光

[Outro - Slowing Tempo, Piano Fade Out]

[End]
```

---

## 二、 YuE2：前沿開源樂理可控音樂大模型

### 1. 核心定位與技術架構
* **定位**：開源社群（M-A-P / 相關研究團隊）推出的音樂生成基座大模型（Open-Source Music Foundation Model）。
* **核心技術亮點**：
  * **雙階段樂理規劃（Symbolic Chain-of-Thought Planning）**：
    1. **Stage 1 (樂理生成)**：將歌詞與提示詞轉譯為 **ABC 樂譜**（包含旋律、和弦進行、拍號與升降調）。
    2. **Stage 2 (音訊渲染)**：神經網絡將 ABC 樂譜渲染為 48kHz 高音質雙聲道立體聲。
  * **零樣本編輯（Zero-Shot CoT Music Editing）**：
    創作者可人工修改中間產出的 ABC 樂譜（例如變更和弦、升降 Key、調整節奏），模型會基於新樂譜重新合成最終音訊。
  * **純本地私有化部署**：權重開源，資料與靈感無需上傳雲端，保障作品版權安全性。

---

### 2. YuE2 本地部署與開發簡介

#### 環境需求：
* GPU：NVIDIA GPU (推薦 24GB+ VRAM，如 RTX 3090/4090 或 A100)
* 系統：Linux (Ubuntu 22.04 LTS 最佳)
* 依賴包：Python 3.10+, PyTorch 2.x, Transformers, Torchaudio

#### Python 推理 API 範例流程：

```python
import torch
from yue2 import YuE2Pipeline, ABCNotationGenerator

# 1. 載入模型
pipeline = YuE2Pipeline.from_pretrained(
    "m-a-p/YuE2-3B", 
    torch_dtype=torch.bfloat16
).to("cuda")

# 2. 定義輸入
lyrics = """
[Verse]
Whispers in the quiet rain
Searching for the lost refrain
"""
style_description = "Acoustic Pop, 90 BPM, Soft Male Vocal, Emotional"

# 3. 階段一：生成 ABC 樂譜 (CoT Planning)
abc_score = pipeline.generate_abc(lyrics=lyrics, style=style_description)
print("Generated ABC Score:\n", abc_score)

# 4. (可選) 在此步驟手動或程式修改 abc_score

# 5. 階段二：將 ABC 樂譜渲染為 48kHz 音訊
audio_waveform = pipeline.render_audio(abc_score, sample_rate=48000)

# 6. 儲存音訊檔案
pipeline.save_wav(audio_waveform, "output_song.wav")
```

---

## 三、 Suno vs YuE2 全方位對比

| 對比維度 | Suno (v4/商業版) | YuE2 (開源版) |
| :--- | :--- | :--- |
| **使用模式** | 雲端 SaaS 服務（訂閱制 / 點數制） | 本地自主部署 / 私有雲 API |
| **技術黑盒度** | 高（黑盒模式，無法直接控制底層音符與樂法） | 低（白盒/半透明，提供中間態 ABC 樂譜） |
| **精準控制力** | 中等（靠 Prompt 與 Meta Tags 導引概率） | 極高（可直接修改和弦進行、音符與節奏） |
| **輸出品質** | 商業級發行音質、自動混音成型 | 高音質 (最高 48kHz)，支援雙聲道渲染 |
| **二次開發** | 僅限 Web/App 操作或官方 API 呼叫 | 可自訂數據集微調 (Fine-tune)、結合 LLM Agent |
| **適用族群** | 音樂創作者、自媒體、內容創作者、Demo 發想 | AI 研究員、音樂製作人、軟體開發者、數據敏感企業 |

---

## 四、 總結與應用建議

1. **快速創作與靈感驗證**：選擇 **Suno**。善用四要素 Prompt 與 Meta Tags 標籤，可以在短時間內生成多種曲風的完整 Demo。
2. **深度編曲與精確樂理控制**：選擇 **YuE2**。利用其生成的 ABC 樂譜進行精細調律與和弦替換，適合追求高可控性與私有化部署的音樂工程師或開發團隊。