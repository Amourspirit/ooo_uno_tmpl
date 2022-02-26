# coding: utf-8
from abc import ABC, abstractmethod, abstractproperty
from typing import List
from ...dataclass.area import Area
from ...dataclass.area_info import AreaInfo


class IRulesArea(ABC):

    @abstractmethod
    def get_area(self,  ai: AreaInfo, alst: List[Area]) -> List[Area]:
        """
        Gets filtered Area list

        Args:
            alst (List[Area]): Areas to filter

         Returns:
            List[Area]: Filtered Area List
        """

    @abstractmethod
    def __len__(self) -> int:
        """Gets the length of rules"""

    @abstractproperty
    def remove_parent_inherited(self) -> bool:
        """Removes Parent Inherite Property"""
