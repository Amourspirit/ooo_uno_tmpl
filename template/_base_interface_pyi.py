# coding: utf-8
from _base_interface import BaseInterface
from _base_json import EventArgs

class BaseInterfacePyi(BaseInterface):

    def on_after_init_data(self, args: EventArgs) -> None:
        super().on_after_init_data(args=args)

