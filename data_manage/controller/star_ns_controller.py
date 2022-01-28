# coding: utf-8
import logging
from typing import Any, Union
from config import AppConfig
from star_ns.write_star_ns import WriteStarNs
from ..db_class.qry_component import QryComponent
from ..db_class.db_connect import DbConnect


class StarNsControler:
    """Star Namespace Controller"""
    def __init__(self, config: AppConfig, **kwargs) -> None:
        """
        Constructor

        Args:
            config (AppConfig): App Config
        
        Keyword Arguments:
            logger (Logger, optional): optional logger
            write_star_ns (bool, optional): If ``True`` then all com.sun.star ... imports will be written
        """
        self._config = config
        self._rel_import = bool(kwargs.get('rel_import', True))
        self._log: Union[logging.Logger, None] = kwargs.get('logger', None)
        self._write_star_ns = bool(kwargs.get('write_star_ns', False))
        self._conn = DbConnect(config)

    def results(self) -> Any:
        """
        Processes base upon options passed into constructor

        Returns:
            Any: Any value as a result that may be returned.
        """
        if self._write_star_ns:
            self._process_star_ns()
        return None

    def _process_star_ns(self) -> None:
        qry = QryComponent(self._conn.connection_str)
        ns_components = qry.get_components_group_by_ns()
        writer = WriteStarNs(config=self._config,
                             data=ns_components,rel_import=self._rel_import, log=self._log)
        writer.write()