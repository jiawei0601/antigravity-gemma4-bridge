# Antigravity Local LLM Bridge (Gemma 4)

🚀 **讓 Antigravity 能夠在本地環境驅動 Gemma 4 的橋接工具。**

## 項目簡介
本專案提供了一個輕量級的介面，讓 Antigravity (AI 助手) 可以透過 Ollama 呼叫本地運行的 Gemma 4 模型。這對於需要保護隱私、離線處理或是利用本地硬體加速的任務非常有用。

## 核心功能
- **本地運算**: 100% 在本地執行，不需上傳數據。
- **Gemma 4 支援**: 針對 Google 最新一代開放模型優化（支援 26B-A4B 版本）。
- **模型切換**: 支援 `e2b` (效率優先) 與 `26b` (能力優先) 模型。
- **豐富終端輸出**: 使用 `Rich` 庫提供精美的 Markdown 與面板輸出。

## 安裝需求

1. **安裝 Ollama**: 
   請至 [ollama.com](https://ollama.com/) 下載並安裝。
2. **下載 Gemma 4 模型**:
   - **26B-A4B 版 (推薦)**:
     ```bash
     ollama pull gemma4:26b
     ```
   - **E2B 版 (輕量)**:
     ```bash
     ollama pull gemma4:e2b
     ```
3. **安裝 Python 依賴**:
   ```bash
   pip install -r requirements.txt
   ```

## 使用方法

### 透過命令行調用
預設使用 26b 模型：
```bash
python main.py "你的問題或指令"
```

切換模型：
```bash
python main.py "你的問題" --model gemma4:e2b
```

### 與 Antigravity 整合
當 Antigravity 需要進行本地分析時，可以直接呼叫此腳本。

## 授權
MIT License
