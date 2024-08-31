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
# Namespace: com.sun.star.chart2
from __future__ import annotations
from .x_chart_document import XChartDocument as XChartDocument_dd6f0cd5
from .x_titled import XTitled as XTitled_8d490a0a
from .data.x_data_receiver import XDataReceiver as XDataReceiver_117d0e1b
from ..lang.x_initialization import XInitialization as XInitialization_d46c0cca
from ..style.x_style_families_supplier import XStyleFamiliesSupplier as XStyleFamiliesSupplier_4c5a1020
from ..util.x_number_formats_supplier import XNumberFormatsSupplier as XNumberFormatsSupplier_3afb0fb7

class ChartDocument(XChartDocument_dd6f0cd5, XTitled_8d490a0a, XDataReceiver_117d0e1b, XInitialization_d46c0cca, XStyleFamiliesSupplier_4c5a1020, XNumberFormatsSupplier_3afb0fb7):
    """
    Service Class


    See Also:
        `API ChartDocument <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1chart2_1_1ChartDocument.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.chart2'
    __ooo_full_ns__: str = 'com.sun.star.chart2.ChartDocument'
    __ooo_type_name__: str = 'service'


__all__ = ['ChartDocument']

