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
# Namespace: com.sun.star.bridge
from __future__ import annotations
import typing

from ..uno.x_interface import XInterface as XInterface_8f010a43


class XBridgeSupplier2(XInterface_8f010a43):
    """
    defines the interface for creating bridges to other object models.
    
    The created bridges are transparent to the user. That is, if one maps an interface into the target model, then the resulting target interface is a bridge implementation, that is not being noticed by an user. During a call on that interface, the bridge is invoked to convert the arguments and carry out a call according to the rules of the source model. Return values are automatically mapped to the types of the target model.
    
    Simple types are mapped to simple target types. That is, there is no additional bridging code involved when those types are being used.
    
    Sometimes a bridge cannot be created, depending on whether a program uses the XBridgeSupplier2 interface remotely. Assuming one wants to bridge an OLE Automation object to UNO by calling createBridge on a proxy, then the UNO remote bridge would not recognise that the Any argument contains an IDispatch interface. Therefore it cannot marshal it as COM requires it and the bridgeing would fail. To prevent this, implementations of this interface should be aware of this scenario and if necessary take the appropriate steps. The process ID argument to the createBridge function represents the calling process and may be used by the implementation to determine if it is being accessed remotely.
    
    All objects, whether they are part of the UNO object model or not, are carried in an any. The representation of this object is heavily model-dependent and has to be specified in the following list:
    
    Any implementation can supply its own bridges to other object models by implementing this interface and returning the bridge when the method XBridgeSupplier2.createBridge() is called with itself as the first parameter.

    See Also:
        `API XBridgeSupplier2 <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1bridge_1_1XBridgeSupplier2.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.bridge.XBridgeSupplier2'

    def createBridge(self, aModelDepObject: typing.Any, aProcessId: typing.Tuple[int, ...], nSourceModelType: int, nDestModelType: int) -> typing.Any:
        """
        creates a bridge to provide an object of one object model with another.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...


