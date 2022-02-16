# coding: utf-8
from typing import Any
from config import AppConfig
from ..parse.parse_module_links import ParseModuleLinks
from ..db_class.init_db import InitDb

class ModuleLinksControler:
    def __init__(self, config: AppConfig, **kwargs) -> None:
        self._parser = ParseModuleLinks(config=config)
        self._write_all = bool(kwargs.get('write_all', False))
        self._update_all = bool(kwargs.get('update_all', False))
        self._count = bool(kwargs.get('count_all', False))

    def results(self) -> Any:
        if self._count:
            return self._parser.get_count_details()
        elif self._write_all:
            self._parser.write_all_details()
        elif self._update_all:
            self._parser.update_all_details()
        return None

    def _init_database(self) -> None:
        db = InitDb(self._conn.connection_str)
        db.init_db()
