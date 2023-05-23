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
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.sheet
# Libre Office Version: 7.4
from __future__ import annotations
import uno
from typing import Any, TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    # document generators will most likely not see this.
    from ooo.helper.enum_helper import UnoEnumMeta
    class CellDeleteMode(metaclass=UnoEnumMeta, type_name="com.sun.star.sheet.CellDeleteMode", name_space="com.sun.star.sheet"):
        """Dynamically created class that represents ``com.sun.star.sheet.CellDeleteMode`` Enum. Class loosely mimics Enum"""
        pass
else:
    if TYPE_CHECKING:
        from com.sun.star.sheet.CellDeleteMode import COLUMNS as CELL_DELETE_MODE_COLUMNS
        from com.sun.star.sheet.CellDeleteMode import LEFT as CELL_DELETE_MODE_LEFT
        from com.sun.star.sheet.CellDeleteMode import NONE as CELL_DELETE_MODE_NONE
        from com.sun.star.sheet.CellDeleteMode import ROWS as CELL_DELETE_MODE_ROWS
        from com.sun.star.sheet.CellDeleteMode import UP as CELL_DELETE_MODE_UP

        class CellDeleteMode(uno.Enum):
            """
            Enum Class


            See Also:
                `API CellDeleteMode <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1sheet.html#af2bbbff47b7abe36f258e59b1351e422>`_
            """

            def __init__(self, value: Any) -> None:
                super().__init__('com.sun.star.sheet.CellDeleteMode', value)

            __ooo_ns__: str = 'com.sun.star.sheet'
            __ooo_full_ns__: str = 'com.sun.star.sheet.CellDeleteMode'
            __ooo_type_name__: str = 'enum'

            COLUMNS = CELL_DELETE_MODE_COLUMNS
            """
            entire columns to the right of the deleted cells are moved left.

            entire columns to the right of the inserted cells are moved right.
            """
            LEFT = CELL_DELETE_MODE_LEFT
            """
            selects the left border.

            the cells to the right of the deleted cells are moved left.
            """
            NONE = CELL_DELETE_MODE_NONE
            """
            no cells are moved.

            sheet is not linked.

            new values are used without changes.

            nothing is calculated.

            nothing is imported.

            no condition is specified.
            """
            ROWS = CELL_DELETE_MODE_ROWS
            """
            entire rows below the deleted cells are moved up.

            entire rows below the inserted cells are moved down.
            """
            UP = CELL_DELETE_MODE_UP
            """
            the cells below the deleted cells are moved up.
            """
    else:
        # keep document generators happy
        from ...lo.sheet.cell_delete_mode import CellDeleteMode as CellDeleteMode


__all__ = ['CellDeleteMode']
