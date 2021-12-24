# coding: utf-8
"""
Handles conversion of LibreOffice types to Python Types
"""
import re
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import List, Match, Set, Union

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
    "aDXArray": "list",
    "com.sun.star.beans.Pair": "tuple"
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
    is_py_type: bool = False

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
    def __init__(self) -> None:
        self._rules: List[ITypeRule] = []
        self._cache = {}
        self._register_known_rules()
    
    def register_rule(self, rule: ITypeRule) -> None:

        if not issubclass(rule, ITypeRule):
            msg = "TypeRules.register_rule(), rule arg must be child class of ITypeRule"
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
            msg = f"{self.__class__.__name__}.unregister_rule() Unable to unregister rule."
            raise ValueError(msg) from e


    def _reg_rule(self, rule: ITypeRule):
        self._rules.append(rule)

    def _register_known_rules(self):
        self._reg_rule(rule=RulePrimative)
        self._reg_rule(rule=RuleKnownType)
        self._reg_rule(rule=RuleComType)
        self._reg_rule(rule=RuleSeqLikePrimative)
        self._reg_rule(rule=RuleSeqLikeNonPrim)
        self._reg_rule(rule=RuleTuple2Like)
        self._reg_rule(rule=RuleSeqLikePair)

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
            requires_typing=False,
            is_py_type=True
        )

class RuleComType(ITypeRule):
    """Matches types that start wihh com.sun.star. such as com.sun.star.uno.XInterface"""

    def __init__(self, rules: ITypeRules) -> None:
        self._rules = rules
        self._rx = re.compile(r"[.]*(com\.sun\.star\.[a-zA-Z0-9_.]+)$")
        self._match: Union[Match[str], None] = False

    def _set_match(self, in_type: str) -> None:
        if not self._match is False:
            return
        self._match = self._rx.match(in_type)
    
    def _set_default(self):
        self._match = False
    
    def get_is_match(self, in_type: str) -> bool:
        self._set_default()
        self._set_match(in_type)
        if not self._match:
            return False
        return True

    def get_python_type(self, in_type: str) -> PythonType:
        self._set_match(in_type)
        if not self._match:
            msg = f"{self.__class__.__name__} get_python_type() Match Failure."
            msg += "Did you forget to call get_is_match()?"
            raise Exception(msg)
        g = self._match.groups()
        s_type: str = g[0]  # like com.sun.star.beans.Pair
        parts = s_type.rsplit(sep='.', maxsplit=1)
        return PythonType(
            type= parts.pop(),
            requires_typing=False,
            imports=set([s_type]),
            is_py_type=False
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
            requires_typing=False,
            is_py_type=True
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
        self._recursive_state = False
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
        self._recursive_state = True
        self._wrapper_type = self._rules.get_python_type(in_type=in_type)
        self._recursive_state = False

    def _set_default(self):
        self._match = False
        self._wrapper_type = None

    def get_is_match(self, in_type: str) -> bool:
        if self._recursive_state:
            return False
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
            requires_typing=True,
            is_py_type=p_type.is_py_type
        )


class RuleSeqLikeNonPrim(ITypeRule):
    """Matches single sequence or simalar, such as aDXArray, that does not have primitive inner type"""

    def __init__(self, rules: ITypeRules) -> None:
        self._rules = rules
        self._seq_prim = self._rules.get_rule_instance(RuleSeqLikePrimative)
        self._rx = re.compile(r"([a-zA-Z]+)<[ ]*([a-zA-Z0-9._]+)[ ]*>")
        self._match: Union[Match[str], None] = False
        self._wrapper_type: PythonType = None
        self._recursive_state = False

    def _set_match(self, in_type: str) -> None:
        if not self._match is False:
            return
        self._match = self._rx.match(in_type)

    def _set_wrapper(self, in_type: str):
        if self._wrapper_type:
            return self._wrapper_type
        self._recursive_state = True
        self._wrapper_type = self._rules.get_python_type(in_type=in_type)
        self._recursive_state = False

    def _set_default(self):
        self._match = False
        self._wrapper_type = None

    def get_is_match(self, in_type: str) -> bool:
        if self._recursive_state:
            return False
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
            requires_typing=True,
            is_py_type=False
        )
        p_type.imports.add(inner_str)
        return p_type

