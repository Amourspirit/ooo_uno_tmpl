# coding: utf-8
# this is a auto generated file generated by Cheetah
import os
from collections import namedtuple
from typing import TYPE_CHECKING

class Selection(object):
    """
    specifies a numerical range.

    See Also:
        `API Selection <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1awt_1_1Selection.html>`_

    Note:
        | At runtime this will be a `namedtuple <https://docs.python.org/3/library/collections.html#collections.namedtuple>`_ and not a class.
        | At design time a class is presumed. This allows for better typings.
        | Effectively functionallity is the same and namedtuple is more efficient than a class.
    """
    def __init__(self, Max: int, Min: int):
        self._Max = Max
        self._Min = Min

    @property
    def Max(self) -> int:
        """
        specifies the upper limit of the range.

        **Libre Office Type:** ``long``
        """
        return self._Max

    @property
    def Min(self) -> int:
        """
        specifies the lower limit of the range.

        **Libre Office Type:** ``long``
        """
        return self._Min

def _dynamic_struct():
    # Dynamically create nametuple that is more efficient as stand in for struct

    global Selection
    ignore = os.environ.get('ooouno_ignore_runtime', 'False')
    if ignore == 'True':
        return
    # if statment is to stop VS Code from reporting errors
    if not TYPE_CHECKING:
        Selection = namedtuple('Selection', ['Max', 'Min'])

if not TYPE_CHECKING:
    _dynamic_struct()

__all__ = ['Selection']

