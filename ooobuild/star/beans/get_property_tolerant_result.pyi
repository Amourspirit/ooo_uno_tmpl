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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.beans
# Libre Office Version: 2024.2
import typing
from .property_state import PropertyState as PropertyState_c97b0c77


class GetPropertyTolerantResult(object):
    """
    Struct Class

    specifies information being retrieved about a single property.

    See Also:
        `API GetPropertyTolerantResult <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1beans_1_1GetPropertyTolerantResult.html>`_
    """
    typeName: str = 'com.sun.star.beans.GetPropertyTolerantResult'

    def __init__(self, Result: typing.Optional[int] = ..., State: typing.Optional[PropertyState_c97b0c77] = ..., Value: typing.Optional[object] = ...) -> None:
        """
        Constructor

        Arguments:
            Result (int, optional): Result value.
            State (PropertyState, optional): State value.
            Value (object, optional): Value value.
        """
        ...

    @property
    def Result(self) -> int:
        """
        specifies a success or error code for the retrieval operation.
        """
        ...
    @Result.setter
    def Result(self, value: int) -> None:
        ...
    @property
    def State(self) -> PropertyState_c97b0c77:
        """
        contains the state of the property.
        
        The value is undefined if Result is not com.sun.star.beans.TolerantPropertySetResultType.SUCCESS.
        """
        ...
    @State.setter
    def State(self, value: PropertyState_c97b0c77) -> None:
        ...
    @property
    def Value(self) -> object:
        """
        contains the value of the property.
        
        The value is undefined if Result is not com.sun.star.beans.TolerantPropertySetResultType.SUCCESS.
        """
        ...
    @Value.setter
    def Value(self, value: object) -> None:
        ...

