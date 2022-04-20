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
# Namespace: com.sun.star.ui
from typing_extensions import Literal
import typing
from abc import ABC
if typing.TYPE_CHECKING:
    from ..awt.x_window import XWindow as XWindow_713b0924

class XPanel(ABC):
    """
    provides access to Panel
    
    **since**
    
        LibreOffice 5.1

    See Also:
        `API XPanel <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1ui_1_1XPanel.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.ui.XPanel']

    def collapse(self) -> None:
        """
        Collapse the panel to only show its title bar.
        """
    def expand(self, bCollapseOther: bool) -> None:
        """
        Expand and display the panel.
        """
    def getDialog(self) -> 'XWindow_713b0924':
        """
        Get the panel dialog element.
        """
    def getId(self) -> str:
        """
        The panel identifier.
        """
    def getOrderIndex(self) -> int:
        """
        Get the ordering index of the panel in the deck.
        """
    def getTitle(self) -> str:
        """
        Get the panel title string.
        """
    def isExpanded(self) -> bool:
        """
        Is the panel expanded.
        """
    def moveDown(self) -> None:
        """
        Move the panel one step down in the deck.
        """
    def moveFirst(self) -> None:
        """
        Move panel as first item of the deck.
        """
    def moveLast(self) -> None:
        """
        Move panel as last item of the deck.
        """
    def moveUp(self) -> None:
        """
        Move panel one step up in the deck.
        """
    def setOrderIndex(self, newOrderIndex: int) -> None:
        """
        Set the ordering index of the panel in the deck.
        """
    def setTitle(self, newTitle: str) -> None:
        """
        Set the panel title string.
        """

