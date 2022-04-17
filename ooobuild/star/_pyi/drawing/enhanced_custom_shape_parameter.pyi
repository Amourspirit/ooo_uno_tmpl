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
# Namespace: com.sun.star.drawing
# Libre Office Version: 7.3
from typing_extensions import Literal
import typing


class EnhancedCustomShapeParameter(object):
    """
    Struct Class

    specifies a single value which is used with EnhancedCustomShapes

    See Also:
        `API EnhancedCustomShapeParameter <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1drawing_1_1EnhancedCustomShapeParameter.html>`_
    """
    typeName: Literal['com.sun.star.drawing.EnhancedCustomShapeParameter']

    def __init__(self, Value: typing.Optional[object] = ..., Type: typing.Optional[int] = ...) -> None:
        """
        Constructor

        Arguments:
            Value (object, optional): Value value.
            Type (int, optional): Type value.
        """


    @property
    def Value(self) -> object:
        """
        the any can be of type long or double
        """


    @property
    def Type(self) -> int:
        ...


