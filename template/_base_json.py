# coding: utf-8
from abc import abstractmethod
import json
from typing import Dict
from _base_tmpl import BaseTpml
from pathlib import Path
from verr import Version

class BaseJson(BaseTpml):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._is_class_init = False
        self._json_version: Version = None

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

    @abstractmethod
    def _hydrate_data(self, json_data: dict): pass

    def _validate_data(self, data: dict) -> bool:
        if not data:
            raise Exception('Invalid Data: No Data to validate')
        if not isinstance(data, dict):
            raise Exception('Invalid Data: Expected a dictionary. Got: ' + type(data))
        if not 'data' in data:
            raise Exception('Invalid Data: data attribute is missing')
        if not 'id' in data:
            raise Exception('Invalid Data: Data has no id attribute')
        if not 'type' in data:
            raise Exception('Invalid Data: Data has no type attribute')
        if not 'name' in data:
            raise Exception('Invalid Data: Data has no name attribute')
        if not data['id'] == 'uno-ooo-parser':
            raise Exception(
                f"Invalid Data: Expected type to be 'uno-ooo-parser' got '{data['id']}'")
        if not data['name']:
            raise Exception('Invalid Data: name attribute missing')
        try:
            self._json_version = Version.parse(data['version'])
        except Exception:
            raise Exception('Invalid Data: version attribute missing or malformed')
        _data: Dict[str, object] = data['data']
        ver_0_1_6 = Version(0, 1, 6)
        if self._json_version >= ver_0_1_6:
            if not 'quote' in _data:
                raise Exception('Invalid Data: data attribute does not have a quote attribute')
            if not 'typings' in _data:
                raise Exception(
                    'Invalid Data: data attribute does not have a typings attribute')

    @property
    def json_version(self) -> Version:
        return self._json_version