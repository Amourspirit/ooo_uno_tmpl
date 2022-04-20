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

class XImageButton(XInterface_8f010a43):
    """
    makes it possible to register for action events of an image button and sets the action command.

    See Also:
        `API XImageButton <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XImageButton.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.awt.XImageButton']

    def addActionListener(self, l: 'XActionListener_c7560c50') -> None:
        """
        registers a listener for action events.
        """
    def removeActionListener(self, l: 'XActionListener_c7560c50') -> None:
        """
        unregisters a listener for action events.
        """
    def setActionCommand(self, Command: str) -> None:
        """
        sets the action command string.
        """

