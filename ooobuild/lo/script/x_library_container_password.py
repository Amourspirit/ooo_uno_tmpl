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
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43

class XLibraryContainerPassword(XInterface_8f010a43):
    """
    Extension of XLibraryContainer to provide password functionality.
    
    This interface should be implemented together with XLibraryContainer2

    See Also:
        `API XLibraryContainerPassword <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1script_1_1XLibraryContainerPassword.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.script'
    __ooo_full_ns__: str = 'com.sun.star.script.XLibraryContainerPassword'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.script.XLibraryContainerPassword'

    @abstractmethod
    def changeLibraryPassword(self, Name: str, OldPassword: str, NewPassword: str) -> None:
        """
        Changes the library's password.
        
        If the library wasn't password protected before: The OldPassword parameter has to be an empty string. Afterwards calls to isLibraryPasswordProtected and isLibraryPasswordVerified for this library will return true.
        
        If the library already was password protected: The OldPassword parameter has to be set to the previous defined password. If then the NewPassword parameter is an empty string the library password protection will be disabled afterwards (afterwards calls to isLibraryPasswordProtected for this library will return false). If the NewPassword parameter is not an empty string it will accepted as the new password for the library.
        
        If a library with the this name doesn't exist but isn't com.sun.star.container.NoSuchElementException is thrown.
        
        If the library exists and is password protected and a wrong OldPassword is passed to the method a com.sun.star.lang.IllegalArgumentException is thrown.
        
        If the library exists and isn't password protected and the OldPassword isn't an empty string or the library is read only a com.sun.star.lang.IllegalArgumentException is thrown.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
        """
        ...
    @abstractmethod
    def isLibraryPasswordProtected(self, Name: str) -> bool:
        """
        Returns true if the accessed library item is protected by a password.
        
        If a library with the this name doesn't exist a com.sun.star.container.NoSuchElementException is thrown.

        Raises:
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
        """
        ...
    @abstractmethod
    def isLibraryPasswordVerified(self, Name: str) -> bool:
        """
        Returns true if the accessed library item is protected by a password (see isLibraryPasswordProtected) and the password was already verified with verifyLibraryPassword or if an initial password was set with changeLibraryPassword.
        
        If a library with the this name doesn't exist a com.sun.star.container.NoSuchElementException is thrown.
        
        If the library exists but isn't password protected a com.sun.star.lang.IllegalArgumentException is thrown.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
        """
        ...
    @abstractmethod
    def verifyLibraryPassword(self, Name: str, Password: str) -> bool:
        """
        Verifies the library's password.
        
        If the correct password was passed, the method returns true and further calls to isLibraryPasswordVerified will also return true.
        
        If a library with the this name doesn't exist a com.sun.star.container.NoSuchElementException is thrown.
        
        If the library exists but isn't password protected a com.sun.star.lang.IllegalArgumentException is thrown.
        
        If the library password is already verified a com.sun.star.lang.IllegalArgumentException is thrown.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
        """
        ...

__all__ = ['XLibraryContainerPassword']

