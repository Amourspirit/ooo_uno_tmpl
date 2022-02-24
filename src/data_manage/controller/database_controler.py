# coding: utf-8
from ...config import AppConfig
from ..parse.parse_module_links import ParseModuleLinks
from ..db_class.init_db import InitDb
from ..db_class.db_connect import DbConnect

class DatabaseControler:
    def __init__(self, config: AppConfig, **kwargs) -> None:
        self._parser = ParseModuleLinks(config=config)
        self._init_db = bool(kwargs.get('init_db', False))
        self._conn = DbConnect(config)

    def results(self) -> None:
        if self._init_db:
            self._init_database()

    def _init_database(self) -> None:
        db = InitDb(self._conn.connection_str)
        db.init_db()
