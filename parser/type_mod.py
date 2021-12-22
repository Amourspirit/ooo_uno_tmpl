# coding: utf-8
"""
Handles conversion of LibreOffice types to Python Types
"""
import re
from abc import ABC, abstractmethod, abstractproperty
from dataclasses import dataclass, field
import logging
from typing import List, Match, Set, Union
from logger.log_handle import get_logger
import hashlib

TYPE_MAP_PRIMITIVE = {
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

TYPE_MAP_KNOWN = {
    "sequence": "list",
    "aDXArray": "list"
}

TYPE_MAP_PY_WRAPPER = {
    "list": "typing.List",
    "tuple": "typing.Tuple"
}
@dataclass
class PythonType:
    type: str = 'object'
    requires_typing: bool = False
    imports: Set[str] = field(default_factory=set)

class ITypeRule(ABC):
    @abstractmethod
    def __init__(self, rules: 'ITypeRules') -> None:
        """Constructor"""
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


class ITypeRules(ABC):
    @abstractmethod
    def get_python_type(self, in_type: str) -> PythonType:
        """gets Python Type info"""

    @abstractmethod
    def get_rule_instance(self, rule: ITypeRule) -> ITypeRule:
        """Gets a rule instance"""


class TypeRules(ITypeRules):
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
        self._reg_rule(rule=RuleKnownType)
        self._reg_rule(rule=RuleSeqLikePrimative)
        self._reg_rule(rule=RuleSeqLikeNonPrim)

    def _get_rule(self, in_type:str) -> Union[ITypeRule, None]:
        
        match_inst = None
        for rule in self._rules:
            key = str(id(rule))
            if key in self._cache:
                inst = self._cache[key]
            else:
                inst: ITypeRule = rule(self)
                self._cache[key] = inst
            if inst.get_is_match(in_type):
                match_inst = inst
                break
        return match_inst

    def get_python_type(self, in_type: str) -> PythonType:
        _in = in_type.replace("::", ".").replace(':', ".").lstrip(".").strip()
        match = self._get_rule(in_type=_in)
        if match:
            return match.get_python_type(_in)
        return PythonType()
    
    def get_rule_instance(self, rule: ITypeRule) -> ITypeRule:
        if not issubclass(rule, ITypeRule):
            msg = "TypeRules.get_rule_instance(), rule arg must be child class of ITypeRule"
            self._log.error(msg)
            raise TypeError(msg)
        key = str(id(rule))
        if key in self._cache:
                return self._cache[key]
        else:
            self._cache[key] = rule(self)
        return self._cache[key]
    
class RulePrimative(ITypeRule):
    def __init__(self, rules: ITypeRules) -> None:
        self._rules =rules

    def get_is_match(self, in_type: str) -> bool:
        return in_type in TYPE_MAP_PRIMITIVE
    
    def get_python_type(self, in_type: str) -> PythonType:
        return PythonType(
            type=TYPE_MAP_PRIMITIVE[in_type],
            requires_typing=False
        )

class RuleKnownType(ITypeRule):
    """Rule for Known uno types sucha s sequence"""

    def __init__(self, rules: ITypeRules) -> None:
        self._rules = rules
    
    def get_is_match(self, in_type: str) -> bool:
        return in_type in TYPE_MAP_KNOWN

    def get_python_type(self, in_type: str) -> PythonType:
        return PythonType(
            type = TYPE_MAP_KNOWN[in_type],
            requires_typing=False
        )

class RuleSeqLikePrimative(ITypeRule):
    """Matches single sequence or simalar, such as aDXArray, that does have primitive inner type"""

    def __init__(self, rules: ITypeRules) -> None:
        self._rules = rules
        self._prim: RulePrimative = self._rules.get_rule_instance(
            RulePrimative)
        self._rx = re.compile(r"([a-zA-Z]+)<[ ]*([a-zA-Z]+)[ ]*>")
        self._match: Union[Match[str], None] = False
        self._wrapper_type: PythonType = None
        # match sequence< string >
        # do not match
        # sequence< com.sun.star.beans.Pair< string, string > >

    def _set_match(self, in_type: str)-> None:
        if not self._match is False:
            return
        self._match = self._rx.match(in_type)

    def _set_wrapper(self, in_type: str):
        if self._wrapper_type:
            return self._wrapper_type
        self._wrapper_type = self._rules.get_python_type(in_type=in_type)

    def _set_default(self):
        self._match = False
        self._wrapper_type = None

    def get_is_match(self, in_type: str) -> bool:
        self._set_default()
        self._set_match(in_type)
        if not self._match:
            return False
        wrapper_str: str = self._match.groups()[0]
        inner_str: str = self._match.groups()[1]
        is_prim = self._prim.get_is_match(inner_str)
        if not is_prim:
            return False
        # recursivly look for wrapper such as list
        self._set_wrapper(wrapper_str)
        if self._wrapper_type.type == "object":
            return False
        if self._wrapper_type.requires_typing:
            return False
        return True
        
    def get_python_type(self, in_type: str) -> PythonType:
        self._set_match(in_type)
        if not self._match:
            msg = f"{self.__class__.__name__} get_python_type() Match Failure."
            msg += "Did you forget to call get_is_match()?"
            raise Exception(msg)
        wrapper_str: str = self._match.groups()[0]
        inner_str: str = self._match.groups()[1]
        self._set_wrapper(wrapper_str)
        p_type = self._prim.get_python_type(inner_str)
        if self._wrapper_type.type in TYPE_MAP_PY_WRAPPER:
            w = TYPE_MAP_PY_WRAPPER[self._wrapper_type.type]
            w += f"[{p_type.type}]"
        else:
            w = f"'typing.List[{p_type.type}]'"
        return PythonType(
            type = w,
            requires_typing=True
        )


class RuleSeqLikeNonPrim(ITypeRule):
    """Matches single sequence or simalar, such as aDXArray, that does not have primitive inner type"""

    def __init__(self, rules: ITypeRules) -> None:
        self._rules = rules
        self._seq_prim = self._rules.get_rule_instance(RuleSeqLikePrimative)
        self._rx = re.compile(r"([a-zA-Z]+)<[ ]*([a-zA-Z0-9._]+)[ ]*>")
        self._match: Union[Match[str], None] = False
        self._wrapper_type: PythonType = None

    def _set_match(self, in_type: str) -> None:
        if not self._match is False:
            return
        self._match = self._rx.match(in_type)

    def _set_wrapper(self, in_type: str):
        if self._wrapper_type:
            return self._wrapper_type
        self._wrapper_type = self._rules.get_python_type(in_type=in_type)

    def _set_default(self):
        self._match = False
        self._wrapper_type = None

    def get_is_match(self, in_type: str) -> bool:
        if self._seq_prim.get_is_match(in_type=in_type):
            # this is a sequence with a primative. let that rule handle it.
            return False
        self._set_default()
        self._set_match(in_type)
        if not self._match:
            return False
        wrapper_str: str = self._match.groups()[0]
        self._set_wrapper(wrapper_str)
        if self._wrapper_type.type == "object":
            return False
        if self._wrapper_type.requires_typing:
            return False
        return True

    def get_python_type(self, in_type: str) -> PythonType:
        self._set_match(in_type)
        if not self._match:
            msg = f"{self.__class__.__name__} get_python_type() Match Failure."
            msg += "Did you forget to call get_is_match()?"
            raise Exception(msg)
        wrapper_str: str = self._match.groups()[0]
        inner_str: str = self._match.groups()[1]
        inner_str = inner_str.lstrip(".").lstrip()
        parts = inner_str.split('.')
        t_name = parts.pop()
        self._set_wrapper(wrapper_str)
        if self._wrapper_type.type in TYPE_MAP_PY_WRAPPER:
            s = TYPE_MAP_PY_WRAPPER[self._wrapper_type.type]
            w = f"'{s}[{t_name}]'"
        else:
            w = f"'typing.List[{t_name}]'"
       
        p_type = PythonType(
            type=w,
            requires_typing=True
        )
        p_type.imports.add(inner_str)
        return p_type
