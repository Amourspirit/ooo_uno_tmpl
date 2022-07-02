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
# Libre Office Version: 7.2
from typing_extensions import Literal
import typing
from .enhanced_custom_shape_parameter import EnhancedCustomShapeParameter as EnhancedCustomShapeParameter_d6171317


class EnhancedCustomShapeParameterPair(object):
    """
    Struct Class

    specifies the coordinates used with EnhancedCustomShapes

    See Also:
        `API EnhancedCustomShapeParameterPair <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1drawing_1_1EnhancedCustomShapeParameterPair.html>`_
    """
    typeName: Literal['com.sun.star.drawing.EnhancedCustomShapeParameterPair']

    def __init__(self, First: typing.Optional[EnhancedCustomShapeParameter_d6171317] = ..., Second: typing.Optional[EnhancedCustomShapeParameter_d6171317] = ...) -> None:
        """
        Constructor

        Arguments:
            First (EnhancedCustomShapeParameter, optional): First value.
            Second (EnhancedCustomShapeParameter, optional): Second value.
        """
        ...


    @property
    def First(self) -> EnhancedCustomShapeParameter_d6171317:
        ...


    @property
    def Second(self) -> EnhancedCustomShapeParameter_d6171317:
        ...


