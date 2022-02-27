# coding: utf-8
from typing import List, Dict
from ...dataclass.area import Area
from ...dataclass.area_info import AreaInfo
from .i_rules_area import IRulesArea
from .rule_area_base import RuleAreaBase


class RuleAreaVertical(RuleAreaBase):
    """Matches when there is a vertical parent"""

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
        # vertical matches are when all areas have the sam x1 value:
        # see: https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1ucb_1_1ContentResultSet.html
        if len(alst) < 2:
            return False
        first = self._get_first_y1(ai=ai, alst=alst)
        if ai.shape:
            # vertical are ofset left or right on x1, Usually right
            # more likley this is a single
            if first.x1 == ai.shape.x1:
                return False
        is_vert = True
        d_lst: Dict[int, List[Area]] = self._list_dict_x1(
            lst=alst)  # grouped by y1
        for area in d_lst[first.x1]:
            if area.x1 != first.x1:
                is_vert = False
                break

        return is_vert

    def get_area(self, ai: AreaInfo, alst: List[Area]) -> List[Area]:
        """
        Gets filtered Area list

        Args:
            alst (List[Area]): Areas to filter

         Returns:
            List[Area]: Filtered Area List
        """
        # remove any duplicates and return list.
        # is it unlikely there would ever be duplicates, but just in case.
        first = self._get_first_y1(ai=ai, alst=alst)
        d_lst: Dict[int, List[Area]] = self._list_dict_x1(
            lst=alst)  # grouped by y1
        # filtering upper by shape or first is a bug fix.
        # in cases such as https://tinyurl.com/yaqul3gs
        # some of child classes have the exact same y1 as the parrent classes
        if ai.shape:
            upper: List[Area] = [
                a for a in d_lst[first.x1] if a.y1 < ai.shape.y1]
        else:
            upper: List[Area] = [
                a for a in d_lst[first.x1] if a.y1 <= first.y1]
        sorted_u = sorted(upper, key=lambda a: a.y1)
        if self.rules.remove_parent_inherited:
            self._remove_duplicates_lst(sorted_u)
        return sorted_u
