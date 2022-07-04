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
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_action_listener import XActionListener as XActionListener_c7560c50

class XButton(XInterface_8f010a43):
    """
    makes it possible to set the label of a button and to register for action events.

    See Also:
        `API XButton <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XButton.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt'
    __ooo_full_ns__: str = 'com.sun.star.awt.XButton'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.awt.XButton'

    @abstractmethod
    def addActionListener(self, l: 'XActionListener_c7560c50') -> None:
        """
        registers an event handler for button action events.
        """
        ...
    @abstractmethod
    def removeActionListener(self, l: 'XActionListener_c7560c50') -> None:
        """
        unregisters an event handler for button action events.
        """
        ...
    @abstractmethod
    def setActionCommand(self, Command: str) -> None:
        """
        sets a command string for pushing the button.
        """
        ...
    @abstractmethod
    def setLabel(self, Label: str) -> None:
        """
        sets the label of the button.
        """
        ...

__all__ = ['XButton']

