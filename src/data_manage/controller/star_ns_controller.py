# coding: utf-8
import logging
from typing import Any, Union
from ..db_class.qry_component import QryComponent
from ..db_class.db_connect import DbConnect
from ...star_ns.write_star_ns import WriteStarNs, WriteNsEnum
from ...star_ns.star_pyi_init_err import write_star_error
from ...cfg.config import AppConfig


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
        self._write_lo = bool(kwargs.get('write_lo', False))
        self._write_dyn = bool(kwargs.get('write_dyn', False))
        self._write_pyi = bool(kwargs.get('write_pyi', False))
        self._write_pyi_star_init = bool(kwargs.get('write_pyi_star_init', True))
        self._conn = DbConnect(config)

    def results(self) -> Any:
        """
        Processes base upon options passed into constructor

        Returns:
            Any: Any value as a result that may be returned.
        """
        if self._write_lo:
            self._process_star_ns(write_ns=WriteNsEnum.CSS_LO)
        elif self._write_dyn:
            self._process_star_ns(write_ns=WriteNsEnum.CSS_DYN)
        elif self._write_pyi:
            self._process_star_ns(write_ns=WriteNsEnum.STAR_PYI)
        return None

    def _process_star_ns(self, write_ns: WriteNsEnum) -> None:
        qry = QryComponent(self._conn.connection_str)
        ns_components = qry.get_components_group_by_ns()
        writer = WriteStarNs(config=self._config,
                             data=ns_components,
                             rel_import=self._rel_import,
                             write_ns=write_ns,
                             log=self._log)
        writer.write()
        if self._write_pyi_star_init:
            write_star_error()
