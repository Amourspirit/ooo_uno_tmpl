# coding: utf-8
from _base_enum import BaseEnum
from _base_json import EventArgs
import uno
import os


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
