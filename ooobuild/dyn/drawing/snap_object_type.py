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
# Namespace: com.sun.star.drawing
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
    class SnapObjectType(metaclass=UnoEnumMeta, type_name="com.sun.star.drawing.SnapObjectType", name_space="com.sun.star.drawing"):
        """Dynamically created class that represents ``com.sun.star.drawing.SnapObjectType`` Enum. Class loosely mimics Enum"""
        pass
else:
    if TYPE_CHECKING:
        from com.sun.star.drawing.SnapObjectType import HORIZONTAL as SNAP_OBJECT_TYPE_HORIZONTAL
        from com.sun.star.drawing.SnapObjectType import POINT as SNAP_OBJECT_TYPE_POINT
        from com.sun.star.drawing.SnapObjectType import VERTICAL as SNAP_OBJECT_TYPE_VERTICAL

        class SnapObjectType(uno.Enum):
            """
            Enum Class

            ENUM SnapObjectType

            See Also:
                `API SnapObjectType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1drawing.html#aac70ce37cdcc7a4bfcf79309db1a438b>`_
            """

            def __init__(self, value: Any) -> None:
                super().__init__('com.sun.star.drawing.SnapObjectType', value)

            __ooo_ns__: str = 'com.sun.star.drawing'
            __ooo_full_ns__: str = 'com.sun.star.drawing.SnapObjectType'
            __ooo_type_name__: str = 'enum'

            HORIZONTAL = SNAP_OBJECT_TYPE_HORIZONTAL
            """
            mirror to the horizontal axis
            """
            POINT = SNAP_OBJECT_TYPE_POINT
            """
            """
            VERTICAL = SNAP_OBJECT_TYPE_VERTICAL
            """
            mirror to the vertical axis
            """
    else:
        # keep document generators happy
        from ...lo.drawing.snap_object_type import SnapObjectType as SnapObjectType


__all__ = ['SnapObjectType']
