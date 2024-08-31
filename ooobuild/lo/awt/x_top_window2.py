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
# Namespace: com.sun.star.awt
from __future__ import annotations
from abc import abstractproperty
from .x_top_window import XTopWindow as XTopWindow_8ebb0a57

class XTopWindow2(XTopWindow_8ebb0a57):
    """
    extends XTopWindow with additional functionality

    See Also:
        `API XTopWindow2 <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XTopWindow2.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt'
    __ooo_full_ns__: str = 'com.sun.star.awt.XTopWindow2'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.awt.XTopWindow2'

    @abstractproperty
    def Display(self) -> int:
        """
        controls on which display the window is shown.
        
        When retrieving this property, in case the window is positioned on multiple displays, the number returned will be of the display containing the upper left pixel of the frame area (that is of the client area on system decorated windows, or the frame area of undecorated resp. owner decorated windows).
        """
        ...

    @abstractproperty
    def IsMaximized(self) -> bool:
        """
        controls whether the window is currently maximized
        """
        ...

    @abstractproperty
    def IsMinimized(self) -> bool:
        """
        controls whether the window is currently minimized
        """
        ...


__all__ = ['XTopWindow2']

