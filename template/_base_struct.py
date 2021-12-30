# coding: utf-8
import json
from typing import Dict, Tuple, List
from _base_tmpl import BaseTpml
from pathlib import Path
from verr import Version


class BaseStruct(BaseTpml):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self._linfo('hello')
        self._sorted_key_index = None

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
        self._linfo('Auto Loaded file: %s', str(p_j))
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
        data: Dict[str, object] = json_data['data']

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
        set_data('auto_imports')
        set_data('namespace')
        set_data('from_imports')
        quote: List[str] = data.get('quote', [])
        self.quote.update(quote)
        typings: List[str] = data.get('typings', [])
        self.typings.update(typings)

        self.requires_typing = data.get('requires_typing', False)
        sort = bool(json_data['parser_args']['sort'])
        self.attribs = self._get_attribs(json_data=json_data, sort=sort)
        ver_json = Version.parse(json_data.get('version'))
        ver_0_1_3 = Version(0, 1, 3)
        if ver_json > ver_0_1_3:
            # self.requires_typing = data.get('requires_typing', False)
            _inherits = self.convert_lst_last(data.get('extends', []))
            setattr(self, 'inherits', _inherits)
            self.dynamic_struct = bool(
                json_data['writer_args'].get('dynamic_struct', False))

    def _get_attribs(self, json_data: dict, sort: bool) -> dict:
        items: List[dict] = json_data['data']['items']
        if not sort:
            return items
        return self._sort_dicts(lst=items, sort_key='name')

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
        if not data['type'] == 'struct':
            raise Exception(
                f"Invalid Data: Expected type to be 'struct' got '{data['type']}'")

        if not data['name']:
            raise Exception('Invalid Data: name attribute is not valid')
        min_ver = Version(0, 1, 2)
        ver = Version.parse(data.get('version', None))
        if ver < min_ver:
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

    def get_constructor_str(self) -> str:
        sorted = self.get_sorted_names()
        d_lst: List[Dict[str, object]] = getattr(self, 'attribs', [])
        
        c_str = ''
        for i, tpl in enumerate(sorted):
            if i > 0:
               c_str += ', ' 
            index = tpl[1]
            itm: Dict[str, object] = d_lst[index]
            name: str = itm['name']
            t: str = self.get_q_type(itm['type'])
            s = f"{name}: {t}"
            c_str += s
            
        return c_str
    
    def get_nt_names_str(self) -> str:
        sorted = self.get_sorted_names()
        d_lst: List[Dict[str, object]] = getattr(self, 'attribs', [])

        c_str = ''
        for i, tpl in enumerate(sorted):
            if i > 0:
               c_str += ', '
            index = tpl[1]
            itm: Dict[str, object] = d_lst[index]
            c_str += "'" + self.get_safe_word(itm['name']) + "'"

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
