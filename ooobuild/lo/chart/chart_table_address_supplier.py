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
# Libre Office Version: 7.2
# Namespace: com.sun.star.chart
import typing
from abc import abstractproperty, ABC
if typing.TYPE_CHECKING:
    from .chart_series_address import ChartSeriesAddress as ChartSeriesAddress_a480e3d

class ChartTableAddressSupplier(ABC):
    """
    Service Class

    This is a helper service for access to table Address to cell ranges of the container document of a chart.
    
    The cell addresses are in the format of the application that contains this chart.

    See Also:
        `API ChartTableAddressSupplier <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1chart_1_1ChartTableAddressSupplier.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.chart'
    __ooo_full_ns__: str = 'com.sun.star.chart.ChartTableAddressSupplier'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def SeriesAddresses(self) -> 'typing.Tuple[ChartSeriesAddress_a480e3d, ...]':
        """
        contains the addresses to the elements of a series.
        
        This sequence should contain one element for each series in the chart.
        """

    @abstractproperty
    def CategoriesRangeAddress(self) -> str:
        """
        contains the address to the cells containing the names of the categories.
        
        Note: Each value of a data series belongs exactly to one category.
        """

    @abstractproperty
    def MainTitleAddress(self) -> str:
        """
        contains the address to the main title.
        """

    @abstractproperty
    def SubTitleAddress(self) -> str:
        """
        contains the address to the sub title.
        """



__all__ = ['ChartTableAddressSupplier']

