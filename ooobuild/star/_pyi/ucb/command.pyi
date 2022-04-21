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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.ucb
# Libre Office Version: 7.2
from typing_extensions import Literal
import typing


class Command(object):
    """
    Struct Class

    contains a command.

    See Also:
        `API Command <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1ucb_1_1Command.html>`_
    """
    typeName: Literal['com.sun.star.ucb.Command']

    def __init__(self, Name: typing.Optional[str] = ..., Handle: typing.Optional[int] = ..., Argument: typing.Optional[object] = ...) -> None:
        """
        Constructor

        Arguments:
            Name (str, optional): Name value.
            Handle (int, optional): Handle value.
            Argument (object, optional): Argument value.
        """


    @property
    def Name(self) -> str:
        """
        contains the name of the command.
        """


    @property
    def Handle(self) -> int:
        """
        contains an implementation specific handle for the command.
        
        It must be -1 if the implementation has no handle. 0 is a valid command handle.
        """


    @property
    def Argument(self) -> object:
        """
        contains the argument of the command
        """


