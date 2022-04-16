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
# Namespace: com.sun.star.script.vba
from typing_extensions import Literal
import typing
from abc import ABC
if typing.TYPE_CHECKING:
    from ..module_info import ModuleInfo as ModuleInfo_b2090b8f

class XVBAModuleInfo(ABC):
    """

    See Also:
        `API XVBAModuleInfo <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1script_1_1vba_1_1XVBAModuleInfo.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.script.vba.XVBAModuleInfo']

    def getModuleInfo(self, ModuleName: str) -> 'ModuleInfo_b2090b8f':
        """

        Raises:
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
    def hasModuleInfo(self, ModuleName: str) -> bool:
        """
        """
    def insertModuleInfo(self, ModuleName: str, ModuleInfo: 'ModuleInfo_b2090b8f') -> None:
        """

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.container.ElementExistException: ``ElementExistException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
    def removeModuleInfo(self, ModuleName: str) -> None:
        """

        Raises:
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """

