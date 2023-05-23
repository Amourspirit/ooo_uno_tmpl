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
# Enum
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.style
# Libre Office Version: 7.4
from __future__ import annotations
from com.sun.star import UnoEnumProto

class BreakTypeProto(UnoEnumProto):
    COLUMN_AFTER: UnoEnumProto
    COLUMN_BEFORE: UnoEnumProto
    COLUMN_BOTH: UnoEnumProto
    NONE: UnoEnumProto
    PAGE_AFTER: UnoEnumProto
    PAGE_BEFORE: UnoEnumProto
    PAGE_BOTH: UnoEnumProto

COLUMN_AFTER: BreakTypeProto
"""
A column break is applied after the object to which it belongs.
"""
COLUMN_BEFORE: BreakTypeProto
"""
A column break is applied before the object to which it belongs.
"""
COLUMN_BOTH: BreakTypeProto
"""
A column break is applied before and after the object to which it belongs.
"""
NONE: BreakTypeProto
"""
No column or page break is applied.

This value specifies that a location is not yet assigned.
"""
PAGE_AFTER: BreakTypeProto
"""
A page break is applied after the object to which it belongs.
"""
PAGE_BEFORE: BreakTypeProto
"""
A page break is applied before the object to which it belongs.
"""
PAGE_BOTH: BreakTypeProto
"""
A page break is applied before and after the object to which it belongs.
"""
