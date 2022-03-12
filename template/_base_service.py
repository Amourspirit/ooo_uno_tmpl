# coding: utf-8
from verr import Version
from typing import Dict, Tuple, List
from _base_json import BaseJson
from oootmpl.model.service.model_service import ModelService


class BaseService(BaseJson):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _hydrate_data(self, json_data: dict):
        try:
            self._model = ModelService(**json_data)
        except Exception as e:
            msg = f"Error occured in service {json_data['namespace']}.{json_data['name']}"
            self._lerr(f"{msg}\n{e}")
            raise Exception(msg) from e
        # self._validate_data(json_data)
        mdata = self._model.data
        self.name = self.get_safe_word(mdata.name)
        self.namespace = mdata.namespace
        self.allow_db = mdata.allow_db
        self.desc = mdata.desc
        self.link = mdata.url
        self.libre_office_ver = self._model.libre_office_ver
        self.include_desc = self._model.writer_args.include_desc
        self.requires_typing = mdata.requires_typing
        self.inherits = mdata.extends
        self.imports = mdata.imports
        self.extends_map.update(mdata.extends_map)

        sort = self._model.parser_args.sort
        self.attribs = self._get_attribs(json_data=json_data, sort=sort)
        self.from_imports = [x.as_tuple()
                             for x in mdata.from_imports]
        self.from_imports_typing = [x.as_tuple()
                                    for x in mdata.from_imports_typing]
        self.quote.update(mdata.quote)
        self.typings.update(mdata.typings)

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

        if not data['type'] == 'service':
            raise Exception(
                f"Invalid Data: Expected type to be 'service' got '{data['type']}'")

        if not data['name']:
            raise Exception('Invalid Data: name attribute is not valid')
        min_ver = Version(0, 1, 1)
        ver = Version.parse(data.get('version', None))
        if ver < min_ver:
            raise Exception(
                "Invalid Data: Expected version to be at least '{min_ver}' got {ver}")

    def _get_formated_arg(self, arg: Dict[str, str]) -> str:
        return f"{self.get_safe_word(arg['name'])}: {self.get_q_type(arg['type'])}"

    def get_args(self, args: List[Dict[str, str]]) -> str:
        result = ''
        for i, arg in enumerate(args):
            if i > 0:
                result += ', '
            result += self._get_formated_arg(arg=arg)
        return result

    def get_out_args(self, meth: dict) -> List[str]:
        args: list = meth['args']
        results: List[str] = []
        for arg in args:
            direction = arg['direction']
            if self.is_out_arg(direction):
                results.append(arg['name'])
        return results

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

    def get_formated_meth(self, meth: dict) -> str:
        name = meth['name']
        iter_args: list = meth['args']
        if len(iter_args) > 0:
            args = 'self, ' + self.get_args(args=meth['args'])
        else:
            args = 'self'
        result = f"def {name}({args})"
        key = 'returns'
        if key in meth:
            ret = meth[key]
            if ret:
                result += f" -> {self.get_q_type(ret)}"
        result += ':'
        return result
