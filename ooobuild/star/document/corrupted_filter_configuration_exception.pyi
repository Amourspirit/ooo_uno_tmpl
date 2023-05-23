# coding: utf-8
#
# Copyright 2023 :Barry-Thomas-Paul: Moss
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
# Namespace: com.sun.star.document
# Libre Office Version: 7.4
from typing_extensions import Literal
import typing
from ..uno.runtime_exception import RuntimeException as RuntimeException_d7390ced
from ..uno.x_interface import XInterface as XInterface_8f010a43

class CorruptedFilterConfigurationException(RuntimeException_d7390ced):
    """
    Exception Class

    This exception is thrown in case the global filter configuration does not exists or contains corrupted data.
    
    **since**
    
        OOo 2.0

    See Also:
        `API CorruptedFilterConfigurationException <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1document_1_1CorruptedFilterConfigurationException.html>`_
    """

    typeName: Literal['com.sun.star.document.CorruptedFilterConfigurationException']

    def __init__(self, Message: typing.Optional[str] = ..., Context: typing.Optional[XInterface_8f010a43] = ..., Details: typing.Optional[str] = ...) -> None:
        """
        Constructor

        Arguments:
            Message (str, optional): Message value.
            Context (XInterface, optional): Context value.
            Details (str, optional): Details value.
        """
        ...
    @property
    def Details(self) -> str:
        """
        Instead of the message part of an exception, this value describe the type of corruption more in detail.
        """
        ...
    @Details.setter
    def Details(self, value: str) -> None:
        ...

__all__ = ['CorruptedFilterConfigurationException']
