# coding: utf-8
from _base_typedef import BaseTypeDef
from _base_json import EventArgs


class BaseTypeDefDyn(BaseTypeDef):

    def on_after_init_data(self, args: EventArgs) -> None:
        super().on_after_init_data(args=args)
        self.uno_obj = self.config.uno_obj_dir
        self.dyn = self.config.dyn_dir

