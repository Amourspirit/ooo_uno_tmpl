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
# Namespace: com.sun.star.sheet
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73
    from .x_sheet_filter_descriptor import XSheetFilterDescriptor as XSheetFilterDescriptor_47cc0ff7
    from .x_sub_total_descriptor import XSubTotalDescriptor as XSubTotalDescriptor_19fd0ec6
    from ..table.cell_range_address import CellRangeAddress as CellRangeAddress_ec450d43

class XDatabaseRange(XInterface_8f010a43):
    """
    provides access to the settings and options of a database range.

    See Also:
        `API XDatabaseRange <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sheet_1_1XDatabaseRange.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.sheet.XDatabaseRange']

    def getDataArea(self) -> 'CellRangeAddress_ec450d43':
        """
        returns the data area of the database range in the spreadsheet document.
        """
        ...
    def getFilterDescriptor(self) -> 'XSheetFilterDescriptor_47cc0ff7':
        """
        returns the filter descriptor stored with the database range.
        
        If the filter descriptor is modified, the new filtering is carried out when XDatabaseRange.refresh() is called.
        """
        ...
    def getImportDescriptor(self) -> 'typing.Tuple[PropertyValue_c9610c73, ...]':
        """
        returns the database import descriptor stored with this database range.
        """
        ...
    def getSortDescriptor(self) -> 'typing.Tuple[PropertyValue_c9610c73, ...]':
        """
        returns the sort descriptor stored with the database range.
        """
        ...
    def getSubTotalDescriptor(self) -> 'XSubTotalDescriptor_19fd0ec6':
        """
        returns the subtotal descriptor stored with the database range.
        
        If the subtotal descriptor is modified, the new subtotals are inserted when XDatabaseRange.refresh() is called.
        """
        ...
    def refresh(self) -> None:
        """
        executes the stored import, filter, sorting, and subtotals descriptors again.
        """
        ...
    def setDataArea(self, aDataArea: 'CellRangeAddress_ec450d43') -> None:
        """
        sets the data area of the database range.
        """
        ...


