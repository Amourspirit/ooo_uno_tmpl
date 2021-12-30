# coding: utf-8
# this is a auto generated file generated by Cheetah
import os
from collections import namedtuple
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .rectangle import Rectangle

class EndDockingEvent(object):
    """
    specifies an end docking event.

    See Also:
        `API EndDockingEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1awt_1_1EndDockingEvent.html>`_

    Note:
        | At runtime this will be a `namedtuple <https://docs.python.org/3/library/collections.html#collections.namedtuple>`_ and not a class.
        | At design time a class is presumed. This allows for better typings.
        | Effectively functionallity is the same and namedtuple is more efficient than a class.
    """
    def __init__(self, WindowRectangle: 'Rectangle', bCancelled: bool, bFloating: bool):
        self._WindowRectangle = WindowRectangle
        self._bCancelled = bCancelled
        self._bFloating = bFloating

    @property
    def WindowRectangle(self) -> 'Rectangle':
        """
        specifies the new bounding rectangle of the window

        **Libre Office Type:** ``com.sun.star.awt.Rectangle``
        """
        return self._WindowRectangle

    @property
    def bCancelled(self) -> bool:
        """
        specifies that the docking procedure was canceled

        **Libre Office Type:** ``boolean``
        """
        return self._bCancelled

    @property
    def bFloating(self) -> bool:
        """
        specifies if the window is now floating TRUE or docked FALSE

        **Libre Office Type:** ``boolean``
        """
        return self._bFloating

def _dynamic_struct():
    # Dynamically create nametuple that is more efficient as stand in for struct

    global EndDockingEvent
    ignore = os.environ.get('ooouno_ignore_runtime', 'False')
    if ignore == 'True':
        return
    # if statment is to stop VS Code from reporting errors
    if not TYPE_CHECKING:
        EndDockingEvent = namedtuple('EndDockingEvent', ['WindowRectangle', 'bCancelled', 'bFloating'])

if not TYPE_CHECKING:
    _dynamic_struct()

__all__ = ['EndDockingEvent']

