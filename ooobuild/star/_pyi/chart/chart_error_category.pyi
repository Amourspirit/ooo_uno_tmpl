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
# Namespace: com.sun.star.chart
# Libre Office Version: 7.3
"""
Enum



See Also:
    `API ChartErrorCategory <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1chart.html#a5dc5747cfef559a2185b3400717ee431>`_
"""

CONSTANT_VALUE: object
"""
displays the same lower and upper error indicators for all data points.

The values for these are given as absolute numbers in ChartStatistics.ConstantErrorLow and ChartStatistics.ConstantErrorHigh
"""
ERROR_MARGIN: object
"""
The length of the error indicators for all data points is calculated by taking the percentage given as ChartStatistics.ErrorMargin of the largest data point value.
"""
NONE: object
"""
error indicators are not displayed.

displays no regression curve.

no chart legend is displayed.

displays no error indicators.
"""
PERCENT: object
"""
The length of the error indicators is calculated for each data point by taking the percentage given as ChartStatistics.PercentageError of its value.
"""
STANDARD_DEVIATION: object
"""
displays error indicators for the standard deviation (square root of variance) of the data row.
"""
VARIANCE: object
"""
displays error indicators for the variance of the data row.
"""

