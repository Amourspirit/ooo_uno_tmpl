# coding: utf-8
from typing import Tuple, List
from Cheetah.Template import Template


class BaseTpml(Template):
    """Base class for all templtes"""
    
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