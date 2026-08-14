---
type: concept
tags:
  - Wordwall
  - AI-Agent
  - Playwright
  - 教育科技
  - 自動化
sources:
  - "[[AI/raw/2026-08-08T113000+0800-一份教材生出 30 種遊戲 AI Agent 全自動操作 Wordwall.md|一份教材生出 30 種遊戲 AI Agent 全自動操作 Wordwall]]"
created: 2026-08-14
updated: 2026-08-14
---

# Wordwall 與教育科技的 AI Agent 自動化實務

## 概述與核心挑戰

在教育科技應用中，許多廣受師生喜愛的互動教學平台（如 **Wordwall**、**LoiLoNote**、**Wayground**、**Quizizz**、**Kahoot**）並未提供公開 API 或官方 MCP 接口。傳統上，教師出題時必須手動逐題複製貼上；一旦想切換題型或重整題目，又必須重覆繁複的工序。

透過 **Playwright 瀏覽器自動化** 技術將網站操作封裝為命令列工具（如 `wordwall-cli`），AI Agent（如 ChatGPT、[[Claude]] Code 或 [[OpenCode 新版架構與模型最佳搭配指南|OpenCode]]）能夠直接模擬人類在瀏覽器上的行為：**「自動開啟網頁 $\rightarrow$ 登入驗證 $\rightarrow$ 選擇模板 $\rightarrow$ 填寫題幹與選項 $\rightarrow$ 儲存與發布」**，實現「將現有教材交給 Agent，全自動生成 30 種互動遊戲」的高效工作流。

---

## 一、AI Agent 操作無 API 平台之架構原理

```mermaid
sequenceDiagram
    autonumber
    actor T as 教師 (自然語言指令)
    participant A as AI Agent (ChatGPT / Luna)
    participant C as wordwall-cli (Playwright 封裝)
    participant W as Wordwall 雲端平台
    
    T->>A: 提供教材與出題需求 (如: 因數倍數 5 題 Quiz)
    A->>A: 規劃題型、出題內容與選項分配 (審查階段)
    A->>T: 回報出題預覽供教師確認
    T->>A: 確認建立
    A->>C: 執行 CLI 建立指令
    C->>W: Playwright 模擬操作 (登入 Session / DOM 表單填寫)
    W-->>C: 建立私有活動成功
    C-->>A: 回傳活動連結
    A-->>T: 完成回報，教師可於後台預覽並發布給學生
```

### 為什麼不自己寫遊戲網站？
1. **資料庫費用與維護**：自行開發並託管互動遊戲需串接 Firebase 或 Supabase，多人同時連線時將產生高額資料庫讀寫費用。
2. **重用成熟生態**：直接利用 Wordwall 現成的遊戲樣式、排行榜與多樣化模板，將資料庫與運算負擔留給平台廠商。

---

## 二、Wordwall 3 級出題模式與 8 大自動化題型

### 1. 三級出題模式演進

| 出題等級 | 模式名稱 | 特點與適用科目 | 技術細節 |
| :---: | :--- | :--- | :--- |
| **Level 1** | **純文字出題** | 最基礎、速度最快。適用於國語文、英文單字句型、歷史事件排序等。 | 題目與選項皆為純文字，透過 DOM 文字輸入框快速注入。 |
| **Level 2** | **考卷截圖出題** | **理科神器**。適用於數學幾何圖形、坐標系、理化實驗電路圖及會考歷屆考卷。 | 題目採用考卷截圖（精確還原根號與圖形），選項維持文字 ABCD。 |
| **Level 3** | **AI 生圖出題** | 視覺解謎、角色情境、歷史地圖、遮擋找錯與型態變化。 | 透過 AI 生成特定風格題目圖，或圖片與圖片互相配對。 |

### 2. 支援之 8 大題型
1. **Quiz 選擇題家族**（標準選擇、迷宮追逐、飛機射擊）
2. **Match up 配對題**（文字對文字、圖文配對）
3. **Random Wheel 隨機輪盤**
4. **True or False 是非判斷**
5. **Group Sort 分類題**（概念與圖片分組）
6. **Cloze 句子填空**
7. **Flip Tiles 翻牌模式**
8. **Labelled Diagram 標籤定位圖**

---

## 三、教學現場資安與 Token 節省實戰

### 1. 學生個資與去識別化安全守則
- **班級座號原則**：派發遊戲作業給學生時，**嚴格要求學生僅輸入「班級座號」（例如：`70105`），禁止輸入真實姓名**。
- **成績下載隱私**：教師透過 Agent 下載成績資料時，資料不含個人可識別資訊 (PII)，確保符合校園資訊安全與去識別化規範。

### 2. Token 節省與模型選用
- **Luna 搭配最大推理強度**：在 ChatGPT 中選用 `GPT 5.6 Luna` 模型並將「推理強度」開至最大，其智力表現逼近頂級 Thinking 模型，但 Token 消耗成本僅約三十分之一，兼具高智力與極低開銷。

---

## 關聯頁面
- `[[AI Agent 基本功系列實踐指南 (EP01-EP07)]]`
- `[[Chrome Skills 與瀏覽器自動化實務]]`
- `[[AI Agent 實戰與 MCP 伺服器整合]]`
- `[[OpenCode 新版架構與模型最佳搭配指南]]`
