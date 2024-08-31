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
# Namespace: com.sun.star.style
# Libre Office Version: 2024.2
from __future__ import annotations
from typing import Protocol, Any
from typing_extensions import Literal


class BreakTypeProto(Protocol):
    """Protocol for BreakType"""

    @property
    def typeName(self) -> Literal["com.sun.star.style.BreakType"]:
        ...
    value: Any
    COLUMN_AFTER: BreakTypeProto
    COLUMN_BEFORE: BreakTypeProto
    COLUMN_BOTH: BreakTypeProto
    NONE: BreakTypeProto
    PAGE_AFTER: BreakTypeProto
    PAGE_BEFORE: BreakTypeProto
    PAGE_BOTH: BreakTypeProto

COLUMN_AFTER: BreakTypeProto
"""
A column break is applied after the object to which it belongs.

This implies that the object to which it belongs is the last in its column.
"""
COLUMN_BEFORE: BreakTypeProto
"""
A column break is applied before the object to which it belongs.

This implies that the object to which it belongs is the first in its column.
"""
COLUMN_BOTH: BreakTypeProto
"""
A column break is applied before and after the object to which it belongs.

This implies that this object is the only one in its column.
"""
NONE: BreakTypeProto
"""
No column or page break is applied.

This value specifies that a location is not yet assigned.
"""
PAGE_AFTER: BreakTypeProto
"""
A page break is applied after the object to which it belongs.

This implies that the object to which it belongs is the last on its page.
"""
PAGE_BEFORE: BreakTypeProto
"""
A page break is applied before the object to which it belongs.

This implies that the object to which it belongs is the first on its page.
"""
PAGE_BOTH: BreakTypeProto
"""
A page break is applied before and after the object to which it belongs.

This implies that this object is the only one on its page.
"""

