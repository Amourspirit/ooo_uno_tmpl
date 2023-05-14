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
import typing
from ..io.x_input_stream import XInputStream as XInputStream_98d40ab4


class InsertCommandArgument(object):
    """
    Struct Class

    The argument for the command \"insert\".

    See Also:
        `API InsertCommandArgument <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1ucb_1_1InsertCommandArgument.html>`_
    """
    typeName: Literal['com.sun.star.ucb.InsertCommandArgument']

    def __init__(self, Data: typing.Optional[XInputStream_98d40ab4] = ..., ReplaceExisting: typing.Optional[bool] = ...) -> None:
        """
        Constructor

        Arguments:
            Data (XInputStream, optional): Data value.
            ReplaceExisting (bool, optional): ReplaceExisting value.
        """
        ...


    @property
    def Data(self) -> XInputStream_98d40ab4:
        """
        A stream containing document data.
        
        This member can be left blank, if no (new) document data shall be written by the implementation of the \"insert\" command.
        """
        ...

    @Data.setter
    def Data(self, value: XInputStream_98d40ab4) -> None:
        ...

    @property
    def ReplaceExisting(self) -> bool:
        """
        A flag indicating whether a possibly existing content (and its data) shall be overwritten.
        
        Implementations that are not able to detect whether there are previous data may ignore this parameter and will always write the new data.
        """
        ...

    @ReplaceExisting.setter
    def ReplaceExisting(self, value: bool) -> None:
        ...

