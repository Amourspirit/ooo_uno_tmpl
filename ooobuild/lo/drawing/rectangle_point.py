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


class RectanglePoint(Enum):
    """
    Enum Class


    See Also:
        `API RectanglePoint <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1drawing.html#a4689f50c3960db0e79b179ddfc7d8827>`_
    """
    __ooo_ns__: str = "com.sun.star.drawing"
    __ooo_full_ns__: str = "com.sun.star.drawing.RectanglePoint"
    __ooo_type_name__: str = "enum"

    @property
    def typeName(self) -> str:
        return "com.sun.star.drawing.RectanglePoint"

    LEFT_BOTTOM = "LEFT_BOTTOM"
    """
    specify to the point on the bottom of the left side from the rectangle.
    """
    LEFT_MIDDLE = "LEFT_MIDDLE"
    """
    specify to the point on the middle of the left side from the rectangle.
    """
    LEFT_TOP = "LEFT_TOP"
    """
    specify to the point on the left side from the top of the rectangle.
    """
    MIDDLE_BOTTOM = "MIDDLE_BOTTOM"
    """
    specify to the point on the middle of the bottom from the rectangle.
    """
    MIDDLE_MIDDLE = "MIDDLE_MIDDLE"
    """
    specify to the point on the center from the rectangle.
    """
    MIDDLE_TOP = "MIDDLE_TOP"
    """
    specify to the point on the middle of the top from the rectangle.
    """
    RIGHT_BOTTOM = "RIGHT_BOTTOM"
    """
    specify to the point on the bottom of the right side from the rectangle.
    """
    RIGHT_MIDDLE = "RIGHT_MIDDLE"
    """
    specify to the point on the middle of the right side from the rectangle.
    """
    RIGHT_TOP = "RIGHT_TOP"
    """
    specify to the point on the right side from the top of the rectangle.
    """

__all__ = ["RectanglePoint"]

