# coding: utf-8
from dataclasses import dataclass
from ..mod_type import PythonType

@dataclass
class SummaryInfo:
    id: str
    """Summary Info ID obtained from web page"""
    name: str
    """Name from page summary"""
    type: str
    """Type from page summary"""
    p_type: PythonType
    """Python Type obtaind usually from Util.get_python_type()"""
    # extra_data: object = None
    # """Extra data that can be set in rules or otherwise"""

    def __lt__(self, other: object):
        if not isinstance(other, SummaryInfo):
            return NotImplemented
        return self.name < other.name
