# coding: utf-8
from typing import List
from _base_json import BaseJson
from verr import Version


class BaseTypeDef(BaseJson):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _hydrate_data(self, json_data: dict):
        self._validate_data(json_data)
        data = json_data['data']

        def set_data(_key: str, a_name=None):
            attr_name = _key if not a_name else a_name
            val = data.get(_key, None)
            if not val is None:
                setattr(self, attr_name, val)

        set_data('name')
        set_data('namespace')
        set_data('allow_db')
        set_data('type')
        set_data('requires_typing')
        set_data('desc')
        set_data('url', 'link')
        set_data('from_imports')
        # get lo ver if it exist. Defaut to False
        self.libre_office_ver = json_data.get('libre_office_ver', False)
        self.include_desc = bool(
            json_data['writer_args'].get('include_desc', True))
        quote: List[str] = data.get('quote', [])
        self.quote.update(quote)
        typings: List[str] = data.get('typings', [])
        self.typings.update(typings)
        set_data('imports')

    def _validate_data(self, data: dict) -> bool:
        super()._validate_data(data=data)

        if not data['type'] == 'typedef':
            raise Exception(
                f"Invalid Data: Expected type to be 'typedef' got '{data['type']}'")
        min_ver = Version(0, 1, 5)
        ver = Version.parse(data.get('version', None))
        if ver < min_ver:
            raise Exception(
                "Invalid Data: Expected version to be at least '{min_ver}' got {ver}")

