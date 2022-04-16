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
# Libre Office Version: 7.3
from typing_extensions import Literal
from enum import Enum


class FillStyle(Enum):
    """
    Enum Class

    

    See Also:
        `API FillStyle <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1drawing.html#a93450c852ea0dc97ffc5168069ed1bc0>`_
    """
    BITMAP: Literal['BITMAP']
    """
    use a bitmap to fill the area.
    """
    GRADIENT: Literal['GRADIENT']
    """
    use a gradient color to fill the area.
    """
    HATCH: Literal['HATCH']
    """
    use a hatch to fill the area.
    """
    NONE: Literal['NONE']
    """
    the area is not filled.
    
    The text size is only defined by the font properties.
    
    Don't animate this text.
    
    the line is hidden.
    
    the joint between lines will not be connected
    
    the line has no special end.
    """
    SOLID: Literal['SOLID']
    """
    use a solid color to fill the area.
    
    the line is solid.
    """

