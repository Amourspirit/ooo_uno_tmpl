# coding: utf-8
import os
from _base_ex import BaseEx
from _base_json import EventArgs

class BaseExDyn(BaseEx):

    def on_after_init_data(self, args: EventArgs) -> None:
        super().on_after_init_data(args=args)
        self.uno_obj = self.config.uno_obj_dir
        self.dyn = self.config.dyn_dir
        self.oenv = self.config.env
        self.helper_ns = self.config.helper_ns
        self.enum_mod = self.config.enum_mod
