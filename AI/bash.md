`bash`（全名為 **Bourne-Again SHell**）是 Unix 和 Linux 系統中最常用、最經典的**命令列直譯器（Shell）**。

簡單來說，它是你和作業系統核心（Kernel）之間的「橋梁」。當你在終端機（Terminal）輸入指令時，Bash 負責幫你解讀這些指令，並叫作業系統去執行。

## Bash 的核心功能

Bash 廣受歡迎的原因主要在於以下幾個強大功能：

- **指令執行**：可以執行系統內建指令（如 `ls`, `cd`, `pwd`）或外部安裝的軟體。
    
- **自動補齊（Tab Completion）**：打出指令或路徑的前幾個字後，按 `Tab` 鍵會自動幫你補齊，省時又防呆。
    
- **指令歷史（History）**：用鍵盤的 `↑` 和 `↓` 鍵可以快速找回之前輸入過的指令。
    
- **自動化腳本（Bash Scripting）**：你可以把一連串的指令寫成一個副檔名為 `.sh` 的檔案，讓電腦自動執行重複性的任務。
    

## 基礎語法與常用指令

在 Bash 中，指令的基本結構通常是：

$$\text{指令} \quad \text{[選項]} \quad \text{[參數]}$$

以下是一些每天都會用到的超基本指令：

|**指令**|**功能說明**|**範例**|
|---|---|---|
|`pwd`|顯示目前所在的資料夾路徑 (Print Working Directory)|`pwd`|
|`ls`|列出目前資料夾底下的所有檔案與目錄|`ls -la` (顯示隱藏檔與詳細資訊)|
|`cd`|切換資料夾 (Change Directory)|`cd Documents/`|
|`mkdir`|建立新的資料夾 (Make Directory)|`mkdir new_folder`|
|`rm`|刪除檔案或資料夾 (Remove)|`rm file.txt`|
|`echo`|在螢幕上印出文字或變數內容|`echo "Hello World"`|

## 簡單的 Bash 腳本範例

如果你把指令寫成腳本（例如 `backup.sh`），它看起來會像這樣：

Bash

```
#!/bin/bash
# 第一行叫做 Shebang，用來指定用什麼直譯器來執行這個檔案

echo "開始備份資料..."
mkdir -p ./backup
cp *.txt ./backup/
echo "備份完成！"
```

> 💡 **小知識**：雖然現在 macOS 預設的 Shell 已經改成 `zsh`，Linux 的 Ubuntu 系統也引入了 `dash`，但 `bash` 依然是目前伺服器維運、DevOps 自動化部署中，最不可或缺的業界標準。