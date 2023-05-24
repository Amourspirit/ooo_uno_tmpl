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
# Namespace: com.sun.star.sheet
from __future__ import annotations
import typing
from abc import abstractproperty
from ..chart.x_chart_data_array import XChartDataArray as XChartDataArray_df4c0cdd
from ..container.x_enumeration_access import XEnumerationAccess as XEnumerationAccess_4bac0ffc
from ..container.x_name_container import XNameContainer as XNameContainer_cb90e47
from .sheet_ranges_query import SheetRangesQuery as SheetRangesQuery_efbe0d90
from .x_sheet_cell_range_container import XSheetCellRangeContainer as XSheetCellRangeContainer_661f1082
from .x_sheet_operation import XSheetOperation as XSheetOperation_e1f50d23
from ..style.character_properties import CharacterProperties as CharacterProperties_1d4f0ef3
from ..style.character_properties_asian import CharacterPropertiesAsian as CharacterPropertiesAsian_6d8a10df
from ..style.character_properties_complex import CharacterPropertiesComplex as CharacterPropertiesComplex_90ca11cb
from ..style.paragraph_properties import ParagraphProperties as ParagraphProperties_1e240efc
from ..table.cell_properties import CellProperties as CellProperties_d4360cbd
from ..util.x_indent import XIndent as XIndent_7b290980
from ..util.x_replaceable import XReplaceable as XReplaceable_b0750b6e
if typing.TYPE_CHECKING:
    from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
    from .x_sheet_conditional_entries import XSheetConditionalEntries as XSheetConditionalEntries_694810c0

class SheetCellRanges(SheetRangesQuery_efbe0d90, CharacterProperties_1d4f0ef3, CharacterPropertiesAsian_6d8a10df, CharacterPropertiesComplex_90ca11cb, ParagraphProperties_1e240efc, CellProperties_d4360cbd, XChartDataArray_df4c0cdd, XEnumerationAccess_4bac0ffc, XNameContainer_cb90e47, XSheetCellRangeContainer_661f1082, XSheetOperation_e1f50d23, XIndent_7b290980, XReplaceable_b0750b6e):
    """
    Service Class

    represents a collection of cell ranges in a spreadsheet document.

    See Also:
        `API SheetCellRanges <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sheet_1_1SheetCellRanges.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.SheetCellRanges'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def AbsoluteName(self) -> str:
        """
        Returns the absolute address of the ranges as string, e.g.
        
        \"$Sheet1.$B$2:$D$5\".
        """
        ...

    @abstractproperty
    def ConditionalFormat(self) -> XSheetConditionalEntries_694810c0:
        """
        contains the conditional formatting settings for this cell.
        
        After a conditional format has been changed it has to be reinserted into the property set.
        """
        ...

    @abstractproperty
    def ConditionalFormatLocal(self) -> XSheetConditionalEntries_694810c0:
        """
        contains the conditional formatting settings for this cell, using localized formulas.
        
        After a conditional format has been changed it has to be reinserted into the property set.
        """
        ...

    @abstractproperty
    def Validation(self) -> XPropertySet_bc180bfa:
        """
        contains the data validation settings for this cell.
        
        After the data validation settings have been changed the validation has to be reinserted into the property set.
        """
        ...

    @abstractproperty
    def ValidationLocal(self) -> XPropertySet_bc180bfa:
        """
        contains the data validation settings for this cell, using localized formulas.
        
        After the data validation settings have been changed the validation has to be reinserted into the property set.
        """
        ...


__all__ = ['SheetCellRanges']

