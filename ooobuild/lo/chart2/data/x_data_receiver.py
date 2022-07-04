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
# Libre Office Version: 7.3
# Namespace: com.sun.star.chart2.data
import typing
from abc import abstractmethod
from ...uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ...awt.x_request_callback import XRequestCallback as XRequestCallback_d4ac0ca2
    from ...beans.property_value import PropertyValue as PropertyValue_c9610c73
    from .x_data_provider import XDataProvider as XDataProvider_122f0e31
    from .x_data_source import XDataSource as XDataSource_f6340d57
    from .x_range_highlighter import XRangeHighlighter as XRangeHighlighter_4e810fc8
    from ...util.x_number_formats_supplier import XNumberFormatsSupplier as XNumberFormatsSupplier_3afb0fb7

class XDataReceiver(XInterface_8f010a43):
    """
    
    **since**
    
        LibreOffice 5.4

    See Also:
        `API XDataReceiver <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1chart2_1_1data_1_1XDataReceiver.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.chart2.data'
    __ooo_full_ns__: str = 'com.sun.star.chart2.data.XDataReceiver'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.chart2.data.XDataReceiver'

    @abstractmethod
    def attachDataProvider(self, xProvider: 'XDataProvider_122f0e31') -> None:
        """
        attaches a component that provides data for the document.
        
        The previously set data provider will be released.
        """
        ...
    @abstractmethod
    def attachNumberFormatsSupplier(self, xSupplier: 'XNumberFormatsSupplier_3afb0fb7') -> None:
        """
        attaches an XNumberFormatsSupplier to this XDataReceiver.
        
        The given number formats will be used for display purposes.
        """
        ...
    @abstractmethod
    def getPopupRequest(self) -> 'XRequestCallback_d4ac0ca2':
        """
        A callback object to execute a foreign popup menu window.
        
        **since**
        
            LibreOffice 5.4
        """
        ...
    @abstractmethod
    def getRangeHighlighter(self) -> 'XRangeHighlighter_4e810fc8':
        """
        Returns a component at which a view representing the data of the attached data provider may listen for highlighting the data ranges used by the currently selected objects in the data receiver component.
        
        This is typically used by a spreadsheet to highlight the ranges used by the currently selected object in a chart.
        
        The range highlighter is optional, i.e., this method may return an empty object.
        """
        ...
    @abstractmethod
    def getUsedData(self) -> 'XDataSource_f6340d57':
        """
        Returns the data requested by the most recently attached data provider, that is still used.
        """
        ...
    @abstractmethod
    def getUsedRangeRepresentations(self) -> 'typing.Tuple[str, ...]':
        """
        returns a list of all range strings for which data has been requested by the most recently attached data provider, and which is still used.
        
        This list may be used by the data provider to swap charts out of memory, but still get informed by changes of ranges while the chart is not loaded.
        """
        ...
    @abstractmethod
    def setArguments(self, aArguments: 'typing.Tuple[PropertyValue_c9610c73, ...]') -> None:
        """

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...

__all__ = ['XDataReceiver']

