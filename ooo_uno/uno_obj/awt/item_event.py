# coding: utf-8
# this is a auto generated file generated by Cheetah
import os
from collections import namedtuple
from typing import TYPE_CHECKING

class ItemEvent(object):
    """
    specifies an event occurred to an item of a menu, a list box etc.

    See Also:
        `API ItemEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1awt_1_1ItemEvent.html>`_

    Note:
        | At runtime this will be a `namedtuple <https://docs.python.org/3/library/collections.html#collections.namedtuple>`_ and not a class.
        | At design time a class is presumed. This allows for better typings.
        | Effectively functionallity is the same and namedtuple is more efficient than a class.
    """
    def __init__(self, Highlighted: int, ItemId: int, Selected: int):
        self._Highlighted = Highlighted
        self._ItemId = ItemId
        self._Selected = Selected

    @property
    def Highlighted(self) -> int:
        """
        specifies which item is newly highlighted.

        **Libre Office Type:** ``long``
        """
        return self._Highlighted

    @property
    def ItemId(self) -> int:
        """
        specifies the id of the item.

        **Libre Office Type:** ``long``
        """
        return self._ItemId

    @property
    def Selected(self) -> int:
        """
        specifies which item is newly selected.

        **Libre Office Type:** ``long``
        """
        return self._Selected

def _dynamic_struct():
    # Dynamically create nametuple that is more efficient as stand in for struct

    global ItemEvent
    ignore = os.environ.get('ooouno_ignore_runtime', 'False')
    if ignore == 'True':
        return
    # if statment is to stop VS Code from reporting errors
    if not TYPE_CHECKING:
        ItemEvent = namedtuple('ItemEvent', ['Highlighted', 'ItemId', 'Selected'])

if not TYPE_CHECKING:
    _dynamic_struct()

__all__ = ['ItemEvent']

