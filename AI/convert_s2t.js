const fs = require('fs');
const path = require('path');
const OpenCC = require('opencc-js');

// 初始化簡繁轉換器 (簡體轉台灣繁體，含詞彙在地化轉換)
const converter = OpenCC.Converter({ from: 'cn', to: 'tw' });

const rawDir = path.join(__dirname, 'raw');
console.log('🔄 開始執行 raw 目錄簡繁轉換...');

if (!fs.existsSync(rawDir)) {
  console.error('❌ 找不到 raw 目錄！');
  process.exit(1);
}

const files = fs.readdirSync(rawDir);
let convertedCount = 0;

files.forEach(file => {
  if (!file.endsWith('.md')) return;
  
  const oldPath = path.join(rawDir, file);
  
  // 1. 轉換內容
  let content = fs.readFileSync(oldPath, 'utf-8');
  const convertedContent = converter(content);
  
  // 2. 轉換檔名
  const convertedFileName = converter(file);
  const newPath = path.join(rawDir, convertedFileName);
  
  // 3. 寫入並重命名
  if (content !== convertedContent || file !== convertedFileName) {
    fs.writeFileSync(oldPath, convertedContent, 'utf-8');
    if (oldPath !== newPath) {
      fs.renameSync(oldPath, newPath);
      console.log(`✓ 檔名與內容已轉換: "${file}" ➔ "${convertedFileName}"`);
    } else {
      console.log(`✓ 內容已轉換: "${file}"`);
    }
    convertedCount++;
  }
});

console.log(`🎉 轉換完成！共處理了 ${convertedCount} 個檔案。\n`);
