from __future__ import annotations
import logging

class RuleFindReplace:
    def __init__(self, log: logging.Logger) -> None:
        self._is_valid = False
        self._find = None
        self._replace = None
        self._log = log

    def get_is_match(self, rule_line: str) -> bool:
        # expect find_replace:some value|some other value
        if not rule_line.startswith('find_replace:'):
            self._log.info("RuleFindReplace.get_is_match() Rule does not match.")
            return False
        # remove find_replace: from the line
        rule_line = rule_line[13:]
        # split on |
        parts = rule_line.split('|', maxsplit=1)
        if len(parts) != 2:
            self._log.warning("RuleFindReplace.get_is_match() Rule does not match. Incorrect number of parts!")
            return False
        self._find = parts[0]
        if self._find == '':
            self._log.warning("RuleFindReplace.get_is_match() Rule does not match. find is empty!")
            return False
        self._replace = parts[1]
        self._is_valid = True
        self._log.info("RuleFindReplace.get_is_match() is a match.")
        return True
        
    
    def apply(self, content: str, rule_line: str) -> str:
        if not self._is_valid:
            return content
        return content.replace(self._find, self._replace)
    
    def get_rule_name(self) -> str:
        return 'find_replace'