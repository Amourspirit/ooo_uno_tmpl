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
from typing_extensions import Literal
import typing
from ...uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .label_origin import LabelOrigin as LabelOrigin_f66b0d5c

class XDataSequence(XInterface_8f010a43):
    """
    allows access to a one-dimensional sequence of data.
    
    The data that is stored in this container may contain different types.

    See Also:
        `API XDataSequence <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1chart2_1_1data_1_1XDataSequence.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.chart2.data.XDataSequence']

    def generateLabel(self, eLabelOrigin: 'LabelOrigin_f66b0d5c') -> 'typing.Tuple[str, ...]':
        """
        creates a label that describes the origin of this data sequence.
        
        This is useful, if a XLabeledDataSequence has no label sequence. In this case you can call this method at the value sequence to obtain a fitting replacement label.
        
        The sequence returned here may be empty if no suitable label can be generated.
        
        The strings returned should be localized.
        
        If you have a non quadratic range you can ask for labels for the longer side with parameter LONG_SIDE or you can obtain labels for the shorter side with parameter SHORT_SIDE.
        
        If the range is not structured in a tabular way you may receive no label.
        
        Example: Assuming this sequence has a Range representation spanning row 5 and 6 in column 8. Following sequences of strings or similar strings are expected as return values:
        
        generateLabel( SHORT_SIDE ) -> \"Column 8\" generateLabel( LONG_SIDE ) -> \"Row 5\" \"Row 6\" generateLabel( COLUMN ) -> \"Column 8\" generateLabel( ROW ) -> \"Row 5\" \"Row 6\"
        
        Which strings exactly you return depends on the naming scheme of the application which provides its tabular data.
        """
        ...
    def getData(self) -> 'typing.Tuple[object, ...]':
        """
        retrieves the data stored in this component.
        """
        ...
    def getNumberFormatKeyByIndex(self, nIndex: int) -> int:
        """
        returns a number format key for the value at the given index in the data sequence.
        
        If nIndex is -1, a key for the entire sequence should be returned, e.g. the most commonly used one.
        
        If number formats are not supported, or there is no heuristic to return a key for the entire series, return 0 here.
        
        The number format key must be valid for the com.sun.star.util.XNumberFormatsSupplier given by the XDataProvider, or 0 which is assumed to be always valid.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
        ...
    def getSourceRangeRepresentation(self) -> str:
        """
        returns the (UI) range representation string used by this XDataSequence.
        """
        ...


