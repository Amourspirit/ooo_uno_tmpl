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
# Namespace: com.sun.star.ui
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .xui_configuration_listener import XUIConfigurationListener as XUIConfigurationListener_34e90f7a

class XUIConfiguration(XInterface_8f010a43):
    """
    supports to notify other implementations about changes of a user interface configuration manager.
    
    The XUIConfiguration interface is provided for user interface configuration managers which need to broadcast changes within the container; that means the actions of adding, replacing and removing elements are broadcast to listeners.
    
    This can be useful for UI to enable/disable some functions without actually accessing the data.
    
    **since**
    
        OOo 2.0

    See Also:
        `API XUIConfiguration <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1ui_1_1XUIConfiguration.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ui'
    __ooo_full_ns__: str = 'com.sun.star.ui.XUIConfiguration'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.ui.XUIConfiguration'

    @abstractmethod
    def addConfigurationListener(self, Listener: 'XUIConfigurationListener_34e90f7a') -> None:
        """
        adds the specified listener to receive events when elements are changed, inserted or removed.
        
        It is suggested to allow multiple registration of the same listener, thus for each time a listener is added, it has to be removed.
        """
        ...
    @abstractmethod
    def removeConfigurationListener(self, Listener: 'XUIConfigurationListener_34e90f7a') -> None:
        """
        removes the specified listener so it does not receive any events from this user interface configuration manager.
        
        It is suggested to allow multiple registration of the same listener, thus for each time a listener is added, it has to be removed.
        """
        ...

__all__ = ['XUIConfiguration']

