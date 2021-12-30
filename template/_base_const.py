# coding: utf-8
from typing import Dict, List
from _base_json import BaseJson, CancelEventArgs
from verr import Version


class BaseConst(BaseJson):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self._linfo('hello')

    def _hydrate_data(self, json_data: dict):
        # print('# _hydrate_data()')
        data: Dict[str, object] = json_data['data']

        def set_data(_key: str, a_name=None):
            attr_name = _key if not a_name else a_name
            val = data.get(_key, None)
            if val:
                setattr(self, attr_name, val)
        # validation ensures min version

        set_data('name')
        set_data('namespace')
        set_data('desc')
        set_data('url', 'link')
        set_data('imports')
        set_data('from_imports')
        set_data('from_typing_imports')
        set_data('base_class')
        self.requires_typing = bool(data.get('requires_typing', False))
        self.sort = bool(json_data['parser_args'].get('sort', False))
        self.hex = bool(json_data['writer_args'].get('hex', False))
        self.flags = bool(data.get('flags', False))
        quote: List[str] = data.get('quote', [])
        self.quote.update(quote)
        typings: List[str] = data.get('typings', [])
        self.typings.update(typings)
        # NameMapper.NotFound: cannot find 'keys' while searching for 'keys'
        # _dict = self._get_attribs(data=data, sort=self.sort)
       
            
        self.attribs = data['items']
        if self.sort:
            self.attribs = self._sort_dicts(lst=self.attribs, sort_key='name')


    def _validate_data(self, data: dict) -> bool:
        super()._validate_data(data=data)
        
        if not data['type'] == 'const':
            raise Exception(
                f"Invalid Data: Expected type to be 'const' got '{data['type']}'")
        min_ver = Version(0, 1, 9)
        ver = Version.parse(data.get('version', None))
        if ver < min_ver:
            raise Exception(
                "Invalid Data: Expected version to be at least '{min_ver}' got {ver}")

    def on_before_load_data(self, args: CancelEventArgs) -> None:
        if not self.auto_load:
            if self.sort:
                self.attribs = self._sort_dicts(lst=self.attribs, sort_key='name')
