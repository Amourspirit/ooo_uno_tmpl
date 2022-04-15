# coding: utf-8
from _base_service import BaseService
from _base_json import EventArgs

class BaseServicePyi(BaseService):

    def on_after_init_data(self, args: EventArgs) -> None:
        super().on_after_init_data(args=args)

