# coding: utf-8
import logging
from typing import List, Union
from ...dataclass.summary_info import SummaryInfo
from .i_rule_summary_info import IRuleSummaryInfo
from .i_rules_summary_info import IRulesSummaryInfo
from ...common.log_load import Log
log = Log()


class RulesSummaryInfo(IRulesSummaryInfo):
    def __init__(self) -> None:
        self._rules: List[type[IRuleSummaryInfo]] = []
        self._cache = {}
        self._register_known_rules()

    def register_rule(self, rule: type[IRuleSummaryInfo]) -> None:

        if not issubclass(rule, IRuleSummaryInfo):
            msg = f"{self.__class__.__name__}.register_rule(), rule arg must be child class of ITypeRule"
            raise TypeError(msg)
        if rule in self._rules:
            msg = f"{self.__class__.__name__}.register_rule() Rule is already registered"
            log.logger.warning(msg)
            return
        self._reg_rule(rule=rule)

    def unregister_rule(self,  rule: type[IRuleSummaryInfo]):
        """
        Unregister a rule

        Args:
            rule (ITypeRule): Rule to unregister
        """
        try:
            key = str(id(rule))
            if key in self._cache:
                del self._cache[key]
            self._rules.remove(rule)
        except ValueError as e:
            msg = f"{self.__class__.__name__}.unregister_rule() Unable to unregister rule."
            raise ValueError(msg) from e

    def _reg_rule(self, rule: type[IRuleSummaryInfo]):
        self._rules.append(rule)

    def _register_known_rules(self):
        pass

    def _get_rule(self, si: SummaryInfo) -> Union[IRuleSummaryInfo, None]:

        match_inst = None
        for rule in self._rules:
            key = str(id(rule))
            if key in self._cache:
                inst = self._cache[key]
            else:
                inst: IRuleSummaryInfo = rule(self)
                self._cache[key] = inst
            if inst.get_is_match(si):
                match_inst = inst
                break
        return match_inst

    def process_summary_info(self, si: SummaryInfo) -> None:
        """
        Process Summary info. Making changes base upon first match if a rule match is found.

        Args:
            si (SummaryInfo): [description]
        """
        match = self._get_rule(si)
        if match:
            match.process_summary_info(si)

    def get_rule_instance(self, rule: IRuleSummaryInfo) -> IRuleSummaryInfo:
        if not issubclass(rule, IRuleSummaryInfo):
            msg = f"{self.__class__.__name__}.get_rule_instance(), rule arg must be child class of IRuleSummaryInfo"
            log.logger.error(msg)
            raise TypeError(msg)
        key = str(id(rule))
        if key in self._cache:
            return self._cache[key]
        else:
            self._cache[key] = rule(self)
        return self._cache[key]
