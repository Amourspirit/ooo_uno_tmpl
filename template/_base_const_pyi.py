# coding: utf-8
from typing import Any
from _base_const import BaseConst
from _base_json import EventArgs
import uno
import os
from src.parser.enumerations.value_type import ValTypeEnum


class BaseConstPyi(BaseConst):

    def on_after_init_data(self, args: EventArgs) -> None:
        super().on_after_init_data(args=args)
        self.write_class = False
        is_cls = os.environ.get("PYI_CLASS", None)
        if is_cls is not None and is_cls.lower() in ('true', '1', 't', 'y', 'yes'):
            self.write_class = True

    def get_const_type(self, data: dict, use_literal: bool = False) -> str:
        def get_from_val(val: Any) -> str:
            if isinstance(val, int):
                if use_literal:
                    return f"Literal[{val}]"
                else:
                    return f"int = {val}"
            if isinstance(val, float):
                return 'float'
            return 'typing.Any'
        name: str = data['name']
        t: str = data['type']
        val_type = ValTypeEnum(data['value_type'])
        val = data['value']
        if val_type == ValTypeEnum.INTEGER:
            if use_literal:
                return f"Literal[{val}]"
            else:
                return f"int = {val}"
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
        return 'typing.Any'
