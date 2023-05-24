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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.chart2
from __future__ import annotations
import typing
from ..beans.property_set import PropertySet as PropertySet_b0e70ba2
from ..drawing.fill_properties import FillProperties as FillProperties_f1200da8
from ..drawing.line_properties import LineProperties as LineProperties_f13f0da9
from ..style.character_properties import CharacterProperties as CharacterProperties_1d4f0ef3
if typing.TYPE_CHECKING:
    from ..awt.size import Size as Size_576707ef
    from .relative_position import RelativePosition as RelativePosition_fae10ddd

class RegressionCurveEquation(PropertySet_b0e70ba2, FillProperties_f1200da8, LineProperties_f13f0da9, CharacterProperties_1d4f0ef3):
    """
    Service Class


    See Also:
        `API RegressionCurveEquation <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1chart2_1_1RegressionCurveEquation.html>`_
    """
    @property
    def NumberFormat(self) -> int:
        """
        """
        ...
    @NumberFormat.setter
    def NumberFormat(self, value: int) -> None:
        ...
    @property
    def ReferencePageSize(self) -> Size_576707ef:
        """
        """
        ...
    @ReferencePageSize.setter
    def ReferencePageSize(self, value: Size_576707ef) -> None:
        ...
    @property
    def RelativePosition(self) -> RelativePosition_fae10ddd:
        """
        """
        ...
    @RelativePosition.setter
    def RelativePosition(self, value: RelativePosition_fae10ddd) -> None:
        ...
    @property
    def ShowCorrelationCoefficient(self) -> bool:
        """
        """
        ...
    @ShowCorrelationCoefficient.setter
    def ShowCorrelationCoefficient(self, value: bool) -> None:
        ...
    @property
    def ShowEquation(self) -> bool:
        """
        """
        ...
    @ShowEquation.setter
    def ShowEquation(self, value: bool) -> None:
        ...
    @property
    def XName(self) -> str:
        """
        """
        ...
    @XName.setter
    def XName(self, value: str) -> None:
        ...
    @property
    def YName(self) -> str:
        """
        """
        ...
    @YName.setter
    def YName(self, value: str) -> None:
        ...

