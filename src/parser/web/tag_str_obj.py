# coding: utf-8
from typing import Iterable, List
from bs4.element import Tag
from ..common.util import Util, str_clean


class TagsStrObj:
    """Class that converts list of tags to string"""

    def __init__(self, tags: Iterable[Tag], **kwargs):
        """
        Constructor

        Args:
            tags (Iterable[Tag]): List of tags

        Keyword Arguments:
            clean (bool, optional): If ``True`` then data will be cleaned
                using ``str_clean`` method. Default ``True``
            empty (bool, optional): If ``True`` empty lines will be added
                between other lines. Default ``True``
            indent (int, optional): The number of spaces to indent for 
                methods that return a string. Default ``0``
        """
        self._tags = tags
        self._clean = bool(kwargs.get('clean', True))
        self._empty_lines = bool(kwargs.get('empty', True))
        self._indent_amt = int(kwargs.get('indent', 0))

    def get_lines(self) -> List[str]:
        """Gets lines for this instance"""
        lines: List[str] = []
        i = 0
        for ln in self._tags:
            s = ln.text.strip().replace("::", '.')
            s = s.replace('\\', '\\\\')
            if not s:
                continue
            if self._clean:
                s = str_clean(input=s)
            if i > 0 and self._empty_lines:
                lines.append("")
            lines.extend(s.splitlines())
            i += 1
        return [line.strip() for line in lines]

    def get_data(self) -> List[str]:
        """Gets Lines as string for this instance"""
        return self.get_lines()

    def get_string_list(self) -> str:
        # lines = self._encode_list(self.get_lines())
        # c_lines = self._decode_list(str(lines).split(','))
        # s = ',\n'.join(c_lines)
        s = Util.get_string_list(self.get_lines())
        if self._indent_amt > 0:
            s = Util.indent(text=s, indent_amt=self._indent_amt)
        return s