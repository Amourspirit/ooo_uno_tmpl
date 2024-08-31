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
# Namespace: com.sun.star.drawing
# Libre Office Version: 2024.2
from __future__ import annotations
from typing import Protocol, Any
from typing_extensions import Literal


class NormalsKindProto(Protocol):
    """Protocol for NormalsKind"""

    @property
    def typeName(self) -> Literal["com.sun.star.drawing.NormalsKind"]:
        ...
    value: Any
    FLAT: NormalsKindProto
    SPECIFIC: NormalsKindProto
    SPHERE: NormalsKindProto

FLAT: NormalsKindProto
"""
forces one normal per flat part.

With FLAT shading, the faces of the object are rendered in a solid color.
"""
SPECIFIC: NormalsKindProto
"""
does not produce standard normals, but leaves the object-specific ones untouched.
"""
SPHERE: NormalsKindProto
"""
forces normals to think that the object is a sphere.

This value forces projection to wrapping in X and/or Y.
"""

