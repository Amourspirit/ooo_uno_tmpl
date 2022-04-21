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
# Namespace: com.sun.star.document
# Libre Office Version: 7.2
from typing_extensions import Literal
import typing
from ..uno.exception import Exception as Exception_85530a09
from ..uno.x_interface import XInterface as XInterface_8f010a43

class LockedOnSavingRequest(Exception_85530a09):
    """
    Exception Class

    Is used for interaction handle to query user decision regarding locked document on saving.
    
    **since**
    
        OOo 3.1

    See Also:
        `API LockedOnSavingRequest <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1document_1_1LockedOnSavingRequest.html>`_
    """

    typeName: Literal['com.sun.star.document.LockedOnSavingRequest']

    def __init__(self, Message: typing.Optional[str] = ..., Context: typing.Optional[XInterface_8f010a43] = ..., DocumentURL: typing.Optional[str] = ..., UserInfo: typing.Optional[str] = ...) -> None:
        """
        Constructor

        Arguments:
            Message (str, optional): Message value.
            Context (XInterface, optional): Context value.
            DocumentURL (str, optional): DocumentURL value.
            UserInfo (str, optional): UserInfo value.
        """
    @property
    def DocumentURL(self) -> str:
        """
        The URL of the locked document.
        """

    @property
    def UserInfo(self) -> str:
        """
        The user information of the locked document.
        """


__all__ = ['LockedOnSavingRequest']

