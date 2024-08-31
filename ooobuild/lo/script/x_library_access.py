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
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43

class XLibraryAccess(XInterface_8f010a43):
    """
    provides access to additional scripting code.
    
    This code is organized in modules and these modules contain the functions. It is possible to get just the code from a function, but you can also get the whole code of a module with all functions in it.
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API XLibraryAccess <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1script_1_1XLibraryAccess.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.script'
    __ooo_full_ns__: str = 'com.sun.star.script.XLibraryAccess'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.script.XLibraryAccess'

    @abstractmethod
    def getFunctionCode(self, FunctionName: str) -> typing.Tuple[int, ...]:
        """
        Get the compiled code of a function.
        """
        ...
    @abstractmethod
    def getFunctionSource(self, aFunctionName: str) -> str:
        """
        get the source code of a function.
        """
        ...
    @abstractmethod
    def getModuleCode(self, aModuleName: str) -> typing.Tuple[int, ...]:
        """
        Get the whole compiled code of a module.
        """
        ...
    @abstractmethod
    def getModuleNames(self) -> typing.Tuple[str, ...]:
        """
        Return all module names which contain code.
        
        e.g., { \"UtilLibrary.ModuleDate\", \"UtilLibrary.Output\", ... }
        """
        ...
    @abstractmethod
    def getModuleSource(self, aModulName: str) -> str:
        """
        get the source code of a module.
        """
        ...
    @abstractmethod
    def isFunction(self, aFunctionName: str) -> bool:
        """
        returns TRUE, if the function is accessible through this library; otherwise it returns FALSE.
        """
        ...
    @abstractmethod
    def isValidPath(self, aPathName: str) -> bool:
        """
        returns TRUE if a fully qualified function name begins with this name.
        """
        ...

__all__ = ['XLibraryAccess']

