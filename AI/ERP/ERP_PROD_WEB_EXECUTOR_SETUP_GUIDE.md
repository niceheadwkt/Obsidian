# 🚀 Antigravity CLI 正式機 Web 查詢技能 (`erp-prod-web-executor`) 配置與省 Token 完全指南

> **文檔定位**：提供給團隊同仁之 Antigravity CLI 技能快速部署手冊。
> **適用場景**：在 Antigravity CLI 中透過已登入之 Chrome/Edge 瀏覽器，安全唯讀查詢 ERP 正式機資料，並徹底解決「查詢失敗、做不出來、Token 巨量消耗」的問題。

---

## 📌 目錄
1. [為什麼同事會做不出來？Token 暴增的四大元兇](#1-為什麼同事會做不出來token-暴增的四大元兇)
2. [核心架構與極致省 Token 原理](#2-核心架構與極致省-token-原理)
3. [三步驟極速部署手冊 (5 分鐘完成)](#3-三步驟極速部署手冊-5-分鐘完成)
   - [步驟 1：建立瀏覽器 AI 連線模式啟動捷徑](#步驟-1建立瀏覽器-ai-連線模式啟動捷徑-bat)
   - [步驟 2：安裝 Python 依賴與放置通用橋接腳本](#步驟-2安裝-python-依賴與放置通用橋接腳本-erp_web_clientpy)
   - [步驟 3：在 Antigravity CLI 註冊 Skill](#步驟-3在-antigravity-cli-註冊-skill-skillmd)
4. [日常使用 SOP 與自然語言指令範例](#4-日常使用-sop-與自然語言指令範例)
5. [常見問題與自我排查清單 (Troubleshooting)](#5-常見問題與自我排查清單-troubleshooting)

---

## 1. 為什麼同事會做不出來？Token 暴增的四大元兇

若沒有標準配置此技能，直接對 Antigravity CLI 說「*幫我查正式機 ERP 資料*」，通常會發生以下幾種致命情況，導致 Token 瘋狂燃燒：

| 元兇編號       | 問題現象                   | 為什麼會狂耗 Token？                                                                                                                   |
| :--------- | :--------------------- | :------------------------------------------------------------------------------------------------------------------------------ |
| 💣 **元兇一** | **沒有定義 Skill 與專屬橋接腳本** | AI 不知道如何連線正式機，於是在背景**盲目嘗試各種無效方案**（寫 Playwright 爬蟲、搜尋整台硬碟找密碼、寫 Java JDBC 連線、反覆重試試錯），每一輪對話都在 Context 中塞滿報錯 log，一次對話就能燒掉數萬 Tokens！ |
| 💣 **元兇二** | **瀏覽器未開啟 9222 遠端調試埠**  | 一般直接點開的 Chrome/Edge **並未開放 CDP (Chrome DevTools Protocol) 埠號**。腳本連不上時，AI 會反覆分析錯誤、搜尋本機進程，陷入死循環。                                  |
| 💣 **元兇三** | **未做查詢結果截斷與自動轉存 CSV**  | 正式機查詢若回傳數百或數千筆資料，若未經截斷**直接全部輸出到終端機/Context**，單次查詢就會塞爆 Context（消耗 50,000 ~ 100,000+ Tokens），造成速度極慢甚至 Token 額度瞬間耗盡。               |
| 💣 **元兇四** | **路徑寫死（工號硬編碼）或缺少套件**   | 複製他人腳本時，檔案路徑若寫死為他人工號（例如 `C:\Users\ch26358\...`）或未安裝 `websocket-client`，Python 一執行就崩潰，AI 又會花費大量 Token 嘗試除錯。                      |

---

## 2. 核心架構與極致省 Token 原理

`erp-prod-web-executor` 是如何做到**秒級查詢 + 極致節省 Token** 的？

```mermaid
flowchart TD
    User([使用者自然語言]) -->|「查正式機 請假資料...」| CLI[Antigravity CLI]
    CLI -->|精準命中 Skill (0 探索 Token)| Script[erp_web_client.py]
    
    subgraph BrowserSession [本機瀏覽器 (Port 9222)]
        Chrome[Chrome / Edge (AI 連線模式)]
        Tab[已登入之命令中心 dsjjsql.jsp]
    end
    
    Script -->|1. 唯讀檢查 (SELECT/WITH)| Guard{安全檢查}
    Guard -->|通過| CDP[CDP WebSocket 連線 9222]
    CDP -->|2. 注入 JS 填入 SQL 並送出| Tab
    Tab -->|3. 抓取查詢結果 CSV| Script
    
    subgraph SmartOutput [智慧雙軌輸出 (省 Token 核心)]
        Script -->|資料 <= 20 筆| Table[直接回傳 Markdown 簡潔表格\n(~100 Tokens)]
        Script -->|資料 > 20 筆| CSV[自動匯出本機 CSV 檔 + 僅顯示前 3 筆預覽\n(~150 Tokens)]
    end
    
    Table --> Result([呈現在 CLI 畫面上])
    CSV --> Result
```

### 💡 三大關鍵優勢：
1. **免密碼安全復用**：直接掛載使用者已經在瀏覽器登入好的 Session，不用在腳本或 CLI 中輸入/儲存任何帳號密碼。
2. **零探索 Token**：透過 `SKILL.md` 明確告訴 AI 唯一的執行指令，AI 不會胡思亂想或亂寫爬蟲，探索成本為 0。
3. **智慧筆數截斷**：查詢結果超過 20 筆時，自動轉存本機 CSV 檔案，Context 永遠只接收 3 筆預覽，**將 Token 消耗減少 99%**。

---

## 3. 三步驟極速部署手冊 (5 分鐘完成)

請依照以下 3 個步驟進行設定，完全相容任何 Windows 使用者電腦（已將路徑通用化，免手動改工號）：

---

### 步驟 1：建立瀏覽器 AI 連線模式啟動捷徑 (.bat)

在 **桌面** 上建立一個批次檔（依您常用的瀏覽器二選一或都建立）：

#### 選項 A：Chrome 專用 ➔ 命名為 `啟動正式機ERP(AI連線模式).bat`
```bat
@echo off
chcp 65001 >nul
echo 正在啟動 Chrome (AI 連線模式)...
start "" "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\ChromeERPProfile" "http://erp.chsteel.com.tw/erp/ds/jsp/dsjjsql.jsp"
exit
```

#### 選項 B：Edge 專用 ➔ 命名為 `啟動正式機ERP(Edge連線模式).bat`
```bat
@echo off
chcp 65001 >nul
echo 正在啟動 Edge (AI 連線模式)...
start "" "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" --remote-debugging-port=9222 --user-data-dir="C:\EdgeERPProfile" "http://erp.chsteel.com.tw/erp/ds/jsp/dsjjsql.jsp"
exit
```

> 💡 **說明**：
> - `--remote-debugging-port=9222`：開放 CDP 調試埠供腳本溝通。
> - `--user-data-dir=...`：使用獨立設定檔目錄，不影響平常上班使用的瀏覽器與分頁。

---

### 步驟 2：安裝 Python 依賴與放置通用橋接腳本 (`erp_web_client.py`)

#### 1. 安裝必要套件：
打開 PowerShell 或 CMD 執行：
```powershell
pip install websocket-client
```

#### 2. 建立通用橋接腳本：
將以下程式碼儲存為 **`%USERPROFILE%\erp_web_client.py`**（即放在您的使用者家目錄，例如 `C:\Users\您的帳號\erp_web_client.py`）：

```python
# -*- coding: utf-8 -*-
import sys
import json
import time
import urllib.request
import urllib.error
import urllib.parse
import csv
import io
import os
import websocket

CDP_PORT = 9222
TARGET_URL_KEY = "dsjjsql.jsp"
DEFAULT_ERP_SQL_URL = "http://erp.chsteel.com.tw/erp/ds/jsp/dsjjsql.jsp"

# 動態取得當前使用者的家目錄，避免寫死工號路徑
USER_HOME = os.path.expanduser("~")
OUTPUT_FILE = os.path.join(USER_HOME, "query_output.txt")
EXPORT_DIR = r"D:\temp\query_results" if os.path.exists("D:\\") else os.path.join(USER_HOME, "query_results")

def get_tab_list():
    try:
        url = f"http://127.0.0.1:{CDP_PORT}/json/list"
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=3) as resp:
            return json.loads(resp.read().decode('utf-8'))
    except Exception:
        return None

def create_tab(target_url):
    try:
        url = f"http://127.0.0.1:{CDP_PORT}/json/new?{urllib.parse.quote(target_url, safe=':/?=&')}"
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}, method="PUT")
        with urllib.request.urlopen(req, timeout=3) as resp:
            return json.loads(resp.read().decode('utf-8'))
    except Exception:
        try:
            url = f"http://127.0.0.1:{CDP_PORT}/json/new?{target_url}"
            with urllib.request.urlopen(url, timeout=3) as resp:
                return json.loads(resp.read().decode('utf-8'))
        except Exception:
            return None

def send_cdp_eval(ws, expression, await_promise=False):
    req_id = int(time.time() * 1000) % 1000000
    msg = {
        "id": req_id,
        "method": "Runtime.evaluate",
        "params": {
            "expression": expression,
            "returnByValue": True,
            "awaitPromise": await_promise
        }
    }
    ws.send(json.dumps(msg))
    
    start_time = time.time()
    while time.time() - start_time < 10:
        raw_res = ws.recv()
        res = json.loads(raw_res)
        if res.get("id") == req_id:
            result_obj = res.get("result", {}).get("result", {})
            return result_obj.get("value")
    return None

def execute_sql_on_web(sql_query, row_limit=0):
    # 1. 唯讀安全防護：正式機僅允許 SELECT / WITH 查詢
    cleaned_sql = sql_query.strip().upper()
    if not (cleaned_sql.startswith("SELECT") or cleaned_sql.startswith("WITH")):
        print("[安全警示] 正式機查詢僅限 SELECT / WITH 唯讀查詢，已攔截執行。")
        return False, "FORBIDDEN_SQL_WRITE"

    # 2. 檢查 CDP 是否可連線
    tabs = get_tab_list()
    if tabs is None:
        print("[錯誤] 無法連線至瀏覽器遠端偵錯埠 (Port 9222)。")
        print("請確認是否已透過桌面「啟動正式機ERP(AI連線模式)」捷徑開啟瀏覽器！")
        return False, "CDP_CONNECTION_ERROR"

    # 3. 尋找或開啟命令中心分頁
    target_tab = None
    for tab in tabs:
        url = tab.get("url", "")
        title = tab.get("title", "")
        if TARGET_URL_KEY in url or "命令中心" in title:
            target_tab = tab
            break

    if not target_tab:
        print(f"[提示] 未發現已開啟的命令中心，正在自動開啟新分頁：{DEFAULT_ERP_SQL_URL}...")
        target_tab = create_tab(DEFAULT_ERP_SQL_URL)
        if not target_tab:
            print("[錯誤] 自動開啟命令中心分頁失敗，請手動在瀏覽器開啟。")
            return False, "FAILED_TO_CREATE_TAB"
        time.sleep(1.5)

    ws_url = target_tab.get("webSocketDebuggerUrl")
    if not ws_url:
        print("[錯誤] 未能取得分頁的 WebSocket 調試位址。")
        return False, "NO_WS_URL"

    # 4. 連線 WebSocket 操控分頁
    try:
        ws = websocket.create_connection(ws_url, timeout=10, suppress_origin=True)
    except Exception as e:
        print(f"[錯誤] 連線分頁 WebSocket 失敗: {e}")
        return False, str(e)

    try:
        escaped_sql = json.dumps(sql_query)
        
        # 注入執行 JavaScript：填入 SQL、選擇 CSV 格式 (Type=1)、提交表單
        js_submit = f'''
        (function() {{
            var sqlArea = document.getElementById('SqlStr') || document.querySelector("textarea[name='SqlStr']");
            if (!sqlArea) return "NO_SQL_FIELD";
            sqlArea.value = {escaped_sql};
            
            var radioCsv = document.querySelector("input[name='Type'][value='1']");
            if (radioCsv) radioCsv.checked = true;
            
            var rowSizeInput = document.querySelector("input[name='RowSize']");
            if (rowSizeInput) rowSizeInput.value = "{row_limit}";
            
            if (document.forms['form1']) {{
                document.forms['form1'].submit();
                return "SUBMITTED";
            }}
            return "NO_FORM";
        }})();
        '''
        
        res = send_cdp_eval(ws, js_submit)
        if res != "SUBMITTED":
            print(f"[警告] 表單提交回傳狀態: {res}")
            if res == "NO_SQL_FIELD":
                return False, "請確認分頁是否處於登入狀態並停留在命令中心頁面。"

        # 等待網頁載入與查詢結果完成（最多等 15 秒）
        time.sleep(1.0)
        max_wait = 15.0
        start_wait = time.time()
        csv_content = None
        err_message = None

        while time.time() - start_wait < max_wait:
            js_check = '''
            (function() {
                var csvArea = document.getElementById('csvData');
                var msgSpan = document.getElementById('msg');
                var msgText = msgSpan ? msgSpan.innerText : '';
                
                if (csvArea && csvArea.value !== undefined) {
                    return { status: 'DONE', data: csvArea.value, msg: msgText };
                }
                
                if (msgText && (msgText.indexOf('錯誤') !== -1 || msgText.indexOf('Error') !== -1 || msgText.indexOf('禁止') !== -1)) {
                    return { status: 'ERROR', msg: msgText };
                }
                
                return { status: 'WAITING', msg: msgText };
            })();
            '''
            check_res = send_cdp_eval(ws, js_check)
            if isinstance(check_res, dict):
                if check_res.get("status") == "DONE":
                    csv_content = check_res.get("data", "")
                    err_message = check_res.get("msg", "")
                    break
                elif check_res.get("status") == "ERROR":
                    err_message = check_res.get("msg", "")
                    break
            time.sleep(0.5)

        ws.close()

        if csv_content is None and err_message:
            return False, f"查詢發生錯誤: {err_message}"
        if csv_content is None:
            return False, "查詢逾時，未能取得結果。"

        return True, csv_content

    except Exception as e:
        ws.close()
        return False, f"執行例外錯誤: {e}"

def parse_and_save_result(csv_raw):
    os.makedirs(EXPORT_DIR, exist_ok=True)
    
    lines = [line for line in csv_raw.strip().splitlines() if line.strip()]
    if not lines:
        print("[結果] 查詢成功，但無符合條件之資料列 (0 rows returned)。")
        with open(OUTPUT_FILE, "w", encoding="utf-8-sig") as f:
            f.write("0 rows returned.")
        return

    reader = csv.reader(io.StringIO(csv_raw))
    rows = list(reader)
    
    total_rows = len(rows)
    print(f"[成功] 共查詢到 {total_rows} 筆資料。")

    with open(OUTPUT_FILE, "w", encoding="utf-8-sig") as f:
        # <= 20 筆：輸出 Markdown 表格直接呈現在對話中
        if total_rows <= 20:
            header = [f"COL_{i+1}" for i in range(len(rows[0]))] if rows else []
            f.write("| " + " | ".join(header) + " |\n")
            f.write("| " + " | ".join(["---"] * len(header)) + " |\n")
            for r in rows:
                f.write("| " + " | ".join([str(c).replace("\n", " ") for c in r]) + " |\n")
            print(f"已將 {total_rows} 筆結果整理為 Markdown 格式輸出。")
        else:
            # > 20 筆：自動匯出 CSV 檔，僅預覽前 3 筆，徹底省 Token
            now_str = time.strftime("%Y%m%d_%H%M%S")
            csv_path = os.path.join(EXPORT_DIR, f"prod_query_{now_str}.csv")
            with open(csv_path, "w", encoding="cp950", errors="replace", newline="") as out_csv:
                writer = csv.writer(out_csv)
                for r in rows:
                    writer.writerow(r)
            
            f.write(f"資料總筆數: {total_rows} 筆（已超過 20 筆限制）\n")
            f.write(f"完整資料已匯出至: {csv_path}\n\n")
            f.write("前 3 筆資料預覽:\n")
            for r in rows[:3]:
                f.write(str(r) + "\n")
            print(f"資料筆數超過 20 筆，已自動匯出 CSV 檔：{csv_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('使用方式: python erp_web_client.py "SELECT ..." [row_limit]')
        sys.exit(1)
        
    sql_input = sys.argv[1]
    limit = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    
    success, result = execute_sql_on_web(sql_input, limit)
    if success:
        parse_and_save_result(result)
    else:
        print(f"[執行失敗] {result}")
        with open(OUTPUT_FILE, "w", encoding="utf-8-sig") as f:
            f.write(f"ERROR: {result}")
```

---

### 步驟 3：在 Antigravity CLI 註冊 Skill (`SKILL.md`)

建立資料夾：`%USERPROFILE%\.gemini\skills\erp-prod-web-executor\`
並在該資料夾內建立檔案 **`SKILL.md`**：

```markdown
---
name: erp-prod-web-executor
description: Execute SQL queries on the PRODUCTION IBM DB2 database via the logged-in ERP Web Command Center (dsjjsql.jsp) using Chrome DevTools Protocol (CDP).
---

# ERP Production Web SQL Executor (Live Browser Integration)

This skill connects directly to the user's active ERP browser session to execute queries on the Production environment safely and extract structured data for instant analysis and code debugging.

## Core Capabilities

1. **Production Session Reuse**: Runs SQL under the user's logged-in credentials without storing or asking for passwords.
2. **Read-Only Safety Guard**: Strictly permits `SELECT` / `WITH` statements, preventing accidental modifications on Production.
3. **Automatic Tab Discovery**: Automatically finds and attaches to the `dsjjsql.jsp` tab (or opens one if missing).
4. **Structured Parsing**: Converts web table / CSV outputs into clean Markdown tables or Excel CSV files.

## ⚠️ Data Display Rules

- **Small Datasets (<= 20 rows)**: Render as a standard Markdown table in the chat.
- **Large Datasets (> 20 rows)**:
  - **Export**: Automatically saved to `D:\\temp\\query_results\\prod_query_YYYYMMDD_HHMMSS.csv` (CP950 encoded).
  - **Summary**: Display first 3 rows in chat and provide the CSV link.

## 🚀 Execution Command

```powershell
python "%USERPROFILE%\\erp_web_client.py" "YOUR_SQL_QUERY"
```

The output is written to `%USERPROFILE%\\query_output.txt`. Read this file to present results to the user.
```

---

## 4. 日常使用 SOP 與自然語言指令範例

設定完成後，日常使用非常簡單：

### 📋 標準操作步驟：
1. 雙擊桌面上的 **`啟動正式機ERP(AI連線模式).bat`**。
2. 在開啟的瀏覽器中輸入帳號密碼登入 ERP（進入任一頁面或命令中心皆可）。
3. 打開 **Antigravity CLI**，直接用自然語言交談！

### 🗣️ 自然語言指令範例：
- 「*幫我查正式機 `db.tbhdd12` 員工 26358 八月份的請假資料*」
- 「*查一下正式機單號 `263582026014057` 的狀態*」
- 「*執行正式機查詢：SELECT * FROM db.tbda001 WHERE orderNo = '1130001'*」

AI 會自動呼叫 `erp-prod-web-executor`，並在 1~2 秒內回傳查詢表格或 CSV 連結，**整個過程花費極少 Token！**

---

## 5. 常見問題與自我排查清單 (Troubleshooting)

### Q1: 出現 `CDP_CONNECTION_ERROR`（無法連線至遠端偵錯埠 9222）？
- **原因**：沒有使用桌面的「AI 連線模式」捷徑開啟瀏覽器，或者瀏覽器被完全關閉了。
- **解法**：請關閉普通瀏覽器視窗，雙擊桌面的 **`啟動正式機ERP(AI連線模式).bat`** 重新開啟並登入。

### Q2: 出現 `No module named 'websocket'`？
- **原因**：Python 環境中缺少套件。
- **解法**：在終端機執行 `pip install websocket-client`。

### Q3: 出現 `FORBIDDEN_SQL_WRITE`（正式機查詢僅限 SELECT/WITH）？
- **原因**：安全攔截防護生效！此工具嚴禁在正式機執行 `UPDATE`、`DELETE`、`INSERT`、`DROP` 等寫入指令。
- **解法**：正式機僅支援唯讀查詢；若需寫入或測試，請使用測試機 DB2 工具。

### Q4: 提示 `NO_SQL_FIELD` 或分頁卡住？
- **原因**：瀏覽器 Session 逾期登出，或停留在錯誤的登入頁。
- **解法**：切換到該瀏覽器視窗，重新登入 ERP 或點擊命令中心 (`dsjjsql.jsp`) 確認畫面正常。

---

*文檔版本：V1.0 | 適用於全體 Antigravity CLI 使用者*
