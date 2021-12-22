# coding: utf-8
"""
Handles conversion of LibreOffice types to Python Types
"""
import re
from abc import ABC, abstractmethod, abstractproperty
from dataclasses import dataclass, field
import logging
from typing import List, Set, Union
from logger.log_handle import get_logger
import hashlib

@dataclass
class PythonType:
    type: str = 'object'
    requires_typing: bool = False
    imports: Set[str] = field(default_factory=set)

class ITypeRule(ABC):
    @abstractmethod
    def get_is_match(self, in_type:str) -> bool:
        """
        Gets if rule is a match
        
        Args:
            in_type (str): LibreOffice Api type such as Long.
        """
    
    @abstractmethod
    def get_python_type(self, in_type: str) -> PythonType:
        """
        Gets python type

        Args:
            in_type (str): LibreOffice Api type such as Long.
        """

class TypeRules:
    def __init__(self, **kwargs) -> None:
        self._rules: List[ITypeRule] = []
        self._log: logging.Logger = kwargs.get('logger', None)
        self._cache = {}
        if self._log is None:
            self._log = get_logger('type_mod')
        self._register_known_rules()
    
    def register_rule(self, rule: ITypeRule) -> None:

        if not issubclass(rule, ITypeRule):
            msg = "TypeRules.register_rule(), rule arg must be child class of ITypeRule"
            self._log.error(msg)
            raise TypeError(msg)
        if rule in self._rules:
            msg = "TypeRules.register_rule() Rule is already registered"
            self._log.warning(msg)
            return
        self._reg_rule(rule=rule)

    def unregister_rule(self,  rule: ITypeRule):
        """
        Unregister a rule

        Args:
            rule (ITypeRule): Rule to unregister
        """
        try:
            self._rules.remove(rule)
        except ValueError as e:
            self._log.error("unable to unregister rule. %s", str(e))


    def _reg_rule(self, rule: ITypeRule):
        self._rules.append(rule)

    def _register_known_rules(self):
        self._reg_rule(rule=RulePrimative)
        self._reg_rule(rule=RuleSequencePrimative)
        self._reg_rule(RuleSequenceSingle)

    def _get_rule(self, in_type:str) -> Union[ITypeRule, None]:
        
        match_inst = None
        for rule in self._rules:
            key = str(id(rule))
            if key in self._cache:
                inst = self._cache[key]
            else:
                inst: ITypeRule = rule()
                self._cache[key] = inst
            if inst.get_is_match(in_type):
                match_inst = inst
                break
        return match_inst

    def get_python_type(self, in_type: str) -> PythonType:
        match = self._get_rule(in_type=in_type)
        if match:
            return match.get_python_type(in_type)
        return PythonType()
    
class RulePrimative(ITypeRule):
    def __init__(self) -> None:
        self._type_map = {
            "any": "object",
            "short": "int",
            "long": "int",
            "float": "float",
            "double": "float",
            "string": "str",
            "char": "str",
            "boolean": "bool",
            "void": "None"
        }
    def get_is_match(self, in_type: str) -> bool:
        return in_type in self._type_map
    
    def get_python_type(self, in_type: str) -> PythonType:
        return PythonType(
            type=self._type_map[in_type],
            requires_typing=False
        )

class RuleSequencePrimative(ITypeRule):
    """Matches single sequence that does have primitive inner type"""
    def __init__(self) -> None:
        self._prim = RulePrimative()
        self._rx = re.compile(r"sequence<[ ]*([a-zA-Z]+)")
        # match sequence< string >
        # do not match
        # sequence< com.sun.star.beans.Pair< string, string > >


    def get_is_match(self, in_type: str) -> bool:
        parts = in_type.split('<')
        if len(parts) != 2:
            return False
        m = self._rx.match(in_type)
        if not m:
            return False
        prim_str: str = m.groups()[0]
        return self._prim.get_is_match(prim_str)
        
    def get_python_type(self, in_type: str) -> PythonType:
        m = self._rx.match(in_type)
        prim_str: str = m.groups()[0]
        p_type = self._prim.get_python_type(prim_str)
        t = f"typing.List[{p_type.type}]"
        return PythonType(
            type = t,
            requires_typing=True
        )


class RuleSequenceSingle(ITypeRule):
    """Matches single sequence that does not have primitive inner type"""
    def __init__(self) -> None:
        self._prim = RuleSequencePrimative()
        self._rx = re.compile(r"sequence<[ ]*([a-zA-Z0-9_.]+)")
        self._parts: List[str] = None
        self._match = None

    def get_is_match(self, in_type: str) -> bool:
        if self._prim.get_is_match(in_type):
            # let RuleSequencePrimative handle it
            return False
        self._parts = in_type.split('<')
        if len(self._parts) != 2:
            return False
        self._match = self._rx.match(in_type)
        if not self._match:
            return False
        return True

    def get_python_type(self, in_type: str) -> PythonType:
        # inner type is not a python type.
        s: str = self._match.groups()[0]
        s = s.lstrip('.')
        parts = s.split('.')
        t = f"'typing.List[{parts.pop()}]'"
        p_type = PythonType(
            type=t,
            requires_typing=True
        )
        p_type.imports.add(s)
        return p_type
