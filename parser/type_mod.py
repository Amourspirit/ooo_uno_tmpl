# coding: utf-8
"""
Handles conversion of LibreOffice types to Python Types
"""
import re
from abc import ABC, abstractmethod
from typing import List, Match, Optional, Set, Union

# hyper is 64 bit int, singed or unsinged. https://ask.libreoffice.org/t/basic-hyper-and-unsigned-hyper/22510

TYPE_MAP_PRIMITIVE = {
    "any": "object",
    "byte": "int",
    "short": "int",
    "int": "int",
    "long": "int",
    "hyper": "int",
    "float": "float",
    "double": "float",
    "string": "str",
    "char": "str",
    "boolean": "bool",
    "void": "None"
}

TYPE_MAP_KNOWN_ITTER = {
    "sequence": "list",
    "aDXArray": "list",
    "com.sun.star.beans.Pair": "tuple"
}

TYPE_MAP_KNOWN_PRIMITAVE = {
    "type": "object",
    "T": "object",
    "U": "object"
}
TYPE_MAP_PY_WRAPPER = {
    "list": "typing.List",
    "tuple": "typing.Tuple"
}
class PythonType(object):
    # region Constructor
    def __init__(
        self, type: str = 'object',
        requires_typing: bool = False,
        imports: Optional[str] = None,
        is_py_type: bool = True,
        children: Optional[List['PythonType']] = None,
        realtype: str = 'object'
        ) -> None:
        self._type = type
        self._requires_typing = requires_typing
        self._imports = imports
        self._is_py_type = is_py_type
        self._realtype = realtype
        if children is None:
            self._children = []
        else:
            self._children = children
        
    # endregion Constructor

    # region Properties
    @property
    def type(self) -> str:
        """Specifies type
    
            :getter: Gets type value.
            :setter: Sets type value.
        """
        return self._type
    
    @type.setter
    def type(self, value: str):
        self._default_check()
        self._type = value

    @property
    def requires_typing(self) -> bool:
        """Specifies requires_typing
    
            :getter: Gets requires_typing value.
            :setter: Sets requires_typing value.
        """
        return self._requires_typing
    
    @requires_typing.setter
    def requires_typing(self, value: bool):
        self._default_check()
        self._requires_typing = value

    @property
    def imports(self) -> Union[str, None]:
        """Specifies imports

            :getter: Gets imports value.
            :setter: Sets imports value.
        """
        return self._imports

    @imports.setter
    def imports(self, value: Union[str, None]):
        self._default_check()
        self._imports = value

    @property
    def is_py_type(self) -> bool:
        """Specifies is_py_type
    
            :getter: Gets is_py_type value.
            :setter: Sets is_py_type value.
        """
        return self._is_py_type
    
    @is_py_type.setter
    def is_py_type(self, value: bool):
        self._default_check()
        self._is_py_type = value

    @property
    def children(self) -> List['PythonType']:
        """Gets children value"""
        return self._children

    @property
    def realtype(self) -> str:
        """Specifies realtype

            :getter: Gets realtype value.
            :setter: Sets realtype value.
        """
        return self._realtype

    @realtype.setter
    def realtype(self, value: str):
        self._default_check()
        self._realtype = value
    # endregion Properties

    # region Methods
    def _default_check(self):
        if self.is_default():
            raise Exception('PythonType Default instance is not allow to be modifiled. Perhaps create a copy first.')

    def copy(self) -> 'PythonType':
        """
        Gets a copy of current instance

        Returns:
            [PythonType]: Copy
        """
        p_type = PythonType(
            type=self.type,
            requires_typing=self.requires_typing,
            imports=self.imports,
            is_py_type=self.is_py_type,
            realtype=self.realtype
        )
        p_type.children.extend(self.children)
        return p_type

    def get_all_imports(self) -> Set[str]:
        """
        Get import for inststance and allof children recursivly

        Returns:
            Set[str]: Set containing all imports
        """
        def _get_imports(p_type: PythonType, imports: Set[str]) -> None:
            if p_type.imports:
                imports.add(p_type.imports)
            for child in p_type.children:
                _get_imports(child, imports)
        im: Set[str] = set()
        _get_imports(self, im)
        return im

    def is_default(self) -> bool:
        """
        Gets if instance is is default instance

        Returns:
            bool: ``True`` if this instance is the same as the default instance; Otherwise, ``False``
        """
        return self is DEFAULT_PYTHON_TYPE
    
    # endregion Methods


