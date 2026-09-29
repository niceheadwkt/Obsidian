---
type: concept
tags:
  - OpenCode
  - DeepSeek
  - Luna
  - 模型選用
  - 成本優化
sources:
  - "[[AI/raw/2026-08-13T081058+0800-OpenCode 基本功 EP07新版本完全體，DeepSeek V4 Flash ＋ Luna 最佳搭配.md|OpenCode 基本功 EP07新版本完全體，DeepSeek V4 Flash ＋ Luna 最佳搭配]]"
  - "[[AI/raw/2026-09-17T075738+0800-OpenCode 從零開始 一部影片一次教完 免費入門 AI Agent.md|OpenCode 從零開始：一部影片一次教完，免費入門 AI Agent]]"
created: 2026-08-14
updated: 2026-09-17
---

# OpenCode 新版架構與模型最佳搭配指南

## 概述與定位

**OpenCode Desktop** 是一款極具彈性且高性價比的跨平台 AI Agent 開發環境。與 Claude Code、Codex 等強綁定單一廠商模型體系的工具不同，OpenCode 的核心優勢在於：**支援在同一個對話 Session 中隨時自由切換各家頂級商業模型，並允許無縫掛載本地端模型 (Local LLM)**。

在最新版本（EP07 完全體）中，OpenCode 推出了高性價比的 **Go 方案**（每月 $10 美元換取高達 $60 美元的額度），並以 **DeepSeek V4 Flash（重新訓練版）** 與 **GPT 5.6 Luna** 組成黃金搭檔，配合「以時間換取智力」的思考強度配置，提供了極致省錢且強悍的 Agent 開發體驗。

---

## 一、雙模型黃金組合與計費機制

```mermaid
graph TD
    A[OpenCode Go 方案 $10/月] --> B[DeepSeek V4 Flash 0731重訓版]
    A --> C[GPT 5.6 Luna 視覺模型]
    
    B -->|純文字/代碼/大量日常事物| D[極致便宜 思考強度開 Max 智力達 52 分]
    C -->|視覺解析/PDF/幾何圖形| E[100萬上下文 原生多模態視覺]
    
    D -.->|同一對話內無縫切換| E
```

### 1. 模型特性對比

| 模型名稱 | 類別與定位 | 上下文窗口 | 核心優勢與適用場景 |
| :--- | :--- | :---: | :--- |
| **DeepSeek V4 Flash**<br>*(0731 重新訓練版)* | 文本 / 代碼主力 | **100 萬** | 極度便宜且聰明。適合處理大量常規任務、重構代碼、日常文本生成。 |
| **GPT 5.6 Luna** | 原生多模態視覺 | **100 萬** | 西方商業模型中 CP 值第一名。原生支援圖片、PDF 幾何圖形與視覺介面解析。 |

### 2. 計費與 2X Usage 解析
- **Go 方案額度分佈**：每月 $10 享有 $60 總用量（每週 $30 額度、5 小時滾動 $12～15 額度）。
- **2X Usage 標記**：因 DeepSeek V4 Flash 與 Luna 需向原廠伺服器採購，OpenCode 在特定方案下標註 2X Usage（相當於折算為 $30 實質額度），但因模型本身單價極低，日常重度使用仍幾乎用不完。

---

## 二、「以時間換智力」思考強度配置哲學

在 AI Agent 時代，商業模型智力水準已普遍大幅提升，處理例行事務無需盲目使用高價模型（如 GPT SOL 5.6 或 Claude Opus 5）：

```
【成本與智力換算】
• GPT 5.6 SOL (思考強度 Max)：智力 58～59 分（基準成本 100%）
• GPT 5.6 Luna (思考強度 Max)：智力 52 分（成本僅 SOL 的 1/30）
• DeepSeek V4 Flash (思考強度 Max)：智力 52 分（成本僅 SOL 的 1/100）
```

