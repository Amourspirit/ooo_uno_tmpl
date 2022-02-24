# coding: utf-8
from typing import Any
from ...config import AppConfig
from ..parse.parse_module_json import ParseModuleJson

class ComponentControler:
    def __init__(self, config: AppConfig, **kwargs) -> None:
        self._parser = ParseModuleJson(config=config)
        self._write_all = bool(kwargs.get('write_all', False))
        self._update_all = bool(kwargs.get('update_all', False))

    def results(self) -> Any:
        if self._update_all or self._write_all:
            self._parser.update_all_details()
        return None
