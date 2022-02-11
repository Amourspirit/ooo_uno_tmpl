# coding: utf-8
import uno
from typing import Dict, Tuple, List, Union
from _base_json import BaseJson
from verr import Version


class BaseStruct(BaseJson):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self._linfo('hello')
        self._sorted_key_index = None
        self._uno_instance = False

    def _hydrate_data(self, json_data: dict):
        self._validate_data(json_data)
        data: Dict[str, object] = json_data['data']

        def set_data(_key: str, a_name=None):
            attr_name = _key if not a_name else a_name
            val = data.get(_key, None)
            if not val is None:
                setattr(self, attr_name, val)
        # validation ensures min version of 0.1.1
        set_data('name')
        set_data('namespace')
        set_data('allow_db')
        set_data('desc')
        set_data('url', 'link')
        setattr(self, 'inherits', data.get('extends', []))
        set_data('imports')
        set_data('from_imports')
        set_data('from_imports_typing')
        # get lo ver if it exist. Defaut to False
        self.libre_office_ver = json_data.get('libre_office_ver', False)
        quote: List[str] = data.get('quote', [])
        self.quote.update(quote)
        typings: List[str] = data.get('typings', [])
        self.typings.update(typings)

        self.requires_typing = data.get('requires_typing', False)
        self.sort = bool(json_data['parser_args'].get('sort', False))
        self.include_desc = bool(
            json_data['writer_args'].get('include_desc', True))
        self.attribs = self._get_attribs(json_data=json_data, sort=self.sort)
        setattr(self, 'inherits', data.get('extends', []))
        self.dynamic_struct = bool(
            json_data['writer_args'].get('dynamic_struct', False))
        extends_map = data.get('extends_map', None)
        if extends_map:
            self.extends_map.update(extends_map)
        self.fullname = f"{self.namespace}.{self.get_safe_word(self.name)}"

    def _get_attribs(self, json_data: dict, sort: bool) -> dict:
        items: List[dict] = json_data['data']['items']
        if not sort:
            return items
        return self._sort_dicts(lst=items, sort_key='name')

    def _validate_data(self, data: dict):
        super()._validate_data(data=data)
        if not data['type'] == 'struct':
            raise Exception(
                f"Invalid Data: Expected type to be 'struct' got '{data['type']}'")

        if not data['name']:
            raise Exception('Invalid Data: name attribute is not valid')
        min_ver = Version(0, 1, 11)
        if self.json_version < min_ver:
            raise Exception(
                "Invalid Data: Expected version to be at least '{min_ver}' got {ver}")

    def get_sorted_names(self) -> List[Tuple[str, int]]:
        """Gets a list of tuples of name and index"""
        if not self._sorted_key_index is None:
            return self._sorted_key_index
        sorted = []
        d_lst: List[Dict[str, object]] = getattr(self, 'attribs', [])
        sort: bool = getattr(self, 'sort', False)
        for i, d in enumerate(d_lst):
            sorted.append((d['name'], i))
        if sort:
            sorted.sort()
        self._sorted_key_index = sorted
        return self._sorted_key_index

    def get_constructor_str(self, opt: bool) -> str:
        sorted = self.get_sorted_names()
        d_lst: List[Dict[str, object]] = getattr(self, 'attribs', [])

        c_str = ''
        for i, tpl in enumerate(sorted):
            if i > 0:
               c_str += ', '
            index = tpl[1]
            itm: Dict[str, object] = d_lst[index]
            name: str = itm['name']

            if opt:
                t: str = self.get_q_type_opt(itm['type'])
                s = f"{name}: {t} = None"
            else:
                t: str = self.get_q_type(itm['type'])
                s = f"{name}: {t}"
            c_str += s

        return c_str

    def get_q_type_opt(self, in_type: object) -> object:
        """If in_type is in quote then it is quoted.  Otherwise in_type is returned"""
        if not isinstance(in_type, str):
            return in_type
        if in_type in self.quote:
            return f"'typing.Optional[{in_type}]'"
        return f"typing.Optional[{in_type}]"

    def get_nt_names_str(self) -> str:
        sorted = self.get_sorted_names()
        d_lst: List[Dict[str, object]] = getattr(self, 'attribs', [])

        c_str = ''
        i = 0
        for tpl in sorted:
            if i > 0:
               c_str += ', '
            index = tpl[1]
            itm: Dict[str, object] = d_lst[index]
            c_str += "'" + self.get_safe_word(itm['name']) + "'"
            i += 1
        if i == 1:
            c_str += ','  # add so tuple is not mistaken as brackets
        return c_str

    def get_attrib_for_prop(self, index: int) -> Dict[str, object]:
        d_lst: List[Dict[str, object]] = getattr(self, 'attribs', [])
        _ = self.get_sorted_names()
        itm: Dict[str, object] = d_lst[index]
        result = {}
        result.update(itm)
        result['type'] = self.get_q_type(result['type'])
        return result

    def get_constructor_args_str(self, include_value: bool = True) -> str:
        sorted_names = self.get_sorted_names()
        d_lst: List[dict] = getattr(self, 'attribs', [])

        c_str = ''
        i = 0
        for tpl in sorted_names:
            if i > 0:
               c_str += ', '
            index = tpl[1]
            itm: dict = d_lst[index]
            str_type = f"typing.Optional[{itm['type']}]"
            is_q = self.is_q_type(itm['type'])
            if is_q:
                str_type = self.get_q_wrapped(str_type)
            c_str += self.get_safe_word(itm['name'])
            c_str += ": " + str_type
            if include_value:
                c_str += " = " + \
                    self.get_attrib_default(prop=itm, obj_none=True)
            i += 1
        return c_str

    def get_constructor(self) -> str:
        default = "def __init__(self, *args, **kwargs):"
        sorted_names = self.get_sorted_names()
        if len(sorted_names) == 0:
            return default
        if self.uno_instance is None:
            return default
        names = self.get_constructor_args_str()
        return f"def __init__(self, *args, {names}, **kwargs):"

    def get_class_inherits_from_db(self, default: str = 'object') -> str:
        # override this method from base class
        # by overriding can used in other methods such as has_uno_extends()
        result = super().get_class_inherits_from_db('object')
        if result == "object":
            return default  # builtin Exception
        return result

    def get_class_inherits(self, class_name: str, imports: Union[str, List[str]]) -> str:
        # override to make default Exception
        result = super().get_class_inherits(class_name=class_name, imports=imports)
        return result

    def has_uno_extends(self) -> bool:
        # com.sun.star.uno.Exception inherits from builtins.Exception
        # and is base class for uno exceptions
        if self.allow_db:
            # get_class_inherits_from_db() is a cached method in base
            ext = super().get_class_inherits_from_db('object')
            if ext == 'object':
                return False
            return True
        safe_name = self.get_safe_word(self.name)
        ext = super().get_class_inherits(safe_name, self.inherits)
        return ext != 'object'

    def get_attrib_default(self, prop:dict, obj_none: bool = False) -> str:
        if self.uno_instance is None:
            return 'None'
        name = prop['name']
        returns = prop['type']
        result = getattr(self.uno_instance, name, None)
        if isinstance(result, str):
            return f"'{result}'"
        if isinstance(result, uno.Enum):
            return f"{returns}.{result.value}"
        if isinstance(result, uno.ByteSequence):
            if obj_none is True:
                return 'UNO_NONE'
            return 'None'
        if hasattr(result, '__pyunostruct__'):
            if obj_none is True:
                return 'UNO_NONE'
            return f"{returns}()"
        return str(result)

    @property
    def uno_instance(self) -> Union[object, None]:
        if self._uno_instance is False:
            try:
                self._uno_instance = uno.createUnoStruct(self.fullname)
            except Exception as e:
                self._lwarn(
                    f"{self.fullname} Error: {e}")
                self._uno_instance = None
        return self._uno_instance
