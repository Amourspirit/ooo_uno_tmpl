# coding: utf-8
from typing import Dict, List
from _base_json import BaseJson
from verr import Version


class BaseConst(BaseJson):
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
        # validation ensures min version of 0.1.1

        set_data('name')
        set_data('namespace')
        set_data('desc')
        set_data('url', 'link')
        set_data('imports')
        set_data('from_imports')
        self.sort = bool(json_data['parser_args'].get('sort', False))
        self.hex = bool(json_data['writer_args'].get('hex', False))
        self.flags = bool(json_data['writer_args'].get('flags',False))
        
        # NameMapper.NotFound: cannot find 'keys' while searching for 'keys'
        # _dict = self._get_attribs(data=data, sort=self.sort)
        def get_const_dict() -> Dict[str, list]:
            # Format:
            # "INVALID": ["0", [
            #     "Invalid relation type.",
            #     "",
            #     "Indicates an invalid relation type. This is used to indicate that a retrieval method could not find a requested relation."
            # ]]
            items: List[Dict[str, list]] = data['items']
            result = {}
            for itm in items:
                itm_lst = [
                    itm['value'],
                    itm['lines']
                    ]
                
                result[itm['name']] = itm_lst
            return result
            
        self.const_dict = get_const_dict()
        if self.sort:
            self.const_dict = self._sort_dict(d=self.const_dict)


    def _validate_data(self, data: dict) -> bool:
        super()._validate_data(data=data)
        
        if not data['type'] == 'const':
            raise Exception(
                f"Invalid Data: Expected type to be 'const' got '{data['type']}'")
        min_ver = Version(0, 1, 1)
        ver = Version.parse(data.get('version', None))
        if ver < min_ver:
            raise Exception(
                "Invalid Data: Expected version to be at least '{min_ver}' got {ver}")
