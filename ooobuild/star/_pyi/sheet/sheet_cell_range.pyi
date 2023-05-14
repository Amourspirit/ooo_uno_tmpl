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
import typing
from ..beans.x_tolerant_multi_property_set import XTolerantMultiPropertySet as XTolerantMultiPropertySet_7bd4114e
from ..chart.x_chart_data_array import XChartDataArray as XChartDataArray_df4c0cdd
from .sheet_ranges_query import SheetRangesQuery as SheetRangesQuery_efbe0d90
from .x_array_formula_range import XArrayFormulaRange as XArrayFormulaRange_b750e3b
from .x_cell_format_ranges_supplier import XCellFormatRangesSupplier as XCellFormatRangesSupplier_786d1116
from .x_cell_range_addressable import XCellRangeAddressable as XCellRangeAddressable_35260f40
from .x_cell_range_data import XCellRangeData as XCellRangeData_d2e70c60
from .x_cell_range_formula import XCellRangeFormula as XCellRangeFormula_fb270dbc
from .x_cell_series import XCellSeries as XCellSeries_af5c0b64
from .x_multiple_operation import XMultipleOperation as XMultipleOperation_d460e76
from .x_sheet_cell_range import XSheetCellRange as XSheetCellRange_e09d0cdf
from .x_sheet_filterable_ex import XSheetFilterableEx as XSheetFilterableEx_ad60e29
from .x_sheet_operation import XSheetOperation as XSheetOperation_e1f50d23
from .x_sub_total_calculatable import XSubTotalCalculatable as XSubTotalCalculatable_37b30f64
from .x_unique_cell_format_ranges_supplier import XUniqueCellFormatRangesSupplier as XUniqueCellFormatRangesSupplier_e8d5138d
from ..style.character_properties import CharacterProperties as CharacterProperties_1d4f0ef3
from ..style.character_properties_asian import CharacterPropertiesAsian as CharacterPropertiesAsian_6d8a10df
from ..style.character_properties_complex import CharacterPropertiesComplex as CharacterPropertiesComplex_90ca11cb
from ..style.paragraph_properties import ParagraphProperties as ParagraphProperties_1e240efc
from ..table.cell_range import CellRange as CellRange_98770a7d
from ..table.x_auto_formattable import XAutoFormattable as XAutoFormattable_ee660d72
from ..table.x_column_row_range import XColumnRowRange as XColumnRowRange_e0e70cfb
from ..util.x_importable import XImportable as XImportable_a5c50b2d
from ..util.x_indent import XIndent as XIndent_7b290980
from ..util.x_mergeable import XMergeable as XMergeable_99dd0aa2
from ..util.x_modify_broadcaster import XModifyBroadcaster as XModifyBroadcaster_fd990df0
from ..util.x_replaceable import XReplaceable as XReplaceable_b0750b6e
from ..util.x_sortable import XSortable as XSortable_8ff20a5a
if typing.TYPE_CHECKING:
    from ..awt.point import Point as Point_5fb2085e
    from ..awt.size import Size as Size_576707ef
    from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
    from .x_sheet_conditional_entries import XSheetConditionalEntries as XSheetConditionalEntries_694810c0

class SheetCellRange(SheetRangesQuery_efbe0d90, CharacterProperties_1d4f0ef3, CharacterPropertiesAsian_6d8a10df, CharacterPropertiesComplex_90ca11cb, ParagraphProperties_1e240efc, CellRange_98770a7d, XTolerantMultiPropertySet_7bd4114e, XChartDataArray_df4c0cdd, XArrayFormulaRange_b750e3b, XCellFormatRangesSupplier_786d1116, XCellRangeAddressable_35260f40, XCellRangeData_d2e70c60, XCellRangeFormula_fb270dbc, XCellSeries_af5c0b64, XMultipleOperation_d460e76, XSheetCellRange_e09d0cdf, XSheetFilterableEx_ad60e29, XSheetOperation_e1f50d23, XSubTotalCalculatable_37b30f64, XUniqueCellFormatRangesSupplier_e8d5138d, XAutoFormattable_ee660d72, XColumnRowRange_e0e70cfb, XImportable_a5c50b2d, XIndent_7b290980, XMergeable_99dd0aa2, XModifyBroadcaster_fd990df0, XReplaceable_b0750b6e, XSortable_8ff20a5a):
    """
    Service Class

    represents a rectangular range of cells in a spreadsheet document.
    
    This service is an extension of the CellRange service for use in spreadsheet documents.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API SheetCellRange <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sheet_1_1SheetCellRange.html>`_
    """
    @property
    def AbsoluteName(self) -> str:
        """
        Returns the absolute address of the range as string, e.g.
        
        \"$Sheet1.$B$2:$D$5\".
        """
        ...
    @AbsoluteName.setter
    def AbsoluteName(self, value: str) -> None:
        ...
    @property
    def ConditionalFormat(self) -> 'XSheetConditionalEntries_694810c0':
        """
        contains the conditional formatting settings for this cell.
        
        After a conditional format has been changed it has to be reinserted into the property set.
        """
        ...
    @ConditionalFormat.setter
    def ConditionalFormat(self, value: 'XSheetConditionalEntries_694810c0') -> None:
        ...
    @property
    def ConditionalFormatLocal(self) -> 'XSheetConditionalEntries_694810c0':
        """
        contains the conditional formatting settings for this cell, using localized formulas.
        
        After a conditional format has been changed it has to be reinserted into the property set.
        """
        ...
    @ConditionalFormatLocal.setter
    def ConditionalFormatLocal(self, value: 'XSheetConditionalEntries_694810c0') -> None:
        ...
    @property
    def Position(self) -> 'Point_5fb2085e':
        """
        contains the position of the top left cell of this range in the sheet (in 1/100 mm).
        
        This property contains the absolute position in the whole sheet, not the position in the visible area.
        """
        ...
    @Position.setter
    def Position(self, value: 'Point_5fb2085e') -> None:
        ...
    @property
    def Size(self) -> 'Size_576707ef':
        """
        contains the size of this range (in 1/100 mm).
        """
        ...
    @Size.setter
    def Size(self, value: 'Size_576707ef') -> None:
        ...
    @property
    def Validation(self) -> 'XPropertySet_bc180bfa':
        """
        contains the data validation settings for this cell.
        
        After the data validation settings have been changed the validation has to be reinserted into the property set.
        """
        ...
    @Validation.setter
    def Validation(self, value: 'XPropertySet_bc180bfa') -> None:
        ...
    @property
    def ValidationLocal(self) -> 'XPropertySet_bc180bfa':
        """
        contains the data validation settings for this cell, using localized formulas.
        
        After the data validation settings have been changed the validation has to be reinserted into the property set.
        """
        ...
    @ValidationLocal.setter
    def ValidationLocal(self, value: 'XPropertySet_bc180bfa') -> None:
        ...

