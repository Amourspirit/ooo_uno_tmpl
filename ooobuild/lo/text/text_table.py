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
# Namespace: com.sun.star.text
from __future__ import annotations
import typing
from abc import abstractmethod
from ..chart.x_chart_data_array import XChartDataArray as XChartDataArray_df4c0cdd
from ..container.x_named import XNamed as XNamed_a6520b08
from ..sheet.x_cell_range_data import XCellRangeData as XCellRangeData_d2e70c60
from ..table.x_auto_formattable import XAutoFormattable as XAutoFormattable_ee660d72
from ..table.x_cell_range import XCellRange as XCellRange_a2f70ad5
from .text_content import TextContent as TextContent_a6810b4d
from .x_text_table import XTextTable as XTextTable_9a810ab2
from ..util.x_sortable import XSortable as XSortable_8ff20a5a
from ..xml.user_defined_attributes_supplier import UserDefinedAttributesSupplier as UserDefinedAttributesSupplier_9fbe1222
if typing.TYPE_CHECKING:
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73
    from ..graphic.x_graphic import XGraphic as XGraphic_a4da0afc
    from ..table.shadow_format import ShadowFormat as ShadowFormat_bb840bdf
    from ..table.table_border import TableBorder as TableBorder_aedf0b56
    from .table_column_separator import TableColumnSeparator as TableColumnSeparator_1b630ed4
    from ..util.color import Color as Color_68e908c5
    from com.sun.star.style.GraphicLocation import GraphicLocationProto  # type: ignore
    from com.sun.star.style.BreakType import BreakTypeProto  # type: ignore

