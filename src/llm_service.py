import ollama
import io
import sys
from typing import Generator, Dict, Any, Optional

# 確保輸出支援 UTF-8
if sys.stdout.encoding != 'utf-8':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

class OllamaBridge:
    """
    負責與本地 Ollama 服務進行通訊的橋接類別。
    封裝了 API 調用、串流處理與錯誤捕捉邏輯。
    """
    def __init__(self):
        pass

    def chat_stream(self, model: str, prompt: str) -> Optional[str]:
        """
        發送 Prompt 至指定模型並以串流方式獲取回應。
        
        Args:
            model: 模型名稱 (如 'gemma4:26b')
            prompt: 用戶輸入的指令
        Returns:
            完整的模型回應字串，若發生錯誤則回傳 None
        """
        try:
            # 發送請求給 Ollama
            response_stream = ollama.chat(
                model=model,
                messages=[
                    {'role': 'user', 'content': prompt}
                ],
                stream=True
            )

            full_response = ""
            
            # 處理串流輸出
            for chunk in response_stream:
                content = chunk['message']['content']
                # 直接輸出至終端機以便即時檢視
                print(content, end='', flush=True)
                full_response += content
            
            print("\n") # 結束換行
            return full_response

        except ollama.ResponseError as e:
            error_message = str(e)
            if "not found" in error_message.lower():
                print(f"\n[錯誤] 找不到模型 '{model}'。請執行 `ollama pull {model}`。")
            else:
                print(f"\n[錯誤] Ollama API 回傳錯誤: {error_message}")
            return None
        
        except Exception as e:
            print(f"\n[錯誤] 發生非預期錯誤: {type(e).__name__}: {str(e)}")
            return None
