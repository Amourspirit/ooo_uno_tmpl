# coding: utf-8
from typing import TYPE_CHECKING
from abc import ABC, abstractmethod
if TYPE_CHECKING:
    from ...dataclass.summary_info import SummaryInfo
    from .i_rule_summary_info import IRuleSummaryInfo

class IRulesSummaryInfo(ABC):
    @abstractmethod
    def process_summary_info(self, si: 'SummaryInfo') -> None:
        """Process Summary Info making changes to si by rules"""

    @abstractmethod
    def get_rule_instance(self, rule: 'IRuleSummaryInfo') -> 'IRuleSummaryInfo':
        """Gets a rule instance"""
