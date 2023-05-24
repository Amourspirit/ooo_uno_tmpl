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
# Namespace: com.sun.star.style
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
    class BreakType(metaclass=UnoEnumMeta, type_name="com.sun.star.style.BreakType", name_space="com.sun.star.style"):
        """Dynamically created class that represents ``com.sun.star.style.BreakType`` Enum. Class loosely mimics Enum"""
        pass
else:
    if TYPE_CHECKING:
        from com.sun.star.style.BreakType import COLUMN_AFTER as BREAK_TYPE_COLUMN_AFTER
        from com.sun.star.style.BreakType import COLUMN_BEFORE as BREAK_TYPE_COLUMN_BEFORE
        from com.sun.star.style.BreakType import COLUMN_BOTH as BREAK_TYPE_COLUMN_BOTH
        from com.sun.star.style.BreakType import NONE as BREAK_TYPE_NONE
        from com.sun.star.style.BreakType import PAGE_AFTER as BREAK_TYPE_PAGE_AFTER
        from com.sun.star.style.BreakType import PAGE_BEFORE as BREAK_TYPE_PAGE_BEFORE
        from com.sun.star.style.BreakType import PAGE_BOTH as BREAK_TYPE_PAGE_BOTH

        class BreakType(uno.Enum):
            """
            Enum Class


            See Also:
                `API BreakType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1style.html#a3ae28cb49c180ec160a0984600b2b925>`_
            """

            def __init__(self, value: Any) -> None:
                super().__init__('com.sun.star.style.BreakType', value)

            __ooo_ns__: str = 'com.sun.star.style'
            __ooo_full_ns__: str = 'com.sun.star.style.BreakType'
            __ooo_type_name__: str = 'enum'

            COLUMN_AFTER = BREAK_TYPE_COLUMN_AFTER
            """
            A column break is applied after the object to which it belongs.
            """
            COLUMN_BEFORE = BREAK_TYPE_COLUMN_BEFORE
            """
            A column break is applied before the object to which it belongs.
            """
            COLUMN_BOTH = BREAK_TYPE_COLUMN_BOTH
            """
            A column break is applied before and after the object to which it belongs.
            """
            NONE = BREAK_TYPE_NONE
            """
            No column or page break is applied.

            This value specifies that a location is not yet assigned.
            """
            PAGE_AFTER = BREAK_TYPE_PAGE_AFTER
            """
            A page break is applied after the object to which it belongs.
            """
            PAGE_BEFORE = BREAK_TYPE_PAGE_BEFORE
            """
            A page break is applied before the object to which it belongs.
            """
            PAGE_BOTH = BREAK_TYPE_PAGE_BOTH
            """
            A page break is applied before and after the object to which it belongs.
            """
    else:
        # keep document generators happy
        from ...lo.style.break_type import BreakType as BreakType


__all__ = ['BreakType']
