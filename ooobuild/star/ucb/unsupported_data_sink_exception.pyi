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
# Exception Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.ucb
# Libre Office Version: 2024.2
from typing_extensions import Literal
import typing
from ..uno.exception import Exception as Exception_85530a09
from ..uno.x_interface import XInterface as XInterface_8f010a43

class UnsupportedDataSinkException(Exception_85530a09):
    """
    Exception Class

    This exception is used to indicate that the requested type of data sink is not supported.
    
    For example, each OpenCommandArgument supplied as argument of the command \"open\" contains such a data sink.

    See Also:
        `API UnsupportedDataSinkException <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1ucb_1_1UnsupportedDataSinkException.html>`_
    """

    typeName: Literal['com.sun.star.ucb.UnsupportedDataSinkException']

    def __init__(self, Message: typing.Optional[str] = ..., Context: typing.Optional[XInterface_8f010a43] = ..., Sink: typing.Optional[XInterface_8f010a43] = ...) -> None:
        """
        Constructor

        Arguments:
            Message (str, optional): Message value.
            Context (XInterface, optional): Context value.
            Sink (XInterface, optional): Sink value.
        """
        ...
    @property
    def Sink(self) -> XInterface_8f010a43:
        """
        contains the data sink that is not supported.
        """
        ...
    @Sink.setter
    def Sink(self, value: XInterface_8f010a43) -> None:
        ...

__all__ = ['UnsupportedDataSinkException']

