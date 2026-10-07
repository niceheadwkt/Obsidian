> [!NOTE]
> 請使用remotion和voiceover skills幫我
> 做一個行銷資料動態報告
> 帶語音和字幕
> 而且配色要優雅

Remotion 是一個讓你**使用 React（HTML/CSS/JS）以寫程式的方式來製作影片與動態圖形**的開源框架。它的核心概念是將影片的時間軸轉換為 React 的渲染幀數（Frame），讓你能夠把網頁開發的經驗直接轉移到影片製作與自動化生成上。

在開發中提到 **Remotion Skill**，通常指的是在系統、開發環境或 AI Agent（如 Claude Code、Cursor、MCP 工具等）中整合與使用 Remotion 的技術能力。

### Remotion 的核心優勢與技能觀念

- **以 React 為核心**：不需要學習專業的剪輯軟體（如 After Effects、Premiere），直接使用 JSX、Tailwind CSS、Three.js 或 Canvas 來設計畫面。
    
- **程式化與數據驅動**：可以傳入動態資料（API、JSON、數據庫數據），實現「一份版型，自動批量生成成千上萬支個人化影片」。
    
- **精準的時間軸控制**：提供 `useCurrentFrame()` 和 `useVideoConfig()` 等 Hooks，輕鬆算出特定時間點的透明度、位移與動畫插值（`interpolate`）。
    
- **伺服器端渲染 (SSR) / Lambda**：支援在 AWS Lambda 或後端 Node.js 環境自動渲染成 MP4 影片。
    

### 基礎程式範例

TypeScript

```
import { useCurrentFrame, useVideoConfig, interpolate, spring } from 'remotion';

export const MyVideoTitle = ({ titleText }: { titleText: string }) => {
  const frame = useCurrentFrame(); // 取得當前幀數
  const { fps } = useVideoConfig(); // 取得影片設定 (例如 30 fps)

  // 1. 使用 interpolate 計算透明度淡入效果 (0~1 秒內淡入)
  const opacity = interpolate(frame, [0, fps], [0, 1], {
    extrapolateRight: 'clamp',
  });

  // 2. 使用物理彈簧效果 (Spring) 計算縮放動畫
  const scale = spring({
    frame,
    fps,
    config: { damping: 12 },
  });

  return (
    <div
      style={{
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
        backgroundColor: '#111827',
        opacity,
        transform: `scale(${scale})`,
      }}
    >
      <h1 style={{ color: 'white', fontSize: 80, fontFamily: 'sans-serif' }}>
        {titleText}
      </h1>
    </div>
  );
};
```

### 常見應用場景

1. **自動化行銷影片**：將數據庫產品資料（圖片、價格、標題）自動合成為社群短影音（Shorts / Reels / TikTok）。
    
2. **數據視覺化與報表**：自動將年度總結（如 Spotify Wrapped 形式）轉換為動態影片。
    
3. **AI 自動剪輯與字幕生成**：結合 Whisper 或大型語言模型（LLM），自動分析逐字稿並繪製動態字幕與重點特效。
    
4. **雲端影片渲染服務**：建構 SaaS 服務，讓使用者透過網頁介面調整文字/圖片後，由 Server 自動輸出 MP4。
    

### 快速開始範例命令

若想在本地建立 Remotion 專案：

Bash

```
# 建立預設 Remotion 專案
npx create-video@latest

# 進入目錄並啟動預覽編輯器 (Player)
cd my-video
npm start

# 將影片渲染成 MP4 檔案
npm run build
```
