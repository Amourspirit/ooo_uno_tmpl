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
# Namespace: com.sun.star.script
import typing
from abc import abstractmethod
from .x_event_attacher import XEventAttacher as XEventAttacher_e3780d23
if typing.TYPE_CHECKING:
    from ..lang.x_event_listener import XEventListener as XEventListener_c7230c4a
    from .event_listener import EventListener as EventListener_d7890ce5
    from ..uno.x_interface import XInterface as XInterface_8f010a43

class XEventAttacher2(XEventAttacher_e3780d23):
    """

    See Also:
        `API XEventAttacher2 <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1script_1_1XEventAttacher2.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.script'
    __ooo_full_ns__: str = 'com.sun.star.script.XEventAttacher2'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.script.XEventAttacher2'

    @abstractmethod
    def attachMultipleEventListeners(self, xTarget: 'XInterface_8f010a43', aListeners: 'typing.Tuple[EventListener_d7890ce5, ...]') -> 'typing.Tuple[XEventListener_c7230c4a, ...]':
        """
        Register a multiple set of listeners listening for the same target.
        
        Besides passing multiple listeners, the behavior of this method is identical to that of attachSingleEventListener().

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.beans.IntrospectionException: ``IntrospectionException``
            com.sun.star.script.CannotCreateAdapterException: ``CannotCreateAdapterException``
            com.sun.star.lang.ServiceNotRegisteredException: ``ServiceNotRegisteredException``
        """
        ...

__all__ = ['XEventAttacher2']

