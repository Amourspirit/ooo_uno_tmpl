# coding: utf-8
import os
from _base_interface import BaseInterface
from _base_json import EventArgs

class BaseInterfaceDyn(BaseInterface):

    def on_after_init_data(self, args: EventArgs) -> None:
        super().on_after_init_data(args=args)
        self.uno_obj = self.config.uno_obj_dir
        self.dyn = self.config.dyn_dir
        self.oenv = self.config.env
        self.helper_ns = self.config.helper_ns
        self.helper_mod = self.config.helper_mod
