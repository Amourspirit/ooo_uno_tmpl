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
    """Writes imports for all 'build/uno_obj' (paths set in config.json) files into  css... __init__.py files."""
    def __init__(self, config: AppConfig, data: Dict[str, Component], rel_import:bool, log: Optional[logging.Logger] = None) -> None:
        """
        Constructor

        Args:
            config (AppConfig): App config
            data (Dict[str, Component]): Dictionry of namespace, component where components are grouped by namespace.
            rel_import (bool): If ``True`` imports are created as relative.
            log (logging.Logger, optional): Logger. Defaults to None.
        """
        self._data = data
        self._config = config
        self._log = log
        root_dir = os.environ.get('project_root', None)
        if root_dir:
            self._root_dir = Path(root_dir)
        else:
            self._root_dir = Path(__main__.__file__).parent
        self._write_root = Path(self._root_dir, self._config.builld_dir, *self._config.com_sun_star_lo)
        self._rel_import = rel_import
    
    def _ensure_init_py(self) -> None:
        # ensure build/com/sun/star/__init__.py exist
        p = Path(self._config.builld_dir)
        for name in self._config.com_sun_star_lo:
            p = Path(p, name)
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
        """
        Writes imports for all 'build/uno_obj' (paths set in config.json) files into  css... __init__.py files. 
        """
        self._ensure_init_py()
        header_lines = ['# coding: utf-8']
        with open(Path(self._root_dir, self._config.inc_lic), 'r') as f_lic:
            header_lines.extend(f_lic.read().splitlines())
        
        for ns, c_data in self._data.items():
            lines = [ln for ln in header_lines]
            ns_path = ns.removeprefix('com.sun.star.')
            ns_parts = ns_path.split('.')
            if self._rel_import:
                rel_ns_parts = [f_name for f_name in self._config.com_sun_star_lo]
                rel_ns_parts.extend(ns_parts)
                rel_ns = '.'.join(rel_ns_parts)
            else:
                rel_ns = None
            write_path = self._write_root.joinpath(Path(*ns_parts))
            self._mkdirp(dest_dir=write_path)
            write_path = write_path.joinpath('__init__.py')
            gen_star = GenerateStarNs(
                config=self._config, c_data=c_data, rel_ns=rel_ns)
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
