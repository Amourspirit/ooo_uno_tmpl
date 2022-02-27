# coding: utf-8
from typing import List, Dict
from ...dataclass.area import Area
from ...dataclass.area_info import AreaInfo
from .i_rules_area import IRulesArea
from .rule_area_base import RuleAreaBase


class RuleAreaMulti(RuleAreaBase):
    """Matches when there is a multiple adjacent parents"""

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
        first = self._get_first_y1(ai=ai, alst=alst)
        match_lst = d_lst[first.y1]
        if len(match_lst) <= 1:
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
        first = self._get_first_y1(ai=ai, alst=alst)
        d_lst: Dict[int, List[Area]] = self._list_dict_y1(
            lst=alst)  # grouped by y1
        # extract group I want
        match_lst: List[Area] = [
            area for area in d_lst[first.y1]]  # list of y1 matches
        if len(match_lst) == 0:
            return match_lst
        del d_lst[first.y1]
        if self.rules.remove_parent_inherited:
            self._get_with_parent_removed(
                first=first, d_lst=d_lst, match_lst=match_lst)

        return match_lst
    # endregion IRuleArea Methods
