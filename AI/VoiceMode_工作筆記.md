# VoiceMode 工作筆記

## 上次做到哪 (2026-07-24)
- **專案中文化**：將整個專案的 `README.md`、`CLAUDE.md`、`docs/tutorials/getting-started.md` 以及 `voice_mode/resources/docs/*.md` 等說明文件翻譯為繁體中文。
- **代碼註解中文化**：將 `voice_mode/tools/converse.py` 等核心工具中的 Python docstring 及註解翻譯為繁體中文，符合全域規範。
- **新增本地語音工具**：新增 `dictate.py` 與 Whisper 相關腳本（`whisperStart.bat`、`whisper-cli.exe` 等）以支援本地語音辨識功能。

## 下一步
- 測試本地 Whisper 工具與 `converse.py` 的語音對話功能。
- 排除與驗證 Whisper 工具的執行權限與環境依賴。
- 檢查與配置本地 TTS 語音（如 Kokoro/OpenAI）的整合測試。
