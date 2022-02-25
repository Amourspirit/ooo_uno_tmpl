# coding: utf-8
import os
from pathlib import Path
from ...cfg.config import AppConfig


class DbConnect:
    def __init__(self, config: AppConfig) -> None:
        self._app_config = config
        root_dir = os.environ.get('project_root', None)
        if root_dir:
            self._root_dir = Path(root_dir)
        else:
            self._root_dir = Path(__file__).parent.parent
        self._conn = str(self._root_dir /
                         config.resource_dir / config.db_mod_info)

    @property
    def connection_str(self) -> str:
        """Gets connection_str value"""
        return self._conn

    @property
    def root_dir(self) -> Path:
        """Gets root_dir value"""
        return self._root_dir
