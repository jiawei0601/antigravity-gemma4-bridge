# run.py

import sys
from src.config_manager import ConfigManager
from src.cli_interface import CLIInterface
from src.llm_service import OllamaBridge

def main():
    """
    Antigravity Local Bridge 專案入口點。
    整合配置載入、參數解析與 LLM 調用。
    """
    # 1. 載入配置
    config_manager = ConfigManager()
    config_manager.load_config()

    # 2. 初始化 CLI 與參數解析
    cli = CLIInterface(config_manager.get_all())
    args = cli.parse_args()

    # 3. 顯示 UI 標頭
    cli.show_header(args.model)

    # 4. 執行 LLM 調用 (橋接 Ollama)
    cli.show_response_header(args.model)
    bridge = OllamaBridge()
    bridge.chat_stream(args.model, args.prompt)

if __name__ == "__main__":
    main()
