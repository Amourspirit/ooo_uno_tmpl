# coding: utf-8
import logging
from pathlib import Path
from typing import Dict, List, Optional, Union
from ..data_manage.data_class.component import Component
from .gen_star_ns import GenerateStarNs
from .opt import WriteNsEnum as WriteNsEnum
from ..cfg.config import AppConfig
from ..utilities import util


class WriteStarNs:
    """Writes imports for all 'ooobuild/lo' (paths set in config.json) files into  css... __init__.py files."""

    def __init__(self, config: AppConfig, data: Dict[str, List[Component]], rel_import: bool, write_ns: WriteNsEnum, log: Optional[logging.Logger] = None) -> None:
        """
        Constructor

        Args:
            config (AppConfig): App config
            data (Dict[str, Component]): Dictionary of namespace, component where components are grouped by namespace.
            rel_import (bool): If ``True`` imports are created as relative.
            log (logging.Logger, optional): Logger. Defaults to None.
        """
        self._data = data
        self._config = config
        self._log = log
        self._dyn_ns_import_check = self._config.css_dyn_ns_import_check
        self._root_dir = Path(util.get_root())
        self._write_ns = write_ns
        if self._write_ns == WriteNsEnum.CSS_LO:
            self._write_root = Path(
                self._root_dir, self._config.build_dir, *self._config.com_sun_star_lo)
        elif self._write_ns == WriteNsEnum.CSS_DYN:
            self._write_root = Path(
                self._root_dir, self._config.build_dir, *self._config.com_sun_star_dyn)
        elif self._write_ns == WriteNsEnum.STAR_PYI:
            self._write_root = Path(
                self._root_dir, self._config.build_dir, *self._config.com_sun_star_pyi)
        else:
            raise ValueError(
                "WriteStarNs.__init__() invalid option for write_ns")
        self._rel_import = rel_import

    def _ensure_init_py(self) -> None:
        # ensure build/com/sun/star/__init__.py exist
        p = Path(self._config.build_dir)
        if self._write_ns == WriteNsEnum.CSS_LO:
            names = self._config.com_sun_star_lo
        else:
            names = self._config.com_sun_star_dyn

        if self._write_ns == WriteNsEnum.STAR_PYI:
            init_file = '__init__.pyi'
        else:
            init_file = '__init__.py'

        for name in names:
            p = Path(p, name)
            if not p.is_absolute():
                p = self._root_dir.joinpath(p)
            util.mkdirp(p)
            init_file = Path(p, init_file)
            try:
                init_file.touch(exist_ok=False)
            except FileExistsError:
                # file already exist so just ignore
                pass

    def write(self) -> None:
        """
        Writes imports for all 'ooobuild/lo' (paths set in config.json) files into  css... __init__.py files. 
        """
        self._ensure_init_py()
        header_lines = ['# coding: utf-8']
        if self._write_ns == WriteNsEnum.STAR_PYI:
            init_file = '__init__.pyi'
        else:
            init_file = '__init__.py'

        with open(Path(self._root_dir, self._config.inc_lic), 'r') as f_lic:
            header_lines.extend(f_lic.read().splitlines())
        
        if self._write_ns == WriteNsEnum.CSS_DYN and self._dyn_ns_import_check:
            header_lines.append('\n')
            header_lines.append('from contextlib import suppress')
        
        if self._write_ns == WriteNsEnum.CSS_DYN and self._config.css_dyn_ns_import_warn:
            self._set_import_warning(header_lines)
        
        if self._write_ns == WriteNsEnum.CSS_LO and self._config.css_lo_ns_import_warn:
            self._set_import_warning(header_lines, old_ns="csslo", new_ns="lo")

        for ns, c_data in self._data.items():
            self._write_components(ns, c_data, header_lines, init_file)

    def _write_components(self, ns: str, c_data: List[Component], header_lines: List[str], init_file: str) -> None:
        def write_ns_file(file: Path, lns: List[str]) -> None:
            new_lns = [s for s in lns]
            if self._write_ns == WriteNsEnum.CSS_DYN and self._dyn_ns_import_check:
                text = "\n".join(header_lines)
                text += '\n'
                text += self._get_import_check_text(new_lns)
            else:
                new_lns.append('')
                all_lines = header_lines + new_lns
                text = "\n".join(all_lines)
            with open(file, 'w') as f:
                f.write(text)
            if self._log:
                rel_path = file.relative_to(self._root_dir)
                self._log.info('Wrote file %s', str(rel_path))

        lines = []
        ns_path = ns.removeprefix('com.sun.star.')
        ns_parts = ns_path.split('.')
        if self._rel_import:
            if self._write_ns == WriteNsEnum.CSS_LO:
                rel_ns_parts = [
                    f_name for f_name in self._config.com_sun_star_lo]
            elif self._write_ns == WriteNsEnum.STAR_PYI:
                # pyi enums need to be written into a separate module that matches the name of the enu.
                rel_ns_parts = [
                    f_name for f_name in self._config.com_sun_star_pyi]
            else:
                rel_ns_parts = [
                    f_name for f_name in self._config.com_sun_star_dyn]
            rel_ns_parts.extend(ns_parts)
            rel_ns = '.'.join(rel_ns_parts)
        else:
            rel_ns = None
        write_path = self._write_root.joinpath(Path(*ns_parts))
        util.mkdirp(dest_dir=write_path)
        write_file = write_path.joinpath(init_file)

        gen_star = GenerateStarNs(
            config=self._config, c_data=c_data,
            write_ns=self._write_ns,  rel_ns=rel_ns)

        lines.extend(gen_star.gen_lines())
        write_ns_file(write_file, lines)

        for finfo in gen_star.get_oth_files():
            write_file = write_path / finfo.file_name
            write_ns_file(write_file, lns=finfo.lines)
        
    
    def _write_enums(self) -> None:
        pass

    def _get_import_check_text(self, lines: List[str]) -> str:
        s = '\n'
        errors = ", ".join(self._config.css_dyn_ns_import_exceptions)
        suppress_ln = f"with suppress({errors}):\n"
        for line in lines:
            s += suppress_ln
            s += f"    {line}\n"
        return s

    def _set_import_warning(self, header: List[str], old_ns: str = "cssdyn", new_ns: str = "dyn") -> None:
        header.append('import warnings')
        header.append("warnings.filterwarnings('module')")
        header.append(f"warnings.warn('The {old_ns} namespace is deprecated. Use {new_ns} instead.', DeprecationWarning, stacklevel=2)")
