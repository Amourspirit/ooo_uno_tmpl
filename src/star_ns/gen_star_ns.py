# coding: utf-8
from typing import List, Optional
from rel import mod_rel as RelInfo
from .opt import WriteNsEnum
from ..data_manage.data_class.component import Component
from ..data_manage.data_class.star_ns_file import StarNsFile
from ..cfg.config import AppConfig


class GenerateStarNs:
    """Generates import lines in format of from ... import ..."""

    def __init__(self, config: AppConfig, c_data: List[Component], write_ns: WriteNsEnum, rel_ns: Optional[str] = None) -> None:
        """
        Constructor

        Args:
            config (AppConfig): App config
            c_data (List[Component]): List of components to build import lines for.
            rel_ns (str, optional): relative namespace. Defaults to None.
        """
        self._c_data = c_data
        self._config = config
        self._is_rel = rel_ns is not None
        self._rel = rel_ns
        self._write_ns = write_ns
        self._include_const_enum = False
        if self._write_ns == WriteNsEnum.CSS_DYN:
            self._include_const_enum = True
            self._import_frm = self._config.dyn_dir
        elif self._write_ns == WriteNsEnum.STAR_PYI:
            self._import_frm = '.'.join(self._config.pyi_dir)
            # self._import_frm = self._config.pyi_dir[-1]
        else:
            self._import_frm = self._config.uno_obj_dir

    def gen_lines(self) -> List[str]:
        """
        Generates import lines

        Returns:
            List[str]: generated import statement in format of from ... import ...
        """
        def build_lines_rel(c: Component) -> List[str]:
            ns = c.namespace.removeprefix('com.sun.star.')
            in_str = self._import_frm + '.' + ns + '.' + c.name
            ns_im = RelInfo.get_rel_import(in_str=in_str, ns=self._rel)
            results = []
            results.append(
                f"from {ns_im.frm} import {ns_im.imp} as {ns_im.imp}")
            if self._include_const_enum and c.type == 'const':
                results.append(
                    f"from {ns_im.frm} import {ns_im.imp}Enum as {ns_im.imp}Enum")
            return results

        def build_lines(c: Component) -> List[str]:
            ns = c.namespace.removeprefix('com.sun.star.')
            results = []
            results.append(
                f"from {self._import_frm}.{ns}.{c.c_name} import {c.name} as {c.name}")
            if self._include_const_enum and c.type == 'const':
                results.append(
                    f"from {self._import_frm}.{ns}.{c.c_name} import {c.name}Enum as {c.name}Enum")
            return results

        lines: List[str] = []
        skip = ('enum', 'const')
        exclude_imports = set(self._config.css_dyn_ns_import_excludes)
        for comp in self._c_data:
            full_name = comp.namespace + '.' + comp.name
            if full_name in exclude_imports:
                continue
            if self._write_ns == WriteNsEnum.STAR_PYI and comp.type in skip:
                continue
            if self._is_rel:
                lines.extend(build_lines_rel(comp))
            else:
                lines.extend(build_lines(comp))
        return lines

    def get_oth_files(self) -> List[StarNsFile]:
        results = []
        # Now PYI const and Enum write directly into star dir and not star/_pyi dir from Make cmd
        return results
        if self._write_ns != WriteNsEnum.STAR_PYI:
            return results
        all_comp = ('enum', 'const')
        for comp in self._c_data:
            if comp.type in all_comp:
                f = f"{comp.name}.pyi"
                if self._is_rel:
                    lines = self._build_line_all_pyi_rel(comp)
                else:
                    lines = self._build_line_all_pyi(comp)
                results.append(
                    StarNsFile(
                        file_name=f,
                        component=comp,
                        lines=lines
                    )
                )
        return results

    def _build_line_all_pyi_rel(self, c: Component) -> List[str]:
        # from .._pyi.awt.font_slant import *
        ns = c.namespace.removeprefix('com.sun.star.')
        in_str = self._import_frm + '.' + ns + '.' + c.name
        ns_im = RelInfo.get_rel_import(in_str=in_str, ns=self._rel)
        return [f"from {ns_im.frm} import *"]

    def _build_line_all_pyi(self, c: Component) -> List[str]:
        # from .._pyi.awt.font_slant import *
        ns = c.namespace.removeprefix('com.sun.star.')
        return [f"from {self._import_frm}.{ns}.{c.c_name} import *"]
