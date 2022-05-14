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
# Libre Office Version: 7.2
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    import uno
from enum import Enum

class MeasureKind(Enum):
    """
    Enum

    

    See Also:
        `API MeasureKind <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1drawing.html#aba601430b0385cb6c2e7db8f7814cbff>`_
    """

    RADIUS: 'uno.Enum'
    """
    use the radius measurement.
    
    This option cannot be used from the GUI Interface.
    """
    STANDARD: 'uno.Enum'
    """
    the graphic is rendered in the default color style of the output device,
    
    use the length measurement.
    
    the connector is drawn with three lines, with the middle line perpendicular to the other two
    """

