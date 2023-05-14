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
# Namespace: com.sun.star.chart2.data
from .x_data_provider import XDataProvider as XDataProvider_122f0e31
from .x_range_xml_conversion import XRangeXMLConversion as XRangeXMLConversion_6cef1070

class DataProvider(XDataProvider_122f0e31, XRangeXMLConversion_6cef1070):
    """
    Service Class


    See Also:
        `API DataProvider <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1chart2_1_1data_1_1DataProvider.html>`_
    """
    @property
    def IncludeHiddenCells(self) -> bool:
        """
        If set to false FALSE, values from hidden cells are not returned.
        """
        ...

    @IncludeHiddenCells.setter
    def IncludeHiddenCells(self, value: bool) -> None:
        ...

