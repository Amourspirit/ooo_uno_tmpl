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
# Const
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.chart
import typing
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal
"""
Const

specifies the style of error indicators.

See Also:
    `API ErrorBarStyle <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1chart_1_1ErrorBarStyle.html>`_
"""
NONE: Literal[0]
"""
error indicators are not displayed.
"""
VARIANCE: Literal[1]
"""
displays error indicators for the variance of the data.
"""
STANDARD_DEVIATION: Literal[2]
"""
displays error indicators for the standard deviation (square root of variance) of the data.
"""
ABSOLUTE: Literal[3]
"""
the error indicators for all data points have the same absolute value as length for either direction.

The values for these are given as absolute numbers in ChartStatistics.ConstantErrorLow and ChartStatistics.ConstantErrorHigh
"""
RELATIVE: Literal[4]
"""
The length of the error indicators is calculated for each data point by taking the percentage given as ChartStatistics.PercentageError of its value.
"""
ERROR_MARGIN: Literal[5]
"""
The length of the error indicators for all data points is calculated by taking the percentage given as ChartStatistics.ErrorMargin of the largest data point value.
"""
STANDARD_ERROR: Literal[6]
"""
displays error indicators for the standard error, also known as the standard deviation of the mean (SDOM).
"""
FROM_DATA: Literal[7]
"""
Uses values given by cell ranges of the container document.

The values for the cell ranges are given in the properties ChartStatistics.ErrorBarRangePositive for positive indicators and ChartStatistics.ErrorBarRangeNegative for negative indicators.
"""

