---
tags:
- Obsidian
- 知識庫
- 知識管理
- 雙向連結
---
在 **App 開發（iOS / Android / Cross-platform）** 的領域中，複雜度通常比單純的網頁開發更高。你需要同時處理 **UI 畫面、生命週期（Lifecycle）、資料流（Data Flow）、異步處理（Async），以及跨裝置適配**。

在這種高複雜度下，[[Obsidian]] 的雙向連結能幫你把大腦從「死記硬背架構」中解放出來。以下為你規劃 3 個最適合 App 開發學習與實戰的雙向連結範例：

## 範例 1：UI 元件與「生命週期 / 狀態管理」的縱向連結

不論是開發 iOS (SwiftUI) 還是 Android (Jetpack Compose)，App 最常遇到的 Bug 都跟「狀態（State）」和「生命週期」有關。將 UI 元件與這些核心觀念連結，能幫你建立正確的開發直覺。

- **筆記名稱**：UI_首頁購物車列表 (ProductListView)
    
- **內文撰寫範例**：
    
    Swift
    
    ```
    // SwiftUI 範例
    struct ProductListView: View {
        @StateObject var viewModel = ProductViewModel() // 監聽資料變更
    
        var body: some View {
            List(viewModel.products) { product in
                ProductRow(product: product)
            }
            .onAppear { viewModel.fetchProducts() } // 畫面出現時抓取資料
        }
    }
    ```
    
    > ### 💡 技術筆記與關聯
    > 
    > - 這裡使用 `@StateObject` 進行 `[[App 狀態管理 (State Management)]]`，確保畫面旋轉或重建時，資料不會丟失。
    >     
    > - `.onAppear` 觸發的時間點屬於 `[[SwiftUI 視圖生命週期 (View Lifecycle)]]` 的一部分。如果未來改為 `[[Flutter 開發]]`，相對應的觀念是 `initState()`。
    >     
    
- **雙向連結產生的威力**： 當你未來點進 `[[App 狀態管理 (State Management)]]` 這篇核心心法時，反向連結會列出所有你寫過的 UI 元件（如：購物車列表、會員登入頁）。你可以一眼看出不同畫面各自用了什麼狀態管理策略（如：`@StateObject`, `@EnvironmentObject`）。
    

## 範例 2：設計模式（Design Pattern）與多個專案的橫向連結

App 開發非常講究架構（如 MVVM, Clean Architecture）。你可以建立一個架構模式的專門筆記，並將它連結到你開發的不同 App 專案中，比對其實踐方式。

- **筆記名稱**：架構_MVVM 模式 (Model-View-ViewModel)
    
- **內文撰寫範例**：
    
    > ## 核心精髓
    > 
    > 將 UI 邏輯（View）與商業邏輯（Model）完全分離，透過 ViewModel 進行橋接，達成解耦（Decoupling）。
    > 
    > ## 🛠️ 實戰專案演練
    > 
    > - `[[💼 專案_天氣預報 App]]`：使用傳統的 MVVM 搭配 Combine 進行資料綁定。
    >     
    > - `[[💼 專案_每日記帳 App]]`：在 Jetpack Compose 中配合 Koin 進行 `[[依賴注入 (Dependency Injection)]]` 的 MVVM 實踐。
    >     
    
- **雙向連結產生的威力**： 架構觀念很抽象，但當你在同一個觀念筆記下，連結了「iOS 天氣 App」與「Android 記帳 App」兩個實例，你就能橫向對比出：_「原來 Swift 的 ObservableObject 和 Kotlin 的 StateFlow 雖然語法不同，但在 MVVM 裡扮演的角色一模一樣！」_
    

## 範例 3：App 商店上架規範與雙平台踩坑紀錄（避坑指南）

App 開發最心累的往往不是寫程式，而是**雙平台商店（App Store / Google Play）的上架審查與權限申請**。

- **筆記名稱**：功能_App 內設定定位權限
    
- **內文撰寫範例**：
    
    > 本功能需要獲取使用者的精確定位（Fine Location）。
    > 
    > ## 平台設定須知
    > 
    > - **iOS**：必須在 `Info.plist` 中設定 `NSLocationWhenInUseUsageDescription`，否則會觸發 `[[App Store 審查退件原因|Guideline 5.1.1 隱私權退件]]`。
    >     
    > - **Android**：需在 `AndroidManifest.xml` 宣告 `ACCESS_FINE_LOCATION`。在 Android 12 以上版本需特別注意 `[[Android 執行階段權限 (Runtime Permissions)]]` 的動態請求邏輯。
    >     
    > 
    > ## 遭遇錯誤
    > 
    > - 曾在此功能上卡關，詳見：`[[錯誤_定位權限造成 App 閃退]]`。
    >     
    
- **雙向連結產生的威力**： 這讓你的筆記變成具備「預警功能」的知識庫。當你在寫新專案需要定位功能時，只要打出 `[[功能_App 內設定定位權限]]`，就能順藤摸瓜看到 `[[App Store 審查退件原因]]`，直接在開發階段就避開會被 Apple 官方退件的坑，省下數天的審查等待時間。
    

## 📱 App 開發者的 Obsidian 標籤（Tag）輔助系統

配合雙向連結，建議在 App 開發筆記中使用以下分類標籤：

- `#平台/iOS` 、 `#平台/Android` 、 `#平台/Flutter` （區分技術棧）
    
- `#層級/UI` 、 `#層級/Data` 、 `#層級/Domain` （區分架構分層）
    
- `#心法/效能優化` （如：記憶體洩漏 Memory Leak 處理、圖片快取）
    

你目前打算採用的開發工具是原生開發（Swift / Kotlin），還是跨平台框架（Flutter / React Native）呢？我們可以針對該技術棧的專有名詞做進一步的架構梳理。