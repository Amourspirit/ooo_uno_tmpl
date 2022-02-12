# coding: utf-8
from _base_ex import BaseEx
from _base_json import EventArgs

class BaseExDyn(BaseEx):

    def on_after_init_data(self, args: EventArgs) -> None:
        super().on_after_init_data(args=args)
        self.uno_obj = self.config.uno_obj_dir
        self.dyn = self.config.dyn_dir
        self.oenv = self.config.env
        self.helper_ns = self.config.helper_ns
        self.helper_mod = self.config.helper_mod

    def get_dyn_fn(self) -> str:
        sorted_names = self.get_sorted_names()
        if len(sorted_names) == 0:
            return "def _ex_init(**kwargs):"
        names = self.get_constructor_args_str(include_value=True, include_type=False, uno_none=False)
        return f"def _ex_init({names}, **kwargs):"
