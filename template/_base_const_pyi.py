# coding: utf-8
from _base_const import BaseConst
from _base_json import EventArgs

class BaseConstPyi(BaseConst):

    def on_after_init_data(self, args: EventArgs) -> None:
        super().on_after_init_data(args=args)

