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
    from .selection import Selection as Selection_84d609fa
    from .x_text_listener import XTextListener as XTextListener_b04d0b97

class XTextComponent(XInterface_8f010a43):
    """
    gives access to the text of a component and makes it possible to register event listeners.

    See Also:
        `API XTextComponent <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XTextComponent.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.awt.XTextComponent']

    def addTextListener(self, l: 'XTextListener_b04d0b97') -> None:
        """
        registers a text event listener.
        """
        ...
    def getMaxTextLen(self) -> int:
        """
        returns the currently set maximum text length.
        """
        ...
    def getSelectedText(self) -> str:
        """
        returns the currently selected text.
        """
        ...
    def getSelection(self) -> 'Selection_84d609fa':
        """
        returns the current user selection.
        """
        ...
    def getText(self) -> str:
        """
        returns the text of the component.
        """
        ...
    def insertText(self, Sel: 'Selection_84d609fa', Text: str) -> None:
        """
        inserts text at the specified position.
        """
        ...
    def isEditable(self) -> bool:
        """
        returns if the text is editable by the user.
        """
        ...
    def removeTextListener(self, l: 'XTextListener_b04d0b97') -> None:
        """
        unregisters a text event listener.
        """
        ...
    def setEditable(self, bEditable: bool) -> None:
        """
        makes the text editable for the user or read-only.
        """
        ...
    def setMaxTextLen(self, nLen: int) -> None:
        """
        sets the maximum text length.
        """
        ...
    def setSelection(self, aSelection: 'Selection_84d609fa') -> None:
        """
        sets the user selection.
        """
        ...
    def setText(self, aText: str) -> None:
        """
        sets the text of the component.
        """
        ...


