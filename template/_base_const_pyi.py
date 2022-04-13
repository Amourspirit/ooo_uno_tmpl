# coding: utf-8
from tkinter.tix import INTEGER
from typing import Any
from _base_const import BaseConst
from _base_json import EventArgs
import uno
from oootmpl.parser.enumerations.value_type import ValTypeEnum
class BaseConstPyi(BaseConst):

    def on_after_init_data(self, args: EventArgs) -> None:
        super().on_after_init_data(args=args)


    def get_const_type(self, data: dict) -> str:
        def get_from_val(val: Any) -> str:
            if isinstance(val, int):
                return f"Literal[{val}]"
            if isinstance(val, float):
                return 'float'
            return 'object'
        name: str = data['name']
        t: str = data['type']
        val_type = ValTypeEnum(data['value_type'])
        val = data['value']
        if val_type == ValTypeEnum.INTEGER:
            return f"Literal[{val}]"
        if val_type == ValTypeEnum.FLOAT:
            return "float"
        if val_type == ValTypeEnum.STRING:
            return "str"
        if val_type == ValTypeEnum.CONST or val_type == ValTypeEnum.CONST_PLUS_INT or val_type == ValTypeEnum.CONST_MINUS_INT:
            fullname = self.namespace + '.' + self.get_safe_word(self.name)
            s = f"{fullname}.{name}"
            c = uno.getConstantByName(s)
            return get_from_val(c)
        try:
            fullname = self.namespace + '.' + self.get_safe_word(self.name)
            s = f"{fullname}.{name}"
            c = uno.getConstantByName(s)
            return get_from_val(c)
        except Exception as e:
            self._lerr(e)
        return 'object'
