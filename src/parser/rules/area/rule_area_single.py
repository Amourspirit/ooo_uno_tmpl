# coding: utf-8
from typing import List
from ...dataclass.area import Area
from ...dataclass.area_info import AreaInfo
from .i_rules_area import IRulesArea
from .rule_area_base import RuleAreaBase


class RuleAreaSingle(RuleAreaBase):
    """Matches when there is a single parent"""

    def __init__(self, rules: IRulesArea) -> None:
        """constructor"""
        super().__init__(rules=rules)

    # region IRuleArea Methods
    def get_is_match(self, ai: AreaInfo, alst: List[Area]) -> bool:
        """
        Gets if rule is a match

        Args:
            alst (List[Area]): Areas to match
        """
        if len(alst) == 0:
            return False
        d_lst = self._list_dict_y1(lst=alst)
        match_lst = d_lst[alst[0].y1]
        if len(match_lst) != 1:
            return False
        if ai.shape:
            m = match_lst[0]
            if m.x1 != ai.shape.x1:
                return False
        return True

    def get_area(self, ai: AreaInfo, alst: List[Area]) -> List[Area]:
        """
        Gets filtered Area list

        Args:
            alst (List[Area]): Areas to filter

         Returns:
            List[Area]: Filtered Area List
        """
        d_lst = self._list_dict_y1(lst=alst)
        return d_lst[alst[0].y1]
    # endregion IRuleArea Methods
