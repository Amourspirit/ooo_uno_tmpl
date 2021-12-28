# coding: utf-8
# this is a auto generated file generated by Cheetah
import os
from collections import namedtuple
from typing import TYPE_CHECKING

class Size(object):
    """
    specifies the 2-dimensional size of an area using width and height.

    See Also:
        `API Size <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1awt_1_1Size.html>`_

    Note:
        | At runtime this will be a `namedtuple <https://docs.python.org/3/library/collections.html#collections.namedtuple>`_ and not a class.
        | At design time a class is presumed. This allows for better typings.
        | Effectively functionallity is the same and namedtuple is more efficient than a class.
    """
    def __init__(self, Height: int, Width: int):
        self._Height = Height
        self._Width = Width

    @property
    def Height(self) -> int:
        """
        specifies the height.

        **Libre Office Type:** ``long``
        """
        return self._Height

    @property
    def Width(self) -> int:
        """
        specifies the width.

        **Libre Office Type:** ``long``
        """
        return self._Width

def _dynamic_struct():
    # Dynamically create nametuple that is more efficient as stand in for struct

    global Size
    ignore = os.environ.get('ooouno_ignore_runtime', 'False')
    if ignore == 'True':
        return
    # if statment is to stop VS Code from reporting errors
    if not TYPE_CHECKING:
        Size = namedtuple('Size', ['Height', 'Width'])

if not TYPE_CHECKING:
    _dynamic_struct()

__all__ = ['Size']
