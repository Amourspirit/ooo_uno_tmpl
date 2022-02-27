# coding: utf-8
from abc import ABC, abstractmethod
from ...dataclass.name_info import NameInfo
from .i_rule_name import IRuleName

class IRulesName(ABC):
    @abstractmethod
    def process_name(self, ni: NameInfo) -> None:
        """
        Changes name info based upon rules match

        Args:
            ni (NameInfo): name info
        """

    @abstractmethod
    def get_rule_instance(self, rule: IRuleName) -> IRuleName:
        """Gets a rule instance"""
