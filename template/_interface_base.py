# coding: utf-8
import logging
import os
import sys
import json
from typing import Tuple, List
from _tmpl_base import BaseTpml
from pathlib import Path
from verr import Version
from inspect import getsourcefile
_logger_module = None


class BaseInterface(BaseTpml):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self._linfo('hello')

    def init_data(self):
        super().init_data()
        if getattr(self, 'auto_load', None) is None:
            self.auto_load = False
        # setting path in init_data allows for json_data_file
        # to be overridden in template
        self._linfo('init template.')
        data_file = getattr(self, 'json_data_file', None)
        if data_file is None:
            p = Path(__file__).parent  # dir
            p = Path(p, self.__class__.__name__ + '.json')
            self._json_data_file = str(p)
        else:
            self._json_data_file = data_file
        self._is_class_init = True

    def load_data(self):
        super().load_data()
        if not self._is_class_init:
            self._lerr('load_data() called without calling init_data() first')
            return
        if not self.auto_load:
            self._linfo('Auto Load disabled.')
            return
        json_data: dict = None
        p_j = Path(self._json_data_file)
        if not p_j.is_absolute():
            p_j = Path(Path(__file__).parent, p_j)
        with open(p_j) as file:
            json_data: dict = json.load(file)
        try:
            self._validate_data(json_data)
        except Exception as e:
            self._lerr('load_data() Validation Failed: %s', str(e))
            return
        try:
            self._hydrate_data(json_data)
        except Exception as e:
            self._lerr(e)
            raise e

    def _hydrate_data(self, json_data: dict):
        data = json_data['data']

        def set_data(_key: str, a_name=None):
            attr_name = _key if not a_name else a_name
            val = data.get(_key, None)
            if val:
                setattr(self, attr_name, val)
        # validation ensures min version of 0.1.1

        set_data('name')
        set_data('desc')
        set_data('url', 'link')
        _inherits = self.convert_lst_last(data.get('extends', []))
        setattr(self, 'inherits', _inherits)
        set_data('imports')
        set_data('namespace')
        sort = bool(json_data['parser_args']['sort'])
        self.attribs = self._get_attribs(json_data=json_data, sort=sort)
        ver_0_1_1 = Version(0, 1, 1)
        ver_json = Version.parse(json_data.get('version'))
        if ver_json == ver_0_1_1:
            self._load_0_1_1(json_data=json_data)
        else:
            setattr(self, 'requires_typing', True)
            setattr(self, 'from_imports', [])
            setattr(self, 'from_imports_typing', [])
            set_data('from_imports')
            set_data('from_imports_typing')
            self.requires_typing = False if len(
                self.from_imports_typing) == 0 else True

    def _load_0_1_1(self, json_data: dict):
        def set_j_data(_key: str):
            val = json_data.get(_key, None)
            if val:
                setattr(self, _key, val)
        set_j_data('from_imports')
        set_j_data('from_imports_typing')
        from_imports_typing = json_data.get('from_imports_typing', [])
        if len(from_imports_typing) == 0:
            setattr(self, 'requires_typing', False)
        else:
            setattr(self, 'requires_typing', True)

    def _get_attribs(self, json_data: dict, sort: bool) -> dict:
        items: dict = json_data['data']['items']
        if not sort:
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
        keys = items.keys()
        result = {}
        for k in keys:
            result[k] = sort_lst_dict(k, 'name')
        return result

    def _validate_data(self, data: dict) -> bool:
        if not data:
            raise Exception('Invalid Data: No Data to validate')
        if not 'id' in data:
            raise Exception('Invalid Data: Data has no id attribute')
        if not 'type' in data:
            raise Exception('Invalid Data: Data has no type attribute')
        if not 'name' in data:
            raise Exception('Invalid Data: Data has no name attribute')
        if not data['id'] == 'uno-ooo-parser':
            raise Exception(
                f"Invalid Data: Expected type to be 'ooo' got '{data['id']}'")
        if not data['type'] == 'interface':
            raise Exception(
                f"Invalid Data: Expected type to be 'interface' got '{data['type']}'")
        
        if not data['name']:
            raise Exception('Invalid Data: name attribute is not valid')
        min_ver = Version(0, 1, 1)
        ver = Version.parse(data.get('version', None))
        if ver < min_ver:
            raise Exception("Invalid Data: Expected version to be at least '{min_ver}' got {ver}")

    def _get_formated_arg(self, arg: Tuple[str]) -> str:
        return f"{arg[0]}: {arg[1]}"

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
                    results.append(arg[1])  # arg name
        return results

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
                result += f" -> {ret}"
        result += ':'
        return result

