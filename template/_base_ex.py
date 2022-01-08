# coding: utf-8
from typing import Dict, List, Tuple
from _base_json import BaseJson
from verr import Version


class BaseEx(BaseJson):
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

        set_data('name')
        set_data('namespace')
        set_data('desc')
        set_data('url', 'link')
        setattr(self, 'inherits', data.get('extends', []))
        set_data('imports')
        set_data('namespace')
        self.sort = bool(json_data['parser_args'].get('sort', False))
        # get lo ver if it exist. Defaut to False
        self.libre_office_ver = json_data.get('libre_office_ver', False)
        self.include_desc = bool(
            json_data['writer_args'].get('include_desc', True))
        self.attribs = self._get_attribs(json_data=json_data, sort=self.sort)
        self.from_imports = []
        self.from_imports_typing = []
        self.requires_typing = bool(data.get('requires_typing', False))
        set_data('from_imports')
        set_data('from_imports_typing')
        extends_map = data.get('extends_map', None)
        if extends_map:
            self.extends_map.update(extends_map)
        # self.requires_typing = False if len(
        #     self.from_imports_typing) == 0 else True
        quote: List[str] = data.get('quote', [])
        self.quote.update(quote)
        typings: List[str] = data.get('typings', [])
        self.typings.update(typings)

    def _get_attribs(self, json_data: dict, sort: bool) -> dict:
        items: dict = json_data['data']['items']
        if not sort:
            return items

        def sort_lst_dict(_key: str, sort_key: str) -> List[dict]:
            key_index: List[Tuple[str, int]] = []
            lst = items[_key]
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
            # k, properties, list of dict
            result[k] = sort_lst_dict(k, 'name')
        return result

    def _validate_data(self, data: dict):
        super()._validate_data(data=data)

        if not data['type'] == 'exception':
            raise Exception(
                f"Invalid Data: Expected type to be 'exception' got '{data['type']}'")
        min_ver = Version(0, 1, 2)
        if self.json_version < min_ver:
            raise Exception(
                "Invalid Data: Expected version to be at least '{min_ver}' got {ver}")

    def _is_properties(self) -> bool:
        key = 'properties'
        if not key in self.attribs:
            return False
        return len(self.attribs[key]) > 0

    # region Raises Methods
    def _get_raises_list(self, d: dict, key: str) -> List[Tuple[str, str]]:
        """
        Converts any raises into a list of tuple.
        First part full name.
        Second Part Short name
        """
        results = []
        if key in d:
            lst = d[key]
            for r in lst:
                results.append((r, self.get_last_part(r)))
        return results

    def get_raises_list(self, meth: dict) -> List[Tuple[str, str]]:
        """
        Converts any raises into a list of tuple.
        First part full name.
        Second Part Short name
        """
        return self._get_raises_list(d=meth, key='raises')

    def get_prop_get_raises(self, prop: dict) -> List[Tuple[str, str]]:
        """
        Converts any raises into a list of tuple.
        First part full name.
        Second Part Short name
        """
        return self._get_raises_list(d=prop, key='raises_get')

    def get_prop_set_raises(self, prop: dict) -> List[Tuple[str, str]]:
        """
        Converts any raises into a list of tuple.
        First part full name.
        Second Part Short name
        """
        return self._get_raises_list(d=prop, key='raises_set')

    def get_prop_get_has_errors(self, prop: dict) -> bool:
        if 'raises_get' in prop:
            if len(prop['raises_get']) > 0:
                return True
        return False

    def get_prop_set_has_errors(self, prop: dict) -> bool:
        if 'raises_set' in prop:
            if len(prop['raises_set']) > 0:
                return True
        return False

    def get_prop_has_errors(self, prop: dict) -> bool:
        if self.get_prop_get_has_errors(prop):
            return True
        if self.get_prop_set_has_errors(prop):
            return True
        return False
    # endregion Raises Methods

    def get_class_end(self):
        end = ':'
        if not self.include_desc and not self._is_properties():
            end += '\n    pass'
        return end