> [!TIP]
> **日常省錢心法**：選用平價模型（DeepSeek V4 Flash 或 Luna），將 **思考強度 (Thinking Budget) 開至 Max 或 X-High**，讓模型多思考數秒鐘，即可用幾十分之一的成本換取逼近頂級大模型的推理表現。

---

## 三、兩大免費外掛技能 (Skills) 實戰

### 1. `image-vision-sidecar`：為 DeepSeek 裝上眼睛
- **GitHub 倉庫**：`mathruffian-dot/image-vision-sidecar`
- **原理**：利用 Groq 提供之免費 Vision API 擔任視覺前處理 Sidecar。當使用純文字的 DeepSeek V4 Flash 時，若遇到 PDF 包含幾何圖形或圖片，自動呼叫 Groq 解析圖形特徵並轉為精準文字描述傳回 DeepSeek。
- **實測效果**：精準辨識國中會考數學試卷之幾何三角形角度與頂點條件。

### 2. `opencode-draw-free`：免費生圖與繁中文字壓印
- **GitHub 倉庫**：`mathruffian-dot/opencode-draw-free`
- **原理**：將繪圖提示詞派發至免費用生圖平台繪製，下載至本機後自動載入思源黑體 (Source Han Sans) 粗體字，於指定對話框位置壓上**繁體中文對話泡泡**。
- **適用場景**：教師研習教材配圖、漫畫教材生成、免 API Key 零成本出圖。

---

## 四、OpenCode 核心優勢總結
1. **跨模型熱切換**：在同一個對話中，可先用 Luna 解析截圖，再切換至 DeepSeek 撰寫代碼，最後切換至其他模型進行交叉審查 (Code Review)。
2. **支援本地模型 (Local LLM)**：可直接串接本機 [[Ollama]] 運行的 [[Qwen 3.8 本地模型部署與企業 ROI 實務|Qwen 3.8]] 等私有模型，彈性超越封閉式 Agent。

---

## 五、零基礎入門實戰：OpenCode Desktop 一站式安裝與四階段工作流

三師爸「OpenCode 從零開始」教學示範了完全免費入門 AI Agent 的完整路徑，分為四個階段：

1. **安裝與啟用免費模型**：下載 OpenCode Desktop → 透過 Zen 帳號（Continue with Google）取得免費 API Key → 在「設定 → 提供者」選擇 OpenCode Zen 方案並貼上金鑰 → 在「設定 → 模型」中啟用 **Muse Spark 1.3 Free**（Meta 提供，多模態、100 萬上下文，思考強度建議開至 High）。
2. **增強電腦內部能力**：向 Agent 說明自己的職業背景與需求，讓它主動搜尋並安裝適合的工具；文中特別推薦三項全電腦通用工具：**Edge TTS**（免 API Key 合成教學語音）、**yt-dlp**（影片下載處理，備課常用）、**FFmpeg**（影音格式處理）。
3. **連接外部工具**：以自然語言請 Agent 決定「授權方式」（如開啟 Chrome 登入視窗保存憑證）與「連接方式」（請 Agent 自行上網搜尋當前最熱門的連接協定），示範對象為 NotebookLM，同樣方法可套用於 Gmail、Canva、Kahoot 等其他外部工具。
4. **技能打包**：待內部工具與外部連接都就緒後，才將可重複的專業工作流打包成「技能」（本質是一份使用說明書），可請 Agent 直接教學設計、打包與優化技能的方法；忘記已裝技能時可請 Agent「列出我所有的技能」。

> [!TIP]
> Muse Spark 1.3 Free 的代價是對話紀錄會被 Meta 用於訓練下一代模型，一般課務與例行工作不涉及隱私資料即可放心使用；待確認 Agent 已上手後再考慮升級付費方案。

---

## 關聯頁面
- `[[AI 工具與框架概覽]]`
- `[[AI Agent 基本功系列實踐指南 (EP01-EP07)]]`
- `[[Qwen 3.8 本地模型部署與企業 ROI 實務]]`
- `[[Claude Cowork 與 Agent Skill 實務]]`
- `[[Wordwall 與教育科技的 AI Agent 自動化實務]]`
