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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.table
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

    class CellVertJustify2(metaclass=UnoConstMeta, type_name="com.sun.star.table.CellVertJustify2", name_space="com.sun.star.table"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.table.CellVertJustify2``"""
        pass

    class CellVertJustify2Enum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.table.CellVertJustify2", name_space="com.sun.star.table"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.table.CellVertJustify2`` as Enum values"""
        pass

else:
    if TYPE_CHECKING:
        from com.sun.star.table import CellVertJustify2 as CellVertJustify2
    else:
        # keep document generators happy
        from ...lo.table.cell_vert_justify2 import CellVertJustify2 as CellVertJustify2

    class CellVertJustify2Enum(IntEnum):
        """
        Enum of Const Class CellVertJustify2

        specifies how cell contents are aligned vertically.
        """
        STANDARD = CellVertJustify2.STANDARD
        """
        default alignment is used.
        """
        TOP = CellVertJustify2.TOP
        """
        contents are aligned with the upper edge of the cell.
        """
        CENTER = CellVertJustify2.CENTER
        """
        contents are aligned to the vertical middle of the cell.
        """
        BOTTOM = CellVertJustify2.BOTTOM
        """
        contents are aligned to the lower edge of the cell.
        """
        BLOCK = CellVertJustify2.BLOCK
        """
        contents are justified to the cell height.
        """

__all__ = ['CellVertJustify2', 'CellVertJustify2Enum']
