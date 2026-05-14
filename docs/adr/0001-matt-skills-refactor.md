# docs/adr/0001-matt-skills-refactor.md - 架構決策紀錄

## 狀態 (Status)
已接受 (Accepted)

## 決策背景 (Context)
原始的 `main.py` 是一個單一檔案 (Monolith)，混合了 CLI 解析、設定檔讀取與 API 通訊邏輯。這導致代碼難以測試且擴展性差。

## 決策內容 (Decision)
我們決定採用 **關注點分離 (SoC)** 原則，將系統拆分為以下模組：
1. **CLI 層**：處理終端輸入與 Rich UI 顯示。
2. **服務層 (Bridge Layer)**：負責與 Ollama API 的通訊。
3. **配置層**：管理設定檔與環境變數。

## 後果 (Consequences)
- **優點**：各模組可獨立進行單元測試，結構清晰，易於增加新的模型支援。
- **缺點**：檔案數量增加，初步開發成本稍高。
