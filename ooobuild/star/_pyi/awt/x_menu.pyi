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
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .menu_item_type import MenuItemType as MenuItemType_a4760b1a
    from .x_menu_listener import XMenuListener as XMenuListener_af9e0b87
    from .x_popup_menu import XPopupMenu as XPopupMenu_8ee90a55

class XMenu(XInterface_8f010a43):
    """
    specifies a simple menu.

    See Also:
        `API XMenu <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XMenu.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.awt.XMenu']

    def addMenuListener(self, xListener: 'XMenuListener_af9e0b87') -> None:
        """
        adds the specified menu listener to receive events from this menu.
        """
        ...
    def clear(self) -> None:
        """
        removes all items from the menu.
        """
        ...
    def enableAutoMnemonics(self, bEnable: bool) -> None:
        """
        specifies whether mnemonics are automatically assigned to menu items, or not.
        """
        ...
    def enableItem(self, nItemId: int, bEnable: bool) -> None:
        """
        enables or disables the menu item.
        """
        ...
    def getCommand(self, nItemId: int) -> str:
        """
        retrieves the command string for the menu item.
        """
        ...
    def getHelpCommand(self, nItemId: int) -> str:
        """
        retrieves the help command string for the menu item.
        """
        ...
    def getHelpText(self, nItemId: int) -> str:
        """
        retrieves the help text for the menu item.
        """
        ...
    def getItemCount(self) -> int:
        """
        returns the number of items in the menu.
        """
        ...
    def getItemId(self, nItemPos: int) -> int:
        """
        returns the ID of the item at the specified position.
        """
        ...
    def getItemPos(self, nItemId: int) -> int:
        """
        returns the position of the item with the specified ID.
        """
        ...
    def getItemText(self, nItemId: int) -> str:
        """
        returns the string for the given item id.
        """
        ...
    def getItemType(self, nItemPos: int) -> 'MenuItemType_a4760b1a':
        """
        retrieves the type of the menu item.
        """
        ...
    def getPopupMenu(self, nItemId: int) -> 'XPopupMenu_8ee90a55':
        """
        returns the popup menu from the menu item.
        """
        ...
    def getTipHelpText(self, nItemId: int) -> str:
        """
        retrieves the tip help text for the menu item.
        """
        ...
    def hideDisabledEntries(self, bHide: bool) -> None:
        """
        specifies whether disabled menu entries should be hidden, or not.
        """
        ...
    def insertItem(self, nItemId: int, aText: str, nItemStyle: int, nItemPos: int) -> None:
        """
        inserts an item into the menu.
        
        The item is appended if the position is greater than or equal to getItemCount() or if it is negative.
        """
        ...
    def isItemEnabled(self, nItemId: int) -> bool:
        """
        returns the state of the menu item.
        """
        ...
    def isPopupMenu(self) -> bool:
        """
        checks whether an XMenu is an XPopupMenu.
        """
        ...
    def removeItem(self, nItemPos: int, nCount: int) -> None:
        """
        removes one or more items from the menu.
        """
        ...
    def removeMenuListener(self, xListener: 'XMenuListener_af9e0b87') -> None:
        """
        removes the specified menu listener so that it no longer receives events from this menu.
        """
        ...
    def setCommand(self, nItemId: int, aCommand: str) -> None:
        """
        sets the command string for the menu item.
        """
        ...
    def setHelpCommand(self, nItemId: int, aCommand: str) -> None:
        """
        sets the help command string for the menu item.
        """
        ...
    def setHelpText(self, nItemId: int, sHelpText: str) -> None:
        """
        sets the help text for the menu item.
        """
        ...
    def setItemText(self, nItemId: int, aText: str) -> None:
        """
        sets the text for the menu item.
        """
        ...
    def setPopupMenu(self, nItemId: int, aPopupMenu: 'XPopupMenu_8ee90a55') -> None:
        """
        sets the popup menu for a specified menu item.
        """
        ...
    def setTipHelpText(self, nItemId: int, sTipHelpText: str) -> None:
        """
        sets the tip help text for the menu item.
        """
        ...


