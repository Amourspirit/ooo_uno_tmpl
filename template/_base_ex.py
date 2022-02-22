# coding: utf-8
import uno
from typing import Dict, List, Tuple, Union
from _base_json import BaseJson
from verr import Version
class BaseEx(BaseJson):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._sorted_key_index = None
        self._uno_instance = None
        self._is_parent = None
        self._cache = {}


    def _hydrate_data(self, json_data: dict):
        self._validate_data(json_data)
        data: Dict[str, object] = json_data['data']
        def set_data(_key: str, a_name=None):
            attr_name = _key if not a_name else a_name
            val = data.get(_key, None)
            if not val is None:
                setattr(self, attr_name, val)

        set_data('name')
        set_data('namespace')
        set_data('allow_db')
        set_data('desc')
        set_data('url', 'link')
        setattr(self, 'inherits', data.get('extends', []))
        set_data('imports')
        # get lo ver if it exist. Defaut to False
        self.libre_office_ver = json_data.get('libre_office_ver', False)
        sort = bool(json_data['parser_args'].get('sort', False))
        self.include_desc = bool(
            json_data['writer_args'].get('include_desc', True))
        self.attribs = self._get_attribs(json_data=json_data, sort=sort)
        setattr(self, 'requires_typing', data.get('requires_typing', False))
        setattr(self, 'from_imports', [])
        setattr(self, 'from_imports_typing', [])
        set_data('from_imports')
        set_data('from_imports_typing')
        # self.requires_typing = False if len(
        #     self.from_imports_typing) == 0 else True
        quote: List[str] = data.get('quote', [])
        self.quote.update(quote)
        typings: List[str] = data.get('typings', [])
        self.typings.update(typings)
        extends_map = data.get('extends_map', None)
        if extends_map:
            self.extends_map.update(extends_map)
        self.fullname = f"{self.namespace}.{self.get_safe_word(self.name)}"

    def _get_attribs(self, json_data: dict, sort: bool) -> dict:
        items: dict = json_data['data'].get('items', {})
        if not sort:
            return items
        keys = list(items.keys())
        if len(keys) == 0:
            return items

        def sort_lst_dict(_key: str, sort_key: str) -> List[dict]:
            key_index: List[Tuple[str, int]] = []
            lst = items[_key]  # methods
            if len(lst) == 0:
                return lst
            for i, itm in enumerate(lst):
                key_index.append((itm[sort_key], i))
            key_index.sort()
            sorted_lst = []
            for k_i in key_index:
                sorted_lst.append(lst[k_i[1]])
            return sorted_lst
        result = {}
        for k in keys:
            result[k] = sort_lst_dict(k, 'name')
        return result

    def _validate_data(self, data: dict) -> bool:
        super()._validate_data(data=data)

        if not data['type'] == 'exception':
            raise Exception(
                f"Invalid Data: Expected type to be 'exception' got '{data['type']}'")

        if not data['name']:
            raise Exception('Invalid Data: name attribute is not valid')
        min_ver = Version(0, 1, 18)
        ver = Version.parse(data.get('version', None))
        if ver < min_ver:
            raise Exception(
                "Invalid Data: Expected version to be at least '{min_ver}' got {ver}")

    def _get_formated_arg(self, arg: Tuple[str]) -> str:
        return f"{self.get_safe_word(arg[0])}: {self.get_q_type(arg[1])}"

    def get_args(self, args: List[Tuple[str]]) -> str:
        result = ''
        for i, arg in enumerate(args):
            if i > 0:
                result += ', '
            result += self._get_formated_arg(arg=arg)
        return result

    def get_out_args(self, meth: dict) -> List[str]:
        args: list = meth['args']
        results: List[str] = []
        for arg in args:
            if len(arg) >= 3:
                if self.is_out_arg(arg[2]):  # dir in or out
                    results.append(arg[0])  # arg name, index 1 is type
        return results

    # region Raises Methods

    def _get_raises_list(self, d: dict, key: str) -> List[Tuple[str, str]]:
        """
        Converts any raises into a list of tuple.
        First part full name.
        Second Part Short name
        """
        results = []
        if key in d:
            lst = d[key]
            for r in lst:
                results.append((r, self.get_last_part(r)))
        return results

    def get_raises_list(self, meth: dict) -> List[Tuple[str, str]]:
        """
        Converts any raises into a list of tuple.
        First part full name.
        Second Part Short name
        """
        return self._get_raises_list(d=meth, key='raises')

    def get_prop_get_raises(self, prop: dict) -> List[Tuple[str, str]]:
        """
        Converts any raises into a list of tuple.
        First part full name.
        Second Part Short name
        """
        return self._get_raises_list(d=prop, key='raises_get')

    def get_prop_set_raises(self, prop: dict) -> List[Tuple[str, str]]:
        """
        Converts any raises into a list of tuple.
        First part full name.
        Second Part Short name
        """
        return self._get_raises_list(d=prop, key='raises_set')

    def get_prop_get_has_errors(self, prop: dict) -> bool:
        if 'raises_get' in prop:
            if len(prop['raises_get']) > 0:
                return True
        return False

    def get_prop_set_has_errors(self, prop: dict) -> bool:
        if 'raises_set' in prop:
            if len(prop['raises_set']) > 0:
                return True
        return False

    def get_prop_has_errors(self, prop: dict) -> bool:
        if self.get_prop_get_has_errors(prop):
            return True
        if self.get_prop_set_has_errors(prop):
            return True
        return False

    # endregion Raises

    def get_formated_meth(self, meth: dict) -> str:
        name = meth['name']
        iter_args: list = meth['args']
        if len(iter_args) > 0:
            args = 'self, ' + self.get_args(args=meth['args'])
        else:
            args = 'self'
        result = f"def {name}({args})"
        key = 'returns'
        if key in meth:
            ret = meth[key]
            if ret:
                result += f" -> {self.get_q_type(ret)}"
        result += ':'
        return result

    def _is_properties(self) -> bool:
        key = 'properties'
        if not key in self.attribs:
            return False
        return len(self.attribs[key]) > 0

    def get_class_end(self):
        end = ':'
        if not self.include_desc and not self._is_properties():
            end += '\n pass'
        return end

    def get_properties_all(self) -> List[dict]:
        results: List[dict] = []
        key = 'types'
        t_lst = self.attribs.get('types', [])
        p_lst = self.attribs.get('properties', [])
        results.extend(t_lst)
        results.extend(p_lst)
        return results

    def get_sorted_names(self) -> List[Tuple[str, int]]:
        """Gets a list of tuples of name and index"""
        if not self._sorted_key_index is None:
            return self._sorted_key_index
        sorted = []
        d_lst: List[dict] = self.get_properties_all()
        sort: bool = getattr(self, 'sort', False)
        for i, d in enumerate(d_lst):
            sorted.append((d['name'], i))
        if sort:
            sorted.sort()
        self._sorted_key_index = sorted
        return self._sorted_key_index

    def get_nt_names_str(self) -> str:
        sorted_names = self.get_sorted_names()
        d_lst = self.get_properties_all()

        c_str = ''
        i = 0
        for tpl in sorted_names:
            if i > 0:
               c_str += ', '
            index = tpl[1]
            itm: dict = d_lst[index]
            c_str += "'" + self.get_safe_word(itm['name']) + "'"
            i += 1
        if i == 1:
            c_str += ','  # add so tuple is not mistaken as brackets
        return c_str

    def get_constructor_args_str(self, include_value: bool = True, include_type: bool = True, uno_none:bool =True) -> str:
        sorted_names = self.get_sorted_names()
        d_lst = self.get_properties_all()

        c_str = ''
        i = 0
        for tpl in sorted_names:
            if i > 0:
               c_str += ', '
            index = tpl[1]
            itm: dict = d_lst[index]
            # is_q = self.is_q_type(itm['returns'])
            # if is_q:
            #     str_type = self.get_q_wrapped(str_type)
            
            c_str += self.get_safe_word(itm['name'])
            if include_type:
                c_str += f": typing.Optional[{itm['returns']}]"
            if include_value:
                c_str += " = " + \
                    self.get_attrib_default(prop=itm, uno_none=uno_none)
            i += 1
        return c_str

    def get_constructor(self) -> str:
        sorted_names = self.get_sorted_names()
        if len(sorted_names) == 0:
            self._linfo("Constructor Args — False")
            if self.is_parent:
                return "def __init__(self, **kwargs) -> None:"
            return "def __init__(self) -> None:"
        self._linfo("Constructor Args — True")
        names = self.get_constructor_args_str(include_value=True, include_type=True)
        if self.is_parent:
            return f"def __init__(self, {names}, **kwargs) -> None:"
        return f"def __init__(self, {names}) -> None:"

    def get_class_inherits_from_db(self, default: str = 'Exception') -> str:
        # override this method from base class
        # by overriding can used in other methods such as has_uno_extends()
        result = super().get_class_inherits_from_db('object')
        if result == "object":
            return default  # builtin Exception
        return result

    def get_class_inherits(self, class_name: str, imports: Union[str, List[str]]) -> str:
        # override to make default Exception
        result = super().get_class_inherits(class_name=class_name,imports=imports)
        if result == 'object':
            return 'Exception'
        return result

    def has_uno_extends(self) -> bool:
        # com.sun.star.uno.Exception inherits from builtins.Exception
        # and is base class for uno exceptions
        if self.fullname == 'com.sun.star.uno.Exception':
            return False
        if self.allow_db:
            # get_class_inherits_from_db() is a cached method in base
            ext = super().get_class_inherits_from_db('object')
            if ext == 'object':
                return False
            return True
        safe_name = self.get_safe_word(self.name)
        ext = super().get_class_inherits(safe_name, self.inherits)
        return ext != 'object'

    def get_attrib_default(self, prop:dict, uno_none: bool = False) -> str:
        name = prop['name']
        returns = prop['returns']
        result = getattr(self.uno_instance, name, None)
        if isinstance(result, str):
            return f"'{result}'"
        elif isinstance(result, uno.Enum):
            return f"{returns}.{result.value}"
        elif isinstance(result, uno.Char):
            char = ''.join(r'\u{:04X}'.format(ord(chr))
                           for chr in result.value)
            return f"'{char}'"
        elif isinstance(result, uno.ByteSequence):
            if uno_none is True:
                return 'UNO_NONE'
            return 'None'
        elif hasattr(result, '__pyunostruct__'):
            if uno_none is True:
                return 'UNO_NONE'
            if returns == 'object':
                return 'None'
            return f"{returns}()"
        return str(result)

    @property
    def uno_instance(self):
        if self._uno_instance is None:
            self._uno_instance = uno.createUnoStruct(self.fullname)
        return self._uno_instance

    @property
    def is_parent(self) -> bool:
        if self._is_parent is None:
            self._is_parent = self.has_uno_extends()
            self._linfo(
                f"parent — {self._is_parent}")
        return self._is_parent