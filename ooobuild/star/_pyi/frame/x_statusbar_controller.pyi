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
# Namespace: com.sun.star.frame
from typing_extensions import Literal
import typing
from .x_status_listener import XStatusListener as XStatusListener_e2740d35
from ..lang.x_component import XComponent as XComponent_98dc0ab5
from ..lang.x_initialization import XInitialization as XInitialization_d46c0cca
from ..util.x_updatable import XUpdatable as XUpdatable_9a420ab0
if typing.TYPE_CHECKING:
    from ..awt.mouse_event import MouseEvent as MouseEvent_8f430a5f
    from ..awt.point import Point as Point_5fb2085e
    from ..awt.rectangle import Rectangle as Rectangle_84b109e9
    from ..awt.x_graphics import XGraphics as XGraphics_842309dd

class XStatusbarController(XStatusListener_e2740d35, XComponent_98dc0ab5, XInitialization_d46c0cca, XUpdatable_9a420ab0):
    """
    interface to be implemented by a component offering a more complex user interface to users within a status bar.
    
    A generic status bar field is represented as a simple text field. A status bar controller can be added to a Statusbar and provide information or functions with a more sophisticated user interface.
    A typical example for status bar controller is a zoom chooser. It shows the current zoom and provides general zoom levels on a pop-up menu that can be activated by a mouse action for context menus.
    
    **since**
    
        OOo 2.0

    See Also:
        `API XStatusbarController <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1frame_1_1XStatusbarController.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.frame.XStatusbarController']

    def click(self, aPos: 'Point_5fb2085e') -> None:
        """
        is called by a status bar if the user clicked with mouse into the field of the corresponding control.
        """
    def command(self, aPos: 'Point_5fb2085e', nCommand: int, bMouseEvent: bool, aData: object) -> None:
        """
        is called by a status bar if a command event is available for a controller.
        """
    def doubleClick(self, aPos: 'Point_5fb2085e') -> None:
        """
        is called by a status bar if the user double-clicked with mouse into the field of the corresponding control.
        """
    def mouseButtonDown(self, aMouseEvent: 'MouseEvent_8f430a5f') -> bool:
        """
        is called by a status bar if the mouse position is within the controller and a mouse button has been pressed.
        
        If the controller has captured the mouse input this function is also called when the mouse position is not within the controller.
        """
    def mouseButtonUp(self, aMouseEvent: 'MouseEvent_8f430a5f') -> bool:
        """
        is called by a status bar if the mouse position is within the controller and a mouse button has been released.
        
        If the controller has captured the mouse input this function is also called when the mouse position is not within the controller.
        """
    def mouseMove(self, aMouseEvent: 'MouseEvent_8f430a5f') -> bool:
        """
        is called by a status bar if the mouse position is within the controller and a mouse has been moved.
        
        If the controller has captured the mouse input this function is also called when the mouse position is not within the controller.
        """
    def paint(self, xGraphics: 'XGraphics_842309dd', OutputRectangle: 'Rectangle_84b109e9', nStyle: int) -> None:
        """
        is called by a status bar if the controller has to update the visual representation.
        """

