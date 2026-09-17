  要為您撰寫一個專門讀取 ERP 正式機資料庫表格範圍資料的 MCP (Model Context Protocol) 伺服器，最推薦且安全的方式是採用 Python FastMCP 搭配您既有的 瀏覽器
  Session 整合機制（CDP 直連 dsjjsql.jsp）。
  這樣設計的優點：
  1. 免寫死帳密：直接復用瀏覽器已登入的 SSO Session，符合資安規範。
  2. 內建唯讀安全鎖：在 MCP 程式層嚴格限制僅能執行 SELECT，杜絕任何異動正式機資料的風險。
  3. 支援精確範圍查詢：支援指定「表格名」、「欄位清單」、「過濾條件 (WHERE)」、「排序 (ORDER BY)」以及「筆數與位移 (LIMIT / OFFSET)」。
  ──────
  ### 一、MCP 工具設計與架構
  我們定義兩個核心 MCP Tools：

  4. read_erp_table：專門讀取指定表格與範圍（自動組合安全的 DB2 SQL 語法與分頁範圍）。
  ──────
  5. query_erp_sql：允許執行自訂的唯讀 SQL 查詢。
  ### 二、完整 MCP 程式碼實作
  請在您的專案目錄（例如 C:/aiTest/erp-mcp/）建立 erp_prod_mcp.py：

    import os
    import sys
    import json
    import time
    import csv
    import io
    import urllib.request
    import websocket
    from fastmcp import FastMCP
    from typing import List, Optional

    # 初始化 FastMCP Server
    mcp = FastMCP("erp-prod-executor")

    CDP_PORT = 9222
    TARGET_URL_KEY = "dsjjsql.jsp"
    DEFAULT_ERP_SQL_URL = "http://127.0.0.1:8080/erp/ds/jsp/dsjjsql.jsp"

    # ==========================================
    # 1. 唯讀安全檢查機制
    # ==========================================
    def validate_readonly_sql(sql: str) -> bool:
        """嚴格限制僅能執行 SELECT 或 WITH 開頭的唯讀查詢"""
        cleaned = sql.strip().upper()
        if not (cleaned.startswith("SELECT") or cleaned.startswith("WITH")):
            return False

        # 禁止危險關鍵字
        forbidden_keywords = [
            "INSERT ", "UPDATE ", "DELETE ", "DROP ", "ALTER ",
            "CREATE ", "TRUNCATE ", "GRANT ", "REVOKE ", "MERGE "
        ]
        for kw in forbidden_keywords:
            if kw in cleaned:
                return False
        return True

    # ==========================================
    # 2. CDP 瀏覽器通訊模組
    # ==========================================
    def get_tab_list():
        try:
            url = f"http://127.0.0.1:{CDP_PORT}/json/list"
            with urllib.request.urlopen(url, timeout=3) as resp:
                return json.loads(resp.read().decode('utf-8'))
        except Exception:
            return None

    def send_cdp_eval(ws, expression: str):
        req_id = int(time.time() * 1000) % 1000000
        msg = {
            "id": req_id,
            "method": "Runtime.evaluate",
            "params": {
                "expression": expression,
                "returnByValue": True,
                "awaitPromise": False
            }
        }
        ws.send(json.dumps(msg))
        start_time = time.time()
        while time.time() - start_time < 10:
            raw_res = ws.recv()
            res = json.loads(raw_res)
            if res.get("id") == req_id:
                return res.get("result", {}).get("result", {}).get("value")
        return None

    def execute_sql_via_cdp(sql_query: str, row_limit: int = 0):
        if not validate_readonly_sql(sql_query):
            raise ValueError("安全攔截：僅允許執行唯讀查詢 (SELECT / WITH)。")

        tabs = get_tab_list()
        if not tabs:
            raise ConnectionError("無法連線至 Chrome (Port 9222)，請確認 Chrome 是否已開啟 Remote Debugging。")

        target_tab = None
        for tab in tabs:
            url = tab.get("url", "")
            title = tab.get("title", "")
            if TARGET_URL_KEY in url or "命令中心" in title:
                target_tab = tab
                break

        if not target_tab:
            raise RuntimeError("找不到 dsjjsql.jsp 命令中心分頁，請先在瀏覽器中開啟該頁面。")

        ws_url = target_tab.get("webSocketDebuggerUrl")
        ws = websocket.create_connection(ws_url, timeout=10, suppress_origin=True)

        try:
            escaped_sql = json.dumps(sql_query)
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
            send_cdp_eval(ws, js_submit)
            time.sleep(1.0)

            # 等候查詢結果
            max_wait = 15.0
            start_wait = time.time()
            csv_content = None

            while time.time() - start_wait < max_wait:
                js_check = '''
                (function() {
                    var csvArea = document.getElementById('csvData');
                    if (csvArea && csvArea.value !== undefined) {
                        return { status: 'DONE', data: csvArea.value };
                    }
                    return { status: 'WAITING' };
                })();
                '''
                check_res = send_cdp_eval(ws, js_check)
                if isinstance(check_res, dict) and check_res.get("status") == "DONE":
                    csv_content = check_res.get("data", "")
                    break
                time.sleep(0.5)

            ws.close()
            if csv_content is None:
                raise TimeoutError("查詢逾時，未能取得資料。")

            # 解析 CSV 回傳結構化資料
            reader = csv.reader(io.StringIO(csv_content.strip()))
            rows = list(reader)
            if not rows:
                return []

            headers = rows[0]
            result_data = []
            for r in rows[1:]:
                if len(r) == len(headers):
                    result_data.append(dict(zip(headers, r)))
                else:
                    result_data.append({"raw_row": r})
            return result_data

        except Exception as e:
            ws.close()
            raise e

    # ==========================================
    # 3. 註冊 MCP Tools
    # ==========================================

    @mcp.tool()
    def read_erp_table(
        table_name: str,
        columns: str = "*",
        where_clause: Optional[str] = None,
        order_by: Optional[str] = None,
        offset: int = 0,
        limit: int = 50
    ) -> dict:
        """
        從 ERP 正式機讀取特定表格某一範圍的資料（支援條件篩選與分頁）。

        :param table_name: 表格名稱 (例如: 'DB.TBHAM1' 或 'TBHAM1')
        :param columns: 欲查詢的欄位清單，以逗號分隔 (例如: 'EMPNO, CHINAME, EMAIL, EXTENSION'，預設 '*')
        :param where_clause: 篩選條件 (例如: "DEPTNO = 'HA01' AND STATUS = 'A'")
        :param order_by: 排序欄位 (例如: "EMPNO ASC")
        :param offset: 跳過筆數 (分頁起點，預設 0)
        :param limit: 回傳筆數上限 (預設 50，上限 200)
        """
        limit = min(max(1, limit), 200)  # 保護上限

        # 組裝 DB2 SQL 範圍查詢
        sql = f"SELECT {columns} FROM {table_name}"
        if where_clause and where_clause.strip():
            sql += f" WHERE {where_clause.strip()}"
        if order_by and order_by.strip():
            sql += f" ORDER BY {order_by.strip()}"

        # DB2 分頁語法支援
        if offset > 0:
            sql += f" OFFSET {offset} ROWS FETCH NEXT {limit} ROWS ONLY"
        else:
            sql += f" FETCH FIRST {limit} ROWS ONLY"

        data = execute_sql_via_cdp(sql, row_limit=limit)
        return {
            "table": table_name,
            "query_sql": sql,
            "returned_rows": len(data),
            "data": data
        }

    @mcp.tool()
    def query_erp_sql(sql: str, limit: int = 50) -> dict:
        """
        執行自訂的 ERP 唯讀 SQL 查詢語法。

        :param sql: 唯讀 SELECT 語法
        :param limit: 筆數上限 (預設 50)
        """
        data = execute_sql_via_cdp(sql, row_limit=limit)
        return {
            "query_sql": sql,
            "returned_rows": len(data),
            "data": data
        }

    if __name__ == "__main__":
        mcp.run(transport="stdio")
  ──────
  ### 三、註冊至 MCP 設定檔 (mcp_config.json)

  請開啟您的全域 MCP 設定檔：
  C:/Users/ch26788/.gemini/config/mcp_config.json

  在 mcpServers 區塊中加入 erp-prod：

    {
      "mcpServers": {
        "erp-prod": {
          "command": "C:/Users/ch26788/.local/bin/uv.exe",
          "args": [
            "run",
            "--with", "fastmcp",
            "--with", "websocket-client",
            "python",
            "C:/aiTest/erp-mcp/erp_prod_mcp.py"
          ]
        }
      }
    }
  ──────
  ### 四、在對話中的叫用範例

  註冊重啟後，AI Agent 即可直接原生調用此 MCP 工具來獲取範圍資料：

  #### 範例 1：查詢特定表格指定欄位與筆數範圍

    {
      "table_name": "DB.TBHAM1",
      "columns": "EMPNO, CHINAME, EMAIL, EXTENSION",
      "where_clause": "EMPNO >= '26780' AND EMPNO <= '26790'",
      "order_by": "EMPNO ASC",
      "limit": 10
    }

  #### 範例 2：分頁讀取第 51 到 100 筆資料

    {
      "table_name": "DB.TBHAM0",
      "columns": "EMPNO, DEPTNO, TITLE",
      "where_clause": "TMNTDATE = ''",
      "order_by": "EMPNO ASC",
      "offset": 50,
      "limit": 50
    }
  ──────
  ### 五、重點技術與注意事項

  6. DB2 範圍語法：
      • DB2 支援標準 FETCH FIRST n ROWS ONLY 與 OFFSET m ROWS FETCH NEXT n ROWS ONLY。
  7. 大資料量保護：
      • 預設限制 limit 上限（如 200 筆），避免一次抓取過多資料塞爆 Token 視窗。
  8. 中文編碼：
      • 透過 CDP 抓取 csvArea.value 取得的是 JavaScript DOM 內已解碼的 Unicode 字串，能避免傳統 Socket/JDBC 的 Big5/CP950 亂碼問題。

