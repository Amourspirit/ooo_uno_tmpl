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
# Namespace: com.sun.star.inspection
from __future__ import annotations
import typing

from .x_property_control import XPropertyControl as XPropertyControl_3f260fe2
if typing.TYPE_CHECKING:
    from ..awt.x_action_listener import XActionListener as XActionListener_c7560c50


class XHyperlinkControl(XPropertyControl_3f260fe2):
    """
    defines the interface for an XPropertyControl which displays its value in a hyperlink-like way
    
    Hyperlink controls exchange their value (XPropertyControl.Value) as strings.
    
    **since**
    
        OOo 2.0.3

    See Also:
        `API XHyperlinkControl <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1inspection_1_1XHyperlinkControl.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.inspection.XHyperlinkControl'

    def addActionListener(self, listener: XActionListener_c7560c50) -> None:
        """
        adds a listener which will be notified when the user clicked the hyperlink text in the control
        """
        ...
    def removeActionListener(self, listener: XActionListener_c7560c50) -> None:
        """
        removes a listener which was previously added via addActionListener()
        """
        ...



