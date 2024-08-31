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
# Enum
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.table
# Libre Office Version: 2024.2
from __future__ import annotations
from typing import Protocol, Any
from typing_extensions import Literal


class CellVertJustifyProto(Protocol):
    """Protocol for CellVertJustify"""

    @property
    def typeName(self) -> Literal["com.sun.star.table.CellVertJustify"]:
        ...
    value: Any
    BOTTOM: CellVertJustifyProto
    CENTER: CellVertJustifyProto
    STANDARD: CellVertJustifyProto
    TOP: CellVertJustifyProto

BOTTOM: CellVertJustifyProto
"""
contents are aligned to the lower edge of the cell.
"""
CENTER: CellVertJustifyProto
"""
contents are horizontally centered.

contents are aligned to the vertical middle of the cell.
"""
STANDARD: CellVertJustifyProto
"""
default alignment is used (left for numbers, right for text).

default alignment is used.

contents are printed from left to right.
"""
TOP: CellVertJustifyProto
"""
contents are aligned with the upper edge of the cell.
"""

