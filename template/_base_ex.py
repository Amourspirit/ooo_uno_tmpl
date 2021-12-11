# coding: utf-8
from typing import Dict, List
from _base_json import BaseJson
from verr import Version


class BaseEx(BaseJson):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self._linfo('hello')

    def _hydrate_data(self, json_data: dict):
        # print('# _hydrate_data()')
        data = json_data['data']

        def set_data(_key: str, a_name=None):
            attr_name = _key if not a_name else a_name
            val = data.get(_key, None)
            if val:
                setattr(self, attr_name, val)

        set_data('name')
        set_data('namespace')
        set_data('desc')
        set_data('url', 'link')
        _inherits = self.convert_lst_last(data.get('extends', []))
        setattr(self, 'inherits', _inherits)
        set_data('imports')
        set_data('namespace')
        self.sort = bool(json_data['parser_args'].get('sort', False))
        self.include_desc = bool(
            json_data['writer_args'].get('include_desc', True))
        self.attribs = self._get_attribs(json_data=json_data, sort=self.sort)
  
        self.from_imports = []
        self.from_imports_typing = []
        set_data('from_imports')
        set_data('from_imports_typing')
        self.requires_typing = False if len(
            self.from_imports_typing) == 0 else True

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
        super()._validate_data(data=data)

        if not data['type'] == 'exception':
            raise Exception(
                f"Invalid Data: Expected type to be 'exception' got '{data['type']}'")
        min_ver = Version(0, 1, 2)
        ver = Version.parse(data.get('version', None))
        if ver < min_ver:
            raise Exception(
                "Invalid Data: Expected version to be at least '{min_ver}' got {ver}")
