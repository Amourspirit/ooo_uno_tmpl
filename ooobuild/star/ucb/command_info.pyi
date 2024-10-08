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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.ucb
# Libre Office Version: 2024.2
import typing


class CommandInfo(object):
    """
    Struct Class

    describes a command.

    See Also:
        `API CommandInfo <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1ucb_1_1CommandInfo.html>`_
    """
    typeName: str = 'com.sun.star.ucb.CommandInfo'

    def __init__(self, Name: typing.Optional[str] = ..., Handle: typing.Optional[int] = ..., ArgType: typing.Optional[object] = ...) -> None:
        """
        Constructor

        Arguments:
            Name (str, optional): Name value.
            Handle (int, optional): Handle value.
            ArgType (object, optional): ArgType value.
        """
        ...

    @property
    def Name(self) -> str:
        """
        contains the name of a command.
        """
        ...
    @Name.setter
    def Name(self, value: str) -> None:
        ...
    @property
    def Handle(self) -> int:
        """
        contains an implementation specific handle for the command.
        
        It may be -1 if the implementation has no handle.
        """
        ...
    @Handle.setter
    def Handle(self, value: int) -> None:
        ...
    @property
    def ArgType(self) -> object:
        """
        contains the type of the command's argument.
        """
        ...
    @ArgType.setter
    def ArgType(self, value: object) -> None:
        ...

