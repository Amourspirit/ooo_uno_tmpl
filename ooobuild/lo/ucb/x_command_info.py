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
# Namespace: com.sun.star.ucb
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .command_info import CommandInfo as CommandInfo_98490a8d

class XCommandInfo(XInterface_8f010a43):
    """
    provides access to information on a set of commands.

    See Also:
        `API XCommandInfo <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1ucb_1_1XCommandInfo.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ucb'
    __ooo_full_ns__: str = 'com.sun.star.ucb.XCommandInfo'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.ucb.XCommandInfo'

    @abstractmethod
    def getCommandInfoByHandle(self, Handle: int) -> 'CommandInfo_98490a8d':
        """
        returns information for a specific command.

        Raises:
            com.sun.star.ucb.UnsupportedCommandException: ``UnsupportedCommandException``
        """
        ...
    @abstractmethod
    def getCommandInfoByName(self, Name: str) -> 'CommandInfo_98490a8d':
        """
        returns information for a specific command.

        Raises:
            com.sun.star.ucb.UnsupportedCommandException: ``UnsupportedCommandException``
        """
        ...
    @abstractmethod
    def getCommands(self) -> 'typing.Tuple[CommandInfo_98490a8d, ...]':
        """
        obtains information for all supported commands.
        """
        ...
    @abstractmethod
    def hasCommandByHandle(self, Handle: int) -> bool:
        """
        checks whether a specific command is supported.
        """
        ...
    @abstractmethod
    def hasCommandByName(self, Name: str) -> bool:
        """
        checks whether a command specific is supported.
        """
        ...

__all__ = ['XCommandInfo']

