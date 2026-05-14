import ollama
import sys
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel

console = Console()

def chat_with_gemma(prompt, model='gemma4:26b'):
    """
    與本地 Gemma 4 模型進行通訊
    """
    try:
        console.print(Panel(f"[bold blue]Antigravity Local Bridge[/bold blue]\n[dim]正在調用模型: {model}[/dim]", border_style="blue"))
        
        # 發送請求給 Ollama
        response = ollama.chat(
            model=model,
            messages=[
                {'role': 'user', 'content': prompt}
            ],
            stream=True
        )

        console.print(f"\n[bold green]Gemma 4 ({model}):[/bold green]")
        
        full_response = ""
        for chunk in response:
            content = chunk['message']['content']
            print(content, end='', flush=True)
            full_response += content
        
        print("\n") # 換行
        return full_response

    except Exception as e:
        console.print(f"[bold red]錯誤:[/bold red] {str(e)}")
        if "not found" in str(e).lower():
            console.print(f"[yellow]提示: 請執行 `ollama pull {model}` 來下載模型。[/yellow]")
        return None

if __name__ == "__main__":
    import argparse
    import json
    import os

    # 嘗試從 settings.json 讀取預設模型
    default_model = "gemma4:26b"
    settings_path = os.path.join(os.path.dirname(__file__), "settings.json")
    if os.path.exists(settings_path):
        try:
            with open(settings_path, 'r') as f:
                settings = json.load(f)
                default_model = settings.get("default_model", default_model)
        except:
            pass

    parser = argparse.ArgumentParser(description="Antigravity Gemma 4 Bridge")
    parser.add_argument("prompt", nargs="?", default="請用繁體中文向我打招呼，並自我介紹。", help="你的問題或指令")
    parser.add_argument("--model", default=default_model, help=f"指定的模型名稱 (預設: {default_model})")
    
    args = parser.parse_args()
    chat_with_gemma(args.prompt, model=args.model)