class RuleSeqLikePair(ITypeRule):
    """Matches single sequence with embeded pair such as sequence< com.sun.star.beans.Pair< string, string > >"""

    def __init__(self, rules: ITypeRules) -> None:
        self._rules = rules
        self._seq_prim = self._rules.get_rule_instance(RuleSeqLikePrimative)
        # https://regex101.com/r/yd32Z6/1
        self._rx = re.compile(r"([a-zA-Z]+)<[ ]*([a-zA-Z0-9._]+[ ]*<.*>)[ ]*>")
        self._match: Union[Match[str], None] = False
        self._wrapper_type: PythonType = None
        self._recursive_state = False

    def _set_match(self, in_type: str) -> None:
        if not self._match is False:
            return
        self._match = self._rx.match(in_type)

    def _set_wrapper(self, in_type: str):
        if self._wrapper_type:
            return self._wrapper_type
        self._recursive_state = True
        self._wrapper_type = self._rules.get_python_type(in_type=in_type)
        self._recursive_state = False

    def _set_default(self):
        self._match = False
        self._wrapper_type = None

    def get_is_match(self, in_type: str) -> bool:
        if self._recursive_state:
            return False
        self._set_default()
        self._set_match(in_type)
        if not self._match:
            return False
        return True

    def get_python_type(self, in_type: str) -> PythonType:
        self._set_match(in_type)
        if not self._match:
            msg = f"{self.__class__.__name__} get_python_type() Match Failure."
            msg += "Did you forget to call get_is_match()?"
            raise Exception(msg)

        #sequence
        wrapper_str: str = self._match.groups()[0]

        # com.sun.star.beans.Pair< string, string >
        inner_str: str = self._match.groups()[1]
        inner_str = inner_str.lstrip(".").lstrip()
        self._recursive_state = True
        p_inner = self._rules.get_python_type(inner_str)
        self._recursive_state = False

        t_name = p_inner.type.replace("'", "")
        self._set_wrapper(wrapper_str)
        if self._wrapper_type.type in TYPE_MAP_PY_WRAPPER:
            s = TYPE_MAP_PY_WRAPPER[self._wrapper_type.type]
            w = f"{s}[{t_name}]"
        else:
            w = f"typing.List[{t_name}]"
        if len(p_inner.imports) > 0:
            w = "'" + w + "'"
        p_type = PythonType(
            type=w,
            requires_typing=True,
            is_py_type=p_inner.is_py_type
        )
        p_type.imports.update(p_inner.imports)
        return p_type


class RuleTuple2Like(ITypeRule):
    """Matches items that can be converted to tuple such as com.sun.star.beans.Pair< string, string >"""

    def __init__(self, rules: ITypeRules) -> None:
        self._rules = rules
        self._seq_prim = self._rules.get_rule_instance(RuleSeqLikePrimative)
        # https://regex101.com/r/aOHaCG/1
        self._rx = re.compile(
            r"([a-zA-Z0-9_.]+)<[ ]*([a-zA-Z0-9._]+),[ ]*([a-zA-Z0-9._]+)[ ]*>")
        self._match: Union[Match[str], None] = False
        self._recursive_state = False

    def _set_match(self, in_type: str) -> None:
        if not self._match is False:
            return
        self._match = self._rx.match(in_type)

    def _set_default(self):
        self._match = False

    def get_is_match(self, in_type: str) -> bool:
        if self._recursive_state:
            return False
        self._set_default()
        self._set_match(in_type)
        if not self._match:
            return False
        return True

    def _get_clean_type(self, in_type: str) -> str:
        s = in_type.lstrip(".").lstrip()
        return s

    def get_python_type(self, in_type: str) -> PythonType:
        self._set_match(in_type)
        if not self._match:
            msg = f"{self.__class__.__name__} get_python_type() Match Failure."
            msg += "Did you forget to call get_is_match()?"
            raise Exception(msg)
        g = self._match.groups()
        s_type: str = self._get_clean_type(g[0])  # like com.sun.star.beans.Pair
        s_one: str = self._get_clean_type(g[1])
        s_two: str = self._get_clean_type(g[2])
        self._recursive_state = True
        if s_type in TYPE_MAP_KNOWN:
            p_type = PythonType(
                type=TYPE_MAP_KNOWN[s_type],
                requires_typing=True,
                is_py_type=True
            )
        else:
            p_type = self._rules.get_python_type(s_type)

        p_type_one = self._rules.get_python_type(s_one)
        p_type_two = self._rules.get_python_type(s_two)
        self._recursive_state = False
        if p_type.type in TYPE_MAP_PY_WRAPPER:
            f_str = TYPE_MAP_PY_WRAPPER[p_type.type]
            f_str = f_str + f"[{p_type_one.type}, {p_type_two.type}]"
        else:
            f_str = f"typing.Tuple[{p_type_one.type}, {p_type_two.type}]"
        if len(p_type_one.imports) > 0 or len(p_type_two.imports) > 0:
            f_str = f"'{f_str}'"
        r_type = PythonType()
        r_type.requires_typing = True
        r_type.imports.update(p_type.imports)
        r_type.imports.update(p_type_one.imports)
        r_type.imports.update(p_type_two.imports)
        r_type.type = f_str
        r_type.is_py_type = p_type.is_py_type and p_type_one.is_py_type and p_type_two.is_py_type
        return r_type
