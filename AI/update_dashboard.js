const fs = require('fs');
const path = require('path');

// 設定目錄路徑
const wikiDir = path.join(__dirname, 'wiki');
const indexFile = path.join(wikiDir, 'index.md');
const logFile = path.join(wikiDir, 'log.md');
const dashboardFile = path.join(__dirname, 'dashboard.html');

console.log('🚀 開始執行 Dashboard 自動更新...');

// ─────────────────────────────────────────────────────────────────────────────
// 1. 解析 Wiki 資料夾中的所有 markdown 檔案 (排除 index.md, log.md, README.md)
// ─────────────────────────────────────────────────────────────────────────────

const wikiPages = [];
const wikiFiles = fs.readdirSync(wikiDir);

// 定義標籤與類別映射
const tagMapping = {
  // 檔名或標籤包含的關鍵字 => 網頁上的標籤與中文標籤
  notebook: { tag: 'notebook', label: 'NotebookLM' },
  notebooklm: { tag: 'notebook', label: 'NotebookLM' },
  claude: { tag: 'claude', label: 'Claude' },
  antigravity: { tag: 'ai', label: 'AI 工具' },
  ai: { tag: 'ai', label: 'AI 工具' },
  ollama: { tag: 'ai', label: 'AI 工具' },
  rag: { tag: 'ai', label: 'AI 工具' },
  git: { tag: 'tech', label: '開發技術' },
  frontend: { tag: 'tech', label: '開發技術' },
  tech: { tag: 'tech', label: '開發技術' },
  business: { tag: 'business', label: '商業投資' },
  investment: { tag: 'business', label: '商業投資' },
  芒格: { tag: 'business', label: '商業投資' },
  納瓦爾: { tag: 'business', label: '商業投資' },
  life: { tag: 'life', label: '語言學習' },
  english: { tag: 'life', label: '語言學習' },
  旅遊: { tag: 'life', label: '語言學習' }
};

// 決定 Icon
function getIcon(name, tags) {
  const allText = (name + ' ' + (tags || []).join(' ')).toLowerCase();
  if (allText.includes('notebook')) return '📓';
  if (allText.includes('antigravity') && allText.includes('video')) return '📹';
  if (allText.includes('antigravity')) return '🧠';
  if (allText.includes('claude') && allText.includes('design')) return '🎨';
  if (allText.includes('claude') && allText.includes('skill')) return '⚙️';
  if (allText.includes('claude') && allText.includes('token')) return '💰';
  if (allText.includes('claude')) return '✍️';
  if (allText.includes('ollama')) return '🦙';
  if (allText.includes('git')) return '🔧';
  if (allText.includes('前端') || allText.includes('開發')) return '💻';
  if (allText.includes('英文') || allText.includes('英語') || allText.includes('外語')) return '🎧';
  if (allText.includes('旅遊')) return '✈️';
  if (allText.includes('投資') || allText.includes('商業') || allText.includes('思維')) return '💼';
  return '📝';
}

// 決定頁面分類
function getTagInfo(name, tags) {
  const allText = (name + ' ' + (tags || []).join(' ')).toLowerCase();
  for (const key in tagMapping) {
    if (allText.includes(key)) {
      return tagMapping[key];
    }
  }
  return { tag: 'ai', label: 'AI 工具' }; // 預設
}

