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
# Namespace: com.sun.star.util
import typing
from abc import abstractmethod
from ..lang.x_event_listener import XEventListener as XEventListener_c7230c4a
if typing.TYPE_CHECKING:
    from ..lang.event_object import EventObject as EventObject_a3d70b03

class XModifyListener(XEventListener_c7230c4a):
    """
    makes it possible to receive events when a model object changes.

    See Also:
        `API XModifyListener <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1util_1_1XModifyListener.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.util'
    __ooo_full_ns__: str = 'com.sun.star.util.XModifyListener'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.util.XModifyListener'

    @abstractmethod
    def modified(self, aEvent: 'EventObject_a3d70b03') -> None:
        """
        is called when something changes in the object.
        
        Due to such an event, it may be necessary to update views or controllers.
        
        The source of the event may be the content of the object to which the listener is registered.
        """

__all__ = ['XModifyListener']

