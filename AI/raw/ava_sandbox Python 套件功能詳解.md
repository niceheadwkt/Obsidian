> [!NOTE]
> 列出ava_sandbox所有套件，說明其個別之功能與用途

# ava_sandbox Python 套件功能詳解

`ava_sandbox` 提供了一個功能豐富且安全的 Python 執行環境。其中預先安裝了大量常用套件，涵蓋了從檔案處理、數據分析、網路通訊到機器學習和區塊鏈等多個領域。本文件將這些套件分類整理，並提供詳細的功能說明，幫助使用者充分利用此環境。

---

## 1. 檔案處理與格式轉換 (File I/O & Data Formats)

這類套件專門用於讀取、寫入、操作及轉換各種常見的辦公室文件和資料格式，是自動化處理文件的利器。

*   **`pandas`**: Python 數據分析的核心函式庫。它提供了名為 DataFrame 的二維資料結構，極其適合處理表格資料（如 Excel、CSV）。可用於數據讀寫、清洗、轉換、合併、分組、計算統計值等。
*   **`openpyxl`**, **`xlrd`**, **`xlsxwriter`**: 專門處理 Microsoft Excel 檔案的組合。
    *   `openpyxl`: 主要用於讀寫較新的 `.xlsx` 格式檔案。
    *   `xlrd`: 主要用於讀取舊版的 `.xls` 格式檔案。
    *   `xlsxwriter`: 高效能寫入 `.xlsx` 檔案，支援圖表、格式化等進階功能。
*   **`python-docx`**: 讀取、建立和修改 Microsoft Word (`.docx`) 文件，可用於自動生成報告或從文件中提取內容。
*   **`python-pptx`**: 讀取、建立和修改 Microsoft PowerPoint (`.pptx`) 簡報，適合自動生成投影片。
*   **`pypdf`**, **`pdfplumber`**, **`pdfminer-six`**: 處理 PDF 檔案的強大工具。
    *   `pypdf`: 用於分割、合併、旋轉、加密和提取 PDF 頁面及資訊。
    *   `pdfplumber`: 專注於從 PDF 中提取文字、表格和元數據，能精準定位元素。
*   **`lxml`**, **`beautifulsoup4`**: 網頁及 XML 解析的黃金組合。`lxml` 速度快，`beautifulsoup4` 語法友善，兩者結合可用於網路爬蟲和資料提取。
*   **`cbor2`**, **`protobuf`**: 高效能的二進位資料序列化格式，相較於 JSON，它們體積更小、速度更快，適用於高效能通訊場景。

---

## 2. 網路與通訊 (Web & Networking)

這些套件負責與外部世界進行通訊，是呼叫 API、爬取網頁資料的基礎。

*   **`requests`**: Python 中最流行、最簡單易用的 HTTP 函式庫。可以輕鬆發送 GET、POST 等網路請求，處理 Cookie、Session，與 RESTful API 互動。
*   **`aiohttp`**: 基於 `asyncio` 的非同步 HTTP 客戶端/伺服器。當需要同時處理大量網路請求時，使用它可以大幅提升程式效能。
*   **`urllib3`**: `requests` 的底層依賴，是一個功能強大、安全且執行緒安全的 HTTP 客戶端。
*   **`websockets`**: 用於實現 WebSocket 通訊，建立即時、雙向的網路連線，常用於聊天室、即時數據更新等應用。

---

## 3. 數據科學與數值計算 (Data Science & Numerical Computing)

提供科學計算、統計分析和機器學習所需的數學運算能力。

*   **`numpy`**: Python 科學計算的基石。它提供了高效能的多維陣列物件 (`ndarray`) 和豐富的線性代數、傅立葉變換等數學函式。`pandas` 等許多高階函式庫都基於 `numpy`。
*   **`sympy`**: 符號數學（代數）函式庫。與 `numpy` 進行數值計算不同，`sympy` 可以進行公式推導、解方程式、微積分等符號運算。
*   **`onnxruntime`**: 用於執行 ONNX (Open Neural Network Exchange) 格式的機器學習模型。讓您可以在不依賴原始訓練框架（如 TensorFlow/PyTorch）的情況下部署和執行模型。

