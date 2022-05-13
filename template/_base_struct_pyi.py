# coding: utf-8
from typing import List
from _base_struct import BaseStruct


class BaseStructPyi(BaseStruct):

    def get_constructor(self) -> str:
        # overrides BaseEx
        if not self.models.is_args():
            # this will alomost never happen
            self._linfo("Constructor Args — False")
            return "def __init__(self) -> None:"
        self._linfo("Constructor Args — True")
        names = self.get_constructor_args_str(
            include_value=True, include_type=True, value=" = ...")
        return f"def __init__(self, {names}) -> None:"
