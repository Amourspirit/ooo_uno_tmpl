# coding: utf-8
from typing import List, Optional
from data_manage.data_class.component import Component
from config import AppConfig
from parser import mod_rel as RelInfo

class GenerateStarNs:
    """Generates import lines in format of from ... import ..."""
    def __init__(self, config: AppConfig, c_data: List[Component], rel_ns: Optional[str] = None) -> None:
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

    def gen_lines(self) -> List[str]:
        """
        Generates import lines

        Returns:
            List[str]: generated import statement in format of from ... import ...
        """
        def buld_line_rel(c: Component) -> str:
            ns = c.namespace.removeprefix('com.sun.star.')
            in_str = self._config.uno_obj_dir + '.' + ns + '.' + c.name
            ns_im = RelInfo.get_rel_import(in_str=in_str, ns=self._rel)
            # ns = c.namespace.removeprefix('com.sun.star.')
            return f"from {ns_im.frm} import {ns_im.imp}"
        
        def build_line(c: Component) -> str:
            ns = c.namespace.removeprefix('com.sun.star.')
            return f"from {self._config.uno_obj_dir}.{ns}.{c.c_name} import {c.name}"
        lines: List[str] = []
        for comp in self._c_data:
            if self._is_rel:
                lines.append(buld_line_rel(comp))
            else:
                lines.append(build_line(comp))
        return lines
