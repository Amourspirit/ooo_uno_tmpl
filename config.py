import json
from dataclasses import dataclass
from pathlib import Path
@dataclass
class AppConfig:
    uno_base_dir: str
    """Base Directory for Uno such as uno_obj"""
    module_links_file: str
    """Json file name for module links such as module_links.json"""

def read_config(config_file: str) -> AppConfig:
    """
    Gets config for given config file

    Args:
        config_file (str): Config file to load

    Returns:
        AppConfig: Configuration object
    """
    with open(config_file, 'r') as file:
        data = json.load(file)
        return AppConfig(**data)

def read_config_default() -> AppConfig:
    """
    Loads default configuration ``config.json``

    Returns:
        AppConfig: Configuration Object
    """
    root = Path(__file__).parent
    config_file = Path(root, 'config.json')
    return read_config(str(config_file))