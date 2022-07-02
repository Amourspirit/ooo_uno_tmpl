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
    from .x_control import XControl as XControl_7a9c098d
    from .x_control_container import XControlContainer as XControlContainer_e22d0d30
    from .x_tab_controller_model import XTabControllerModel as XTabControllerModel_fbef0dd8

class XTabController(XInterface_8f010a43):
    """
    specifies the basic operations for a tab controller.

    See Also:
        `API XTabController <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XTabController.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.awt.XTabController']

    def activateFirst(self) -> None:
        """
        sets the focus to the first control that can be reached with the TAB key.
        """
        ...
    def activateLast(self) -> None:
        """
        sets the focus to the last control that can be reached with the TAB key.
        """
        ...
    def activateTabOrder(self) -> None:
        """
        activates tab order.
        """
        ...
    def autoTabOrder(self) -> None:
        """
        enables automatic tab order.
        """
        ...
    def getContainer(self) -> 'XControlContainer_e22d0d30':
        """
        returns the control container.
        """
        ...
    def getControls(self) -> 'typing.Tuple[XControl_7a9c098d, ...]':
        """
        returns all controls of the control container.
        """
        ...
    def getModel(self) -> 'XTabControllerModel_fbef0dd8':
        """
        returns the tab controller model.
        """
        ...
    def setContainer(self, Container: 'XControlContainer_e22d0d30') -> None:
        """
        set the control container.
        """
        ...
    def setModel(self, Model: 'XTabControllerModel_fbef0dd8') -> None:
        """
        sets the tab controller model.
        """
        ...


