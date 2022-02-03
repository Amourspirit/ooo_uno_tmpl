# coding: utf-8
import os
from _base_singleton import BaseSingleton


class BaseSingletonDyn(BaseSingleton):

    def _hydrate_data(self, json_data: dict):
        super()._hydrate_data(json_data=json_data)
        self.uno_obj = os.environ.get('config_uno_obj_dir', 'uno_obj')
        self.dyn = os.environ.get('config_dyn_dir', 'dyn')
