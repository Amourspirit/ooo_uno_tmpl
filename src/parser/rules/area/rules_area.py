# coding: utf-8
from typing import List, Union
from ...dataclass.area import Area
from ...dataclass.area_info import AreaInfo
from .i_rules_area import IRulesArea
from .i_rule_area import IRuleArea
from ...common.log_load import Log
log = Log()


class RulesArea(IRulesArea):
    """Manages rules for NameInfo"""

    def __init__(self, remove_parent_inherited) -> None:
        self._remove_parent_inherited: bool = remove_parent_inherited
        self._rules: List[type[IRuleArea]] = []
        self._cache = {}
        self._register_known_rules()

    def __len__(self) -> int:
        return len(self._rules)

    # region Methods

    def register_rule(self, rule: type[IRuleArea]) -> None:
        """
        Register rule

        Args:
            rule (type[IRuleArea]): Rule to register

        Raises:
            TypeError: If rules is not inherited form IRuleArea
        """
        if not issubclass(rule, IRuleArea):
            msg = f"{self.__class__.__name__}.register_rule(), rule arg must be child class of ITypeRule"
            raise TypeError(msg)
        if rule in self._rules:
            msg = f"{self.__class__.__name__}.register_rule() Rule is already registered"
            log.logger.warning(msg)
            return
        self._reg_rule(rule=rule)

    def unregister_rule(self,  rule: type[IRuleArea]):
        """
        [summary]

        Args:
            rule (type[IRuleArea]): Rule to unregister

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

    def _reg_rule(self, rule: type[IRuleArea]):
        self._rules.append(rule)

    def _register_known_rules(self):
        pass

    def _get_rule(self, ai: AreaInfo, alst: List[Area]) -> Union[IRuleArea, None]:

        match_inst = None
        for rule in self._rules:
            key = str(id(rule))
            if key in self._cache:
                inst = self._cache[key]
            else:
                inst: IRuleArea = rule(rules=self)
                self._cache[key] = inst
            if inst.get_is_match(ai=ai, alst=alst):
                match_inst = inst
                break
        return match_inst

    def get_area(self, ai: AreaInfo, alst: List[Area]) -> Union[List[Area], None]:
        """
        Gets filtered Area list

        Args:
            alst (List[Area]): Areas to filter

         Returns:
            List[Area]: Filtered Area List
        """
        match = self._get_rule(ai=ai, alst=alst)
        if match:
            return match.get_area(ai=ai, alst=alst)
        return None
    # endregion Methods

    # region Properties
    @property
    def remove_parent_inherited(self) -> bool:
        """Specifies remove_parent_inherited

            :getter: Gets remove_parent_inherited value.
            :setter: Sets remove_parent_inherited value.
        """
        return self._remove_parent_inherited

    @remove_parent_inherited.setter
    def remove_parent_inherited(self, value: bool):
        self._remove_parent_inherited = value
    # endregion Properties
