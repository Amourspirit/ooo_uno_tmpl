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
# Libre Office Version: 7.3
from typing_extensions import Literal
from .open_command_argument2 import OpenCommandArgument2 as OpenCommandArgument2_9210e08
from ..beans.property import Property as Property_8f4e0a76
from ..uno.x_interface import XInterface as XInterface_8f010a43
from .numbered_sorting_info import NumberedSortingInfo as NumberedSortingInfo_fd0e0de6
import typing
from ..beans.named_value import NamedValue as NamedValue_a37a0af3


class OpenCommandArgument3(OpenCommandArgument2_9210e08):
    """
    Struct Class

    Extended argument for commands like \"open\".
    
    We're extending OpenCommandArgument even more, to provide some opening flags on to webdav.

    See Also:
        `API OpenCommandArgument3 <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1ucb_1_1OpenCommandArgument3.html>`_
    """
    typeName: Literal['com.sun.star.ucb.OpenCommandArgument3']

    def __init__(self, Properties: typing.Optional[typing.Tuple[Property_8f4e0a76, ...]] = ..., Mode: typing.Optional[int] = ..., Priority: typing.Optional[int] = ..., Sink: typing.Optional[XInterface_8f010a43] = ..., SortingInfo: typing.Optional[typing.Tuple[NumberedSortingInfo_fd0e0de6, ...]] = ..., OpeningFlags: typing.Optional[typing.Tuple[NamedValue_a37a0af3, ...]] = ...) -> None:
        """
        Constructor

        Arguments:
            Properties (typing.Tuple[Property, ...], optional): Properties value.
            Mode (int, optional): Mode value.
            Priority (int, optional): Priority value.
            Sink (XInterface, optional): Sink value.
            SortingInfo (typing.Tuple[NumberedSortingInfo, ...], optional): SortingInfo value.
            OpeningFlags (typing.Tuple[NamedValue, ...], optional): OpeningFlags value.
        """
        ...


    @property
    def OpeningFlags(self) -> typing.Tuple[NamedValue_a37a0af3, ...]:
        """
        Flags to use for opening.
        
        WebDav e.g. uses \"KeepAlive\" to enable/disable the respective http feature.
        """
        ...

    @OpeningFlags.setter
    def OpeningFlags(self, value: typing.Tuple[NamedValue_a37a0af3, ...]) -> None:
        ...