// 解析 YAML Frontmatter
function parseFrontmatter(content) {
  const matches = content.match(/^---\r?\n([\s\S]+?)\r?\n---/);
  if (!matches) return {};
  
  const yamlText = matches[1];
  const yamlObj = {};
  
  yamlText.split('\n').forEach(line => {
    const parts = line.split(':');
    if (parts.length >= 2) {
      const key = parts[0].trim();
      let value = parts.slice(1).join(':').trim();
      
      // 解析陣列格式，例如 [tag1, tag2] 或 ["[[source]]"]
      if (value.startsWith('[') && value.endsWith(']')) {
        try {
          // 清除外圍雙括號與引號，簡易解析
          value = value.slice(1, -1)
            .split(',')
            .map(item => item.replace(/['"\[\]]/g, '').trim())
            .filter(Boolean);
        } catch (e) {
          value = [];
        }
      }
      yamlObj[key] = value;
    }
  });
  return yamlObj;
}

// 遍歷所有 Wiki 檔案
wikiFiles.forEach(file => {
  if (!file.endsWith('.md')) return;
  if (['index.md', 'log.md', 'README.md', '檔案清冊.base.md'].includes(file)) return;
  
  const filePath = path.join(wikiDir, file);
  const content = fs.readFileSync(filePath, 'utf-8');
  
  const frontmatter = parseFrontmatter(content);
  const pageName = file.replace('.md', '');
  
  const sourcesCount = Array.isArray(frontmatter.sources) ? frontmatter.sources.length : 0;
  const tagInfo = getTagInfo(pageName, frontmatter.tags);
  
  wikiPages.push({
    name: pageName,
    icon: getIcon(pageName, frontmatter.tags),
    tag: tagInfo.tag,
    tagLabel: tagInfo.label,
    sources: sourcesCount,
    date: frontmatter.updated || frontmatter.created || '2026-06-11'
  });
});

// 按更新日期降序排列
wikiPages.sort((a, b) => new Date(b.date) - new Date(a.date));
console.log(`✓ 成功解析 ${wikiPages.length} 個 Wiki 知識頁面`);

// ─────────────────────────────────────────────────────────────────────────────
// 2. 解析 index.md 提取 Sources Catalog
// ─────────────────────────────────────────────────────────────────────────────

const indexContent = fs.readFileSync(indexFile, 'utf-8');
const sourceLines = indexContent.split('\n');
const sourceCatalog = [];

// 正則表達式匹配：| `SRC-XXX` | `檔名` | 類型 | 日期 | 關聯 Wiki 頁面 |
const sourceRegex = /\|\s*`?(SRC-\d+)`?\s*\|\s*`?([^|]+?)`?\s*\|\s*([^|]+?)\s*\|\s*([\d-]+)\s*\|\s*([^|]+?)\s*\|/;

sourceLines.forEach(line => {
  const match = line.match(sourceRegex);
  if (match) {
    const id = match[1].trim();
    const title = match[2].trim();
    const type = match[3].trim();
    const date = match[4].trim();
    const relatedWiki = match[5].trim().replace(/[\[\]]/g, '').trim(); // 移除雙括號
    
    sourceCatalog.push({ id, title, type, date, relatedWiki });
  }
});

const totalSourcesCount = sourceCatalog.length;
console.log(`✓ 成功解析 ${totalSourcesCount} 份原始文獻來源`);

// ─────────────────────────────────────────────────────────────────────────────
// 3. 計算主題分布 (Topics count)
// ─────────────────────────────────────────────────────────────────────────────

const topicCounts = {
  claude: 0,
  notebook: 0,
  ai: 0,
  business: 0,
  tech: 0,
  life: 0
};

// 依據原始文獻關聯的 Wiki 頁面來統計各主題下的文獻數量
sourceCatalog.forEach(src => {
  const page = wikiPages.find(p => p.name === src.relatedWiki);
  if (page) {
    if (topicCounts[page.tag] !== undefined) {
      topicCounts[page.tag]++;
    }
  } else {
    // 預設與後備邏輯
    if (src.relatedWiki.toLowerCase().includes('claude')) topicCounts.claude++;
    else if (src.relatedWiki.toLowerCase().includes('notebook')) topicCounts.notebook++;
    else if (src.relatedWiki.toLowerCase().includes('git') || src.relatedWiki.toLowerCase().includes('前端')) topicCounts.tech++;
    else if (src.relatedWiki.toLowerCase().includes('英文') || src.relatedWiki.toLowerCase().includes('旅遊')) topicCounts.life++;
    else if (src.relatedWiki.toLowerCase().includes('思維') || src.relatedWiki.toLowerCase().includes('芒格') || src.relatedWiki.toLowerCase().includes('投資')) topicCounts.business++;
    else topicCounts.ai++;
  }
});

const topics = [
  { name: 'Claude 系列', color: '#8b5cf6', count: topicCounts.claude, max: 50 },
  { name: 'NotebookLM', color: '#22d3ee', count: topicCounts.notebook, max: 50 },
  { name: 'AI 工具 & 概念', color: '#4f8ef7', count: topicCounts.ai, max: 50 },
  { name: '商業投資思維', color: '#f59e0b', count: topicCounts.business, max: 50 },
  { name: '開發技術', color: '#10b981', count: topicCounts.tech, max: 50 },
  { name: '語言學習', color: '#f43f5e', count: topicCounts.life, max: 50 }
];

console.log('✓ 主題分布統計完成：');
topics.forEach(t => console.log(`  - ${t.name}: ${t.count} 份`));

// ─────────────────────────────────────────────────────────────────────────────
// 4. 生成 Heatmap 顏色數組 (srcColors)
// ─────────────────────────────────────────────────────────────────────────────

const categoryColors = {
  claude: '#8b5cf6',   // 紫色
  notebook: '#22d3ee', // 青色
  ai: '#4f8ef7',       // 藍色
  business: '#f59e0b', // 黃橘色
  tech: '#10b981',     // 綠色
  life: '#f43f5e'      // 紅色
};

const srcColors = sourceCatalog.map(src => {
  const page = wikiPages.find(p => p.name === src.relatedWiki);
  if (page) {
    return categoryColors[page.tag] || '#f59e0b';
  }
  // 後備邏輯
  if (src.relatedWiki.toLowerCase().includes('claude')) return categoryColors.claude;
  if (src.relatedWiki.toLowerCase().includes('notebook')) return categoryColors.notebook;
  if (src.relatedWiki.toLowerCase().includes('git') || src.relatedWiki.toLowerCase().includes('前端')) return categoryColors.tech;
  if (src.relatedWiki.toLowerCase().includes('英文') || src.relatedWiki.toLowerCase().includes('旅遊')) return categoryColors.life;
  return categoryColors.ai;
});

// ─────────────────────────────────────────────────────────────────────────────
// 5. 解析 log.md 提取日誌
// ─────────────────────────────────────────────────────────────────────────────

const logContent = fs.readFileSync(logFile, 'utf-8');
const logLines = logContent.split('\n');
const parsedLogs = [];
let totalIngestBatches = 0;

// 匹配 ## [YYYY-MM-DD] <操作類型> | <操作主題/描述>
const logHeaderRegex = /^##\s*\[([\d-]+)\]\s*(\w+)\s*\|\s*([^|\r\n]+)/;

for (let i = 0; i < logLines.length; i++) {
  const match = logLines[i].match(logHeaderRegex);
  if (match) {
    const date = match[1].trim();
    const type = match[2].trim();
    const title = match[3].trim();
    
    if (type === 'ingest') {
      if (title.includes('第二至五批')) {
        totalIngestBatches += 4;
      } else {
        totalIngestBatches++;
      }
    }
    
    // 讀取下面第一行的細節 (通常是 - **來源文獻**：... 或 - **描述**：...)
    let detail = '';
    for (let j = i + 1; j < Math.min(i + 5, logLines.length); j++) {
      const detailLine = logLines[j].trim();
      if (detailLine.startsWith('- ')) {
        detail = detailLine.replace(/^-\s*(\*\*[^*]+\*\*：)?/, '').trim();
        break;
      }
    }
    
    parsedLogs.push({ type, title, detail, date });
  }
}

// 倒序排列，使最新日誌顯示在最前方
parsedLogs.reverse();

// 只取前 6 筆日誌顯示在 Dashboard
const logsToShow = parsedLogs.slice(0, 6);
const latestUpdateDate = logsToShow.length > 0 ? logsToShow[0].date : '2026-06-18';
console.log(`✓ 成功解析日誌，累計批次匯入數: ${totalIngestBatches}，最新日期: ${latestUpdateDate}`);

// ─────────────────────────────────────────────────────────────────────────────
// 6. 重寫 dashboard.html
// ─────────────────────────────────────────────────────────────────────────────

let htmlContent = fs.readFileSync(dashboardFile, 'utf-8');

// A. 替換 JS Data 區塊
const jsDataStartMark = '// <!--WIKI_DATA_START-->';
const jsDataEndMark = '// <!--WIKI_DATA_END-->';

const startIdx = htmlContent.indexOf(jsDataStartMark);
const endIdx = htmlContent.indexOf(jsDataEndMark);

if (startIdx === -1 || endIdx === -1) {
  console.error('❌ 錯誤：找不到 WIKI_DATA_START 或 WIKI_DATA_END 標記！');
  process.exit(1);
}

const formattedWikiPages = JSON.stringify(wikiPages, null, 2);
const formattedTopics = JSON.stringify(topics, null, 2);
const formattedLogs = JSON.stringify(logsToShow, null, 2);
const formattedSrcColors = JSON.stringify(srcColors, null, 2);

const newJsDataSection = `${jsDataStartMark}
const wikiPages = ${formattedWikiPages};

const topics = ${formattedTopics};

const logs = ${formattedLogs};

const srcColors = ${formattedSrcColors};
${jsDataEndMark}`;

// 重建帶有新 JS 資料的 HTML 內容
htmlContent = htmlContent.substring(0, startIdx) + newJsDataSection + htmlContent.substring(endIdx + jsDataEndMark.length);

// B. 替換 HTML 統計計數 (Counters)
// 1. Wiki 頁面數
htmlContent = htmlContent.replace(
  /(<div class="stat-value blue count-up" data-target=")\d+(")/,
  `$1${wikiPages.length}$2`
);
// 2. 原始資料數
htmlContent = htmlContent.replace(
  /(<div class="stat-value purple count-up" data-target=")\d+(")/,
  `$1${totalSourcesCount}$2`
);
// 3. 完成批次匯入數
htmlContent = htmlContent.replace(
  /(<div class="stat-value emerald count-up" data-target=")\d+(")/,
  `$1${totalIngestBatches}$2`
);
// 4. 最後更新日期（統計欄）
htmlContent = htmlContent.replace(
  /(完成批次匯入<\/div>\s*<div class="stat-change">最後更新：)[\d-]+(<\/div>)/,
  `$1${latestUpdateDate}$2`
);
// 5. 頁面總覽 Badge 數量
htmlContent = htmlContent.replace(
  /(Wiki 知識頁面總覽[\s\S]+?<span class="section-badge">)\d+ 頁面(<\/span>)/,
  `$1${wikiPages.length} 頁面$2`
);
// 6. 日誌卡片最新日期
htmlContent = htmlContent.replace(
  /(最新：)[\d-]+(\s*<\/span>)/,
  `$1${latestUpdateDate}$2`
);
// 7. Heatmap 卡片說明文字
htmlContent = htmlContent.replace(
  /(共 <strong>)\d+(<\/strong> 份已編目文件)/,
  `$1${totalSourcesCount}$2`
);

fs.writeFileSync(dashboardFile, htmlContent, 'utf-8');
console.log('✓ 成功更新 dashboard.html！儀表板同步完成 🎉\n');
