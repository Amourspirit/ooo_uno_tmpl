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
# Namespace: com.sun.star.chart
from abc import abstractproperty
from .chart_axis_x_supplier import ChartAxisXSupplier as ChartAxisXSupplier_a950e4d
from .x_two_axis_x_supplier import XTwoAxisXSupplier as XTwoAxisXSupplier_fcdb0ded

class ChartTwoAxisXSupplier(ChartAxisXSupplier_a950e4d, XTwoAxisXSupplier_fcdb0ded):
    """
    Service Class

    a helper service for chart documents which supply primary and secondary x-axes.
    
    **since**
    
        OOo 3.0

    See Also:
        `API ChartTwoAxisXSupplier <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1chart_1_1ChartTwoAxisXSupplier.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.chart'
    __ooo_full_ns__: str = 'com.sun.star.chart.ChartTwoAxisXSupplier'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def HasSecondaryXAxis(self) -> bool:
        """
        determines if the secondary x-axis is shown or hidden.
        """
        ...

    @abstractproperty
    def HasSecondaryXAxisDescription(self) -> bool:
        """
        determines for the secondary x-axis if the labels at the tick marks are shown or hidden.
        """
        ...

    @abstractproperty
    def HasSecondaryXAxisTitle(self) -> bool:
        """
        determines if the title of the secondary X-axis is shown or hidden.
        
        **since**
        
            OOo 3.0
        """
        ...


__all__ = ['ChartTwoAxisXSupplier']

