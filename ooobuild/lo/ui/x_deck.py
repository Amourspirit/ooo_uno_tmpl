# coding: utf-8
#
# Copyright 2023 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 7.4
# Namespace: com.sun.star.ui
from __future__ import annotations
import typing
from abc import abstractmethod, ABC
if typing.TYPE_CHECKING:
    from .x_panels import XPanels as XPanels_676608a1

class XDeck(ABC):
    """
    provides access to Deck
    
    **since**
    
        LibreOffice 5.1

    See Also:
        `API XDeck <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1ui_1_1XDeck.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ui'
    __ooo_full_ns__: str = 'com.sun.star.ui.XDeck'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.ui.XDeck'

    @abstractmethod
    def activate(self, bActivate: bool) -> None:
        """
        Activate the deck and display its content.
        """
        ...
    @abstractmethod
    def getId(self) -> str:
        """
        The deck identifier.
        """
        ...
    @abstractmethod
    def getOrderIndex(self) -> int:
        """
        Get the ordering index of the deck button in sidebar.
        """
        ...
    @abstractmethod
    def getPanels(self) -> XPanels_676608a1:
        """
        Panels collection attached to the deck.
        """
        ...
    @abstractmethod
    def getTitle(self) -> str:
        """
        Get the deck title string.
        """
        ...
    @abstractmethod
    def isActive(self) -> bool:
        """
        Is the deck the active one.
        """
        ...
    @abstractmethod
    def moveDown(self) -> None:
        """
        Move deck one step down in the sidebar.
        """
        ...
    @abstractmethod
    def moveFirst(self) -> None:
        """
        Move deck button at first position in sidebar.
        """
        ...
    @abstractmethod
    def moveLast(self) -> None:
        """
        Move deck button at last position in sidebar.
        """
        ...
    @abstractmethod
    def moveUp(self) -> None:
        """
        Move deck one step up in the sidebar.
        """
        ...
    @abstractmethod
    def setOrderIndex(self, newOrderIndex: int) -> None:
        """
        Set the ordering index of the deck button in sidebar.
        """
        ...
    @abstractmethod
    def setTitle(self, newTitle: str) -> None:
        """
        Set the deck title string.
        """
        ...

__all__ = ['XDeck']


