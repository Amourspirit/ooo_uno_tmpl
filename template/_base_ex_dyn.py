# coding: utf-8
from typing import List
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

    def get_dyn_constructor_args_str(self) -> str:
        sorted_names = self.get_sorted_names()
        d_lst: List[dict] = self.get_properties_all()
        c_str = ''
        i = 0
        for tpl in sorted_names:
            if i > 0:
               c_str += ', '
            index = tpl[1]
            itm: dict = d_lst[index]
            c_str += self.get_safe_word(itm['name'])
            c_str += " = UNO_NONE"
            i += 1
        return c_str

    def get_dyn_fn(self) -> str:
        sorted_names = self.get_sorted_names()
        if len(sorted_names) == 0:
            self._linfo("Constructor Args — False")
            if self.is_parent:
                return "def _ex_init(**kwargs):"
            return "def _ex_init():"
        self._linfo("Constructor Args — True")
        names = self.get_dyn_constructor_args_str()
        if self.is_parent:
            return f"def _ex_init({names}, **kwargs):"
        return f"def _ex_init({names}):"
