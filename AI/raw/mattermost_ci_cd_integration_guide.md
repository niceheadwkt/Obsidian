# Mattermost 與 CI/CD 流程整合指南

本文整理了將 **Mattermost**（開源企業即時通訊平台）與 **CI/CD（持續整合與持續部署）** 流程進行整合的核心概念、應用場景，以及與 **GitLab CI** 實作的具體步驟。

---

## 一、 Mattermost 在 CI/CD 流程中的核心應用

將自動化流程與 Mattermost 結合可實現 **ChatOps（以聊天作為協作與自動化控制中心）**，讓團隊成員免去頻繁切換儀表板的困擾。

### 1. 核心整合功能與應用場景
* **即時建置與測試通知（Status Notifications）**：當 CI/CD 流程（如 GitLab CI、GitHub Actions、Jenkins）開始、成功或失敗時，自動發送通知到對應的專案頻道，並可對特定人員進行 `@mention`。
* **互動式審核與部署（Interactive Approvals）**：在流水線進入正式環境（Production）部署前，Mattermost 訊息內帶有互動按鈕（如「核准部署」或「拒絕」），點擊後由 Webhook 回調給 CI/CD 伺服器繼續執行。
* **斜線指令觸發（Slash Commands）**：直接在 Mattermost 輸入指令（例如 `/deploy staging v1.2.0`）來觸發對應的流水線。
* **結合 Playbooks 進行事件應變**：當 CI/CD 偵測到重大錯誤時，自動觸發 Mattermost 的 **Playbooks（操作手冊）**，建立專屬障礙排除頻道並指派任務。

### 2. 常見 CI/CD 工具整合對照
| 工具 | 整合方式 | 主要用途 |
| :--- | :--- | :--- |
| **GitLab** | 官方 GitLab Plugin / Webhooks | MR 通知、Pipeline 狀態回報、Issue 雙向同步 |
| **GitHub** | GitHub Actions / Webhooks | PR 狀態、Action 執行結果通知 |
| **Jenkins** | Mattermost Jenkins Plugin / Webhook | 建置失敗告警、觸發建置、傳送測試覆蓋率報告 |

---

## 二、 GitLab CI 與 Mattermost 整合實作

整合 GitLab CI 與 Mattermost 主要有兩種常見方式：

### 方法一：透過 GitLab 內建的 Mattermost 整合服務（接收系統級通知）
1. **取得 Mattermost Webhook URL**：
   * 在 Mattermost 目標頻道點擊頻道名稱 $\rightarrow$ **Integration** $\rightarrow$ **Incoming Webhook** $\rightarrow$ **Add Incoming Webhook**，建立並複製產生的 **URL**。
2. **在 GitLab 中設定**：
   * 進入 GitLab 專案 $\rightarrow$ **Settings** $\rightarrow$ **Integrations** $\rightarrow$ **Mattermost notifications**。
   * 貼上 Webhook URL，勾選欲觸發的事件（如 Pipeline、Push、Merge request），並儲存變更。

---

### 方法二：在 `.gitlab-ci.yml` 中使用 `curl` 發送自定義通知（高彈性）

透過 GitLab CI 的環境變數與 `after_script` 搭配 `curl` 發送客製化訊息。

#### 1. 設定 GitLab CI/CD 變數
* 前往 GitLab 專案 $\rightarrow$ **Settings** $\rightarrow$ **CI/CD** $\rightarrow$ **Variables**。
* 新增變數：
  * **Key**: `MATTERMOST_WEBHOOK_URL`
  * **Value**: 你的 Mattermost Incoming Webhook URL

#### 2. 編寫 `.gitlab-ci.yml` 範例
```yaml
stages:
  - build
  - test
  - deploy

build_job:
  stage: build
  script:
    - echo "Building the application..."

# 失敗時發送通知
notify_mattermost_fail:
  stage: deploy
  script:
    - echo "Pipeline failed, sending notification..."
  when: on_failure
  after_script:
    - |
      PAYLOAD="{\"channel\": \"devops-alerts\", \"username\": \"GitLab-CI\", \"text\": \"🚨 **Build Failed!**\n專案: \`${CI_PROJECT_NAME}\`\n分支: \`${CI_COMMIT_REF_NAME}\`\n觸發者: ${GITLAB_USER_NAME}\n查看詳情: ${CI_PIPELINE_URL}\"}"
      curl -X POST -H 'Content-Type: application/json' --data "$PAYLOAD" "$MATTERMOST_WEBHOOK_URL"

# 成功時發送通知
notify_mattermost_success:
  stage: deploy
  script:
    - echo "Deployment successful!"
  when: on_success
  after_script:
    - |
      PAYLOAD="{\"channel\": \"devops-alerts\", \"username\": \"GitLab-CI\", \"text\": \"✅ **Deployment Successful!**\n專案: \`${CI_PROJECT_NAME}\`\n環境已成功更新至最新版本。\n[查看 Pipeline 記錄](${CI_PIPELINE_URL})\"}"
      curl -X POST -H 'Content-Type: application/json' --data "$PAYLOAD" "$MATTERMOST_WEBHOOK_URL"