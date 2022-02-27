# coding: utf-8
from ...cfg.config import AppConfig, read_config_default

# region config
APP_CONFIG: AppConfig = None

def _load_config():
    global APP_CONFIG
    APP_CONFIG = read_config_default()

_load_config()
# endregion config
