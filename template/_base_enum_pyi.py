# coding: utf-8
from _base_enum import BaseEnum
from _base_json import EventArgs
import uno
import os
import re

class BaseEnumPyi(BaseEnum):

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
  
