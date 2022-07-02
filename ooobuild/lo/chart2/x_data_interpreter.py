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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.chart2
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73
    from .interpreted_data import InterpretedData as InterpretedData_ed4f0d4c
    from .x_data_series import XDataSeries as XDataSeries_b8150b89
    from .data.x_data_source import XDataSource as XDataSource_f6340d57

class XDataInterpreter(XInterface_8f010a43):
    """
    offers tooling to interpret different data sources in a structural and chart-type-dependent way.

    See Also:
        `API XDataInterpreter <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1chart2_1_1XDataInterpreter.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.chart2'
    __ooo_full_ns__: str = 'com.sun.star.chart2.XDataInterpreter'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.chart2.XDataInterpreter'

    @abstractmethod
    def getChartTypeSpecificData(self, sKey: str) -> object:
        """
        Get chart information that is specific to a particular chart type, by key.
        
        Supported key strings:
        """
        ...
    @abstractmethod
    def interpretDataSource(self, xSource: 'XDataSource_f6340d57', aArguments: 'typing.Tuple[PropertyValue_c9610c73, ...]', aSeriesToReUse: 'typing.Tuple[XDataSeries_b8150b89, ...]') -> 'InterpretedData_ed4f0d4c':
        """
        Interprets the given data.
        
        For standard parameters that may be used, see the service StandardDiagramCreationParameters.
        """
        ...
    @abstractmethod
    def isDataCompatible(self, aInterpretedData: 'InterpretedData_ed4f0d4c') -> bool:
        """
        parses the given data and states, if a reinterpretDataSeries() call can be done without data loss.
        """
        ...
    @abstractmethod
    def mergeInterpretedData(self, aInterpretedData: 'InterpretedData_ed4f0d4c') -> 'XDataSource_f6340d57':
        """
        Try to reverse the operation done in interpretDataSource().
        
        In case aInterpretedData is the result of interpretDataSource()( xSource ), the result of this method should be xSource.
        """
        ...
    @abstractmethod
    def reinterpretDataSeries(self, aInterpretedData: 'InterpretedData_ed4f0d4c') -> 'InterpretedData_ed4f0d4c':
        """
        Re-interprets the data given in aInterpretedData while keeping the number of data series and the categories.
        """
        ...

__all__ = ['XDataInterpreter']

