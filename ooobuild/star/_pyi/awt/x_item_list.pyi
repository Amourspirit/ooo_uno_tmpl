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
from abc import ABC
if typing.TYPE_CHECKING:
    from .x_item_list_listener import XItemListListener as XItemListListener_e1020d1d

class XItemList(ABC):
    """
    provides convenient access to the list of items in a list box

    See Also:
        `API XItemList <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XItemList.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.awt.XItemList']

    def addItemListListener(self, Listener: 'XItemListListener_e1020d1d') -> None:
        """
        registers a listener which is notified about changes in the item list.
        """
    def getAllItems(self) -> 'typing.Tuple[typing.Tuple[str, str], ...]':
        """
        retrieves the texts and images of all items in the list
        """
    def getItemData(self, Position: int) -> object:
        """
        retrieves the implementation dependent value associated with the given list item.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
    def getItemImage(self, Position: int) -> str:
        """
        retrieves the URL of the image of an existing item

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
    def getItemText(self, Position: int) -> str:
        """
        retrieves the text of an existing item

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
    def getItemTextAndImage(self, Position: int) -> 'typing.Tuple[str, str]':
        """
        retrieves both the text and the image URL of an existing item

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
    def insertItem(self, Position: int, ItemText: str, ItemImageURL: str) -> None:
        """
        inserts a new item into the list

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
    def insertItemImage(self, Position: int, ItemImageURL: str) -> None:
        """
        inserts an item which has only an image, but no text

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
    def insertItemText(self, Position: int, ItemText: str) -> None:
        """
        inserts an item which has only a text, but no image

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
    def removeAllItems(self) -> None:
        """
        removes all items from the list
        """
    def removeItem(self, Position: int) -> None:
        """
        removes an item from the list

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
    def removeItemListListener(self, Listener: 'XItemListListener_e1020d1d') -> None:
        """
        revokes a listener which is notified about changes in the item list.
        """
    def setItemData(self, Position: int, ItemData: object) -> None:
        """
        associates an implementation dependent value with the given list item.
        
        You can use this to store data for an item which does not interfere with the displayed text and image, but can be used by the client of the list box for an arbitrary purpose.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
    def setItemImage(self, Position: int, ItemImageURL: str) -> None:
        """
        sets a new image for an existing item

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
    def setItemText(self, Position: int, ItemText: str) -> None:
        """
        sets a new text for an existing item

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
    def setItemTextAndImage(self, Position: int, ItemText: str, ItemImageURL: str) -> None:
        """
        sets both a new position and text for an existing item

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
    @property
    def ItemCount(self) -> int:
        """
        is the number of items in the list
        """


