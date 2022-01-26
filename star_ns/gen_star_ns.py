# coding: utf-8
from typing import List
from data_manage.data_class.component import Component
from config import AppConfig


class GenerateStarNs:
    def __init__(self, config: AppConfig, c_data: List[Component]) -> None:
        self._c_data = c_data
        self._config = config

    def gen(self) -> str:
        def build_line(c: Component) -> str:
            ns = c.namespace.removeprefix('com.sun.star.')
            return f"from {self._config.uno_obj_dir}.{ns}.{c.c_name} import {c.name}"
        lines: List[str] = ['# coding: utf-8']
        for comp in self._c_data:
            lines.append(build_line(comp))
        lines.append('')
        return "\n".join(lines)
