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
        # check if we should write a class by checking the environment variable.
        # this environment variable is set by the make._make_pyi().
        is_cls = os.environ.get("PYI_CLASS_CONST", None)
        if is_cls is not None and is_cls.lower() in ('true', '1', 't', 'y', 'yes'):
            self.write_class = True

    def get_const_type(self, data: dict, use_literal: bool = False, get_val: bool = False) -> str:
        def get_from_val(val: Any, use_val: bool) -> str:
            if isinstance(val, int):
                if use_literal:
                    if use_val:
                        raise ValueError("use_literal and get_val cannot be True at the same time")
                    return f"Literal[{val}]"
                else:
                    if use_val:
                        return f"int = {val}"
                    else:
                        return "int = ..."
            if isinstance(val, float):
                if use_val:
                    return f"float = {val}"
                else:
                    return "float = ..."
            return 'typing.Any = ...'
        name: str = data['name']
        t: str = data['type']
        val_type = ValTypeEnum(data['value_type'])
        val = data['value']
        if val_type == ValTypeEnum.INTEGER:
            if use_literal:
                if get_val:
                    raise ValueError("use_literal and get_val cannot be True at the same time")
                return f"Literal[{val}]"
            else:
                if get_val:
                    return f"int = {val}"
                else:
                    return f"int = ..."
        if val_type == ValTypeEnum.FLOAT:
            return "float = ..."
        if val_type == ValTypeEnum.STRING:
            return "str = ..."
        if val_type == ValTypeEnum.CONST or val_type == ValTypeEnum.CONST_PLUS_INT or val_type == ValTypeEnum.CONST_MINUS_INT:
            fullname = self.namespace + '.' + self.get_safe_word(self.name)
            s = f"{fullname}.{name}"
            c = uno.getConstantByName(s)
            return get_from_val(c, use_val=get_val)
        try:
            fullname = self.namespace + '.' + self.get_safe_word(self.name)
            s = f"{fullname}.{name}"
            c = uno.getConstantByName(s)
            return get_from_val(c, use_val=get_val)
        except Exception as e:
            self._lerr(e)
        return 'typing.Any = ...'
