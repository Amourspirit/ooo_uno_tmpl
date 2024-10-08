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
# Namespace: com.sun.star.bridge
# Libre Office Version: 2024.2
from typing_extensions import Literal
import typing
from ..uno.exception import Exception as Exception_85530a09
from ..uno.x_interface import XInterface as XInterface_8f010a43
from .protocol_property import ProtocolProperty as ProtocolProperty_ff280e2c

class InvalidProtocolChangeException(Exception_85530a09):
    """
    Exception Class

    Indicates, that a requested property change could not be executed by the remote counterpart.

    See Also:
        `API InvalidProtocolChangeException <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1bridge_1_1InvalidProtocolChangeException.html>`_
    """

    typeName: Literal['com.sun.star.bridge.InvalidProtocolChangeException']

    def __init__(self, Message: typing.Optional[str] = ..., Context: typing.Optional[XInterface_8f010a43] = ..., invalidProperty: typing.Optional[ProtocolProperty_ff280e2c] = ..., reason: typing.Optional[int] = ...) -> None:
        """
        Constructor

        Arguments:
            Message (str, optional): Message value.
            Context (XInterface, optional): Context value.
            invalidProperty (ProtocolProperty, optional): invalidProperty value.
            reason (int, optional): reason value.
        """
        ...
    @property
    def invalidProperty(self) -> ProtocolProperty_ff280e2c:
        """
        The first invalid property.
        """
        ...
    @invalidProperty.setter
    def invalidProperty(self, value: ProtocolProperty_ff280e2c) -> None:
        ...
    @property
    def reason(self) -> int:
        """
        Contains 1, if the property name is unknown to the thrower; or contains 2, if the property's value can't be accepted by the thrower.
        """
        ...
    @reason.setter
    def reason(self, value: int) -> None:
        ...

__all__ = ['InvalidProtocolChangeException']

