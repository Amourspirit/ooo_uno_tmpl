# coding: utf-8
from _base_typedef import BaseTypeDef
from _base_json import EventArgs

class BaseTypeDefPyi(BaseTypeDef):

    def on_after_init_data(self, args: EventArgs) -> None:
        super().on_after_init_data(args=args)