DEFAULT_PYTHON_TYPE = PythonType()
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
        self._rules: List[type[ITypeRule]] = []
        self._cache = {}
        self._register_known_rules()
    
    def register_rule(self, rule: type[ITypeRule]) -> None:

        if not issubclass(rule, ITypeRule):
            msg = "TypeRules.register_rule(), rule arg must be child class of ITypeRule"
            raise TypeError(msg)
        if rule in self._rules:
            msg = "TypeRules.register_rule() Rule is already registered"
            self._log.warning(msg)
            return
        self._reg_rule(rule=rule)

    def unregister_rule(self,  rule: type[ITypeRule]):
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


    def _reg_rule(self, rule: type[ITypeRule]):
        self._rules.append(rule)

    def _register_known_rules(self):
        self._reg_rule(rule=RuleNone)
        self._reg_rule(rule=RulePrimative)
        self._reg_rule(rule=RuleKnownPrimative)
        self._reg_rule(rule=RuleKnownItterType)
        self._reg_rule(rule=RuleComType)
        self._reg_rule(rule=RuleTypeDef)
        self._reg_rule(rule=RuleWordSigned)
        self._reg_rule(rule=RuleWordUnSigned)
        self._reg_rule(rule=RuleWordShort)
        self._reg_rule(rule=RuleWordLong)
        self._reg_rule(rule=RuleWordHyper)
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
        return DEFAULT_PYTHON_TYPE
    
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
    

class RuleNone(ITypeRule):
    def __init__(self, rules: ITypeRules) -> None:
        self._rules = rules

    def get_is_match(self, in_type: str) -> bool:
        return in_type == ''

    def get_python_type(self, in_type: str) -> PythonType:
        return PythonType(
            type="None",
            requires_typing=False,
            is_py_type=True,
            realtype=None
        )

class RulePrimative(ITypeRule):
    def __init__(self, rules: ITypeRules) -> None:
        self._rules =rules

    def get_is_match(self, in_type: str) -> bool:
        return in_type in TYPE_MAP_PRIMITIVE
    
    def get_python_type(self, in_type: str) -> PythonType:
        s = TYPE_MAP_PRIMITIVE[in_type]
        return PythonType(
            type=s,
            requires_typing=False,
            is_py_type=True,
            realtype=s
        )


