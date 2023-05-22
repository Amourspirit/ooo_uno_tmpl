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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.graphic
import uno
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    # document generators will most likely not see this.
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class GraphicType(metaclass=UnoConstMeta, type_name="com.sun.star.graphic.GraphicType", name_space="com.sun.star.graphic"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.graphic.GraphicType``"""
        pass

    class GraphicTypeEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.graphic.GraphicType", name_space="com.sun.star.graphic"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.graphic.GraphicType`` as Enum values"""
        pass

else:
    if TYPE_CHECKING:
        from com.sun.star.graphic import GraphicType as GraphicType
    else:
        # keep document generators happy
        from ...lo.graphic.graphic_type import GraphicType as GraphicType

    class GraphicTypeEnum(IntEnum):
        """
        Enum of Const Class GraphicType

        Constants that describe the type of graphic.
        """
        EMPTY = GraphicType.EMPTY
        """
        Graphic is empty.
        """
        PIXEL = GraphicType.PIXEL
        """
        Graphic is represented through single pixels.
        """
        VECTOR = GraphicType.VECTOR
        """
        Graphic is represented through vectors.
        """

__all__ = ['GraphicType', 'GraphicTypeEnum']
