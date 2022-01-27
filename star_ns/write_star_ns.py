# coding: utf-8
import os
import logging
import __main__
from pathlib import Path
from .gen_star_ns import GenerateStarNs
from typing import Dict, Optional, Union
from data_manage.data_class.component import Component
from config import AppConfig

class WriteStarNs:
    def __init__(self, config: AppConfig, data: Dict[str, Component], log: Optional[logging.Logger] = None) -> None:
        self._data = data
        self._config = config
        self._log = log
        root_dir = os.environ.get('project_root', None)
        if root_dir:
            self._root_dir = Path(root_dir)
        else:
            self._root_dir = Path(__main__.__file__).parent
        self._write_root = Path(self._root_dir, self._config.builld_dir, *self._config.com_sun_star)
    
    def _ensure_init_py(self) -> None:
        # ensure build/com/sun/star/__init__.py exist
        p = Path(self._config.builld_dir, *self._config.com_sun_star)
        if not p.is_absolute():
            p = self._root_dir.joinpath(p)
        self._mkdirp(p)
        init_file = Path(p, '__init__.py')
        try:
            init_file.touch(exist_ok=False)
        except FileExistsError:
            # file already exist so just ignore
            pass

    def write(self) -> None:
        # self._ensure_init_py()
        header_lines = ['# coding: utf-8']
        with open(Path(self._root_dir, self._config.inc_lic), 'r') as f_lic:
            header_lines.extend(f_lic.read().splitlines())
        
        for ns, c_data in self._data.items():
            lines = [ln for ln in header_lines]
            ns_path = ns.removeprefix('com.sun.star.')
            write_path = self._write_root.joinpath(Path(*ns_path.split('.')))
            self._mkdirp(dest_dir=write_path)
            write_path = write_path.joinpath('__init__.py')
            gen_star = GenerateStarNs(config=self._config, c_data=c_data)
            lines.extend(gen_star.gen_lines())
            lines.append('')
            text = "\n".join(lines)
            with open(write_path, 'w') as f:
                f.write(text)
            if self._log:
                rel_path = write_path.relative_to(self._root_dir)
                self._log.info('Wrote file %s', str(rel_path))
    
    def _mkdirp(self, dest_dir: Union[str, Path]):
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
