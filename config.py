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
    uno_obj_dir: str
    """Uno obj dir such as uno_obj. This is the directory that templates and json data file are written to."""
    builld_dir: str
    """Output build dir such as scratch"""
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
    base_const: str
    """
    module path to const such as ``ooo_uno.base.const``
    """
    base_const_int: str
    """
    Base class for constants of int type such as ``ConstIntBase``
    """
    base_const_int_flags: str
    """
    Base class for constants of int flags type such as ``ConstIntFlagsBase``
    """
    env: str
    """
    module path to oenv suca as ``ooo_uno.oenv``
    """
    template_struct_ext: str
    """Extension for struct files such as .tmpl"""
    template_const_ext: str
    """Extension for const files such as .tmpl"""
    template_interface_ext: str
    """Extension for interface files such as .tmpl"""
    template_singleton_ext: str
    """Extension for singleton files such as .tmpl"""
    template_enum_ext: str
    """Extension for enum files such as .tmpl"""
    template_exception_ext: str
    """Extension for exception files such as .tppi"""
    template_typedef_ext: str
    """Extension for typedef files such as .tppi"""
    template_service_ext: str
    """Extension for service files such as .tppi"""

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