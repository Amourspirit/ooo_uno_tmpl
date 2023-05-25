from __future__ import annotations
import logging
from os import PathLike
from typing import List, Union, Type, Set
from .rule_find_replace import RuleFindReplace
from ..parser.common.log_load import Log
from .post_rule_proto import PostRuleProto


class RulesPost:
    """Manages rules for post processing"""

    def __init__(self, fnm: PathLike, log: logging.Logger) -> None:
        self._log = log
        self._rules: List[Type[PostRuleProto]] = []
        self._register_known_rules()
        self._fnm = fnm
        self._post_lines: Set[str] = set()
        with open(fnm, "r") as f:
            self._content = f.read()
            self._log.info(f"Rules Post: Loaded file: {fnm}")
        self._process_post_content_lines()


    def register_rule(self, rule: Type[PostRuleProto]) -> None:
        """
        Register rule

        Args:
            rule (type[PostRuleProto]): Rule to register

        Raises:
            TypeError: If rules is not inherited form PostRuleProto
        """
        if rule in self._rules:
            msg = f"{self.__class__.__name__}.register_rule() Rule is already registered"
            self._log.logger.warning(msg)
            return
        self._reg_rule(rule=rule)

    def unregister_rule(self, rule: Type[PostRuleProto]):
        """
        [summary]

        Args:
            rule (type[PostRuleProto]): Rule to unregister

        Raises:
            ValueError: If rule is not present
        """
        try:
            self._rules.remove(rule)
        except ValueError as e:
            msg = f"{self.__class__.__name__}.unregister_rule() Unable to unregister rule."
            raise ValueError(msg) from e

    def _reg_rule(self, rule: Type[PostRuleProto]):
        self._rules.append(rule)

    def _register_known_rules(self):
        self._reg_rule(RuleFindReplace)

    def _process_post_content_lines(self) -> None:
        # find all lines that start with a # post_process: rule_name:
        lines = self._content.splitlines()
        indexes: List[int] = []
        for i, line in enumerate(lines):
            # self._log.info(f"Processing line: {line}")
            if line.startswith("# post_process: rule_name:"):
                s = line[26:]
                s = s.lstrip()
                self._log.info(f"Found post process line: {s}")
                self._post_lines.add(s)
                indexes.append(i)
        # remove lines from content
        if not indexes:
            return
        for i in reversed(indexes):
            del lines[i]
        self._content = "\n".join(lines)

    def _save_content(self) -> None:
        with open(self._fnm, "w") as f:
            f.write(self._content)

    def apply(self) -> None:
        found_match = False
        for rule in self._rules:
            rule_instance = self.get_rule_instance(rule=rule)
            for line in self._post_lines:
                if rule_instance.get_is_match(rule_line=line):
                    found_match = True
                    self._content = rule_instance.apply(content=self._content, rule_line=line)
                    self._log.info(f"Applied rule: {rule_instance.get_rule_name()}")
        if found_match:
            self._save_content()

    def get_rule_instance(self, rule: Type[PostRuleProto]) -> PostRuleProto:
        return rule(log=self._log)
