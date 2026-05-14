# src/config_manager.py

import json
from pathlib import Path
from typing import Dict, Any

class ConfigManager:
    """
    負責管理專案的配置讀取、預設值以及配置文件的載入。
    """
    def __init__(self, config_path: str = "settings.json"):
        self.config_path = Path(config_path)
        self.settings: Dict[str, Any] = {}
        self._defaults = self._get_defaults()

    def _get_defaults(self) -> Dict[str, Any]:
        """定義所有配置的預設值。"""
        return {
            "default_model": "gemma4:26b",
            "bridge_name": "Antigravity Local Bridge",
            "log_level": "INFO"
        }

    def load_config(self) -> bool:
        """從 settings.json 載入配置。"""
        # 先套用預設值
        self.settings.update(self._defaults)
        
        if not self.config_path.exists():
            return False
        
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                loaded_data = json.load(f)
                self.settings.update(loaded_data)
                return True
        except Exception:
            return False

    def get(self, key: str) -> Any:
        return self.settings.get(key, self._defaults.get(key))

    def get_all(self) -> Dict[str, Any]:
        return self.settings
