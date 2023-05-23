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
from ..beans.property_set import PropertySet as PropertySet_b0e70ba2
from .x_regression_curve import XRegressionCurve as XRegressionCurve_fa3c0dca
from ..drawing.line_properties import LineProperties as LineProperties_f13f0da9

class RegressionCurve(PropertySet_b0e70ba2, LineProperties_f13f0da9, XRegressionCurve_fa3c0dca):
    """
    Service Class


    See Also:
        `API RegressionCurve <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1chart2_1_1RegressionCurve.html>`_
    """
    @property
    def MovingAverageType(self) -> int:
        """
        """
        ...
    @MovingAverageType.setter
    def MovingAverageType(self, value: int) -> None:
        ...
