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
# Libre Office Version: 7.4
# Namespace: com.sun.star.script.vba
import typing
from abc import abstractmethod, abstractproperty, ABC
if typing.TYPE_CHECKING:
    from .xvba_script_listener import XVBAScriptListener as XVBAScriptListener_533e0ff0

class XVBACompatibility(ABC):
    """

    See Also:
        `API XVBACompatibility <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1script_1_1vba_1_1XVBACompatibility.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.script.vba'
    __ooo_full_ns__: str = 'com.sun.star.script.vba.XVBACompatibility'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.script.vba.XVBACompatibility'

    @abstractmethod
    def addVBAScriptListener(self, Listener: 'XVBAScriptListener_533e0ff0') -> None:
        """
        """
        ...
    @abstractmethod
    def broadcastVBAScriptEvent(self, Identifier: int, ModuleName: str) -> None:
        """
        """
        ...
    @abstractmethod
    def removeVBAScriptListener(self, Listener: 'XVBAScriptListener_533e0ff0') -> None:
        """
        """
        ...
    @abstractproperty
    def ProjectName(self) -> str:
        """
        """
        ...

    @abstractproperty
    def RunningVBAScripts(self) -> int:
        """
        """
        ...

    @abstractproperty
    def VBACompatibilityMode(self) -> bool:
        """
        """
        ...


__all__ = ['XVBACompatibility']

