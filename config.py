import json
from dataclasses import dataclass
from pathlib import Path
@dataclass
class AppConfig:
    uno_base_dir: str
    """Base Directory for Uno such as uno_obj"""
    module_links_file: str
    """Json file name for module links such as module_links.json"""
    cache_dir: str
    """The cache directory to use. This is generally used in creating a cache directory is system temp dir."""
    cache_duration: float
    """
    The amount of time in seconds to keep files in cache.

    Note:
        Files cached in system tmp folder will be cleared upon reboot.
    """
    pixel_inherit: int
    """
    Index color of component map images for inherits.
    """
    pixel_noinherit: int
    """
    Index color of component map images for NON-inherits.
    """

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