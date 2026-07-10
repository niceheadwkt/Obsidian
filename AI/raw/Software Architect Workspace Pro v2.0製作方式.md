將它拆分成一套完整專案，每個檔案都能獨立維護、版本控制與擴充。

```
Software-Architect-Workspace-Pro/
│
├── README.md
├── CHANGELOG.md
├── LICENSE
│
├── docs/
│   ├── 01_設計理念.md
│   ├── 02_工作流程.md
│   ├── 03_架構原則.md
│   ├── 04_程式設計規範.md
│   ├── 05_程式碼審查.md
│   ├── 06_技術決策(ADR).md
│   ├── 07_文件規範.md
│   ├── 08_Git_Workflow.md
│   ├── 09_AI_Agent_Workflow.md
│   └── 10_最佳實務.md
│
├── prompts/
│   ├── SystemPrompt.md
│   ├── CodeArchitect.md
│   ├── Reviewer.md
│   ├── Refactor.md
│   ├── Research.md
│   ├── Documentation.md
│   └── Debug.md
│
├── workspace/
│   ├── Workspace_State.md
│   ├── Architecture.md
│   ├── Decisions.md
│   ├── Roadmap.md
│   ├── TODO.md
│   ├── Risks.md
│   ├── File_Map.md
│   └── Glossary.md
│
├── templates/
│   ├── ADR_Template.md
│   ├── Project_Template.md
│   ├── API_Template.md
│   ├── Module_Template.md
│   ├── Bug_Template.md
│   └── Feature_Template.md
│
└── examples/
    ├── Example_Project.md
    ├── Example_Architecture.md
    └── Example_Workspace.md
```

## 我希望做到的品質

這不是網路上常見的 Prompt 集合，而是參考：

- Domain-Driven Design（DDD）
- Clean Architecture
- Hexagonal Architecture
- SOLID
- ADR（Architecture Decision Records）
- C4 Model
- Arc42
- Claude Code 的工作流程
- GPT-5 的提示工程最佳實務
- AI Agent 的協作模式

建立一套真正可落地的「AI 軟體架構師工作系統」。

## 建議分階段完成

由於內容龐大，我建議分成 4 個版本：

- **Part 1：Core**（README、SystemPrompt、Workspace、Architecture）
- **Part 2：Code**（Code Architect、Review、Refactor、Debug）
- **Part 3：Document & Research**（Documentation、Research、ADR、模板）
- **Part 4：AI Agent**（MCP、RAG、Ollama、Open WebUI、Git Workflow）

每一部分我都可以整理成獨立的 Markdown 檔，最後組成完整專案。

---

### 我建議的目標

我希望把它做成一本真正的 **《Software Architect Workspace Pro v2.0》**，而不是只有 Prompt。

規模大約：

- 📄 40～60 個 Markdown 檔
- 📚 約 300～500 頁內容
- 🧩 30+ 專業 Prompt 模板
- 🏗️ 完整 Workspace 系統
- 💻 完整 Code Architect 系統
- 🤖 AI Agent 開發規範
- 📖 可直接放到 GitHub 維護

我認為這樣才是真正接近 **Claude Code + Claude Artifacts** 的專業工作環境，而不是一段很長但難以維護的 Prompt。