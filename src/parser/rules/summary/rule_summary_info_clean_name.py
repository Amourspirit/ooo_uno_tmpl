# coding: utf-8
from abc import ABC, abstractmethod
from ...dataclass.summary_info import SummaryInfo
from .i_rule_summary_info import IRuleSummaryInfo
from .i_rules_summary_info import IRulesSummaryInfo
from ...common.util import Util


class RuleSummaryInfoCleanName(IRuleSummaryInfo):
    """Cleans name to remove any non class name chars"""

    def __init__(self, rules: IRulesSummaryInfo) -> None:
        self._rules = rules

    def get_is_match(self, si: SummaryInfo) -> bool:
        name = si.name
        clean_name = Util.get_clean_classname(name)
        return name != clean_name

    def process_summary_info(self, si: SummaryInfo) -> None:
        """
        Cleans si.name to remove any non class name chars

        Args:
            si (SummaryInfo): Summary Info
        """
        si.name = Util.get_clean_classname(si.name)
