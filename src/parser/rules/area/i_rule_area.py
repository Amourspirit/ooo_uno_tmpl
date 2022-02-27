# coding: utf-8
from abc import ABC, abstractmethod
from typing import List
from ...dataclass.area import Area
from ...dataclass.area_info import AreaInfo
from .i_rules_area import IRulesArea


class IRuleArea(ABC):

    @abstractmethod
    def __init__(self, rules: IRulesArea) -> None:
        """constructor"""

    @abstractmethod
    def get_is_match(self, ai: AreaInfo, alst: List[Area]) -> bool:
        """
        Gets if rule is a match

        Args:
            alst (List[Area]): Areas to match
        """

    @abstractmethod
    def get_area(self, ai: AreaInfo,  alst: List[Area]) -> List[Area]:
        """
        Gets filtered Area list

        Args:
            alst (List[Area]): Areas to filter

         Returns:
            List[Area]: Filtered Area List
        """
