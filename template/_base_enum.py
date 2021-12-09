# coding: utf-8
from typing import Dict, List
from _base_json import BaseJson
from verr import Version


class BaseEnum(BaseJson):
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
        set_data('ns')
        set_data('desc')
        set_data('url', 'link')
        self.sort = bool(json_data['parser_args'].get('sort', False))

        def get_dict() -> Dict[str, list]:
            # Format:
            # {
            # "ANY": [
            #     "reflecting the any type; anys can carry any UNO value except of any values"
            # ],
            # "ARRAY": [
            #     "Deprecated, UNOIDL does not have an array concept."
            # ]
            # }
            items: List[Dict[str, list]] = data['items']
            result = {}
            for itm in items:
                result[itm['name']] = itm['desc']
            return result

        self.enum_dict = get_dict()
        if self.sort:
            self.enum_dict = self._sort_dict(d=self.enum_dict)

    def _validate_data(self, data: dict) -> bool:
        super()._validate_data(data=data)

        if not data['type'] == 'enum':
            raise Exception(
                f"Invalid Data: Expected type to be 'enum' got '{data['type']}'")
        min_ver = Version(0, 1, 1)
        ver = Version.parse(data.get('version', None))
        if ver < min_ver:
            raise Exception(
                "Invalid Data: Expected version to be at least '{min_ver}' got {ver}")