class TextTable(TextContent_a6810b4d, UserDefinedAttributesSupplier_9fbe1222, XChartDataArray_df4c0cdd, XNamed_a6520b08, XCellRangeData_d2e70c60, XAutoFormattable_ee660d72, XCellRange_a2f70ad5, XTextTable_9a810ab2, XSortable_8ff20a5a):
    """
    Service Class

    is a table of text cells which is anchored to a surrounding text.
    
    Note: The anchor of the actual implementation for text tables does not have a position in the text. Thus that anchor can not be used for some operation like XTextContent.attach() or XText.insertTextContent() or other function that require the object to have a position in the text.
    
    The reason why a text table still needs an anchor is that for example tables should be insertable via XText.insertTextContent() and that interface uses a parameter of that type.
    
    Example: Create and insert a TextTable:
    
    **since**
    
        LibreOffice 6.1

    See Also:
        `API TextTable <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1text_1_1TextTable.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.text'
    __ooo_full_ns__: str = 'com.sun.star.text.TextTable'
    __ooo_type_name__: str = 'service'

    @property
    @abstractmethod
    def BackColor(self) -> Color_68e908c5:
        """
        contains the color of the background.
        """
        ...

    @property
    @abstractmethod
    def BackGraphic(self) -> XGraphic_a4da0afc:
        """
        contains the graphic for the background.
        
        **since**
        
            LibreOffice 6.1
        """
        ...

    @property
    @abstractmethod
    def BackGraphicFilter(self) -> str:
        """
        contains the name of the file filter for the background graphic.
        """
        ...

    @property
    @abstractmethod
    def BackGraphicLocation(self) -> GraphicLocationProto:
        """
        determines the position of the background graphic.
        """
        ...

    @property
    @abstractmethod
    def BackGraphicURL(self) -> str:
        """
        contains the URL for the background graphic.
        
        Note the new behaviour since it this was deprecated: This property can only be set and only external URLs are supported (no more vnd.sun.star.GraphicObject scheme). When an URL is set, then it will load the graphic and set the BackGraphic property.
        """
        ...

    @property
    @abstractmethod
    def BackTransparent(self) -> bool:
        """
        determines if the background color is transparent.
        """
        ...

    @property
    @abstractmethod
    def BottomMargin(self) -> int:
        """
        determines the bottom margin.
        """
        ...

    @property
    @abstractmethod
    def BreakType(self) -> BreakTypeProto:
        """
        determines the type of break that is applied at the beginning of the table.
        """
        ...

    @property
    @abstractmethod
    def ChartColumnAsLabel(self) -> bool:
        """
        determines if the first column of the table should be treated as axis labels when a chart is to be created.
        """
        ...

    @property
    @abstractmethod
    def ChartRowAsLabel(self) -> bool:
        """
        determines if the first row of the table should be treated as axis labels when a chart is to be created.
        """
        ...

    @property
    @abstractmethod
    def CollapsingBorders(self) -> bool:
        """
        determines whether borders of neighboring table cells are collapsed into one
        """
        ...

    @property
    @abstractmethod
    def HeaderRowCount(self) -> int:
        """
        determines the number of rows of the table repeated on every new page.
        """
        ...

    @property
    @abstractmethod
    def HoriOrient(self) -> int:
        """
        contains the horizontal orientation.
        """
        ...

    @property
    @abstractmethod
    def IsWidthRelative(self) -> bool:
        """
        determines if the value of the relative width is valid.
        """
        ...

    @property
    @abstractmethod
    def KeepTogether(self) -> bool:
        """
        Setting this property to TRUE prevents page or column breaks between this table and the following paragraph or text table.
        """
        ...

    @property
    @abstractmethod
    def LeftMargin(self) -> int:
        """
        contains the left margin of the table.
        """
        ...

    @property
    @abstractmethod
    def PageDescName(self) -> str:
        """
        If this property is set, it creates a page break before the table and assigns the value as the name of the new page style sheet to use.
        """
        ...

    @property
    @abstractmethod
    def PageNumberOffset(self) -> int:
        """
        If a page break property is set at the table, this property contains the new value for the page number.
        """
        ...

    @property
    @abstractmethod
    def RelativeWidth(self) -> int:
        """
        determines the width of the table relative to its environment.
        """
        ...

    @property
    @abstractmethod
    def RepeatHeadline(self) -> bool:
        """
        determines if the first row of the table is repeated on every new page.
        """
        ...

    @property
    @abstractmethod
    def RightMargin(self) -> int:
        """
        contains the right margin of the table.
        """
        ...

    @property
    @abstractmethod
    def ShadowFormat(self) -> ShadowFormat_bb840bdf:
        """
        determines the type, color and size of the shadow.
        """
        ...

    @property
    @abstractmethod
    def Split(self) -> bool:
        """
        Setting this property to FALSE prevents the table from getting spread on two pages.
        """
        ...

    @property
    @abstractmethod
    def TableBorder(self) -> TableBorder_aedf0b56:
        """
        contains the description of the table borders.
        """
        ...

    @property
    @abstractmethod
    def TableColumnRelativeSum(self) -> int:
        """
        contains the sum of the column width values used in TableColumnSeparators.
        """
        ...

    @property
    @abstractmethod
    def TableColumnSeparators(self) -> typing.Tuple[TableColumnSeparator_1b630ed4, ...]:
        """
        contains the column description of the table.
        """
        ...

    @property
    @abstractmethod
    def TableInteropGrabBag(self) -> typing.Tuple[PropertyValue_c9610c73, ...]:
        """
        Grab bag of table properties, used as a string-any map for interim interop purposes.
        
        This property is intentionally not handled by the ODF filter. Any member that should be handled there should be first moved out from this grab bag to a separate property.
        
        **since**
        
            LibreOffice 4.3
        """
        ...

    @property
    @abstractmethod
    def TableTemplateName(self) -> str:
        """
        contains the name of table style used by the table.
        
        **since**
        
            LibreOffice 5.3
        """
        ...

    @property
    @abstractmethod
    def TopMargin(self) -> int:
        """
        determines the top margin.
        """
        ...

    @property
    @abstractmethod
    def Width(self) -> int:
        """
        contains the absolute table width.
        
        As this is only a describing property the value of the actual table may vary depending on the environment the table is located in and the settings of LeftMargin, RightMargin and HoriOrient.
        """
        ...


__all__ = ['TextTable']