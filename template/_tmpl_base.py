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
