# coding: utf-8
import logging
from typing import List
from ..dataclass.ns import Ns
from ..dataclass.area import Area
from ..dataclass.area_info import AreaInfo
from ..rules.area.i_rules_area import IRulesArea
from ..common import log_load
# region Logger
logger: logging.Logger = log_load.get_logger()
# endregion Logger


class AreaFilter:
    def __init__(self, alst: List[Area], area_info: AreaInfo, rules_engine: IRulesArea) -> None:
        self._lst = alst
        self._ai = area_info
        self._rules_engine: IRulesArea = rules_engine
        self._first: Area = None if len(self._lst) == 0 else self._lst[0]
        # self._inherited = self._get_inherited()
        self._inherited = self._get_from_rules()

    def _get_from_rules(self) -> List[Area]:
        if self._ai.is_inherited is False:
            return []
        if len(self._rules_engine) == 0:
            msg = f"{self.__class__.__name__}._get_from_rules() Rules must not contain rules to process."
            logger.error(msg)
            raise Exception(msg)

        # rules_engine determines sorting
        area_lst = self._rules_engine.get_area(ai=self._ai, alst=self._lst)
        return area_lst or []

    def get_as_ns(self) -> List[Ns]:
        """
        Gets the current inherited list of Area as a list of ``Ns``

        Sorting if any has been determined by IRulesArea

        Returns:
            List[Ns]: List if inherited Namespaces
        """
        # no sorting should be done here.
        return [el.ns for el in self._inherited]

    @property
    def inherited(self) -> List[Area]:
        """Gets inherited value"""
        return self._ai.is_inherited

    @property
    def area_info(self) -> AreaInfo:
        """Gets the area info containing inherited and cordinates info."""
        return self._ai
