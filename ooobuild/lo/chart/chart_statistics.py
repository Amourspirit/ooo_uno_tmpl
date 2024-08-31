# coding: utf-8
#
# Copyright 2023-2024 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 2024.2
# Namespace: com.sun.star.chart
from __future__ import annotations
import typing
from abc import abstractproperty
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
if typing.TYPE_CHECKING:
    from com.sun.star.chart.ChartErrorCategory import ChartErrorCategoryProto  # type: ignore
    from com.sun.star.chart.ChartErrorIndicatorType import ChartErrorIndicatorTypeProto  # type: ignore
    from com.sun.star.chart.ChartRegressionCurveType import ChartRegressionCurveTypeProto  # type: ignore

class ChartStatistics(XPropertySet_bc180bfa):
    """
    Service Class

    offers statistical properties for the data in the chart.
    
    It is available for a single data row and for the whole diagram.

    See Also:
        `API ChartStatistics <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1chart_1_1ChartStatistics.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.chart'
    __ooo_full_ns__: str = 'com.sun.star.chart.ChartStatistics'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def ConstantErrorHigh(self) -> float:
        """
        specifies the upper limit of the error range of a data row.
        
        this setting is effective if the ChartStatistics.ErrorCategory is set to ChartErrorCategory.CONSTANT_VALUE.
        """
        ...

    @abstractproperty
    def ConstantErrorLow(self) -> float:
        """
        specifies the lower limit of the error range of a data row.
        
        this setting is effective if the ChartStatistics.ErrorCategory is set to ChartErrorCategory.CONSTANT_VALUE.
        """
        ...

    @abstractproperty
    def ErrorBarRangeNegative(self) -> str:
        """
        contains a cell range string for negative error bars.
        
        This property is used when the ErrorBarCategory is set to ErrorBarCategory.FROM_DATA.
        """
        ...

    @abstractproperty
    def ErrorBarRangePositive(self) -> str:
        """
        contains a cell range string for positive error bars.
        
        This property is used when the ErrorBarCategory is set to ErrorBarCategory.FROM_DATA.
        """
        ...

    @abstractproperty
    def ErrorBarStyle(self) -> int:
        """
        determines the style of the error bars.
        
        Use this instead of ErrorCategory
        """
        ...

    @abstractproperty
    def ErrorCategory(self) -> ChartErrorCategoryProto:
        """
        determines the type of error to indicate.
        """
        ...

    @abstractproperty
    def ErrorIndicator(self) -> ChartErrorIndicatorTypeProto:
        """
        determines how the error is indicated.
        
        You can enable indicators pointing up, down or both.
        """
        ...

    @abstractproperty
    def ErrorMargin(self) -> float:
        """
        specifies the percentage for the margin of errors.
        
        The length of the error indicators is calculated by taking the percentage given of the largest data point value.
        
        this setting is effective if the ChartStatistics.ErrorCategory is set to ChartErrorCategory.ERROR_MARGIN.
        """
        ...

    @abstractproperty
    def MeanValue(self) -> bool:
        """
        determines if the mean value for a data row is displayed as a line.
        """
        ...

    @abstractproperty
    def PercentageError(self) -> float:
        """
        specifies the percentage that is used to display error bars.
        
        The length of the error indicators is calculated for each data point by taking the given percentage of its value.
        
        this setting is effective if the ChartStatistics.ErrorCategory is set to ChartErrorCategory.PERCENT.
        """
        ...

    @abstractproperty
    def RegressionCurves(self) -> ChartRegressionCurveTypeProto:
        """
        determines a type of regression for the data row values.
        """
        ...


__all__ = ['ChartStatistics']