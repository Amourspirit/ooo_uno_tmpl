# coding: utf-8
#
# Copyright 2022 :Barry-Thomas-Paul: Moss
#
# Licensed under the Apache License, Version 2.0 (the "License")
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http: // www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.awt
from typing_extensions import Literal
import typing
from ..lang.x_event_listener import XEventListener as XEventListener_c7230c4a
if typing.TYPE_CHECKING:
    from .item_list_event import ItemListEvent as ItemListEvent_afba0b81
    from ..lang.event_object import EventObject as EventObject_a3d70b03

class XItemListListener(XEventListener_c7230c4a):
    """
    describes a listener for changes in an item list

    See Also:
        `API XItemListListener <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XItemListListener.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.awt.XItemListListener']

    def allItemsRemoved(self, Event: 'EventObject_a3d70b03') -> None:
        """
        is called when the list has been completely cleared, i.e.
        
        after an invocation of XItemList.removeAllItems()
        """
    def itemListChanged(self, Event: 'EventObject_a3d70b03') -> None:
        """
        is called when the changes to the item list which occurred are too complex to be notified in single events.
        
        Consumers of this event should discard their cached information about the current item list, and completely refresh it from the XItemList's current state.
        """
    def listItemInserted(self, Event: 'ItemListEvent_afba0b81') -> None:
        """
        is called when an item is inserted into the list
        """
    def listItemModified(self, Event: 'ItemListEvent_afba0b81') -> None:
        """
        is called when an item in the list is modified, i.e.
        
        its text or image changed
        """
    def listItemRemoved(self, Event: 'ItemListEvent_afba0b81') -> None:
        """
        is called when an item is removed from the list
        """

