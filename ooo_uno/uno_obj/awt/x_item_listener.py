# coding: utf-8
# this is a auto generated file generated by Cheetah
import typing
from abc import abstractmethod
from ..lang.x_event_listener import XEventListener
if typing.TYPE_CHECKING:
    from .item_event import ItemEvent


class XItemListener(XEventListener):
    """
    makes it possible to receive events from a component when the state of an item changes.

    See Also:
        `API XItemListener <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XItemListener.html>`_
    """

    @abstractmethod
    def itemStateChanged(self, rEvent: 'ItemEvent') -> None:
        """
        is invoked when an item changes its state.
        """
