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
from enum import Enum


class HorizontalDimensioning(Enum):
    """
    Enum Class


    See Also:
        `API HorizontalDimensioning <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1drawing.html#a6c20b7eb17d1eb1746fddc52487581f9>`_
    """
    __ooo_ns__: str = "com.sun.star.drawing"
    __ooo_full_ns__: str = "com.sun.star.drawing.HorizontalDimensioning"
    __ooo_type_name__: str = "enum"

    @property
    def typeName(self) -> str:
        return "com.sun.star.drawing.HorizontalDimensioning"

    AUTO = "AUTO"
    """
    the connection point is chosen automatically,
    
    Set this to have the application select the best horizontal position for the text.
    """
    CENTERED = "CENTERED"
    """
    The text is positioned at the center.
    
    The text is positioned over the main line.
    """
    LEFT = "LEFT"
    """
    the connection line leaves the connected object to the left,
    
    The left edge of the text is adjusted to the left edge of the shape.
    
    The text is positioned to the left.
    """
    RIGHT = "RIGHT"
    """
    the connection line leaves the connected object to the right,
    
    The right edge of the text is adjusted to the right edge of the shape.
    
    The text is positioned to the right.
    """

__all__ = ["HorizontalDimensioning"]

