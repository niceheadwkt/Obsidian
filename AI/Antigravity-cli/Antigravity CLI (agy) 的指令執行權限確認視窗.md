Antigravity CLI (agy) 的指令執行權限確認視窗。
  ──────
  ### 一、為什麼會一直跳出詢問？

  因為預設按 Enter 選到的是 1. Yes：

  • 1. Yes：僅核准這一次執行。下一個指令（即使只是稍微修改參數）就會再次跳出提示要求確認。
  ──────
  ### 二、如何讓它不要一直問？（三種解決方式）

  #### 方式 1：啟動 CLI 時加上自動核准參數（最推薦、一勞永逸）

  啟動 agy 時加上 --dangerously-skip-permissions 旗標，即可在整個 Session 中自動核准所有指令與工具操作，不再跳出任何確認提示：

    agy --dangerously-skip-permissions

  │ Tip
  │ 建立 PowerShell 捷徑指令：
  │ 若不想每次手打長參數，可以在您的 PowerShell 設定檔（$PROFILE）中加入別名：
  │
  │   function agya { agy --dangerously-skip-permissions @args }
  │
  │ 之後只要在終端機輸入 agya 即可直接進入全自動核准模式。
  ──────
  #### 方式 2：跳出提示時，利用鍵盤下鍵選擇第 2 或第 3 項

  當權限提示出現時，用鍵盤方向鍵 ↓ 切換選項後按 Enter：

  • 2. Yes, and always allow in this conversation...
  在本次對話 Session 中，只要開頭前綴相符的指令（例如 python -c ...）都不會再跳出詢問。
  • 3. Yes, and always allow... (Persist to settings.json)
  永久放行該指令前綴，並自動寫入全域設定檔，未來重開 CLI 也不會再問。
  ──────
  #### 方式 3：編輯全域設定檔設定白名單前綴

  可以直接開啟設定檔 settings.json]，在 permissions.allow 清單中加入您允許自動執行的通用指令前綴（如 python *、Get-* 等）：

    {
      "allowNonWorkspaceAccess": true,
      "permissions": {
        "allow": [
          "command(python *)",
          "command(Get-*)",
          "command(git *)"
        ]
      }
    }

---

  ### 修改內容說明

  在 permissions.allow 白名單中加入了常用的前綴規則，涵蓋以下指令：

   前綴規則                                                                                             | 涵蓋指令範例
  ------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------
   command(python)                                                                                      | 所有的 python script.py、python -c "..." 等 Python 指令
   command(pip)                                                                                         | 所有的 pip install ...、pip list 等模組管理指令
   command(git)                                                                                         | 所有的 git status、git diff、git commit 等版本控制指令
   command(chezmoi)                                                                                     | 所有的 chezmoi status、chezmoi diff 等設定同步指令
   command(agy)                                                                                         | 所有的 agy 相關子指令
   command(pwsh) / command(powershell) / command(cmd)                                                   | 終端機與子 shell 執行
   command(Get-) / command(Set-) / command(Test-) / command(Select-)                                    | PowerShell 常見 Cmdlet（如 Get-Content、Get-ChildItem、Test-Path 等）
   command(Copy-) / command(Move-) / command(Remove-) / command(New-)                                   | 檔案操作 Cmdlet
   command($) / command([)                                                                              | PowerShell 變數讀取（如 $env:USERPROFILE）與型別呼叫
   command(dir) / command(cat) / command(ls) / command(type) / command(findstr)                         | 常用系統檢視與搜尋指令
   command(node) / command(npm) / command(npx)                                                          | Node.js 與 npm 工具
  ──────
  ### 生效方式

  未來在 Antigravity CLI 中執行符合上述前綴的指令時，將不再跳出權限選擇視窗，直接自動放行。
