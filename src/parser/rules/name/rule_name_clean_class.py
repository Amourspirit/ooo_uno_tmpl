# coding: utf-8
from ...dataclass.name_info import NameInfo
from .i_rules_name import IRulesName
from ...common.util import Util

class RuleNameCleanClass(IRulesName):
    """Cleans name to remove any non class name chars"""

    def __init__(self, rules: IRulesName) -> None:
        self._rules = rules

    def get_is_match(self, ni: NameInfo) -> bool:
        """Gets if name is a match"""
        clean_name = Util.get_clean_classname(ni.name)
        return ni.name != clean_name

    def process_name(self, ni: NameInfo) -> None:
        """
        Cleans ni.name to remove any non class name chars

        Args:
            ni (NameInfo): name info
        """
        ni.name = Util.get_clean_classname(ni.name)
