# src/cli_interface.py

import argparse
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from typing import Dict, Any

class CLIInterface:
    """
    負責處理命令行參數解析和使用 rich 庫進行美觀的介面輸出。
    """
    def __init__(self, config_data: Dict[str, Any]):
        self.console = Console()
        self.config = config_data

    def parse_args(self) -> argparse.Namespace:
        """解析命令行參數。"""
        parser = argparse.ArgumentParser(description="Antigravity Gemma 4 Bridge")
        parser.add_argument(
            "prompt", 
            nargs="?", 
            default="請用繁體中文向我打招呼，並自我介紹。", 
            help="你的問題或指令"
        )
        parser.add_argument(
            "--model", 
            default=self.config.get("default_model"), 
            help=f"指定的模型名稱 (預設: {self.config.get('default_model')})"
        )
        return parser.parse_args()

    def show_header(self, model: str):
        """顯示啟動標頭。"""
        self.console.print(Panel(
            f"[bold blue]Antigravity Local Bridge[/bold blue]\n[dim]正在調用模型: {model}[/dim]", 
            border_style="blue"
        ))

    def show_response_header(self, model: str):
        """顯示回應標頭。"""
        self.console.print(f"\n[bold green]Gemma 4 ({model}):[/bold green]")
