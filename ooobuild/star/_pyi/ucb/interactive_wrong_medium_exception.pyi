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
# Namespace: com.sun.star.ucb
# Libre Office Version: 7.3
from typing_extensions import Literal
import typing
from ..task.classified_interaction_request import ClassifiedInteractionRequest as ClassifiedInteractionRequest_9f72121b
from ..uno.x_interface import XInterface as XInterface_8f010a43
from ..task.interaction_classification import InteractionClassification as InteractionClassification_6c4d10e7

class InteractiveWrongMediumException(ClassifiedInteractionRequest_9f72121b):
    """
    Exception Class

    is thrown when the wrong medium is inserted into a removable drive during an operation.

    See Also:
        `API InteractiveWrongMediumException <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1ucb_1_1InteractiveWrongMediumException.html>`_
    """

    typeName: Literal['com.sun.star.ucb.InteractiveWrongMediumException']

    def __init__(self, Message: typing.Optional[str] = ..., Context: typing.Optional[XInterface_8f010a43] = ..., Classification: typing.Optional[InteractionClassification_6c4d10e7] = ..., Medium: typing.Optional[object] = ...) -> None:
        """
        Constructor

        Arguments:
            Message (str, optional): Message value.
            Context (XInterface, optional): Context value.
            Classification (InteractionClassification, optional): Classification value.
            Medium (object, optional): Medium value.
        """
        ...
    @property
    def Medium(self) -> object:
        """
        identifies the medium that's needed to continue with the pending operation.
        """
        ...

    @Medium.setter
    def Medium(self, value: object) -> None:
        ...

__all__ = ['InteractiveWrongMediumException']

