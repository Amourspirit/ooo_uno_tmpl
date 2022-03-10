# coding: utf-8
import uno
from typing import Any, Dict, List, Tuple, Union
from _base_json import BaseJson
from verr import Version
from oootmpl.template_helper.models_exception import ModelsException


class BaseEx(BaseJson):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._sorted_key_index = None
        self._uno_instance: Any = False
        self._is_parent = None
        self._cache = {}

    def _hydrate_data(self, json_data: dict):
        self._models = ModelsException(json_data=json_data)
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
        setattr(self, 'inherits', data.get('extends', []))
        set_data('imports')
        # get lo ver if it exist. Defaut to False
        self.libre_office_ver = json_data.get('libre_office_ver', False)
        sort = bool(json_data['parser_args'].get('sort', False))
        self.include_desc = bool(
            json_data['writer_args'].get('include_desc', True))
        self.attribs = self._get_attribs(json_data=json_data, sort=sort)
        self.requires_typing = mdata.requires_typing
        if self.requires_typing is False:
            if self._models.is_args():
                self.requires_typing = True
        self.from_imports = [x.as_tuple()
                             for x in self._models.get_full_imports()]
        setattr(self, 'from_imports_typing', [])
        set_data('from_imports_typing')
        quote: List[str] = data.get('quote', [])
        self.quote.update(quote)
        typings: List[str] = data.get('typings', [])
        self.typings.update(typings)
        extends_map = data.get('extends_map', None)
        if extends_map:
            self.extends_map.update(extends_map)
        self.fullname = f"{self.namespace}.{self.name}"

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

    def get_class_args_all(self, uno_none: bool = True):
        # returns list of ClassArg
        return self._models.get_class_args_all(uno_none=uno_none)

    def get_class_args_inst(self, uno_none: bool = True):
        return self._models.get_class_args(uno_none=uno_none)

    def _get_class_args(self, include_value: bool = True, include_type: bool = True, uno_none: bool = True):
        args = self._models.get_class_args(uno_none=uno_none)
        results: List[str] = []
        for arg in args:
            s = arg.name
            if include_type:
                s += f": typing.Optional[{arg.type}]"
            if include_value:
                s += " = " + \
                    self.get_attrib_default(
                        name=arg.name, returns=arg.type, uno_none=uno_none)
            results.append(s)
        return results
    
    def _get_parent_class_args(self, include_value: bool = True, include_type: bool = True, uno_none: bool = True):
        args = self._models.get_parents_class_args(uno_none=uno_none)
        results: List[str] = []
        for arg in args:
            s = arg.name
            if include_type:
                s += f": typing.Optional[{arg.type}]"
            if include_value:
                s += " = " + \
                    self.get_attrib_default(
                        name=arg.name, returns=arg.type, uno_none=uno_none)
            results.append(s)
        return results

    def get_constructor_args_str(self, include_value: bool = True, include_type: bool = True, uno_none: bool = True) -> str:
        pargs = self._get_parent_class_args(
            include_value=include_value,
            include_type=include_type,
            uno_none=uno_none)
        cargs = self._get_class_args(
            include_value=include_value,
            include_type=include_type,
            uno_none=uno_none)
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

    def get_class_inherits_from_db(self, default: str = 'Exception') -> str:
        # override this method from base class
        # by overriding can used in other methods such as has_uno_extends()
        result = super().get_class_inherits_from_db('object')
        if result == "object":
            return default  # builtin Exception
        return result

    def get_class_inherits(self, class_name: str, imports: Union[str, List[str]]) -> str:
        # override to make default Exception
        result = super().get_class_inherits(class_name=class_name, imports=imports)
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
            if uno_none is True:
                return 'UNO_NONE'
            return 'None'
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
    def uno_instance(self) -> Any:
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
    def models(self) -> ModelsException:
        return self._models