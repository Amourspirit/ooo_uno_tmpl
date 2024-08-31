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
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.drawing
# Libre Office Version: 2024.2
from __future__ import annotations
from enum import Enum


class Arrangement(Enum):
    """
    Enum Class


    See Also:
        `API Arrangement <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1drawing.html#ac4d32be4f663e5f65aa208c47e1faa81>`_
    """
    __ooo_ns__: str = "com.sun.star.drawing"
    __ooo_full_ns__: str = "com.sun.star.drawing.Arrangement"
    __ooo_type_name__: str = "enum"

    @property
    def typeName(self) -> str:
        return "com.sun.star.drawing.Arrangement"

    BACK = "BACK"
    """
    Move this object behind all other objects.
    """
    FRONT = "FRONT"
    """
    Move this object in front of all other objects.
    """
    MORE_BACK = "MORE_BACK"
    """
    Move this object one object more to the back.
    """
    MORE_FRONT = "MORE_FRONT"
    """
    Move this object one object more to the front.
    """

__all__ = ["Arrangement"]

