# coding: utf-8
from typing import Dict, List
from _base_json import BaseJson, CancelEventArgs
from verr import Version


class BaseConst(BaseJson):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self._linfo('hello')

    def _hydrate_data(self, json_data: dict):
        self._validate_data(json_data)
        data: Dict[str, object] = json_data['data']

        def set_data(_key: str, a_name=None):
            attr_name = _key if not a_name else a_name
            val = data.get(_key, None)
            if val:
                setattr(self, attr_name, val)
        # validation ensures min version

        set_data('name')
        set_data('namespace')
        set_data('allow_db')
        set_data('desc')
        set_data('url', 'link')
        set_data('imports')
        set_data('from_imports')
        set_data('from_typing_imports')
        set_data('base_class')
        # get lo ver if it exist. Defaut to False
        self.libre_office_ver = json_data.get('libre_office_ver', False)
        self.requires_typing = bool(data.get('requires_typing', False))
        self.hex = bool(json_data['writer_args'].get('hex', False))
        self.flags = bool(data.get('flags', False))
        quote: List[str] = data.get('quote', [])
        self.quote.update(quote)
        typings: List[str] = data.get('typings', [])
        self.typings.update(typings)
        # NameMapper.NotFound: cannot find 'keys' while searching for 'keys'
        # _dict = self._get_attribs(data=data, sort=self.sort)
       
        # Note: attribs should never be sorted.
        # Some const have flags and original order must be maintained.
        # see: https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1i18n_1_1KParseTokens.html
        self.attribs = data['items']
  


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

