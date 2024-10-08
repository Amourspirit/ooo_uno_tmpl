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
# Namespace: com.sun.star.uno
# Libre Office Version: 2024.2
from typing_extensions import Literal
import typing
from .exception import Exception as Exception_85530a09
from .x_interface import XInterface as XInterface_8f010a43

class RuntimeException(Exception_85530a09):
    """
    Exception Class

    This exception or a subclass can occur at every interface method.
    
    It shall signal an error, which was not covered by the interface method specification. This exception (or a derived one) is thrown, when for instance an interprocess bridge to the object broke down, some explicitly forbidden invalid parameters were passed ( e.g. null references ) or the called object has been disposed before.

    See Also:
        `API RuntimeException <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1uno_1_1RuntimeException.html>`_
    """

    typeName: Literal['com.sun.star.uno.RuntimeException']

    def __init__(self, Message: typing.Optional[str] = ..., Context: typing.Optional[XInterface_8f010a43] = ...) -> None:
        """
        Constructor

        Arguments:
            Message (str, optional): Message value.
            Context (XInterface, optional): Context value.
        """
        ...

__all__ = ['RuntimeException']

