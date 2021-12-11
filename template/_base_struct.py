# coding: utf-8
import json
from typing import Tuple, List
from _base_tmpl import BaseTpml
from pathlib import Path
from verr import Version


class BaseStruct(BaseTpml):
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
        set_data('auto_imports')
        set_data('namespace')
        set_data('from_imports')
        sort = bool(json_data['parser_args']['sort'])
        self.attribs = self._get_attribs(json_data=json_data, sort=sort)


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
