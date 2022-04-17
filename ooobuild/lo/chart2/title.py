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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.chart2
import typing
from abc import abstractproperty
from ..beans.property_set import PropertySet as PropertySet_b0e70ba2
from .x_title import XTitle as XTitle_833f09a6
from ..drawing.fill_properties import FillProperties as FillProperties_f1200da8
from ..drawing.line_properties import LineProperties as LineProperties_f13f0da9
from ..style.paragraph_properties import ParagraphProperties as ParagraphProperties_1e240efc
if typing.TYPE_CHECKING:
    from ..awt.size import Size as Size_576707ef
    from .relative_position import RelativePosition as RelativePosition_fae10ddd

class Title(PropertySet_b0e70ba2, FillProperties_f1200da8, LineProperties_f13f0da9, ParagraphProperties_1e240efc, XTitle_833f09a6):
    """
    Service Class


    See Also:
        `API Title <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1chart2_1_1Title.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.chart2'
    __ooo_full_ns__: str = 'com.sun.star.chart2.Title'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def ReferencePageSize(self) -> 'Size_576707ef':
        """
        contains the size of the page at the time when properties were set (e.g.
        
        the CharHeight).
        
        This way it is possible to resize objects (like text) in the view without modifying the model.
        """

    @abstractproperty
    def RelativePosition(self) -> 'RelativePosition_fae10ddd':
        """
        The position is a relative position on the page.
        
        If a relative position is given the title is not automatically placed, but instead is placed relative on the page.
        """

    @abstractproperty
    def StackCharacters(self) -> bool:
        """
        writes the characters of the title on top of each other if set to TRUE.
        """

    @abstractproperty
    def TextRotation(self) -> float:
        """
        the rotation of the title's text in degrees in the range [0,360).
        """



__all__ = ['Title']
