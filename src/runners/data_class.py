# coding: utf-8
import logging
from dataclasses import dataclass
from pathlib import Path
from typing import Optional
from ..cfg.config import AppConfig
from ..model.shared.ooo_class import OooClass
# region Data Class


@dataclass
class WriteInfo:
    file: str
    py_file: str
    scratch_path: Path
    ext: str = '.py'
    model: Optional[OooClass] = None


@dataclass
class CompileLinkArgs:
    config: AppConfig
    log: logging.Logger
    write_json: bool = True
    write_template: bool = True
    path: Optional[str] = None
    allow_known_json = True
    use_sub_process: bool = False
    out_dir: Optional[str] = None
# endregion Data Class
