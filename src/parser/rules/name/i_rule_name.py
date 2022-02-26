# coding: utf-8
from abc import ABC, abstractmethod
from ...dataclass.name_info import NameInfo
from .i_rules_name import IRulesName

class IRuleName(ABC):
    @abstractmethod
    def __init__(self, rules: IRulesName) -> None:
        """Constructor"""

    @abstractmethod
    def get_is_match(self, ni: NameInfo) -> bool:
        """
        Gets if rule is a match

        Args:
            ni (NameInfo): name info
        """

    @abstractmethod
    def process_name(self, ni: NameInfo) -> None:
        """
        Changes name info based upon rules match

        Args:
            ni (NameInfo): name info
        """