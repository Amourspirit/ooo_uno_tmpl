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


class TextureProjectionModeProto(Protocol):
    """Protocol for TextureProjectionMode"""

    @property
    def typeName(self) -> Literal["com.sun.star.drawing.TextureProjectionMode"]:
        ...
    value: Any
    OBJECTSPECIFIC: TextureProjectionModeProto
    PARALLEL: TextureProjectionModeProto
    SPHERE: TextureProjectionModeProto

OBJECTSPECIFIC: TextureProjectionModeProto
"""
This value specifies that the standard object projection method is used.
"""
PARALLEL: TextureProjectionModeProto
"""
the 3D objects are drawn in the parallel projection.

This value specifies a flat parallel projection in the specified degree of freedom (X or Y).
"""
SPHERE: TextureProjectionModeProto
"""
forces normals to think that the object is a sphere.

This value forces projection to wrapping in X and/or Y.
"""

