# coding: utf-8
#
# Copyright 2023-2024 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 2024.2
# Namespace: com.sun.star.embed
from __future__ import annotations
import typing

from ..lang.x_component import XComponent as XComponent_98dc0ab5
if typing.TYPE_CHECKING:
    from ..awt.size import Size as Size_576707ef
    from .x_hatch_window_controller import XHatchWindowController as XHatchWindowController_45430fe1


class XHatchWindow(XComponent_98dc0ab5):
    """
    specifies the operations for a hatch window.
    
    A hatch window is a kind of window that is adopted to contain an embedded object window to represent the contained window border and to handle resizing/moving in a specific way: after user have selected the new size/placement the hatching window sends request to owner for resizing/moving. Thus the window can not resize/move itself.

    See Also:
        `API XHatchWindow <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1embed_1_1XHatchWindow.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.embed.XHatchWindow'

    def setController(self, xController: XHatchWindowController_45430fe1) -> None:
        """
        sets the object that will control resizing/moving, if the object is not set the window can not be resized/moved.
        """
        ...

    @property
    def HatchBorderSize(self) -> Size_576707ef:
        """
        """
        ...
    @HatchBorderSize.setter
    def HatchBorderSize(self, value: Size_576707ef) -> None:
        ...

