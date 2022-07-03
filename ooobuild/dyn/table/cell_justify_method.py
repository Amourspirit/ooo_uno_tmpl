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
# Libre Office Version: 7.3
# Namespace: com.sun.star.table
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class CellJustifyMethod(metaclass=UnoConstMeta, type_name="com.sun.star.table.CellJustifyMethod", name_space="com.sun.star.table"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.table.CellJustifyMethod``"""
        pass

    class CellJustifyMethodEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.table.CellJustifyMethod", name_space="com.sun.star.table"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.table.CellJustifyMethod`` as Enum values"""
        pass

else:
    from ...lo.table.cell_justify_method import CellJustifyMethod as CellJustifyMethod

    class CellJustifyMethodEnum(IntEnum):
        """
        Enum of Const Class CellJustifyMethod

        Specifies how text inside a cell is justified.
        
        The justification methods closely follow the methods described under the text-justify property of the CSS Text Level 3 specification. The latest version of the aforementioned specification is found here http://www.w3.org/TR/css3-text/.
        """
        AUTO = CellJustifyMethod.AUTO
        """
        Automatic.
        """
        DISTRIBUTE = CellJustifyMethod.DISTRIBUTE
        """
        When applied in the direction of text flow, characters in each line are distributed at equal intervals so that the ends of each line are aligned with the start and end edges of the cell.
        
        When applied in the perpendicular direction of text flow, the lines are distributed at equal intervals so that the first and last lines are aligned with the start and end edges of the cell.
        """

__all__ = ['CellJustifyMethod', 'CellJustifyMethodEnum']
