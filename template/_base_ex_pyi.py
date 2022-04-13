# coding: utf-8
from typing import List
from _base_ex import BaseEx
from _base_json import EventArgs

class BaseExPyi(BaseEx):

    def on_after_init_data(self, args: EventArgs) -> None:
        super().on_after_init_data(args=args)
        self.uno_obj = self.config.uno_obj_dir
        self.dyn = self.config.dyn_dir
        self.helper_ns = self.config.helper_ns
        self.helper_mod = self.config.helper_mod

    def get_dyn_constructor_args_lst(self, add_default: bool) -> List[str]:
        key = f'get_dyn_constructor_args_lst_{add_default}'
        if key in self._cache:
            return self._cache[key]
        sorted_names = self.get_sorted_names()
        d_lst: List[dict] = self.get_properties_all()
        results = []
        for tpl in sorted_names:
            index = tpl[1]
            itm: dict = d_lst[index]
            c_str = self.get_safe_word(itm['name'])
            if add_default:
                c_str += " = UNO_NONE"
            results.append(c_str)
        self._cache[key] = results
        return self._cache[key]

    def get_dyn_constructor_args_str(self) -> str:
        lst = self.get_dyn_constructor_args_lst(add_default=True)
        return ', '.join(lst)

    def get_dyn_fn(self, fn_name: str = '__init__') -> str:
        sorted_names = self.get_sorted_names()
        if len(sorted_names) == 0:
            self._linfo("Constructor Args — False")
            if self.is_parent:
                return f"def {fn_name}(self, **kwargs):"
            return f"def {fn_name}(self):"
        self._linfo("Constructor Args — True")
        names = self.get_dyn_constructor_args_str()
        if self.is_parent:
            return f"def {fn_name}(self, {names}, **kwargs):"
        return f"def {fn_name}(self, {names}):"
