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


class TextAnimationKind(Enum):
    """
    Enum Class

    

    See Also:
        `API TextAnimationKind <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1drawing.html#a86ab93c592ed65e3f2cd0eebaf5660a2>`_
    """
    __ooo_ns__: str = 'com.sun.star.drawing'
    __ooo_full_ns__: str = 'com.sun.star.drawing.TextAnimationKind'
    __ooo_type_name__: str = 'enum'

    @property
    def typeName(self) -> str:
        return 'com.sun.star.drawing.TextAnimationKind'

    ALTERNATE = 'ALTERNATE'
    """
    Scroll the text from one side to the other and back.
    """
    BLINK = 'BLINK'
    """
    Let this text switch its state from visible to invisible continuously.
    """
    NONE = 'NONE'
    """
    the area is not filled.
    
    The text size is only defined by the font properties.
    
    Don't animate this text.
    
    the line is hidden.
    
    the joint between lines will not be connected
    
    the line has no special end.
    """
    SCROLL = 'SCROLL'
    """
    Let this text scroll.
    """
    SLIDE = 'SLIDE'
    """
    Scroll the text from one side to the final position and stop there.
    """

__all__ = ['TextAnimationKind']

