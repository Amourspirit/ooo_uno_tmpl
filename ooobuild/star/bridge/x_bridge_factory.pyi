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
# Namespace: com.sun.star.bridge
from __future__ import annotations
import typing

from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_bridge import XBridge as XBridge_8e4e0a1a
    from .x_instance_provider import XInstanceProvider as XInstanceProvider_b090e4d
    from ..connection.x_connection import XConnection as XConnection_f2320da0


class XBridgeFactory(XInterface_8f010a43):
    """
    factory to create interprocess bridges.

    See Also:
        `API XBridgeFactory <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1bridge_1_1XBridgeFactory.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.bridge.XBridgeFactory'

    def createBridge(self, sName: str, sProtocol: str, aConnection: XConnection_f2320da0, anInstanceProvider: XInstanceProvider_b090e4d) -> XBridge_8e4e0a1a:
        """
        tries to create a UNO interprocess bridge.
        
        If empty, an anonymous bridge is created, which cannot be retrieved with getBridge(). No BridgeExistsException can be thrown in this case.

        Raises:
            : ````
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    def getBridge(self, sName: str) -> XBridge_8e4e0a1a:
        """
        tries to get a bridge by this name.
        
        Cannot be retrieved, when the bridge got disposed before.
        """
        ...
    def getExistingBridges(self) -> typing.Tuple[XBridge_8e4e0a1a, ...]:
        """
        returns the sequence of all named and unnamed UNO interprocess bridges that are instantiated at the time the call is made.
        """
        ...



