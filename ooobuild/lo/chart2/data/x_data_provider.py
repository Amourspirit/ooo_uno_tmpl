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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.chart2.data
import typing
from abc import abstractmethod
from ...uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ...beans.property_value import PropertyValue as PropertyValue_c9610c73
    from .x_data_sequence import XDataSequence as XDataSequence_11f00e1f
    from .x_data_source import XDataSource as XDataSource_f6340d57
    from ...sheet.x_range_selection import XRangeSelection as XRangeSelection_e1310d0c

class XDataProvider(XInterface_8f010a43):
    """
    An application that provides data for a chart must implement this interface.

    See Also:
        `API XDataProvider <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1chart2_1_1data_1_1XDataProvider.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.chart2.data'
    __ooo_full_ns__: str = 'com.sun.star.chart2.data.XDataProvider'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.chart2.data.XDataProvider'

    @abstractmethod
    def createDataSequenceByRangeRepresentation(self, aRangeRepresentation: str) -> 'XDataSequence_11f00e1f':
        """
        creates a single data sequence for the given data range.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    @abstractmethod
    def createDataSequenceByRangeRepresentationPossible(self, aRangeRepresentation: str) -> bool:
        """
        If TRUE is returned, a call to createDataSequenceByRangeRepresentation with the same argument must return a valid XDataSequence object.
        
        If FALSE is returned, createDataSequenceByRangeRepresentation throws an exception.
        """
        ...
    @abstractmethod
    def createDataSequenceByValueArray(self, aRole: str, aValueArray: str, aRoleQualifier: str) -> 'XDataSequence_11f00e1f':
        """
        Creates a single data sequence from the string value array representation.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    @abstractmethod
    def createDataSource(self, aArguments: 'typing.Tuple[PropertyValue_c9610c73, ...]') -> 'XDataSource_f6340d57':
        """
        Creates a data source object that matches the given range representation string.
        
        This can be used for creating the necessary data for a new chart out of a previously selected range of cells in a spreadsheet.
        
        For spreadsheets and text document tables there exists a service TabularDataProviderArguments describing valid values for this list.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    @abstractmethod
    def createDataSourcePossible(self, aArguments: 'typing.Tuple[PropertyValue_c9610c73, ...]') -> bool:
        """
        If TRUE is returned, a call to createDataSource with the same arguments must return a valid XDataSequence object.
        
        If FALSE is returned, createDataSource throws an exception.
        """
        ...
    @abstractmethod
    def detectArguments(self, xDataSource: 'XDataSource_f6340d57') -> 'typing.Tuple[PropertyValue_c9610c73, ...]':
        """
        Tries to find out with what parameters the passed DataSource most probably was created.
        
        if xDataSource is a data source that was created with createDataSource(), the arguments returned here should be the same than the ones passed to the function. Of course, this cannot be guaranteed. However, if detection is ambiguous, the returned arguments should be empty.
        
        This method may merge representation strings together if adjacent ranges appear successively in the range identifiers. E.g., if the first range refers to \"$Sheet1.$A$1:$A$8\" and the second range refers to \"$Sheet1.$B$1:$B$8\", those should be merged together to \"$Sheet1.$A$1:$B$8\".
        """
        ...
    @abstractmethod
    def getRangeSelection(self) -> 'XRangeSelection_e1310d0c':
        """
        Returns a component that is able to change a given range representation to another one.
        
        This usually is a controller-component that uses the GUI to allow a user to select a new range.
        
        This method may return nothing, if it does not support range selection or if there is no current controller available that offers the functionality.
        """
        ...

__all__ = ['XDataProvider']

