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
# Namespace: com.sun.star.ucb
# Libre Office Version: 7.4
from typing_extensions import Literal
import typing
from ..task.classified_interaction_request import ClassifiedInteractionRequest as ClassifiedInteractionRequest_9f72121b
from ..uno.x_interface import XInterface as XInterface_8f010a43
from ..task.interaction_classification import InteractionClassification as InteractionClassification_6c4d10e7

class AuthenticationFallbackRequest(ClassifiedInteractionRequest_9f72121b):
    """
    Exception Class

    An interaction continuation handing back some authentication data.
    
    **since**
    
        LibreOffice 4.4

    See Also:
        `API AuthenticationFallbackRequest <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1ucb_1_1AuthenticationFallbackRequest.html>`_
    """

    typeName: Literal['com.sun.star.ucb.AuthenticationFallbackRequest']

    def __init__(self, Message: typing.Optional[str] = ..., Context: typing.Optional[XInterface_8f010a43] = ..., Classification: typing.Optional[InteractionClassification_6c4d10e7] = ..., instructions: typing.Optional[str] = ..., url: typing.Optional[str] = ...) -> None:
        """
        Constructor

        Arguments:
            Message (str, optional): Message value.
            Context (XInterface, optional): Context value.
            Classification (InteractionClassification, optional): Classification value.
            instructions (str, optional): instructions value.
            url (str, optional): url value.
        """
        ...
    @property
    def instructions(self) -> str:
        """
        Instructions to be followed by the user.
        """
        ...
    @instructions.setter
    def instructions(self, value: str) -> None:
        ...
    @property
    def url(self) -> str:
        """
        url to be opened in browser
        """
        ...
    @url.setter
    def url(self, value: str) -> None:
        ...

__all__ = ['AuthenticationFallbackRequest']

