# coding: utf-8
from typing import List, Dict
from ...dataclass.area import Area
from ...dataclass.area_info import AreaInfo
from .i_rules_area import IRulesArea
from .i_rule_area import IRuleArea


class RuleAreaBase(IRuleArea):
    """Matches when there is a single parent"""

    def __init__(self, rules: IRulesArea) -> None:
        """constructor"""
        self._rules = rules
      # region Private Methods

    def _get_with_parent_removed(self, first: Area, d_lst: Dict[int, List[Area]],  match_lst: List[Area]) -> None:
        """
        Remove any parent inherits from match_lst. This method does not affect sort order of match_lst

        Args:
            first (Area): First Area
            d_lst (Dict[int, List[Area]]): dict of y1 grouped Area list
            match_lst (List[Area]): List of area that is considered inherits. Out Arg.
        """
        # flatten all others into a single set
        # Any keys in d_lst that are are lower y1 then first.y1 are parent objects. Higher are child object.
        # The lower the y1 value the closer it is to the top if image.
        flat = set()
        for k, v in d_lst.items():
            if k >= first.y1:
                continue
            for area in v:
                flat.add(area.ns.fullns)

        # find any
        remove: List[int] = []
        for i, area in enumerate(match_lst):
            if area.ns.fullns in flat:
                remove.append(i)
        # any entry that is found in flat then remove it.
        if len(remove) > 0:
            remove.sort(reverse=True)
            for i in remove:
                match_lst.pop(i)

    def _list_dict_y1(self, lst: List[Area]) -> Dict[int, List[Area]]:
        """groups lst into area y1"""
        d = {}
        for area in lst:
            if not area.y1 in d:
                d[area.y1] = []
            d[area.y1].append(area)
        return d

    def _list_dict_x1(self, lst: List[Area]) -> Dict[int, List[Area]]:
        """groups lst into area x1"""
        d = {}
        for area in lst:
            if not area.x1 in d:
                d[area.x1] = []
            d[area.x1].append(area)
        return d

    def _get_upper(self, first: Area, d_lst: Dict[int, List[Area]]) -> List[Area]:
        """
        Get a list of all areas that have a y1 value equal then first.y1

        In area map lower y1 values are higer in inheritance.
        """
        lst: List[Area] = []
        for k, v in d_lst.items():
            if k < first.y1:
                lst.extend(v)
        return lst

    def _remove_duplicates_lst(self, lst: List[Area]) -> bool:
        """
        Removes any duplicates base upon namespace.
        Method does not change the sort order of lst

        Args:
            clean_lst (List[Area]): List to remove duplicates from
            filter_lst (List[Area]): List used as filter

        Returns:
            bool: True if any duplicates were found; Otherwise False.
        """
        unique_names: Set[str] = set()
        remove_indexes: List[int] = []
        for i, area in enumerate(lst):
            if area.ns.fullns in unique_names:
                remove_indexes.append(i)
            else:
                unique_names.add(area.ns.fullns)
        if len(remove_indexes) == 0:
            return False
        remove_indexes.sort(reverse=True)
        for i in remove_indexes:
            lst.pop(i)
        return True

    def _get_first_y1(self, ai: AreaInfo, alst: List[Area]) -> Area:
        if not ai.shape:
            # go with first it should always work. However order is scraped form html
            return alst[0]
        first = None
        lst_y = [(a.y1, i) for i, a in enumerate(alst)]
        lst_y.sort(reverse=True)
        for y in lst_y:
            if y[0] < ai.shape.y1:
                first = alst[y[1]]
                break
        if first:
            return first
        return alst[0]

    # endregion Privae Methods

    # region Properties
    @property
    def rules(self) -> IRulesArea:
        """Gets rules value"""
        return self._rules
    # endregion Properties
