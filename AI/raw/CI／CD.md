**CI/CD** 是現代軟體開發（特別是 DevOps 架構）中非常核心的自動化流程，它是 **Continuous Integration（持續整合）** 與 **Continuous Delivery / Continuous Deployment（持續交付 / 持續部署）** 的縮寫。

簡單來說，CI/CD 的核心目標就是：**透過「自動化」工具，把工程師寫好的程式碼，經過自動化測試、建置，最後安全且快速地送到生產環境（Production）讓使用者使用。**

以下為您詳細拆解這兩個概念：

### 1. CI：Continuous Integration（持續整合）

「持續整合」專注於**程式碼提交到合併**的階段。當多位工程師同時開發同一個專案時，大家各自修改程式碼，很容易在合併時發生衝突（也就是俗稱的補丁地獄）。

- **怎麼做：** 工程師只要將程式碼推送到程式庫（如 GitHub/GitLab），自動化伺服器就會立刻啟動。
    
- **自動化流程：**
    
    1. **自動建置（Build）：** 自動將程式碼編譯、打包（例如包成 Docker Image）。
        
    2. **自動測試（Test）：** 自動執行單元測試（Unit Test）、整合測試，檢查新寫的程式碼有沒有改壞原本的功能。
        
- **好處：** 提早發現 Bug。如果測試失敗，系統會立刻通知工程師，確保主分支（Main/Master）的程式碼永遠是健康、隨時可以執行的狀態。
    

### 2. CD：Continuous Delivery / Deployment（持續交付 / 持續部署）

當程式碼通過了 CI 的測試後，接下來就進入 CD 階段。這裡的 CD 根據自動化的程度，分為兩種層次：

#### A. 持續交付 (Continuous Delivery)

- **含意：** 程式碼通過測試後，會**自動**被打包並發佈到「類生產環境」（如 Staging 或 Testing 環境）。
    
- **關鍵點：** 它做好了隨時可以上線的準備，但**最終要不要部署到真正的生產環境（對外營運的伺服器），需要由人工（例如 PM 或技術主管）點擊按鈕來決定**。
    

#### B. 持續部署 (Continuous Deployment)

- **含意：** 自動化程度最高。只要程式碼通過了 CI 的所有測試，系統就會**完全不經人工干預，直接自動部署到生產環境**讓使用者看到。
    
- **關鍵點：** 這需要團隊對自己的自動化測試有極高的信心，因為任何一個漏網的 Bug 都會直接上線。
    

### 💡 總結：CI/CD 的完整管線（Pipeline）

一個標準的 CI/CD 流程通常會像一條自動化工廠的流水線：

$$\text{Code (寫程式)} \rightarrow \text{Commit (提交)} \rightarrow \text{Build (建置)} \rightarrow \text{Test (測試)} \rightarrow \text{Release (交付)} \rightarrow \text{Deploy (部署)}$$

- **傳統開發方式：** 寫完程式 ➔ 手動編譯 ➔ 手動執行測試 ➔ 用 FTP 或連線到伺服器手動貼上檔案 ➔ 重啟服務。費時且容易因人為疏忽而出錯。
    
- **CI/CD 開發方式：** 寫完程式 ➔ `git push` ➔ 自動化工具接手完成後續所有動作。
    

### 🛠️ 常見的 CI/CD 工具

在實務上，我們會建立設定檔（通常是 YAML 格式）來叫工具執行這些流水線，常見的工具有：

- **GitHub Actions**（目前非常主流，直接整合在 GitHub 中）
    
- **GitLab CI/CD**（內建於 GitLab，大型企業愛用）
    
- **Jenkins**（老牌、功能強大、擴充性極高，但需要自行架設與維護伺服器）
    
- **Argo CD / Drone**（常用於雲端原生與 Kubernetes 環境）