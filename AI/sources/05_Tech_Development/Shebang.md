---
tags:
- Bash
- Shebang
- 技術開發
---
在 Unix/Linux 的世界裡，**Shebang**（也常被稱為 Hashbang、Pound-bang）指的是出現在腳本檔案**第一行**、以 `#!` 開頭的特殊字元序列。

它的主要作用是告訴作業系統：「**請不要用預設的方式執行我，而是用我後面指定的那個程式（直譯器）來跑我底下的原始碼。**」

## 為什麼叫 Shebang？

這個名字其實是兩個程式界術語的結合縮寫：

- **Sharp / Hash**：指井字號 `#`
    
- **Bang**：指驚嘆號 `!`
    

合在一起 `#!` 就被稱作 **Shebang**。

## 它是如何運作的？

當你在終端機輸入 `./script.sh` 執行一個檔案時，核心（Kernel）會先讀取這個檔案的開頭兩個位元組。

- 如果看到了 `#!`，核心就知道這是一個腳本。
    
- 核心會把 `#!` 後面路徑所指定的程式載入記憶體。
    
- 接著，把這個腳本的檔案路徑當作參數，傳給該程式去執行。
    

## 常見的 Shebang 範例

Shebang 不僅僅用於 [[bash|Bash]]，任何腳本語言（如 Python、Perl、Ruby）都可以使用：

### 1. Bash 腳本

Bash

```
#!/bin/bash
echo "這是一段 Bash 腳本"
```

### 2. Python 腳本

Python

```
#!/usr/bin/env python3
print("這是一段 Python 腳本")
```

### 3. Node.js 腳本

JavaScript

```
#!/usr/bin/env node
console.log("這是一段 Node.js 腳本");
```

## 為什麼有些寫法是 `/usr/bin/env`？

你可能會注意到，上面的範例中有兩種不同的風格：

- 絕對路徑寫法：`#!/bin/bash`
    
- 使用 `env` 的寫法：`#!/usr/bin/env python3`
    

**強烈建議使用 `env` 的寫法**，尤其是在寫 Python、Node.js 等跨平台腳本時。

因為在不同的作業系統（例如 Ubuntu、CentOS、macOS）中，`python3` 或 `node` 被安裝的路徑可能完全不同（有的在 `/usr/bin`，有的在 `/usr/local/bin`）。如果寫死絕對路徑，換一台電腦可能就動不了了。

使用 `#!/usr/bin/env python3`，作業系統會去你的系統變數（`$PATH`）裡尋找第一個找到的 `python3` 來執行，大大提高了腳本的**移植性（Portability）**。

> ⚠️ **注意事項**：Shebang 必須嚴格放在檔案的**第一行**，前面不能有任何空格、空行或其它的註解，否則作業系統會無法識別，直接把它當作普通註解或文字處理。