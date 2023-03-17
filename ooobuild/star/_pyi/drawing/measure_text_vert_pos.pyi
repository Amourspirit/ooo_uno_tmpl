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
# Libre Office Version: 7.4
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    import uno
from enum import Enum

class MeasureTextVertPos(Enum):
    """
    Enum

    

    See Also:
        `API MeasureTextVertPos <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1drawing.html#afb97f6590316423181878e8f5f79f087>`_
    """
    typeName: str = 'com.sun.star.drawing.MeasureTextVertPos'

    AUTO: 'uno.Enum'
    """
    the connection point is chosen automatically,
    
    Set this to have the application select the best horizontal position for the text.
    """
    BREAKEDLINE: 'uno.Enum'
    """
    """
    CENTERED: 'uno.Enum'
    """
    The text is positioned at the center.
    
    The text is positioned over the main line.
    """
    EAST: 'uno.Enum'
    """
    """
    WEST: 'uno.Enum'
    """
    """

