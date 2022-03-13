# coding: utf-8
import os
import sys
import __main__
from pathlib import Path
from ..cfg import config

_APP_ROOT = None
_OS_PATH_SET = False
_APP_CFG = None

RESERVER_WORDS = {
    'and', 'as', 'assert', 'break', 'class',
    'continue', 'def', 'del', 'elif', 'else',
    'except', 'False', 'finally', 'for',
    'from', 'global', 'if', 'import', 'in',
    'is', 'lambda', 'None', 'nonlocal',
    'not', 'or', 'pass', 'raise', 'return',
    'True', 'try', 'while', 'with', 'yield'
}

def get_root() -> str:
    """
    Gets Application Root Path

    Returns:
        str: App root as string.
    """
    global _APP_ROOT
    if _APP_ROOT is None:
        _APP_ROOT = os.environ.get(
            'project_root', str(Path(__main__.__file__).parent))
    return _APP_ROOT

def set_os_root_path() -> None:
    """
    Ensures application root dir is in sys.path
    """
    global _OS_PATH_SET
    if _OS_PATH_SET is False:
        _app_root = get_root()
        if not _app_root in sys.path:
            sys.path.insert(0, _app_root)
    _OS_PATH_SET = True

def get_app_cfg() -> config.AppConfig:
    """
    Get App Config. config is cached
    """
    global _APP_CFG
    if _APP_CFG is None:
        _APP_CFG = config.read_config_default()
    return _APP_CFG