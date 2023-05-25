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
# Namespace: com.sun.star.drawing
# Libre Office Version: 7.4
from __future__ import annotations
from typing import Protocol, Any
from typing_extensions import Literal


class ShadeModeProto(Protocol):
    """Protocol for ShadeMode"""

    @property
    def typeName(self) -> Literal["com.sun.star.drawing.ShadeMode"]:
        ...
    value: Any
    DRAFT: ShadeModeProto
    FLAT: ShadeModeProto
    PHONG: ShadeModeProto
    SMOOTH: ShadeModeProto

DRAFT: ShadeModeProto
"""
DRAFT is a special mode which uses a BSP tree and triangle subdivision for displaying.
"""
FLAT: ShadeModeProto
"""
forces one normal per flat part.

With FLAT shading, the faces of the object are rendered in a solid color.
"""
PHONG: ShadeModeProto
"""
With PHONG shading, the normal itself is interpolated to get more realistic colors and light reflections.
"""
SMOOTH: ShadeModeProto
"""
the point is smooth, the first derivation from the curve discussion view.

With SMOOTH shading, the colors of the lit vertices is interpolated.
"""

