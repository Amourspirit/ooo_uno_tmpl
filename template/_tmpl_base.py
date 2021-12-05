# coding: utf-8
import re
from typing import Tuple, List
from Cheetah.Template import Template
py_name_pattern = re.compile('[\W_]+')
class BaseTpml(Template):
    """Base class for all templtes"""
    
    def get_clean_name(self, input: str) -> str:
        """
        Removes all char from a string except for ``a-zA-Z0-9_``

        Args:
            input (str): string to clean    

        Returns:
            str: input with any other chars removed
        """
        # https://stackoverflow.com/questions/1276764/stripping-everything-but-alphanumeric-chars-from-a-string-in-python
        return py_name_pattern.sub('', input)
    
    def line_gen(self, input) -> str:
        """
        Generates lines from str or list like

        Args:
            input (str, list, tuple, set): input str or iterable str

        Yields:
            [str]: line by line
        """
        if isinstance(input, str):
            yield input
            return
        for s in input:
            yield s

    def lst_to_str(self, input, sep:str = ', ') -> str:
        """
        Writes list items into a str seperated by ``sep``.
        If input is ``str`` then it is returned verbatium

        Args:
            input (str, Iterable[str]): input to parse
            sep (str, optional): Seperate usd when joining list. Defaults to ', '.

        Returns:
            str: value
        """
        if isinstance(input, str):
            return input
        if len(input) == 0:
            return ''
        return sep.join(input)
    
    def is_out_arg(self, input: str) -> bool:
        """Gets if input is ``out`"""
        if not input:
            return False
        return input == 'out'
    
    def get_last_part(self, input: str, sep='.') -> str:
        """
        Splits a string and returns the last part

        Args:
            input (str): string to get last part of.
            sep (str, optional): string used to split. Defaults to ``.``

        Returns:
            str: [description]
        """
        if not input:
            return ''
        _parts = input.rsplit(sep, 1)
        return _parts[0] if len(_parts) == 1 else _parts[1]
