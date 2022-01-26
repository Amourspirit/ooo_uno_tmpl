# coding: utf-8
import os
from pathlib import Path
from .gen_star_ns import GenerateStarNs
from typing import Dict, Optional
from data_manage.data_class.component import Component
from config import AppConfig
import logging

class WriteStarNs:
    def __init__(self, config: AppConfig, data: Dict[str, Component], log: Optional[logging.Logger] = None) -> None:
        self._data = data
        self._config = config
        self._log = log
        root_dir = os.environ.get('project_root', None)
        if root_dir:
            self._root_dir = Path(root_dir)
        else:
            self._root_dir = Path(__file__).parent.parent
        self._write_root = self._root_dir / self._config.builld_dir
    

    def write(self) -> None:
        for ns, c_data in self._data.items():
            write_path = self._write_root.joinpath(Path(*ns.split('.'))).joinpath('__init__.py')
            gen_star = GenerateStarNs(config=self._config, c_data=c_data)
            text = gen_star.gen()
            with open(write_path, 'w') as f:
                f.write(text)
            if self._log:
                rel_path = write_path.relative_to(self._root_dir)
                self._log.info('Wrote file %s', str(rel_path))