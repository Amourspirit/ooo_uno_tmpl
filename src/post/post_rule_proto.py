from __future__ import annotations
from typing import Protocol
import logging

class PostRuleProto(Protocol):

    def __init__(self, log: logging.Logger) -> None:
        ...

    def get_is_match(self, rule_line: str) -> bool:
        ...
    
    def apply(self, content: str, rule_line: str) -> str:
        ...

    def get_rule_name(self) -> str:
        ...