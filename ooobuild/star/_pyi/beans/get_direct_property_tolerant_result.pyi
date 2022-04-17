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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.beans
# Libre Office Version: 7.3
from typing_extensions import Literal
from .get_property_tolerant_result import GetPropertyTolerantResult as GetPropertyTolerantResult_7c4e115e
from .property_state import PropertyState as PropertyState_c97b0c77
import typing


class GetDirectPropertyTolerantResult(GetPropertyTolerantResult_7c4e115e):
    """
    Struct Class

    specifies information being retrieved about a single property.
    
    This type is used for the elements in the sequence returned by com.sun.star.beans.XTolerantMultiPropertySet.GetDirectPropertyTolerantResult.

    See Also:
        `API GetDirectPropertyTolerantResult <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1beans_1_1GetDirectPropertyTolerantResult.html>`_
    """
    typeName: Literal['com.sun.star.beans.GetDirectPropertyTolerantResult']

    def __init__(self, Result: typing.Optional[int] = ..., State: typing.Optional[PropertyState_c97b0c77] = ..., Value: typing.Optional[object] = ..., Name: typing.Optional[str] = ...) -> None:
        """
        Constructor

        Arguments:
            Result (int, optional): Result value.
            State (PropertyState, optional): State value.
            Value (object, optional): Value value.
            Name (str, optional): Name value.
        """


    @property
    def Name(self) -> str:
        """
        specifies the name of the property.
        """