---

## 4. 影像處理與光學字元辨識 (Image Processing & OCR)

提供處理圖片檔案及從中辨識文字的能力。

*   **`Pillow` (PIL Fork)**: Python 最重要的影像處理函式庫。支援開啟、操作和儲存幾乎所有常見的影像格式，功能包括裁切、旋轉、濾鏡、繪圖等。
*   **`pytesseract`**: Google 的 Tesseract OCR 引擎的 Python 介面，可以從圖片中辨識和提取文字，是實現自動化資料輸入的關鍵工具。
*   **`pdf2image`**: 將 PDF 檔案的頁面轉換為 `Pillow` 可以處理的圖片物件，是 OCR PDF 檔案的前置步驟。
*   **`qrcode`**: 用於生成 QR Code (二維條碼) 圖片。

---

## 5. 加密與安全性 (Cryptography & Security)

提供加密、解密、數位簽章和雜湊等安全相關功能，是保護資料安全的基礎。

*   **`cryptography`**: 一個高階的密碼學函式庫，提供了易於使用的加密演算法（如 AES）、雜湊函式（如 SHA256）和金鑰管理功能。
*   **`pycryptodome`**: 一個底層的密碼學函式庫，功能非常廣泛，提供了多種加密演算法和協定。
*   **`pynacl`**: Networking and Cryptography (NaCl) 函式庫的 Python 封裝，以簡單易用為設計哲學，提供高安全性的加密 API。
*   **`ecdsa`**, **`eth-keys`**: 實現橢圓曲線數位簽章演算法 (ECDSA)，這是比特幣和以太坊等區塊鏈技術的核心元件，用於驗證交易所有權。

---

## 6. 文字與標記語言處理 (Text & Markup Processing)

這類套件用於處理純文字、解析標記語言，並在不同格式間進行轉換。

*   **`regex`**: 一個功能更強大的正規表示式引擎，相較於 Python 內建的 `re` 模組，它提供了更豐富的 Unicode 支援和更快的執行速度，適用於複雜的文字模式匹配。
*   **`markdown`**, **`markdownify`**, **`html2text`**: 這三個工具組成了在 Markdown、HTML 和純文字之間的雙向轉換橋樑。
    *   `markdown`: 將 Markdown 文本轉換為 HTML。
    *   `markdownify`: 將 HTML 轉換為 Markdown。
    *   `html2text`: 將 HTML 轉換為易於閱讀的純文字。

---

## 7. 區塊鏈與以太坊 (Blockchain & Ethereum)

專門用於與以太坊 (Ethereum) 區塊鏈互動的工具集。

*   **`web3`**: 與以太坊節點互動的主要函式庫。可用於查詢區塊鏈狀態、發送交易、與智能合約互動等。
*   **`eth-abi`**: 用於編碼和解碼以太坊 ABI (Application Binary Interface)，這是與智能合約函式互動的標準格式。
*   **`eth-account`**: 用於建立和管理以太坊帳戶及私鑰。
*   **`eth-utils`**: 提供一系列與以太坊相關的輔助工具函式。

---

## 8. 核心工具與公用程式 (Core Utilities)

這些是許多其他函式庫賴以運作的基礎，同時也提供了許多開發上的便利。

*   **`pydantic`**: 透過 Python 的型別提示 (Type Hints) 進行資料驗證和設定管理。它能確保傳入的資料符合預期格式，並自動生成清晰的錯誤訊息，極大提升程式的穩定性。
*   **`python-dateutil`**, **`pytz`**: 強大的日期和時間處理工具。`dateutil` 可以解析幾乎任何格式的日期字串，而 `pytz` 則用於處理複雜的時區轉換。
*   **`tabulate`**: 將列表或字典等資料轉換成格式精美的 ASCII 表格，方便在終端機中呈現。
---

總結來說，這個 `ava_sandbox` 環境是一個功能非常全面的沙箱，具備了從**文件處理**、**網路爬蟲**、**數據分析**到**機器學習模型推理**和**區塊鏈互動**的各種能力，讓您可以在一個隔離且安全的環境中執行多樣化的任務。