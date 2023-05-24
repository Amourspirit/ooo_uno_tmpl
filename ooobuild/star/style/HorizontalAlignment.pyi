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

class HorizontalAlignmentProto(UnoEnumProto):
    CENTER: UnoEnumProto
    LEFT: UnoEnumProto
    RIGHT: UnoEnumProto

CENTER: HorizontalAlignmentProto
"""
set the horizontal alignment to the center between the margins from the container object

The text range is centered between the previous tabulator (or the left border, if none) and this tabulator.

adjusted to the center
"""
LEFT: HorizontalAlignmentProto
"""
set the horizontal alignment to the left margin from the container object

The text range is left-aligned between the previous tabulator (or the left border, if none) and this tabulator.

adjusted to the left border

The page style is only used for left pages.
"""
RIGHT: HorizontalAlignmentProto
"""
set the horizontal alignment to the right margin from the container object

The text range is right-aligned between the previous tabulator (or the left border, if none) and this tabulator.

adjusted to the right border

The page style is only used for right pages.
"""

