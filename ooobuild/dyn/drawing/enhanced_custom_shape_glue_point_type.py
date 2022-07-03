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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.drawing
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import UnoConstMeta,ConstEnumMeta
    class EnhancedCustomShapeGluePointType(metaclass=UnoConstMeta, type_name="com.sun.star.drawing.EnhancedCustomShapeGluePointType", name_space="com.sun.star.drawing"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.drawing.EnhancedCustomShapeGluePointType``"""
        pass

    class EnhancedCustomShapeGluePointTypeEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.drawing.EnhancedCustomShapeGluePointType", name_space="com.sun.star.drawing"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.drawing.EnhancedCustomShapeGluePointType`` as Enum values"""
        pass

else:
    from ...lo.drawing.enhanced_custom_shape_glue_point_type import EnhancedCustomShapeGluePointType as EnhancedCustomShapeGluePointType

    class EnhancedCustomShapeGluePointTypeEnum(IntEnum):
        """
        Enum of Const Class EnhancedCustomShapeGluePointType

        defines which glue points are being offered by the EnhancedCustomShape
        """
        NONE = EnhancedCustomShapeGluePointType.NONE
        """
        no glue points are offered
        """
        SEGMENTS = EnhancedCustomShapeGluePointType.SEGMENTS
        """
        glue points are offered for each segment
        """
        CUSTOM = EnhancedCustomShapeGluePointType.CUSTOM
        """
        only glue points of the GluePoints property from the com.sun:star.drawing.EnhancedCustomShapePath are offered
        """
        RECT = EnhancedCustomShapeGluePointType.RECT
        """
        standard top, left, right, bottom glue points are offered
        """

__all__ = ['EnhancedCustomShapeGluePointType', 'EnhancedCustomShapeGluePointTypeEnum']
