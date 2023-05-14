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
# Exception Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.script
# Libre Office Version: 7.3
from typing_extensions import Literal
import typing
from ..uno.exception import Exception as Exception_85530a09
from ..uno.x_interface import XInterface as XInterface_8f010a43

class BasicErrorException(Exception_85530a09):
    """
    Exception Class

    is thrown in order to transport an error to Basic.
    
    **since**
    
        OOo 2.0

    See Also:
        `API BasicErrorException <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1script_1_1BasicErrorException.html>`_
    """

    typeName: Literal['com.sun.star.script.BasicErrorException']

    def __init__(self, Message: typing.Optional[str] = ..., Context: typing.Optional[XInterface_8f010a43] = ..., ErrorCode: typing.Optional[int] = ..., ErrorMessageArgument: typing.Optional[str] = ...) -> None:
        """
        Constructor

        Arguments:
            Message (str, optional): Message value.
            Context (XInterface, optional): Context value.
            ErrorCode (int, optional): ErrorCode value.
            ErrorMessageArgument (str, optional): ErrorMessageArgument value.
        """
        ...
    @property
    def ErrorCode(self) -> int:
        """
        The error code.
        """
        ...

    @ErrorCode.setter
    def ErrorCode(self, value: int) -> None:
        ...
    @property
    def ErrorMessageArgument(self) -> str:
        """
        Specifies the argument which is used in the localized error message for the placeholder.
        """
        ...

    @ErrorMessageArgument.setter
    def ErrorMessageArgument(self, value: str) -> None:
        ...

__all__ = ['BasicErrorException']

