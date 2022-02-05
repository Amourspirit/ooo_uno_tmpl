# coding: utf-8
from typing import List, Optional
from data_manage.data_class.component import Component
from config import AppConfig
from rel import mod_rel as RelInfo

class GenerateStarNs:
    """Generates import lines in format of from ... import ..."""
    def __init__(self, config: AppConfig, c_data: List[Component], rel_ns: Optional[str] = None, include_const_enum: Optional[bool] = False) -> None:
        """
        Constructor

        Args:
            config (AppConfig): App config
            c_data (List[Component]): List of componets to build import lines for.
            rel_ns (str, optional): relative namespace. Defaults to None.
        """
        self._c_data = c_data
        self._config = config
        self._is_rel = rel_ns is not None
        self._rel = rel_ns
        self._include_const_enum = include_const_enum

    def gen_lines(self) -> List[str]:
        """
        Generates import lines

        Returns:
            List[str]: generated import statement in format of from ... import ...
        """
        def buld_lines_rel(c: Component) -> List[str]:
            ns = c.namespace.removeprefix('com.sun.star.')
            in_str = self._config.uno_obj_dir + '.' + ns + '.' + c.name
            ns_im = RelInfo.get_rel_import(in_str=in_str, ns=self._rel)
            results = []
            results.append(f"from {ns_im.frm} import {ns_im.imp} as {ns_im.imp}")
            if self._include_const_enum and c.type == 'const':
                results.append(
                    f"from {ns_im.frm} import {ns_im.imp}Enum as {ns_im.imp}Enum")
            return results
        
        def build_lines(c: Component) -> List[str]:
            ns = c.namespace.removeprefix('com.sun.star.')
            results = []
            results.append(f"from {self._config.uno_obj_dir}.{ns}.{c.c_name} import {c.name} as {c.name}")
            if self._include_const_enum and c.type == 'const':
                results.append(
                    f"from {self._config.uno_obj_dir}.{ns}.{c.c_name} import {c.name}Enum as {c.name}Enum")
            return results

        lines: List[str] = []
        for comp in self._c_data:
            if self._is_rel:
                lines.extend(buld_lines_rel(comp))
            else:
                lines.extend(build_lines(comp))
        return lines
