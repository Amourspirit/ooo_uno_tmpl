# coding: utf-8
from typing import Dict, List
from _base_json import BaseJson
from verr import Version


class BaseService(BaseJson):
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
        set_data('from_imports')
        _inherits = self.convert_lst_last(data.get('extends', []))
        setattr(self, 'inherits', _inherits)
        self.include_desc = bool(json_data['writer_args'].get('include_desc', True))
            
        

    def _validate_data(self, data: dict) -> bool:
        super()._validate_data(data=data)

        if not data['type'] == 'service':
            raise Exception(
                f"Invalid Data: Expected type to be 'service' got '{data['type']}'")
        min_ver = Version(0, 1, 2)
        ver = Version.parse(data.get('version', None))
        if ver < min_ver:
            raise Exception(
                "Invalid Data: Expected version to be at least '{min_ver}' got {ver}")

    def get_class_end(self):
        end = ':'
        if not self.include_desc:
            end += ' ...'
        return end