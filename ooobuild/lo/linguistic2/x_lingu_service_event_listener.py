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
# Namespace: com.sun.star.linguistic2
from __future__ import annotations
import typing
from abc import abstractmethod
from ..lang.x_event_listener import XEventListener as XEventListener_c7230c4a
if typing.TYPE_CHECKING:
    from .lingu_service_event import LinguServiceEvent as LinguServiceEvent_5ab71047

class XLinguServiceEventListener(XEventListener_c7230c4a):
    """
    is used to inform listeners about LinguServiceEvents.
    
    The function of this interface is used by the com.sun.star.linguistic2.XLinguServiceEventBroadcaster to inform its listeners about the com.sun.star.linguistic2.LinguServiceEvents.

    See Also:
        `API XLinguServiceEventListener <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1linguistic2_1_1XLinguServiceEventListener.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.linguistic2'
    __ooo_full_ns__: str = 'com.sun.star.linguistic2.XLinguServiceEventListener'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.linguistic2.XLinguServiceEventListener'

    @abstractmethod
    def processLinguServiceEvent(self, aLngSvcEvent: LinguServiceEvent_5ab71047) -> None:
        """
        """
        ...

__all__ = ['XLinguServiceEventListener']

