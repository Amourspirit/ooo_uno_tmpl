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
# Namespace: com.sun.star.rendering
# Libre Office Version: 7.4
from __future__ import annotations
from typing import cast, TYPE_CHECKING
from enum import Enum
if TYPE_CHECKING:
    from com.sun.star.rendering.FillRule import FillRuleProto

class FillRule(Enum):
    """
    Enum Class


    See Also:
        `API FillRule <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1rendering.html#a9a534b0377c9ca41983d53b0dae0d5a4>`_
    """
    __ooo_ns__: str = 'com.sun.star.rendering'
    __ooo_full_ns__: str = 'com.sun.star.rendering.FillRule'
    __ooo_type_name__: str = 'enum'

    @property
    def typeName(self) -> str:
        return 'com.sun.star.rendering.FillRule'

    EVEN_ODD = cast("FillRuleProto", 'EVEN_ODD')
    """
    Fill every area, where, when traveling along a line, an uneven number of intersections with polygon edges have happened.
    """
    NON_ZERO = cast("FillRuleProto", 'NON_ZERO')
    """
    Fill every area, where, when traveling along a line, the summed winding number (that is, -1 for a counter-clockwise-oriented polygon, and +1 for a clockwise-oriented) is non-zero.
    
    For example, a poly-polygon consisting of two concentric circles with similar orientation is filled the same way as if only the outer circle would exist. If both have opposite orientation, then the filled representation looks the same as if filled with the EVEN_ODD fill rule.
    """

__all__ = ['FillRule']

