# coding: utf-8
import logging
from typing import List, Union
from ...dataclass.name_info import NameInfo
from .i_rules_name import IRulesName
from .i_rule_name import IRuleName
from ...common.log_load import Log
log = Log()

class RulesName(IRulesName):
    """Manages rules for NameInfo"""

    def __init__(self) -> None:
        self._rules: List[type[IRuleName]] = []
        self._cache = {}
        self._register_known_rules()

    def register_rule(self, rule: type[IRuleName]) -> None:
        """
        Register rule

        Args:
            rule (type[IRuleName]): Rule to register

        Raises:
            TypeError: If rules is not inherited form IRuleName
        """
        if not issubclass(rule, IRuleName):
            msg = f"{self.__class__.__name__}.register_rule(), rule arg must be child class of ITypeRule"
            raise TypeError(msg)
        if rule in self._rules:
            msg = f"{self.__class__.__name__}.register_rule() Rule is already registered"
            log.logger.warning(msg)
            return
        self._reg_rule(rule=rule)

    def unregister_rule(self,  rule: type[IRuleName]):
        """
        [summary]

        Args:
            rule (type[IRuleName]): Rule to unregister

        Raises:
            ValueError: If rule is not present
        """
        try:
            key = str(id(rule))
            if key in self._cache:
                del self._cache[key]
            self._rules.remove(rule)
        except ValueError as e:
            msg = f"{self.__class__.__name__}.unregister_rule() Unable to unregister rule."
            raise ValueError(msg) from e

    def _reg_rule(self, rule: type[IRuleName]):
        self._rules.append(rule)

    def _register_known_rules(self):
        pass

    def _get_rule(self, ni: NameInfo) -> Union[IRuleName, None]:

        match_inst = None
        for rule in self._rules:
            key = str(id(rule))
            if key in self._cache:
                inst = self._cache[key]
            else:
                inst: IRuleName = rule(self)
                self._cache[key] = inst
            if inst.get_is_match(ni):
                match_inst = inst
                break
        return match_inst

    def process_name(self, ni: NameInfo) -> None:
        match = self._get_rule(ni)
        if match:
            match.process_name(ni)

    def get_rule_instance(self, rule: IRuleName) -> IRuleName:
        if not issubclass(rule, IRuleName):
            msg = f"{self.__class__.__name__}.get_rule_instance(), rule arg must be child class of IRuleName"
            log.logger.error(msg)
            raise TypeError(msg)
        key = str(id(rule))
        if key in self._cache:
            return self._cache[key]
        else:
            self._cache[key] = rule(self)
        return self._cache[key]
