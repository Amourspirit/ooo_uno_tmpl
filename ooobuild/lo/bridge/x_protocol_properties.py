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
# Namespace: com.sun.star.bridge
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .protocol_property import ProtocolProperty as ProtocolProperty_ff280e2c

class XProtocolProperties(XInterface_8f010a43):
    """
    Bridge internal interface, that allows to change protocol settings of the remote counter part.
    
    In general, this interface is implemented by the bridge itself. It must not be called from outside the bridge.
    
    INTERNAL INTERFACE, DO NOT USE IT ELSEWHERE!

    See Also:
        `API XProtocolProperties <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1bridge_1_1XProtocolProperties.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.bridge'
    __ooo_full_ns__: str = 'com.sun.star.bridge.XProtocolProperties'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.bridge.XProtocolProperties'

    @abstractmethod
    def commitChange(self, newValues: 'typing.Tuple[ProtocolProperty_ff280e2c, ...]') -> None:
        """
        called to commit a protocol change.
        
        It is only allowed to call commitChange, if requestChange has been called previously and the return value was true. The new properties are valid after the reply of commitChange has been received. Note, that this is difficult for the callee, because it must marshal the reply with the old settings.
        
        All properties not mentioned in the list are unchanged. Note that the bridge must be blocked for other threads, before commitChange is sent and unblocked after the reply has been received. This blocks the bridge.

        Raises:
            com.sun.star.bridge.InvalidProtocolChangeException: ``InvalidProtocolChangeException``
        """
        ...
    @abstractmethod
    def getProperties(self) -> 'typing.Tuple[ProtocolProperty_ff280e2c, ...]':
        """
        called to get a list of bridge internal properties.
        
        Which properties can be retrieved, is protocol dependent.
        
        The properties MUST NOT change between a requestChange and a commit change call.
        """
        ...
    @abstractmethod
    def requestChange(self, nRandomNumber: int) -> int:
        """
        called to initiate a protocol change.
        
        This method should always be called in the scope of the local bridge setting object, because the remote counter part may do such a call at the same time (typically at startup time).
        """
        ...

__all__ = ['XProtocolProperties']

