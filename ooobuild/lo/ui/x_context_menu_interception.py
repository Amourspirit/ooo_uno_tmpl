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
# Namespace: com.sun.star.ui
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_context_menu_interceptor import XContextMenuInterceptor as XContextMenuInterceptor_295c0f47

class XContextMenuInterception(XInterface_8f010a43):
    """
    This interface enables an object to get interceptors registered that change context menus or prevent them from being executed.

    See Also:
        `API XContextMenuInterception <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1ui_1_1XContextMenuInterception.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ui'
    __ooo_full_ns__: str = 'com.sun.star.ui.XContextMenuInterception'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.ui.XContextMenuInterception'

    @abstractmethod
    def registerContextMenuInterceptor(self, Interceptor: 'XContextMenuInterceptor_295c0f47') -> None:
        """
        registers an XContextMenuInterceptor, which will become the first interceptor in the chain of registered interceptors.
        """
        ...
    @abstractmethod
    def releaseContextMenuInterceptor(self, Interceptor: 'XContextMenuInterceptor_295c0f47') -> None:
        """
        removes an XContextMenuInterceptor which was previously registered using XContextMenuInterception.registerContextMenuInterceptor().
        
        The order of removals is arbitrary. It is not necessary to remove the last registered interceptor first.
        """
        ...

__all__ = ['XContextMenuInterception']

