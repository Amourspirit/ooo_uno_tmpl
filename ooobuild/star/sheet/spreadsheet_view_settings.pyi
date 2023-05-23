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
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
if typing.TYPE_CHECKING:
    from ..util.color import Color as Color_68e908c5

class SpreadsheetViewSettings(XPropertySet_bc180bfa):
    """
    Service Class

    contains settings which are specific to each view of a spreadsheet
    
    **since**
    
        LibreOffice 7.4

    See Also:
        `API SpreadsheetViewSettings <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sheet_1_1SpreadsheetViewSettings.html>`_
    """
    @property
    def FormulaBarHeight(self) -> int:
        """
        Number of lines shown in the Formula bar Default is 1, maximum value is 25.
        
        **since**
        
            LibreOffice 7.4
        """
        ...
    @FormulaBarHeight.setter
    def FormulaBarHeight(self, value: int) -> None:
        ...
    @property
    def GridColor(self) -> 'Color_68e908c5':
        """
        specifies the color in which the cell grid is displayed.
        """
        ...
    @GridColor.setter
    def GridColor(self, value: 'Color_68e908c5') -> None:
        ...
    @property
    def HasColumnRowHeaders(self) -> bool:
        """
        enables the column and row headers of the view.
        """
        ...
    @HasColumnRowHeaders.setter
    def HasColumnRowHeaders(self, value: bool) -> None:
        ...
    @property
    def HasHorizontalScrollBar(self) -> bool:
        """
        enables the horizontal scroll bar of the view.
        """
        ...
    @HasHorizontalScrollBar.setter
    def HasHorizontalScrollBar(self, value: bool) -> None:
        ...
    @property
    def HasSheetTabs(self) -> bool:
        """
        enables the sheet tabs of the view.
        """
        ...
    @HasSheetTabs.setter
    def HasSheetTabs(self, value: bool) -> None:
        ...
    @property
    def HasVerticalScrollBar(self) -> bool:
        """
        enables the vertical scroll bar of the view.
        """
        ...
    @HasVerticalScrollBar.setter
    def HasVerticalScrollBar(self, value: bool) -> None:
        ...
    @property
    def HideSpellMarks(self) -> bool:
        """
        disables the display of marks from online spelling.
        """
        ...
    @HideSpellMarks.setter
    def HideSpellMarks(self, value: bool) -> None:
        ...
    @property
    def IsOutlineSymbolsSet(self) -> bool:
        """
        enables the display of outline symbols.
        """
        ...
    @IsOutlineSymbolsSet.setter
    def IsOutlineSymbolsSet(self, value: bool) -> None:
        ...
    @property
    def IsValueHighlightingEnabled(self) -> bool:
        """
        controls whether strings, values, and formulas are displayed in different colors.
        """
        ...
    @IsValueHighlightingEnabled.setter
    def IsValueHighlightingEnabled(self, value: bool) -> None:
        ...
    @property
    def ShowAnchor(self) -> bool:
        """
        enables display of anchor symbols when drawing objects are selected.
        """
        ...
    @ShowAnchor.setter
    def ShowAnchor(self, value: bool) -> None:
        ...
    @property
    def ShowCharts(self) -> int:
        """
        enables the display of charts in the view.
        """
        ...
    @ShowCharts.setter
    def ShowCharts(self, value: int) -> None:
        ...
    @property
    def ShowDrawing(self) -> int:
        """
        enables the display of drawing objects in the view.
        """
        ...
    @ShowDrawing.setter
    def ShowDrawing(self, value: int) -> None:
        ...
    @property
    def ShowFormulas(self) -> bool:
        """
        controls whether formulas are displayed instead of their results.
        """
        ...
    @ShowFormulas.setter
    def ShowFormulas(self, value: bool) -> None:
        ...
    @property
    def ShowGrid(self) -> bool:
        """
        enables the display of the cell grid.
        """
        ...
    @ShowGrid.setter
    def ShowGrid(self, value: bool) -> None:
        ...
    @property
    def ShowHelpLines(self) -> bool:
        """
        enables display of help lines when moving drawing objects.
        """
        ...
    @ShowHelpLines.setter
    def ShowHelpLines(self, value: bool) -> None:
        ...
    @property
    def ShowNotes(self) -> bool:
        """
        controls whether a marker is shown for notes in cells.
        """
        ...
    @ShowNotes.setter
    def ShowNotes(self, value: bool) -> None:
        ...
    @property
    def ShowObjects(self) -> int:
        """
        enables display of embedded objects in the view.
        """
        ...
    @ShowObjects.setter
    def ShowObjects(self, value: int) -> None:
        ...
    @property
    def ShowPageBreaks(self) -> bool:
        """
        enables display of page breaks.
        """
        ...
    @ShowPageBreaks.setter
    def ShowPageBreaks(self, value: bool) -> None:
        ...
    @property
    def ShowZeroValues(self) -> bool:
        """
        enables display of zero-values.
        """
        ...
    @ShowZeroValues.setter
    def ShowZeroValues(self, value: bool) -> None:
        ...
    @property
    def ZoomType(self) -> int:
        """
        This property defines the zoom type for the document.
        """
        ...
    @ZoomType.setter
    def ZoomType(self, value: int) -> None:
        ...
    @property
    def ZoomValue(self) -> int:
        """
        Defines the zoom value to use.
        
        Valid only if the ZoomType is set to com.sun.star.view.DocumentZoomType.BY_VALUE.
        """
        ...
    @ZoomValue.setter
    def ZoomValue(self, value: int) -> None:
        ...
