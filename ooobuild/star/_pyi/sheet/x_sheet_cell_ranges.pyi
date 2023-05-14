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
# Namespace: com.sun.star.sheet
from typing_extensions import Literal
import typing
from ..container.x_index_access import XIndexAccess as XIndexAccess_f0910d6d
if typing.TYPE_CHECKING:
    from ..container.x_enumeration_access import XEnumerationAccess as XEnumerationAccess_4bac0ffc
    from ..table.cell_range_address import CellRangeAddress as CellRangeAddress_ec450d43

class XSheetCellRanges(XIndexAccess_f0910d6d):
    """
    provides methods to access cell ranges in a collection via index and other helper methods.

    See Also:
        `API XSheetCellRanges <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sheet_1_1XSheetCellRanges.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.sheet.XSheetCellRanges']

    def getCells(self) -> 'XEnumerationAccess_4bac0ffc':
        """
        returns the collection of all used cells.
        """
        ...
    def getRangeAddresses(self) -> 'typing.Tuple[CellRangeAddress_ec450d43, ...]':
        """
        creates a sequence with addresses of all contained cell ranges.
        """
        ...
    def getRangeAddressesAsString(self) -> str:
        """
        creates a string with addresses of all contained cell ranges.
        
        The range addresses are separated with semicolons. For instance the string could have the form \"Sheet1.A1:C3;Sheet2.D5:F8\".
        """
        ...


