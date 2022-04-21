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
from abc import abstractproperty
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
from .x_chart_document import XChartDocument as XChartDocument_d3630ca3
from ..drawing.x_draw_page_supplier import XDrawPageSupplier as XDrawPageSupplier_1a030eab
from ..xml.user_defined_attributes_supplier import UserDefinedAttributesSupplier as UserDefinedAttributesSupplier_9fbe1222

class ChartDocument(UserDefinedAttributesSupplier_9fbe1222, XPropertySet_bc180bfa, XChartDocument_d3630ca3, XDrawPageSupplier_1a030eab):
    """
    Service Class

    is the service for a chart document.
    
    A chart document consists of a reference to the data source, the diagram and some additional elements like a main title, a sub-title or a legend.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API ChartDocument <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1chart_1_1ChartDocument.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.chart'
    __ooo_full_ns__: str = 'com.sun.star.chart.ChartDocument'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def HasLegend(self) -> bool:
        """
        determines if the legend is shown or hidden.
        """

    @abstractproperty
    def HasMainTitle(self) -> bool:
        """
        determines if the main title is shown or hidden.
        """

    @abstractproperty
    def HasSubTitle(self) -> bool:
        """
        determines if the subtitle is shown or hidden.
        """



__all__ = ['ChartDocument']

