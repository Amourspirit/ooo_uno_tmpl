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
# Namespace: com.sun.star.text
import typing
from .x_text_columns import XTextColumns as XTextColumns_b17f0bab
if typing.TYPE_CHECKING:
    from ..style.vertical_alignment import VerticalAlignment as VerticalAlignment_8d0e12
    from ..util.color import Color as Color_68e908c5

class TextColumns(XTextColumns_b17f0bab):
    """
    Service Class

    provides access to columns in text (e.g., in TextFrames ).

    See Also:
        `API TextColumns <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1text_1_1TextColumns.html>`_
    """
    @property
    def AutomaticDistance(self) -> int:
        """
        contains the distance between the columns.
        
        It is valid if the property IsAutomatic is set. Half of this distance is set to the left and right margins of all columns, except for the left margin of the first column, and the right margin of the last column.
        """
    @property
    def IsAutomatic(self) -> bool:
        """
        determines whether the columns all have equal width.
        
        This flag is set if XTextColumns.setColumnCount() is called and it is reset if XTextColumns.setColumns() is called.
        """
    @property
    def SeparatorLineColor(self) -> 'Color_68e908c5':
        """
        determines the color of the separator lines between the columns.
        """
    @property
    def SeparatorLineIsOn(self) -> bool:
        """
        determines whether separator lines are on.
        """
    @property
    def SeparatorLineRelativeHeight(self) -> int:
        """
        determines the relative height of the separator lines between the columns.
        """
    @property
    def SeparatorLineStyle(self) -> int:
        """
        determines the style of the separator lines between the columns.
        """
    @property
    def SeparatorLineVerticalAlignment(self) -> 'VerticalAlignment_8d0e12':
        """
        determines the vertical alignment of the separator lines between the columns.
        """
    @property
    def SeparatorLineWidth(self) -> int:
        """
        determines the width of the separator lines between the columns.
        """


