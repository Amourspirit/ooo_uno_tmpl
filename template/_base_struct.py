# coding: utf-8
import json
from typing import Dict, Tuple, List
from _base_json import BaseJson
from pathlib import Path
from verr import Version


class BaseStruct(BaseJson):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self._linfo('hello')
        self._sorted_key_index = None


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
        
        d_lst: List[Dict[str, object]] = self.attribs.get('properties', [])
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
        d_lst: List[Dict[str, object]] = self.attribs.get('properties', [])

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
            c_str += ',' # add so tuple is not mistaken as brackets
        return c_str
    
    def get_attrib_for_prop(self, index: int) -> Dict[str, object]:
        d_lst: List[Dict[str, object]] = getattr(self, 'attribs', [])
        _ = self.get_sorted_names()
        itm: Dict[str, object] = d_lst[index]
        result = {}
        result.update(itm)
        result['type'] = self.get_q_type(result['type'])
        # is_py_type: bool = bool(result.get('is_py_type', False))
        # if not is_py_type:
        #     result['type'] = "'" + result['type'] + "'"
        return result
