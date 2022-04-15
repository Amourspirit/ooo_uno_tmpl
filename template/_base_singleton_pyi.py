# coding: utf-8
from _base_singleton import BaseSingleton
from _base_json import EventArgs

class BaseSingletonPyi(BaseSingleton):

    def on_after_init_data(self, args: EventArgs) -> None:
        super().on_after_init_data(args=args)