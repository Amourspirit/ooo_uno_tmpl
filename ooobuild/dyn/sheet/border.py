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
    class Border(metaclass=UnoEnumMeta, type_name="com.sun.star.sheet.Border", name_space="com.sun.star.sheet"):
        """Dynamically created class that represents ``com.sun.star.sheet.Border`` Enum. Class loosely mimics Enum"""
        pass
else:
    if TYPE_CHECKING:
        from com.sun.star.sheet.Border import BOTTOM as BORDER_BOTTOM
        from com.sun.star.sheet.Border import LEFT as BORDER_LEFT
        from com.sun.star.sheet.Border import RIGHT as BORDER_RIGHT
        from com.sun.star.sheet.Border import TOP as BORDER_TOP

        class Border(uno.Enum):
            """
            Enum Class


            See Also:
                `API Border <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1sheet.html#aea307cd05a4c363d9cac3828a62f4127>`_
            """

            def __init__(self, value: Any) -> None:
                super().__init__('com.sun.star.sheet.Border', value)

            __ooo_ns__: str = 'com.sun.star.sheet'
            __ooo_full_ns__: str = 'com.sun.star.sheet.Border'
            __ooo_type_name__: str = 'enum'

            BOTTOM = BORDER_BOTTOM
            """
            selects the bottom border.
            """
            LEFT = BORDER_LEFT
            """
            selects the left border.

            the cells to the right of the deleted cells are moved left.
            """
            RIGHT = BORDER_RIGHT
            """
            selects the right border.

            the cells to the right of the inserted cells are moved right.
            """
            TOP = BORDER_TOP
            """
            selects the top border.
            """
    else:
        # keep document generators happy
        from ...lo.sheet.border import Border as Border


__all__ = ['Border']
