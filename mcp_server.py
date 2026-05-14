import ollama
import os
import json
from fastmcp import FastMCP

# 初始化 FastMCP Server
mcp = FastMCP("Gemma4 Local Bridge")

# 讀取設定
def get_default_model():
    default_model = "gemma4:26b"
    settings_path = os.path.join(os.path.dirname(__file__), "settings.json")
    if os.path.exists(settings_path):
        try:
            with open(settings_path, 'r', encoding='utf-8') as f:
                settings = json.load(f)
                return settings.get("default_model", default_model)
        except:
            pass
    return default_model

@mcp.tool()
def query_gemma4(prompt: str, model: str = None) -> str:
    """
    使用本地運行的 Gemma 4 模型進行查詢。
    
    Args:
        prompt: 你想要問模型的問題或指令。
        model: 選用的模型名稱 (例如 'gemma4:26b')。如果未提供，將使用預設模型。
    """
    target_model = model if model else get_default_model()
    
    try:
        response = ollama.chat(
            model=target_model,
            messages=[{'role': 'user', 'content': prompt}]
        )
        return response['message']['content']
    except Exception as e:
        return f"錯誤: 調用本地模型時發生問題 - {str(e)}"

@mcp.resource("settings://config")
def get_config() -> str:
    """獲取目前的橋接器設定"""
    settings_path = os.path.join(os.path.dirname(__file__), "settings.json")
    if os.path.exists(settings_path):
        with open(settings_path, 'r', encoding='utf-8') as f:
            return f.read()
    return "{}"

if __name__ == "__main__":
    mcp.run()
