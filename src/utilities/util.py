# coding: utf-8
import os
import sys
import __main__
from typing import Union
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


def mkdirp(dest_dir: Union[str, Path]):
    """
    Creates directory and all child directories if needed

    Args:
        dest_dir (Union[str, Path]): path to create directories for.
            Must be dir path only. No checking is done for file names.
    """
    # Python ≥ 3.5
    if isinstance(dest_dir, Path):
        dest_dir.mkdir(parents=True, exist_ok=True)
    else:
        Path(dest_dir).mkdir(parents=True, exist_ok=True)

def _get_virtual_path() -> str:
    spath = os.environ.get("VIRTUAL_ENV", None)
    if spath is not None:
        return spath
    return sys.base_exec_prefix


def get_site_packeges_dir() -> Union[Path, None]:
    """
    Gets the ``site-packages`` directory for current python environment.

    Returns:
        Union[Path, None]: site-packages dir if found; Otherwise, None.
    """
    v_path = _get_virtual_path()
    p_site = Path(v_path, "Lib", "site-packages")
    if p_site.exists() and p_site.is_dir():
        return p_site

    ver = f"{sys.version_info[0]}.{sys.version_info[1]}"
    p_site = Path(v_path, "lib", f"python{ver}", "site-packages")
    if p_site.exists() and p_site.is_dir():
        return p_site
    return None