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
    from ..embed.x_storage import XStorage as XStorage_8e460a32

class XUIConfigurationPersistence(XInterface_8f010a43):
    """
    specifies a persistence interface which supports to load/store user interface configuration data to a storage and to retrieve information about the current state.
    
    **since**
    
        OOo 2.0

    See Also:
        `API XUIConfigurationPersistence <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1ui_1_1XUIConfigurationPersistence.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ui'
    __ooo_full_ns__: str = 'com.sun.star.ui.XUIConfigurationPersistence'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.ui.XUIConfigurationPersistence'

    @abstractmethod
    def isModified(self) -> bool:
        """
        provides the current modify state of the configuration manager instance.
        """
        ...
    @abstractmethod
    def isReadOnly(self) -> bool:
        """
        provides the current read-only state of the user configuration manager.
        
        Storing a user interface configuration to a read-only storage is not possible. A read-only configuration manager instance will also not support any changes to its configuration settings.
        """
        ...
    @abstractmethod
    def reload(self) -> None:
        """
        reloads the configuration data from the storage and reinitialize the user interface configuration manager instance with this data.
        
        It is up to the implementation if it defers the first loading process until the first data request using XUIConfigurationManager interface.

        Raises:
            com.sun.star.uno.Exception: ``Exception``
        """
        ...
    @abstractmethod
    def store(self) -> None:
        """
        stores the configuration data to the storage provided by setStorage() from the storage and initialize the user interface configuration manager instance with the newly data.
        
        This call can throw an com.sun.star.io.IOException if store() cannot store its data into the internal storage.

        Raises:
            com.sun.star.uno.Exception: ``Exception``
        """
        ...
    @abstractmethod
    def storeToStorage(self, Storage: 'XStorage_8e460a32') -> None:
        """
        stores the configuration data to the provided storage, ignoring the previously set storage by setStorage().
        
        Can be used to make copy of the current user interface configuration data to another storage. This call will throw an com.sun.star.io.IOException if the provided storage is in read-only mode.

        Raises:
            com.sun.star.uno.Exception: ``Exception``
        """
        ...

__all__ = ['XUIConfigurationPersistence']

