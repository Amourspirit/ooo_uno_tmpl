# coding: utf-8
import uno
from typing import Dict, Optional, Set, Tuple, List, Union
from _base_json import BaseJson
from verr import Version
from _base_tmpl import SqlComponent
from oootmpl.template_helper.models_struct import ModelsStruct
from _base_json import EventArgs


class BaseStruct(BaseJson):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self._linfo('hello')
        self._sorted_key_index = None
        self._uno_instance = False
        self._is_parent = None
        self._cache = {}

    def _hydrate_data(self, json_data: dict):
        try:
            self._models = ModelsStruct(json_data=json_data)
        except Exception as e:
            msg = f"Error occured in struct {json_data['namespace']}.{json_data['name']}"
            self._lerr(f"{msg}\n{e}")
            raise Exception(msg) from e
        # self._validate_data(json_data)
        data: Dict[str, object] = json_data['data']

        def set_data(_key: str, a_name=None):
            attr_name = _key if not a_name else a_name
            val = data.get(_key, None)
            if not val is None:
                setattr(self, attr_name, val)
        mdata = self._models.model.data
        self.name = self.get_safe_word(mdata.name)
        self.namespace = mdata.namespace
        self.allow_db = mdata.allow_db
        self.desc = mdata.desc
        self.link = mdata.url
        self.libre_office_ver = self._models.model.libre_office_ver
        setattr(self, 'inherits', data.get('extends', []))
        set_data('imports')
        # set_data('from_imports')
        self.from_imports = [x.as_tuple()
                             for x in self._models.get_full_imports()]
        set_data('from_imports_typing')
        quote: List[str] = data.get('quote', [])
        self.quote.update(quote)
        typings: List[str] = data.get('typings', [])
        self.typings.update(typings)

        self.requires_typing = mdata.requires_typing
        if self.requires_typing is False:
            if self._models.is_args():
                self.requires_typing = True
        self.sort = self._models.model.parser_args.sort
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

    # region Events
    def on_after_init_data(self, args: EventArgs) -> None:
        super().on_after_init_data(args=args)
        self.oenv = self.config.env
    # endregion Events

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

    def get_nt_names_all_str(self) -> str:
        args = self._models.get_class_args_all()
        c_str = ''
        i = 0
        for arg in args:
            if i > 0:
                c_str += ', '
            c_str += "'" + arg.name + "'"
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
        result['type'] = result['type']  # self.get_q_type(result['type'])
        return result

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

    def get_class_args_all(self, uno_none: bool = True):
        # returns list of ClassArg
        return self._models.get_class_args_all(uno_none=uno_none)

    def get_class_args_inst(self, uno_none: bool = True):
        return self._models.get_class_args(uno_none=uno_none)

    def _get_class_args(self, include_value: bool = True, include_type: bool = True, uno_none: bool = True, value: Optional[str] = None):
        args = self._models.get_class_args(uno_none=uno_none)
        results: List[str] = []
        for arg in args:
            s = arg.name
            if include_type:
                s += f": typing.Optional[{arg.type}]"
            if include_value:
                if value is None:
                    s += " = " + \
                        self.get_attrib_default(
                            name=arg.name, returns=arg.type, uno_none=uno_none)
                else:
                    s += value
            results.append(s)
        return results

    def _get_parent_class_args(self, include_value: bool = True, include_type: bool = True, uno_none: bool = True, value: Optional[str] = None):
        args = self._models.get_parents_class_args(uno_none=uno_none)
        results: List[str] = []
        for arg in args:
            s = arg.name
            if include_type:
                s += f": typing.Optional[{arg.type}]"
            if include_value:
                if value is None:
                    s += " = " + \
                        self.get_attrib_default(
                            name=arg.name, returns=arg.type, uno_none=uno_none)
                else:
                    s += value
            results.append(s)
        return results

    def get_constructor_args_str(self, include_value: bool = True, include_type: bool = True, uno_none: bool = True, value: Optional[str] = None) -> str:
        pargs = self._get_parent_class_args(
            include_value=include_value,
            include_type=include_type,
            uno_none=uno_none,
            value=value)
        cargs = self._get_class_args(
            include_value=include_value,
            include_type=include_type,
            uno_none=uno_none,
            value=value)
        args = pargs + cargs
        if len(args) == 0:
            return ""
        return ", ".join(args)

    def get_constructor(self) -> str:
        if not self._models.is_args():
            # this will alomost never happen
            self._linfo("Constructor Args — False")
            return "def __init__(self) -> None:"
        self._linfo("Constructor Args — True")
        names = self.get_constructor_args_str(
            include_value=True, include_type=True)
        # if self.is_parent:
        #     return f"def __init__(self, {names}, **kwargs) -> None:"
        return f"def __init__(self, {names}) -> None:"

    def get_attrib_default(self, name: str, returns: str, uno_none: bool = False) -> str:
        """
        Get defatul attribute value from uno

        Args:
            name (str): Name of property to get attrib for.
            returns (str): property returns type
            uno_none (bool, optional): If ``True`` replaces ``None`` with ``UNO_NONE`` where needed; Otherwise uses ``None``. Defaults to False.

        Returns:
            str: attribute default value as string.

        Note:
            If current exception/struct is not in the installled uno version then
            all unknow value are either ``None`` or ``UNO_NONE``

            For instance ReadOnlyOpenRequest: https://tinyurl.com/ycu8u8wu
            is a 7.2 version
        """
        if self.uno_instance is None:
            return 'None'
        key = f"get_attrib_default_{name}_{returns},_{uno_none}"
        if key in self._cache:
            return self._cache[key]
        result = getattr(self.uno_instance, name, None)
        if isinstance(result, str):

            self._cache[key] = f"'{result}'"
            return self._cache[key]
        elif isinstance(result, uno.Enum):
            self._cache[key] = f"{returns}.{result.value}"
            return self._cache[key]
        elif isinstance(result, uno.Char):
            char = ''.join(r'\u{:04X}'.format(ord(chr))
                           for chr in result.value)
            self._cache[key] = f"'{char}'"
            return self._cache[key]
        elif isinstance(result, uno.ByteSequence):
            if uno_none is True:
                self._cache[key] = 'UNO_NONE'
                return self._cache[key]
            self._cache[key] = 'None'
            return self._cache[key]
        elif isinstance(result, uno.Type):
            self._cache[key] = 'None'
            return self._cache[key]
        elif hasattr(result, '__pyunostruct__'):
            if uno_none is True:
                self._cache[key] = 'UNO_NONE'
                return self._cache[key]
            if returns == 'object':
                self._cache[key] = 'None'
                return self._cache[key]
            self._cache[key] = f"{returns}()"
            return self._cache[key]
        db_comp = SqlComponent()
        is_typedef = db_comp.is_type_from_map_name(
            map_name=returns, tipe='typedef')
        if is_typedef:
            if result is None:
                self._linfo(
                    f"typedef — constructor arg: {name}: {returns} = {result}")
                self._cache[key] = f"{result}"
                return self._cache[key]
            self._linfo(
                f"typedef — constructor arg: {name}: {returns} = {returns}({result})")
            self._cache[key] = f"{returns}({result})"
            return self._cache[key]
        self._cache[key] = str(result)
        return self._cache[key]

    def get_constructor_types(self) -> Set[str]:
        key = 'get_constructor_types'
        if key in self._cache:
            return self._cache[key]
        d_lst: List[dict] = getattr(self, 'attribs', [])
        result = set()
        for itm in d_lst:
            tipe = itm['type']
            if tipe == 'object':
                continue
            attr = getattr(self.uno_instance, itm['name'], None)
            if attr is None:
                continue
            if isinstance(attr, uno.Enum):
                result.add(tipe)
            elif hasattr(attr, '__pyunostruct__'):
                result.add(tipe)
        self._cache[key] = result
        return self._cache[key]

    def is_constructor_type(self, imp: List) -> bool:
        # imp will be two or three elements
        # last element will match constructor type
        c_types = self.get_constructor_types()
        if len(c_types) == 0:
            return False
        el: str = imp[-1:][0]
        # self._linfo(str(el))
        return el in c_types

    def is_args(self) -> bool:
        """
        Gets if there is any args for current instance or its parent classes.

        Returns:
            bool: ``True`` if instance or parent classes have constructor args;
            Otherwise ``False``.
        """
        return self._models.is_args()

    def is_inst_args(self) -> bool:
        """
        Gets if there is any args for current instance only.

        Returns:
            bool: ``True`` if instance has constructor args;
            Otherwise ``False``.
        """
        args = self._models.get_class_args()
        return len(args) > 0

    def is_parent_args(self) -> bool:
        """
        Gets if there is any args for parents only.

        Returns:
            bool: ``True`` if any partent has constructor args;
            Otherwise ``False``.
        """
        args = self._models.get_parents_class_args()
        return len(args) > 0

    @property
    def uno_instance(self) -> Union[object, None]:
        """
        Get a uno instance of current uno exception being processed

        Returns:
            Any: return uno instance if it can be created; Otherwise, ``None``

        Note:
            not all exceptions/struct are available in all version.
            ReadOnlyOpenRequest: https://tinyurl.com/ycu8u8wu
            is a 7.2 version
        """
        if self._uno_instance is False:
            try:
                self._uno_instance = uno.createUnoStruct(self.fullname)
            except Exception as e:
                self._lwarn(
                    f"{self.fullname} Error: {e}")
                self._uno_instance = None
        return self._uno_instance

    @property
    def is_parent(self) -> bool:
        if self._is_parent is None:
            self._is_parent = self.has_uno_extends()
            self._linfo(
                f"parent — {self._is_parent}")
        return self._is_parent

    @property
    def models(self) -> ModelsStruct:
        return self._models
