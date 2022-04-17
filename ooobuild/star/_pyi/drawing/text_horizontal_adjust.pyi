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
"""
Enum



See Also:
    `API TextHorizontalAdjust <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1drawing.html#adc845a26c59f91e9ad752a717b3c2386>`_
"""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ooo.stubs.uno_enum import UnoEnum

ALLLINES: 'UnoEnum'
"""
Nowadays this is the same as PROPORTIONAL.
"""
AUTOFIT: 'UnoEnum'
"""
The font size is scaled down (never up!) isotropically to fit the available space.

Auto line-breaks will keep working.
"""
NONE: 'UnoEnum'
"""
the area is not filled.

The text size is only defined by the font properties.

Don't animate this text.

the line is hidden.

the joint between lines will not be connected

the line has no special end.
"""
PROPORTIONAL: 'UnoEnum'
"""
The bitmap with the rendered glyphs is scaled up or down proportionally to fit the size of the shape.

This may scale anisotropically. No AutoGrow and no Auto line-breaks in this case.

On fontwork custom shapes, the rendering is different: each line of text is separately scaled proportionally to fit the width.
"""

