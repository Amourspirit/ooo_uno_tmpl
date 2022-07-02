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
# Namespace: com.sun.star.configuration.backend
import typing
from abc import abstractmethod
from ...uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_backend_changes_listener import XBackendChangesListener as XBackendChangesListener_924c1675

class XBackendChangesNotifier(XInterface_8f010a43):
    """
    broadcasts changes when data from backend sources has changed.

    See Also:
        `API XBackendChangesNotifier <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1configuration_1_1backend_1_1XBackendChangesNotifier.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.configuration.backend'
    __ooo_full_ns__: str = 'com.sun.star.configuration.backend.XBackendChangesNotifier'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.configuration.backend.XBackendChangesNotifier'

    @abstractmethod
    def addChangesListener(self, aListener: 'XBackendChangesListener_924c1675', component: str) -> None:
        """
        adds the specified listener to receive events when changes occurred.
        """
        ...
    @abstractmethod
    def removeChangesListener(self, aListener: 'XBackendChangesListener_924c1675', component: str) -> None:
        """
        removes the specified listener.
        """
        ...

__all__ = ['XBackendChangesNotifier']

