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
# Libre Office Version: 7.2
# Namespace: com.sun.star.awt
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_action_listener import XActionListener as XActionListener_c7560c50
    from .x_item_listener import XItemListener as XItemListener_af710b81

class XListBox(XInterface_8f010a43):
    """
    gives access to the items of a list box and makes it possible to register item and action event listeners.

    See Also:
        `API XListBox <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XListBox.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.awt.XListBox']

    def addActionListener(self, l: 'XActionListener_c7560c50') -> None:
        """
        registers a listener for action events.
        """
    def addItem(self, aItem: str, nPos: int) -> None:
        """
        adds an item at the specified position.
        """
    def addItemListener(self, l: 'XItemListener_af710b81') -> None:
        """
        registers a listener for item events.
        """
    def addItems(self, aItems: 'typing.Tuple[str, ...]', nPos: int) -> None:
        """
        adds multiple items at the specified position.
        """
    def getDropDownLineCount(self) -> int:
        """
        returns the number of visible lines in drop down mode.
        """
    def getItem(self, nPos: int) -> str:
        """
        returns the item at the specified position.
        """
    def getItemCount(self) -> int:
        """
        returns the number of items in the listbox.
        """
    def getItems(self) -> 'typing.Tuple[str, ...]':
        """
        returns all items of the list box.
        """
    def getSelectedItem(self) -> str:
        """
        returns the currently selected item.
        
        When multiple items are selected, the first one is returned. When nothing is selected, an empty string is returned.
        """
    def getSelectedItemPos(self) -> int:
        """
        returns the position of the currently selected item.
        
        When multiple items are selected, the position of the first one is returned. When nothing is selected, -1 is returned.
        """
    def getSelectedItems(self) -> 'typing.Tuple[str, ...]':
        """
        returns all currently selected items.
        """
    def getSelectedItemsPos(self) -> 'typing.Tuple[int, ...]':
        """
        returns the positions of all currently selected items.
        """
    def isMutipleMode(self) -> bool:
        """
        returns TRUE if multiple items can be selected, FALSE if only one item can be selected.
        """
    def makeVisible(self, nEntry: int) -> None:
        """
        makes the item at the specified position visible by scrolling.
        """
    def removeActionListener(self, l: 'XActionListener_c7560c50') -> None:
        """
        unregisters a listener for action events.
        """
    def removeItemListener(self, l: 'XItemListener_af710b81') -> None:
        """
        unregisters a listener for item events.
        """
    def removeItems(self, nPos: int, nCount: int) -> None:
        """
        removes a number of items at the specified position.
        """
    def selectItem(self, aItem: str, bSelect: bool) -> None:
        """
        selects/deselects the specified item.
        """
    def selectItemPos(self, nPos: int, bSelect: bool) -> None:
        """
        selects/deselects the item at the specified position.
        """
    def selectItemsPos(self, aPositions: 'typing.Tuple[int, ...]', bSelect: bool) -> None:
        """
        selects/deselects multiple items at the specified positions.
        """
    def setDropDownLineCount(self, nLines: int) -> None:
        """
        sets the number of visible lines for drop down mode.
        """
    def setMultipleMode(self, bMulti: bool) -> None:
        """
        determines if only a single item or multiple items can be selected.
        """

