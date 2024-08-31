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
# Namespace: com.sun.star.script
from __future__ import annotations
import typing

from .x_library_container2 import XLibraryContainer2 as XLibraryContainer2_1c490e9f
from ..util.x_modifiable import XModifiable as XModifiable_a4f60b0a


class XPersistentLibraryContainer(XLibraryContainer2_1c490e9f, XModifiable_a4f60b0a):
    """
    describes a container of script libraries which is persistent.
    
    The type of persistence of the container elements is not defined here, but in derived interfaces or services using XPersistentLibraryContainer.
    
    The actual libraries are stored in some object - a sub folder, or a sub storage, for example - below the root location.
    
    **since**
    
        OOo 2.3

    See Also:
        `API XPersistentLibraryContainer <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1script_1_1XPersistentLibraryContainer.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.script.XPersistentLibraryContainer'

    def storeLibraries(self) -> None:
        """
        stores the libraries to the current location.

        Raises:
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
        ...

    @property
    def ContainerLocationName(self) -> str:
        """
        denotes the name of the sub location where the container elements are actually stored.
        """
        ...
    @ContainerLocationName.setter
    def ContainerLocationName(self, value: str) -> None:
        ...
    @property
    def RootLocation(self) -> object:
        """
        denotes the root location associated with the container.
        
        The type of this location - it might be a folder in a file system, a storage, or anything else - is not specified here, but in derived interfaces or services implementing XPersistentLibraryContainer.
        
        All operations of the library container take place in a location below the root location, the so-called container location, whose name is exposed as ContainerLocationName.
        """
        ...
    @RootLocation.setter
    def RootLocation(self, value: object) -> None:
        ...

