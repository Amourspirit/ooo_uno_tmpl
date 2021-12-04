# coding: utf-8
from typing import Tuple, List
from _tmpl_base import BaseTpml


class BaseInterface(BaseTpml):
    def _get_formated_arg(self, arg: Tuple[str]) -> str:
        return f"{arg[0]}: {arg[1]}"
    
    def get_args(self, args: List[Tuple[str]]) -> str:
        result = ''
        for i, arg in enumerate(args):
            if i > 0:
                result += ', '
            result += self._get_formated_arg(arg=arg)
        return result
    
    def get_out_args(self, meth:dict) -> List[str]:
        args: list = meth['args']
        results: List[str] = []
        for arg in args:
            if len(arg) >= 3:
                if self.is_out_arg(arg[2]): #dir in or out
                    results.append(arg[1]) # arg name
        return results

    def get_formated_meth(self, meth:dict) -> str:
        name = meth['name']
        iter_args:list = meth['args']
        if len(iter_args) > 0:
            args = 'self, ' + self.get_args(args=meth['args'])
        else:
            args = 'self'
        result = f"def {name}({args})"
        key = 'returns'
        if key in meth:
            ret = meth[key]
            if ret:
                result += f" -> {ret}"
        result += ':'
        return result