class RuleKnownPrimative(ITypeRule):
    def __init__(self, rules: ITypeRules) -> None:
        self._rules = rules

    def get_is_match(self, in_type: str) -> bool:
        return in_type in TYPE_MAP_KNOWN_PRIMITAVE

    def get_python_type(self, in_type: str) -> PythonType:
        s = TYPE_MAP_KNOWN_PRIMITAVE[in_type]
        return PythonType(
            type=s,
            requires_typing=False,
            is_py_type=True,
            realtype=s
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
        s = parts.pop()
        return PythonType(
            type = s,
            requires_typing = False,
            imports = s_type,
            is_py_type = False,
            realtype=s
        )


class RuleKnownItterType(ITypeRule):
    """Rule for Known itter uno types such as sequence"""

    def __init__(self, rules: ITypeRules) -> None:
        self._rules = rules
    
    def get_is_match(self, in_type: str) -> bool:
        return in_type in TYPE_MAP_KNOWN_ITTER

    def get_python_type(self, in_type: str) -> PythonType:
        s = TYPE_MAP_KNOWN_ITTER[in_type]
        return PythonType(
            type = s,
            requires_typing = False,
            is_py_type = True,
            realtype = s
        )


class RuleBaseWord(ITypeRule):
    """Abstrace Class: Matches types that start with a word"""
    # https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1sdb_1_1RowsChangeEvent.html

    def __init__(self, rules: ITypeRules) -> None:
        self._rules = rules

    def _get_ptype(self, in_type: str) -> PythonType:
            return self._rules.get_python_type(in_type)

    def get_is_match(self, in_type: str) -> bool:
        word = self._get_word()
        if in_type.startswith(word):
            parts = in_type.split()
            if len(parts) > 1:
                return True
        return False

    def get_python_type(self, in_type: str) -> PythonType:
        s = in_type.split(maxsplit=1)[1]
        return self._get_ptype(s)

    @abstractmethod
    def _get_word(self) -> str:
        """Word to match"""


class RuleTypeDef(RuleBaseWord):
    """Matches types that start with typedef"""
    # https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1sdb_1_1RowsChangeEvent.html

    def _get_word(self) -> str:
        return 'typedef ' # space on purpose


class RuleWordLong(RuleBaseWord):
    """Matches types that start with long and have more then one word"""

    def _get_word(self) -> str:
        return 'long '  # space on purpose


class RuleWordHyper(RuleBaseWord):
    """Matches types that start with hyper and have more then one word"""

    def _get_word(self) -> str:
        return 'hyper '  # space on purpose

class RuleWordShort(RuleBaseWord):
    """Matches types that start with short and have more then one word"""

    def _get_word(self) -> str:
        return 'short '  # space on purpose
class RuleWordSigned(RuleBaseWord):
    """Matches types that start with signed"""

    def _get_word(self) -> str:
        return 'signed '  # space on purpose

class RuleWordUnSigned(RuleBaseWord):
    """Matches types that start with unsigned"""

    def _get_word(self) -> str:
        return 'unsigned '  # space on purpose
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
            realtype = self._wrapper_type.type
            w += f"[{p_type.type}]"
        else:
            w = f"typing.List[{p_type.type}]"
            realtype = 'list'
        result = PythonType(
            type = w,
            requires_typing=True,
            is_py_type=p_type.is_py_type,
            realtype = realtype
        )
        result.children.append(p_type)
        return result

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

    def _get_ptype(self, in_type: str) -> PythonType:
        try:
            self._recursive_state = True
            result = self._rules.get_python_type(in_type)
            return result
        finally:
            self._recursive_state = False

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
        is_py_type = False
        wrapper_str: str = self._match.groups()[0]
        inner_str: str = self._match.groups()[1]
        inner_str = inner_str.lstrip(".").lstrip()
        parts = inner_str.split('.')
        # t_name can not be a primative because primative sequence rule has
        # ruled it out.
        t_name = parts.pop()
        child = self._get_ptype(t_name)
        if child.is_default():
            child = child.copy()
        if child.type == 'object':
            # default, t_name will never be object
            child.type = t_name
            child.realtype = t_name
            child.is_py_type = False
            child.requires_typing = True
        if t_name in TYPE_MAP_KNOWN_PRIMITAVE:
            t_name = TYPE_MAP_KNOWN_PRIMITAVE[t_name]
            is_py_type = True
            child.is_py_type = True
            child.children.clear()
            child.imports = None
            child.is_py_type = True
            child.requires_typing = False
            child.type = t_name
            child.realtype = t_name
        self._set_wrapper(wrapper_str)
        if self._wrapper_type.type in TYPE_MAP_PY_WRAPPER:
            realtype = self._wrapper_type.type
            s = TYPE_MAP_PY_WRAPPER[self._wrapper_type.type]
            w = f"{s}[{child.type}]"
        else:
            realtype = 'list'
            w = f"typing.List[{child.type}]"

        p_type = PythonType(
            type = w,
            requires_typing = True,
            is_py_type = is_py_type,
            children = [child],
            realtype = realtype
        )
        if not is_py_type:
            p_type.imports = inner_str
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

    def _get_ptype(self, in_type: str) -> PythonType:
        try:
            self._recursive_state = True
            result = self._rules.get_python_type(in_type)
            return result
        finally:
            self._recursive_state = False
        
    
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
        p_inner = self._get_ptype(inner_str)

        self._set_wrapper(wrapper_str)
        if self._wrapper_type.type in TYPE_MAP_PY_WRAPPER:
            realtype = self._wrapper_type.type
            s = TYPE_MAP_PY_WRAPPER[self._wrapper_type.type]
            w = f"{s}[{p_inner.type}]"
        else:
            realtype = 'list'
            w = f"typing.List[{p_inner.type}]"
        # if len(p_inner.imports) > 0:
        #     w = "'" + w + "'"
        p_type = PythonType(
            type = w,
            requires_typing = True,
            is_py_type = p_inner.is_py_type,
            realtype = realtype
        )
        p_type.children.append(p_inner)
        # p_type.imports.update(p_inner.imports)
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

    def _get_ptype(self, in_type: str) -> PythonType:
        try:
            self._recursive_state = True
            result = self._rules.get_python_type(in_type)
            return result
        finally:
            self._recursive_state = False

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
        if s_type in TYPE_MAP_KNOWN_ITTER:
            p_type = PythonType(
                type=TYPE_MAP_KNOWN_ITTER[s_type],
                requires_typing=True,
                is_py_type=True
            )
        else:
            p_type = self._get_ptype(s_type)

        p_type_one = self._get_ptype(s_one)
        p_type_two = self._get_ptype(s_two)
        if p_type.type in TYPE_MAP_PY_WRAPPER:
            realtype = p_type.type
            f_str = TYPE_MAP_PY_WRAPPER[p_type.type]
            f_str = f_str + f"[{p_type_one.type}, {p_type_two.type}]"
        else:
            realtype = 'tuple'
            f_str = f"typing.Tuple[{p_type_one.type}, {p_type_two.type}]"
        # if len(p_type_one.imports) > 0 or len(p_type_two.imports) > 0:
        #     f_str = f"'{f_str}'"
        r_type = PythonType(type=f_str, realtype=realtype, requires_typing=True)
        r_type.imports = p_type.imports
        r_type.is_py_type = p_type.is_py_type and p_type_one.is_py_type and p_type_two.is_py_type
        r_type.children.append(p_type_one)
        r_type.children.append(p_type_two)
        return r_type
