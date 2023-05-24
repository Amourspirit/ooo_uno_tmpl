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
# Namespace: com.sun.star.view
from __future__ import annotations
import typing

from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_printable_listener import XPrintableListener as XPrintableListener_fe8a0e02


class XPrintableBroadcaster(XInterface_8f010a43):
    """
    allows for getting information about a print job.
    
    XPrintableBroadcaster can be implemented by classes which implement XPrintable. It allows a XPrintableListener to be registered, thus a client object will learn about the print progress.

    See Also:
        `API XPrintableBroadcaster <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1view_1_1XPrintableBroadcaster.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.view.XPrintableBroadcaster'

    def addPrintableListener(self, xListener: XPrintableListener_fe8a0e02) -> None:
        """
        adds an XPrintableListener to be notified about print progress.
        """
        ...
    def removePrintableListener(self, xListener: XPrintableListener_fe8a0e02) -> None:
        """
        removes an XPrintableListener.
        """
        ...


