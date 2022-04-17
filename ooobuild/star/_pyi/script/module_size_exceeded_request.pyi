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
from ooo.oenv.env_const import UNO_NONE
import typing
from ..uno.exception import Exception as Exception_85530a09
from ..uno.x_interface import XInterface as XInterface_8f010a43

class ModuleSizeExceededRequest(Exception_85530a09):
    """
    Exception Class

    Is used for interaction handle in case password protected modules exceed the size that can be stored in OpenOffice 2.x, 1.x formats.

    See Also:
        `API ModuleSizeExceededRequest <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1script_1_1ModuleSizeExceededRequest.html>`_
    """

    typeName: Literal['com.sun.star.script.ModuleSizeExceededRequest']

    def __init__(self, Message: typing.Optional[str] = ..., Context: typing.Optional[XInterface_8f010a43] = ..., Names: typing.Optional[typing.Tuple[str, ...]] = ...) -> None:
        """
        Constructor

        Arguments:
            Message (str, optional): Message value.
            Context (XInterface, optional): Context value.
            Names (typing.Tuple[str, ...], optional): Names value.
        """
    @property
    def Names(self) -> typing.Tuple[str, ...]:
        """
        The name of the modules that exceed size that can be stored.
        """


__all__ = ['ModuleSizeExceededRequest']

