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
# Enum
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.drawing
# Libre Office Version: 7.3
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    import uno
from enum import Enum

class TextVerticalAdjust(Enum):
    """
    Enum

    

    See Also:
        `API TextVerticalAdjust <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1drawing.html#a4c2c10f0a1a5fa20d9f200d0fb5707ad>`_
    """

    BLOCK: 'uno.Enum'
    """
    The text extends from the left to the right edge of the shape.
    
    The text extends from the top to the bottom edge of the shape.
    """
    BOTTOM: 'uno.Enum'
    """
    the connection line leaves the connected object from the bottom,
    
    The text is positioned below the main line.
    
    The bottom edge of the text is adjusted to the bottom edge of the shape.
    """
    CENTER: 'uno.Enum'
    """
    The text is centered inside the shape.
    """
    TOP: 'uno.Enum'
    """
    the connection line leaves the connected object from the top,
    
    The text is positioned above the main line.
    
    The top edge of the text is adjusted to the top edge of the shape.
    """
