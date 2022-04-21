# coding: utf-8
#
# Copyright 2022 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 7.2
from enum import Enum


class TextAdjust(Enum):
    """
    Enum Class

    

    See Also:
        `API TextAdjust <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1drawing.html#adf031187199b98bb1b6581c7e69d4810>`_
    """
    __ooo_ns__: str = 'com.sun.star.drawing'
    __ooo_full_ns__: str = 'com.sun.star.drawing.TextAdjust'
    __ooo_type_name__: str = 'enum'

    BLOCK = 'BLOCK'
    """
    The text extends from the left to the right edge of the shape.
    
    The text extends from the top to the bottom edge of the shape.
    """
    CENTER = 'CENTER'
    """
    The text is centered inside the shape.
    """
    LEFT = 'LEFT'
    """
    the connection line leaves the connected object to the left,
    
    The left edge of the text is adjusted to the left edge of the shape.
    
    The text is positioned to the left.
    """
    RIGHT = 'RIGHT'
    """
    the connection line leaves the connected object to the right,
    
    The right edge of the text is adjusted to the right edge of the shape.
    
    The text is positioned to the right.
    """
    STRETCH = 'STRETCH'
    """
    the bitmap is stretched to fill the area.
    
    The text is stretched so that the longest line goes from the left to the right edge of the shape.
    """

__all__ = ['TextAdjust']

