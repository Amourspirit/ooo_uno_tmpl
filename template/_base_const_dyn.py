# coding: utf-8
from _base_const import BaseConst
from _base_json import EventArgs

class BaseConstDyn(BaseConst):

    def on_after_init_data(self, args: EventArgs) -> None:
        super().on_after_init_data(args=args)
        self.uno_obj = self.config.uno_obj_dir
        self.dyn = self.config.dyn_dir
        self.oenv = self.config.env
        

    def _hydrate_data(self, json_data: dict):
        super()._hydrate_data(json_data)
        if self.flags:
            self.enum_class = "IntFlag"
        else:
            self.enum_class = "IntEnum"

        if self.pytype:
            if self.pytype == "int":
                if self.flags:
                    self.enum_class = "IntFlag"
                else:
                    self.enum_class = "IntEnum"
            elif self.pytype == "float":
                self.enum_class = "Enum"
            else:
                self.enum_class = "Enum"