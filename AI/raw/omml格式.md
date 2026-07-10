**OMML（Office Math Markup Language）**是微軟（Microsoft）專門為 Office 軟體（如 Word、Excel、PowerPoint）開發的**數學公式標記語言**。

從 Word 2007 開始，微軟引入了全新的公式編輯器（即我們現在常用的「插入 > 公式」功能），其背後的核心儲存格式就是 OMML。它是基於 XML 的架構，並且整合在 Office Open XML（即 `.docx`、`.xlsx` 等檔案的底層結構）規範中。

以下為您整理 OMML 的關鍵特性、與 LaTeX / MathML 的比較，以及常見的轉換方法：

### 1. OMML 的核心特性

- **Office 原生整合**：當你在 Word 中輸入 `(a+b)^2 = a^2 + 2ab + b^2` 並轉換為公式時，Word 底層會將其轉譯為一長串的 XML 標記（即 OMML）。
    
- **與文字排版緊密結合**：OMML 設計時考慮到了 Office 的字型（如 Cambria Math）、顏色、字級與對齊特性，因此在 Word 裡面的渲染速度極快且排版美觀。
    
- **結構較為冗長**：因為要記錄大量的排版、字型與微軟特有的屬性，OMML 的程式碼通常比 LaTeX 或 MathML 冗長許多。
    

### 2. 常見公式格式對比

|**格式**|**開發者 / 組織**|**主要應用場景**|**優點**|**缺點**|
|---|---|---|---|---|
|**OMML**|微軟 (Microsoft)|MS Office 家族（Word、PPT 等）|Word 內建、排版完美相容、支援圖形化編輯|出了 Office 生態圈支援度低，程式碼臃腫|
|**LaTeX**|科技與學術界|學術論文、書籍排版、Markdown 擴充|語法精簡、純文字好寫、學術界標準|需要編譯、語法初學門檻較高|
|**MathML**|W3C 協會|網頁瀏覽器 (Web)|網頁標準、對螢幕閱讀器友善（無障礙）|語法繁複、部分老舊瀏覽器支援不一|

### 3. OMML 的程式碼範例

同樣是表示一個簡單的公式 $a+b$，各格式的寫法如下：

#### LaTeX 寫法：

程式碼片段

```
a+b
```

#### OMML 寫法（片段）：

在 `.docx` 的解壓檔案中，它看起來會像這樣：

XML

```
<m:oMath>
  <m:r>
    <m:t>a</m:t>
  </m:r>
  <m:r>
    <m:t>+</m:t>
  </m:r>
  <m:r>
    <m:t>b</m:t>
  </m:r>
</m:oMath>
```

### 4. 實用技巧：OMML 與其他格式的轉換

如果你在開發程式（例如用 Python 處理 Word 檔案）或編寫文件時遇到 OMML，通常會需要進行轉換：

#### ① 在 Word 中將 LaTeX 轉為 OMML（原生支援）

現在新版的 Word 已經支援直接輸入 LaTeX 語法。

1. 在 Word 中按 `Alt` + `=` 插入公式。
    
2. 在上方的「公式」工具列中，將模式切換為 **LaTeX**。
    
3. 輸入 `\frac{a}{b}` 後按下 `Enter` 或空白鍵，Word 會自動將其轉換為 OMML 圖形公式。
    

#### ② 程式開發中的轉換 (Python)

如果你在使用 `python-docx` 或處理 Word 的 XML，經常需要將 OMML 轉成 MathML 或 LaTeX 以利在網頁顯示。

- **利用 XSLT 轉換**：微軟在 Word 的安裝目錄中通常會提供一個名為 `OMML2MML.XSL` 的轉換檔案，可以用它透過 XSLT 把 OMML 完美的轉成標準的 MathML。
    
- **第三方套件**：Python 的 `latex2mathml` 或 `pypandoc`（調用 Pandoc 工具）也能在這些格式間進行複雜的格式轉換。