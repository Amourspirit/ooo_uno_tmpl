# coding: utf-8
from abc import ABC, abstractmethod
from ...dataclass.summary_info import SummaryInfo
from .i_rules_summary_info import IRulesSummaryInfo

class IRuleSummaryInfo(ABC):
    @abstractmethod
    def __init__(self, rules: IRulesSummaryInfo) -> None:
        """Constructor"""

    @abstractmethod
    def get_is_match(self, si: SummaryInfo) -> bool:
        """
        Gets if rule is a match

        Args:
            si (SummaryInfo): Summary Info
        """

    @abstractmethod
    def process_summary_info(self, si: SummaryInfo) -> None:
        """
        Makes changes to si based upon rule

        Args:
            si (SummaryInfo): Summary Info
        """