# coding: utf-8
from .i_rule_name import IRuleName
from .i_rules_name import IRulesName
from ...dataclass.name_info import NameInfo
from ...common.util import Util


class RuleNameNoGenerics(IRuleName):
    """Cleans name to remove any Generic < U, T > like strings"""

    def __init__(self, rules: IRulesName) -> None:
        self._rules = rules

    def get_is_match(self, ni: NameInfo) -> bool:
        """Gets if name is a match"""
        parts = ni.name.split(sep='<', maxsplit=1)
        if len(parts) == 1:
            return False
        return True

    def process_name(self, ni: NameInfo) -> None:
        """
        Cleans ni.name to remove any Generic < U, T > like strings

        Args:
            ni (NameInfo): name info
        """
        ni.name = Util.get_clean_classname(ni.name)
