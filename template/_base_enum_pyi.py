# coding: utf-8
from _base_enum import BaseEnum
from _base_json import EventArgs
import uno
import os
import re

class BaseEnumPyi(BaseEnum):

    def on_after_init_data(self, args: EventArgs) -> None:
        super().on_after_init_data(args=args)
        self.write_class = False
        is_cls = os.environ.get("PYI_CLASS", None)
        if is_cls is not None and is_cls.lower() in ('true', '1', 't', 'y', 'yes'):
            self.write_class = True

    def get_typing(self, name: str) -> str:
        fullname = self.namespace + '.' + self.get_safe_word(self.name)
        try:
            e = uno.Enum(fullname, name)
            if isinstance(e.value, str):
                return f": Literal['{e.value}']"
            if isinstance(e.value, int):
                return f": Literal[{e.value}]"
            return f": {type(e.value).__name__}"
        except Exception as e:
            self._lerr(e)
        return ' = ...'
  
    def get_pyi_com_import(self) -> str:
        """
        Get import string in the format of ``from com.sun.star._pyi.drawing.line_end_type import LineEndType as PyiLineEndType```

        Returns:
            str: Import String
        """
        ns = self.namespace.replace("com.sun.star.", "com.sun.star._pyi.")
        return f"from {ns}.{self.camel_to_snake(self.name)} import {self.name} as Pyi{self.name}"
