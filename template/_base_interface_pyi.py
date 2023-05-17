# coding: utf-8
from typing import Dict, List, cast
from _base_interface import BaseInterface
from _base_json import EventArgs

class BaseInterfacePyi(BaseInterface):

    def on_after_init_data(self, args: EventArgs) -> None:
        super().on_after_init_data(args=args)


    # region Overrides
    def _get_formated_arg(self, arg: Dict[str, str]) -> str:
        tipe = cast(str, arg['type'])
        if tipe == "object":
            return f"{self.get_safe_word(arg['name'])}: typing.Any"
        return f"{self.get_safe_word(arg['name'])}: {self.get_q_type(arg['type'])}"

    def get_args(self, args: List[Dict[str, str]]) -> str:
        result = ''
        for i, arg in enumerate(args):
            if i > 0:
                result += ', '
            result += self._get_formated_arg(arg=arg)
        return result
    
    
    def get_formated_meth(self, meth: dict) -> str:
        name = meth['name']
        iter_args: list = meth['args']
        if len(iter_args) > 0:
            args = 'self, ' + self.get_args(args=meth['args'])
        else:
            args = 'self'
        result = f"def {name}({args})"
        key = 'returns'
        if key in meth:
            ret = meth[key]
            if ret:
                q_type = self.get_q_type(ret)
                if q_type == 'object':
                    q_type = 'typing.Any'
                result += f" -> {q_type}"
        result += ':'
        return result
    # endregion Overrides