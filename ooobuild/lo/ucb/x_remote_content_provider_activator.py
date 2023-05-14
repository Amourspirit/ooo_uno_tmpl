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
# Namespace: com.sun.star.ucb
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_content_provider_manager import XContentProviderManager as XContentProviderManager_37e00f7b

class XRemoteContentProviderActivator(XInterface_8f010a43):
    """
    This interface should be implemented together with XRemoteContentProviderAcceptor and allows for a lazy implementation of XRemoteContentProviderAcceptor.addRemoteContentProvider().
    
    The way this works might change, therefore this interface is marked as deprecated.
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API XRemoteContentProviderActivator <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1ucb_1_1XRemoteContentProviderActivator.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ucb'
    __ooo_full_ns__: str = 'com.sun.star.ucb.XRemoteContentProviderActivator'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.ucb.XRemoteContentProviderActivator'

    @abstractmethod
    def activateRemoteContentProviders(self) -> 'XContentProviderManager_37e00f7b':
        """
        Activate (i.e., register at the broker) the remote content providers that until now have only been remembered by XRemoteContentProviderAcceptor.addRemoteContentProvider(), but not registered.
        
        This allows for XRemoteContentProviderAcceptor.addRemoteContentProvider() to be implemented in a lazy fashion (remember the remote content providers, but do not register them right away), which can increase performance in certain situations. But it is not required that an implementation of XRemoteContentProviderAcceptor uses this lazy strategy (and thus also implements this interface).
        """
        ...

__all__ = ['XRemoteContentProviderActivator']

