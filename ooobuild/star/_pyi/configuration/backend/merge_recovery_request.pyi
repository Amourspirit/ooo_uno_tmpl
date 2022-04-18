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
# Namespace: com.sun.star.configuration.backend
# Libre Office Version: 7.3
from typing_extensions import Literal
import typing
from ...uno.exception import Exception as Exception_85530a09
from ...uno.x_interface import XInterface as XInterface_8f010a43

class MergeRecoveryRequest(Exception_85530a09):
    """
    Exception Class

    is passed to an InteractionHandler when merging fails due to invalid layer data or access problems.
    
    **since**
    
        OOo 2.0

    See Also:
        `API MergeRecoveryRequest <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1configuration_1_1backend_1_1MergeRecoveryRequest.html>`_
    """

    typeName: Literal['com.sun.star.configuration.backend.MergeRecoveryRequest']

    def __init__(self, Message: typing.Optional[str] = ..., Context: typing.Optional[XInterface_8f010a43] = ..., ErrorDetails: typing.Optional[object] = ..., ErrorLayerId: typing.Optional[str] = ..., IsRemovalRequest: typing.Optional[bool] = ...) -> None:
        """
        Constructor

        Arguments:
            Message (str, optional): Message value.
            Context (XInterface, optional): Context value.
            ErrorDetails (object, optional): ErrorDetails value.
            ErrorLayerId (str, optional): ErrorLayerId value.
            IsRemovalRequest (bool, optional): IsRemovalRequest value.
        """
    @property
    def ErrorDetails(self) -> object:
        """
        data that provides more detailed information about the reason and location of the error.
        
        Typically this member should contain an exception characterizing the error in detail.
        
        For example the following exceptions may be used:
        
        If no more detail information is available, this may be left VOID.
        """

    @property
    def ErrorLayerId(self) -> str:
        """
        Identifier of the layer object containing the invalid data.
        """

    @property
    def IsRemovalRequest(self) -> bool:
        """
        specifies whether the requester wants to remove or skip the invalid layer.
        
        If TRUE the requester wants to remove the underlying data of the layer.
        If FALSE the request is to skip the underlying data this time, but without removing it.
        """


__all__ = ['MergeRecoveryRequest']

