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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.style
import typing
from abc import ABC
if typing.TYPE_CHECKING:
    from ..awt.size import Size as Size_576707ef
    from ..container.x_name_container import XNameContainer as XNameContainer_cb90e47
    from ..graphic.x_graphic import XGraphic as XGraphic_a4da0afc
    from .graphic_location import GraphicLocation as GraphicLocation_e3ef0d30
    from .page_style_layout import PageStyleLayout as PageStyleLayout_e4070d45
    from ..table.border_line import BorderLine as BorderLine_a3f80af6
    from ..table.shadow_format import ShadowFormat as ShadowFormat_bb840bdf
    from ..text.x_text import XText as XText_690408ca
    from ..text.x_text_columns import XTextColumns as XTextColumns_b17f0bab
    from ..util.color import Color as Color_68e908c5

class PageProperties(ABC):
    """
    Service Class

    describes the style of pages.
    
    **since**
    
        LibreOffice 6.1

    See Also:
        `API PageProperties <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1style_1_1PageProperties.html>`_
    """
    @property
    def BackColor(self) -> 'Color_68e908c5':
        """
        contains the background color of the page.
        """
        ...

    @BackColor.setter
    def BackColor(self, value: 'Color_68e908c5') -> None:
        ...
    @property
    def BackGraphic(self) -> 'XGraphic_a4da0afc':
        """
        contains the graphic of the background.
        
        **since**
        
            LibreOffice 6.1
        """
        ...

    @BackGraphic.setter
    def BackGraphic(self, value: 'XGraphic_a4da0afc') -> None:
        ...
    @property
    def BackGraphicFilter(self) -> str:
        """
        contains the filter name of the background graphic.
        """
        ...

    @BackGraphicFilter.setter
    def BackGraphicFilter(self, value: str) -> None:
        ...
    @property
    def BackGraphicLocation(self) -> 'GraphicLocation_e3ef0d30':
        """
        determines the location of the background graphic.
        """
        ...

    @BackGraphicLocation.setter
    def BackGraphicLocation(self, value: 'GraphicLocation_e3ef0d30') -> None:
        ...
    @property
    def BackGraphicURL(self) -> str:
        """
        contains the URL of the background graphic.
        
        Note the new behaviour since it this was deprecated: This property can only be set and only external URLs are supported (no more vnd.sun.star.GraphicObject scheme). When an URL is set, then it will load the graphic and set the BackGraphic property.
        """
        ...

    @BackGraphicURL.setter
    def BackGraphicURL(self, value: str) -> None:
        ...
    @property
    def BackTransparent(self) -> bool:
        """
        determines if the background color is transparent.
        
        If this property is set to TRUE, PageStyle.BackColor will not be used.
        """
        ...

    @BackTransparent.setter
    def BackTransparent(self, value: bool) -> None:
        ...
    @property
    def BackgroundFullSize(self) -> bool:
        """
        does the background cover the full page or only inside the margins?
        
        **since**
        
            LibreOffice 7.2
        """
        ...

    @BackgroundFullSize.setter
    def BackgroundFullSize(self, value: bool) -> None:
        ...
    @property
    def BorderDistance(self) -> int:
        """
        determines the distance of all borders of the page.
        """
        ...

    @BorderDistance.setter
    def BorderDistance(self, value: int) -> None:
        ...
    @property
    def BottomBorder(self) -> 'BorderLine_a3f80af6':
        """
        determines the style of the bottom border line of the page.
        """
        ...

    @BottomBorder.setter
    def BottomBorder(self, value: 'BorderLine_a3f80af6') -> None:
        ...
    @property
    def BottomBorderDistance(self) -> int:
        """
        determines the bottom border distance of the page.
        """
        ...

    @BottomBorderDistance.setter
    def BottomBorderDistance(self, value: int) -> None:
        ...
    @property
    def BottomMargin(self) -> int:
        """
        determines the bottom margin of the page.
        """
        ...

    @BottomMargin.setter
    def BottomMargin(self, value: int) -> None:
        ...
    @property
    def FirstIsShared(self) -> bool:
        """
        determines if the header/footer content on the first page and remaining pages is the same.
        
        **since**
        
            LibreOffice 4.0
        """
        ...

    @FirstIsShared.setter
    def FirstIsShared(self, value: bool) -> None:
        ...
    @property
    def FooterBackColor(self) -> 'Color_68e908c5':
        """
        contains the color of the background of the footer.
        """
        ...

    @FooterBackColor.setter
    def FooterBackColor(self, value: 'Color_68e908c5') -> None:
        ...
    @property
    def FooterBackGraphic(self) -> 'XGraphic_a4da0afc':
        """
        contains the graphic of the background of the footer.
        
        **since**
        
            LibreOffice 6.1
        """
        ...

    @FooterBackGraphic.setter
    def FooterBackGraphic(self, value: 'XGraphic_a4da0afc') -> None:
        ...
    @property
    def FooterBackGraphicFilter(self) -> str:
        """
        contains the filter name of the background graphic in the footer.
        """
        ...

    @FooterBackGraphicFilter.setter
    def FooterBackGraphicFilter(self, value: str) -> None:
        ...
    @property
    def FooterBackGraphicLocation(self) -> 'GraphicLocation_e3ef0d30':
        """
        determines the location of the background graphic in the footer.
        """
        ...

    @FooterBackGraphicLocation.setter
    def FooterBackGraphicLocation(self, value: 'GraphicLocation_e3ef0d30') -> None:
        ...
    @property
    def FooterBackGraphicURL(self) -> str:
        """
        contains the URL of the background graphic in the footer.
        
        Note the new behaviour since it this was deprecated: This property can only be set and only external URLs are supported (no more vnd.sun.star.GraphicObject scheme). When an URL is set, then it will load the graphic and set the FooterBackGraphic property.
        """
        ...

    @FooterBackGraphicURL.setter
    def FooterBackGraphicURL(self, value: str) -> None:
        ...
    @property
    def FooterBackTransparent(self) -> bool:
        """
        determines if the background of the footer is transparent.
        """
        ...

    @FooterBackTransparent.setter
    def FooterBackTransparent(self, value: bool) -> None:
        ...
    @property
    def FooterBodyDistance(self) -> int:
        """
        determines the distance between the footer and the body text area.
        """
        ...

    @FooterBodyDistance.setter
    def FooterBodyDistance(self, value: int) -> None:
        ...
    @property
    def FooterBorderDistance(self) -> int:
        """
        contains the distance of all borders of the footer.
        """
        ...

    @FooterBorderDistance.setter
    def FooterBorderDistance(self, value: int) -> None:
        ...
    @property
    def FooterBottomBorder(self) -> 'BorderLine_a3f80af6':
        """
        contains the style of the bottom border line of the footer.
        """
        ...

    @FooterBottomBorder.setter
    def FooterBottomBorder(self, value: 'BorderLine_a3f80af6') -> None:
        ...
    @property
    def FooterBottomBorderDistance(self) -> int:
        """
        contains the bottom border distance of the footer.
        """
        ...

    @FooterBottomBorderDistance.setter
    def FooterBottomBorderDistance(self, value: int) -> None:
        ...
    @property
    def FooterDynamicSpacing(self) -> bool:
        """
        determines whether to use dynamic spacing in footer or not.
        """
        ...

    @FooterDynamicSpacing.setter
    def FooterDynamicSpacing(self, value: bool) -> None:
        ...
    @property
    def FooterHeight(self) -> int:
        """
        determines the height of the footer.
        """
        ...

    @FooterHeight.setter
    def FooterHeight(self, value: int) -> None:
        ...
    @property
    def FooterIsDynamicHeight(self) -> bool:
        """
        determines if the height of the footer depends on the content.
        """
        ...

    @FooterIsDynamicHeight.setter
    def FooterIsDynamicHeight(self, value: bool) -> None:
        ...
    @property
    def FooterIsOn(self) -> bool:
        """
        determines if a footer is used on the page.
        """
        ...

    @FooterIsOn.setter
    def FooterIsOn(self, value: bool) -> None:
        ...
    @property
    def FooterIsShared(self) -> bool:
        """
        determines if the footer content on left and right pages is the same.
        """
        ...

    @FooterIsShared.setter
    def FooterIsShared(self, value: bool) -> None:
        ...
    @property
    def FooterLeftBorder(self) -> 'BorderLine_a3f80af6':
        """
        contains the style of the left border line of the footer.
        """
        ...

    @FooterLeftBorder.setter
    def FooterLeftBorder(self, value: 'BorderLine_a3f80af6') -> None:
        ...
    @property
    def FooterLeftBorderDistance(self) -> int:
        """
        contains the left border distance of the footer.
        """
        ...

    @FooterLeftBorderDistance.setter
    def FooterLeftBorderDistance(self, value: int) -> None:
        ...
    @property
    def FooterLeftMargin(self) -> int:
        """
        determines the left margin of the footer.
        """
        ...

    @FooterLeftMargin.setter
    def FooterLeftMargin(self, value: int) -> None:
        ...
    @property
    def FooterRightBorder(self) -> 'BorderLine_a3f80af6':
        """
        contains the style of the right border line of the footer.
        """
        ...

    @FooterRightBorder.setter
    def FooterRightBorder(self, value: 'BorderLine_a3f80af6') -> None:
        ...
    @property
    def FooterRightBorderDistance(self) -> int:
        """
        contains the right border distance of the footer.
        """
        ...

    @FooterRightBorderDistance.setter
    def FooterRightBorderDistance(self, value: int) -> None:
        ...
    @property
    def FooterRightMargin(self) -> int:
        """
        determines the right margin of the footer.
        """
        ...

    @FooterRightMargin.setter
    def FooterRightMargin(self, value: int) -> None:
        ...
    @property
    def FooterShadowFormat(self) -> 'ShadowFormat_bb840bdf':
        """
        determines the shadow of the footer.
        """
        ...

    @FooterShadowFormat.setter
    def FooterShadowFormat(self, value: 'ShadowFormat_bb840bdf') -> None:
        ...
    @property
    def FooterText(self) -> 'XText_690408ca':
        """
        contains the interface to the text of the footer.
        """
        ...

    @FooterText.setter
    def FooterText(self, value: 'XText_690408ca') -> None:
        ...
    @property
    def FooterTextLeft(self) -> 'XText_690408ca':
        """
        contains the interface to the text of the footer of a left page.
        """
        ...

    @FooterTextLeft.setter
    def FooterTextLeft(self, value: 'XText_690408ca') -> None:
        ...
    @property
    def FooterTextRight(self) -> 'XText_690408ca':
        """
        contains the interface to the text of the footer of a right page.
        """
        ...

    @FooterTextRight.setter
    def FooterTextRight(self, value: 'XText_690408ca') -> None:
        ...
    @property
    def FooterTopBorder(self) -> 'BorderLine_a3f80af6':
        """
        contains the style of the top border line of the footer.
        """
        ...

    @FooterTopBorder.setter
    def FooterTopBorder(self, value: 'BorderLine_a3f80af6') -> None:
        ...
    @property
    def FooterTopBorderDistance(self) -> int:
        """
        contains the top border distance of the footer.
        """
        ...

    @FooterTopBorderDistance.setter
    def FooterTopBorderDistance(self, value: int) -> None:
        ...
    @property
    def FootnoteHeight(self) -> int:
        """
        contains the maximum height of the footnote area.
        
        If set to zero then the height of the current page is used as limit.
        """
        ...

    @FootnoteHeight.setter
    def FootnoteHeight(self, value: int) -> None:
        ...
    @property
    def FootnoteLineAdjust(self) -> int:
        """
        contains the adjustment of the separator line between the text and the footnote area.
        
        com.sun.star.text.HorizontalAdjusts.
        """
        ...

    @FootnoteLineAdjust.setter
    def FootnoteLineAdjust(self, value: int) -> None:
        ...
    @property
    def FootnoteLineColor(self) -> 'Color_68e908c5':
        """
        contains the color of the separator line between the text and the footnote area.
        """
        ...

    @FootnoteLineColor.setter
    def FootnoteLineColor(self, value: 'Color_68e908c5') -> None:
        ...
    @property
    def FootnoteLineDistance(self) -> int:
        """
        contains the distance between the footnote area and the separator line between the text and the footnote area.
        """
        ...

    @FootnoteLineDistance.setter
    def FootnoteLineDistance(self, value: int) -> None:
        ...
    @property
    def FootnoteLineRelativeWidth(self) -> int:
        """
        contains the relative width of the separator line between the text and the footnote area.
        """
        ...

    @FootnoteLineRelativeWidth.setter
    def FootnoteLineRelativeWidth(self, value: int) -> None:
        ...
    @property
    def FootnoteLineStyle(self) -> int:
        """
        contains the style of the separator line between the text and the footnote area.
        """
        ...

    @FootnoteLineStyle.setter
    def FootnoteLineStyle(self, value: int) -> None:
        ...
    @property
    def FootnoteLineTextDistance(self) -> int:
        """
        contains the distance between the text and the separator line between the text and the footnote area.
        """
        ...

    @FootnoteLineTextDistance.setter
    def FootnoteLineTextDistance(self, value: int) -> None:
        ...
    @property
    def FootnoteLineWeight(self) -> int:
        """
        contains the weight of the separator line between the text and the footnote area.
        """
        ...

    @FootnoteLineWeight.setter
    def FootnoteLineWeight(self, value: int) -> None:
        ...
    @property
    def GridBaseHeight(self) -> int:
        """
        contains the height of the base text line inside the text grid
        """
        ...

    @GridBaseHeight.setter
    def GridBaseHeight(self, value: int) -> None:
        ...
    @property
    def GridColor(self) -> 'Color_68e908c5':
        """
        contains the display color of the text grid
        """
        ...

    @GridColor.setter
    def GridColor(self, value: 'Color_68e908c5') -> None:
        ...
    @property
    def GridDisplay(self) -> bool:
        """
        determines whether the text grid lines are visible or not
        """
        ...

    @GridDisplay.setter
    def GridDisplay(self, value: bool) -> None:
        ...
    @property
    def GridLines(self) -> int:
        """
        contains the number of lines in the text grid
        """
        ...

    @GridLines.setter
    def GridLines(self, value: int) -> None:
        ...
    @property
    def GridMode(self) -> int:
        """
        contains the mode of the text grid (none, lines, ...), as represented by com.sun.star.text.TextGridMode constants
        """
        ...

    @GridMode.setter
    def GridMode(self, value: int) -> None:
        ...
    @property
    def GridPrint(self) -> bool:
        """
        determines whether the text grid lines are printed
        """
        ...

    @GridPrint.setter
    def GridPrint(self, value: bool) -> None:
        ...
    @property
    def GridRubyBelow(self) -> bool:
        """
        determines whether the text grid's ruby line is located below or above the base line
        """
        ...

    @GridRubyBelow.setter
    def GridRubyBelow(self, value: bool) -> None:
        ...
    @property
    def GridRubyHeight(self) -> int:
        """
        contains the height of the ruby text line inside the text grid
        """
        ...

    @GridRubyHeight.setter
    def GridRubyHeight(self, value: int) -> None:
        ...
    @property
    def GutterMargin(self) -> int:
        """
        determines the gutter margin of the page.
        
        **since**
        
            LibreOffice 7.2
        """
        ...

    @GutterMargin.setter
    def GutterMargin(self, value: int) -> None:
        ...
    @property
    def HeaderBackColor(self) -> 'Color_68e908c5':
        """
        contains the color of the background of the header.
        """
        ...

    @HeaderBackColor.setter
    def HeaderBackColor(self, value: 'Color_68e908c5') -> None:
        ...
    @property
    def HeaderBackGraphic(self) -> 'XGraphic_a4da0afc':
        """
        contains the graphic of the background of the header.
        
        **since**
        
            LibreOffice 6.1
        """
        ...

    @HeaderBackGraphic.setter
    def HeaderBackGraphic(self, value: 'XGraphic_a4da0afc') -> None:
        ...
    @property
    def HeaderBackGraphicFilter(self) -> str:
        """
        contains the filter name of the background graphic of the header.
        """
        ...

    @HeaderBackGraphicFilter.setter
    def HeaderBackGraphicFilter(self, value: str) -> None:
        ...
    @property
    def HeaderBackGraphicLocation(self) -> 'GraphicLocation_e3ef0d30':
        """
        determines the location of the background graphic of the header.
        """
        ...

    @HeaderBackGraphicLocation.setter
    def HeaderBackGraphicLocation(self, value: 'GraphicLocation_e3ef0d30') -> None:
        ...
    @property
    def HeaderBackGraphicURL(self) -> str:
        """
        contains the URL of the background graphic of the header.
        
        Note the new behaviour since it this was deprecated: This property can only be set and only external URLs are supported (no more vnd.sun.star.GraphicObject scheme). When an URL is set, then it will load the graphic and set the HeaderBackGraphic property.
        """
        ...

    @HeaderBackGraphicURL.setter
    def HeaderBackGraphicURL(self, value: str) -> None:
        ...
    @property
    def HeaderBackTransparent(self) -> bool:
        """
        determines if the background color of the header is transparent.
        
        If this property is set to TRUE, PageStyle.HeaderBackColor will not be used.
        """
        ...

    @HeaderBackTransparent.setter
    def HeaderBackTransparent(self, value: bool) -> None:
        ...
    @property
    def HeaderBodyDistance(self) -> int:
        """
        determines the distance between the header and the body text area.
        """
        ...

    @HeaderBodyDistance.setter
    def HeaderBodyDistance(self, value: int) -> None:
        ...
    @property
    def HeaderBorderDistance(self) -> int:
        """
        determines the distance of all borders of the header.
        """
        ...

    @HeaderBorderDistance.setter
    def HeaderBorderDistance(self, value: int) -> None:
        ...
    @property
    def HeaderBottomBorder(self) -> 'BorderLine_a3f80af6':
        """
        determines the style of the bottom border line of the header.
        """
        ...

    @HeaderBottomBorder.setter
    def HeaderBottomBorder(self, value: 'BorderLine_a3f80af6') -> None:
        ...
    @property
    def HeaderBottomBorderDistance(self) -> int:
        """
        determines the bottom border distance of the header.
        """
        ...

    @HeaderBottomBorderDistance.setter
    def HeaderBottomBorderDistance(self, value: int) -> None:
        ...
    @property
    def HeaderDynamicSpacing(self) -> bool:
        """
        determines whether to use dynamic spacing in header or not.
        """
        ...

    @HeaderDynamicSpacing.setter
    def HeaderDynamicSpacing(self, value: bool) -> None:
        ...
    @property
    def HeaderHeight(self) -> int:
        """
        contains the height of the header.
        """
        ...

    @HeaderHeight.setter
    def HeaderHeight(self, value: int) -> None:
        ...
    @property
    def HeaderIsDynamicHeight(self) -> bool:
        """
        determines if the height of the header depends on the content.
        """
        ...

    @HeaderIsDynamicHeight.setter
    def HeaderIsDynamicHeight(self, value: bool) -> None:
        ...
    @property
    def HeaderIsOn(self) -> bool:
        """
        determines if a header is used on the page.
        """
        ...

    @HeaderIsOn.setter
    def HeaderIsOn(self, value: bool) -> None:
        ...
    @property
    def HeaderIsShared(self) -> bool:
        """
        determines if the header content on left and right pages is the same.
        """
        ...

    @HeaderIsShared.setter
    def HeaderIsShared(self, value: bool) -> None:
        ...
    @property
    def HeaderLeftBorder(self) -> 'BorderLine_a3f80af6':
        """
        determines the style of the left border line of the header.
        """
        ...

    @HeaderLeftBorder.setter
    def HeaderLeftBorder(self, value: 'BorderLine_a3f80af6') -> None:
        ...
    @property
    def HeaderLeftBorderDistance(self) -> int:
        """
        determines the left border distance of the header.
        """
        ...

    @HeaderLeftBorderDistance.setter
    def HeaderLeftBorderDistance(self, value: int) -> None:
        ...
    @property
    def HeaderLeftMargin(self) -> int:
        """
        contains the left margin of the header.
        """
        ...

    @HeaderLeftMargin.setter
    def HeaderLeftMargin(self, value: int) -> None:
        ...
    @property
    def HeaderRightBorder(self) -> 'BorderLine_a3f80af6':
        """
        determines the style of the right border line of the header.
        """
        ...

    @HeaderRightBorder.setter
    def HeaderRightBorder(self, value: 'BorderLine_a3f80af6') -> None:
        ...
    @property
    def HeaderRightBorderDistance(self) -> int:
        """
        determines the right border distance of the header.
        """
        ...

    @HeaderRightBorderDistance.setter
    def HeaderRightBorderDistance(self, value: int) -> None:
        ...
    @property
    def HeaderRightMargin(self) -> int:
        """
        contains the right margin of the header.
        """
        ...

    @HeaderRightMargin.setter
    def HeaderRightMargin(self, value: int) -> None:
        ...
    @property
    def HeaderShadowFormat(self) -> 'ShadowFormat_bb840bdf':
        """
        determines the shadow of the header.
        """
        ...

    @HeaderShadowFormat.setter
    def HeaderShadowFormat(self, value: 'ShadowFormat_bb840bdf') -> None:
        ...
    @property
    def HeaderText(self) -> 'XText_690408ca':
        """
        contains the interface to the text of the header.
        """
        ...

    @HeaderText.setter
    def HeaderText(self, value: 'XText_690408ca') -> None:
        ...
    @property
    def HeaderTextLeft(self) -> 'XText_690408ca':
        """
        contains the interface to the text of the header of left pages.
        """
        ...

    @HeaderTextLeft.setter
    def HeaderTextLeft(self, value: 'XText_690408ca') -> None:
        ...
    @property
    def HeaderTextRight(self) -> 'XText_690408ca':
        """
        contains the interface to the text of the header of right pages.
        """
        ...

    @HeaderTextRight.setter
    def HeaderTextRight(self, value: 'XText_690408ca') -> None:
        ...
    @property
    def HeaderTopBorder(self) -> 'BorderLine_a3f80af6':
        """
        determines the style of the top border line of the header.
        """
        ...

    @HeaderTopBorder.setter
    def HeaderTopBorder(self, value: 'BorderLine_a3f80af6') -> None:
        ...
    @property
    def HeaderTopBorderDistance(self) -> int:
        """
        determines the top border distance of the header.
        """
        ...

    @HeaderTopBorderDistance.setter
    def HeaderTopBorderDistance(self, value: int) -> None:
        ...
    @property
    def Height(self) -> int:
        """
        contains the height of the page.
        """
        ...

    @Height.setter
    def Height(self, value: int) -> None:
        ...
    @property
    def IsLandscape(self) -> bool:
        """
        determines if the page format is landscape.
        """
        ...

    @IsLandscape.setter
    def IsLandscape(self, value: bool) -> None:
        ...
    @property
    def LeftBorder(self) -> 'BorderLine_a3f80af6':
        """
        determines the style of the left border line of the page.
        """
        ...

    @LeftBorder.setter
    def LeftBorder(self, value: 'BorderLine_a3f80af6') -> None:
        ...
    @property
    def LeftBorderDistance(self) -> int:
        """
        determines the left border distance of the page.
        """
        ...

    @LeftBorderDistance.setter
    def LeftBorderDistance(self, value: int) -> None:
        ...
    @property
    def LeftMargin(self) -> int:
        """
        determines the left margin of the page.
        """
        ...

    @LeftMargin.setter
    def LeftMargin(self, value: int) -> None:
        ...
    @property
    def NumberingType(self) -> int:
        """
        determines the default numbering type for this page.
        """
        ...

    @NumberingType.setter
    def NumberingType(self, value: int) -> None:
        ...
    @property
    def PageStyleLayout(self) -> 'PageStyleLayout_e4070d45':
        """
        determines the layout of the page.
        """
        ...

    @PageStyleLayout.setter
    def PageStyleLayout(self, value: 'PageStyleLayout_e4070d45') -> None:
        ...
    @property
    def PrinterPaperTray(self) -> str:
        """
        contains the name of a paper tray of the selected printer.
        """
        ...

    @PrinterPaperTray.setter
    def PrinterPaperTray(self, value: str) -> None:
        ...
    @property
    def RegisterModeActive(self) -> bool:
        """
        determines if the register mode is active on that page.
        """
        ...

    @RegisterModeActive.setter
    def RegisterModeActive(self, value: bool) -> None:
        ...
    @property
    def RegisterParagraphStyle(self) -> str:
        """
        contains the name of the paragraph style that is used as reference of the register mode.
        """
        ...

    @RegisterParagraphStyle.setter
    def RegisterParagraphStyle(self, value: str) -> None:
        ...
    @property
    def RightBorder(self) -> 'BorderLine_a3f80af6':
        """
        determines the style of the right border line of the page.
        """
        ...

    @RightBorder.setter
    def RightBorder(self, value: 'BorderLine_a3f80af6') -> None:
        ...
    @property
    def RightBorderDistance(self) -> int:
        """
        determines the right border distance of the page.
        """
        ...

    @RightBorderDistance.setter
    def RightBorderDistance(self, value: int) -> None:
        ...
    @property
    def RightMargin(self) -> int:
        """
        determines the right margin of the page.
        """
        ...

    @RightMargin.setter
    def RightMargin(self, value: int) -> None:
        ...
    @property
    def RtlGutter(self) -> bool:
        """
        specifies that the page gutter shall be placed on the right side of the page.
        
        **since**
        
            LibreOffice 7.2
        """
        ...

    @RtlGutter.setter
    def RtlGutter(self, value: bool) -> None:
        ...
    @property
    def ShadowFormat(self) -> 'ShadowFormat_bb840bdf':
        """
        determines the shadow of the page.
        """
        ...

    @ShadowFormat.setter
    def ShadowFormat(self, value: 'ShadowFormat_bb840bdf') -> None:
        ...
    @property
    def Size(self) -> 'Size_576707ef':
        """
        contains the paper size of the page.
        """
        ...

    @Size.setter
    def Size(self, value: 'Size_576707ef') -> None:
        ...
    @property
    def TextColumns(self) -> 'XTextColumns_b17f0bab':
        """
        contains the column settings of the page.
        """
        ...

    @TextColumns.setter
    def TextColumns(self, value: 'XTextColumns_b17f0bab') -> None:
        ...
    @property
    def TopBorder(self) -> 'BorderLine_a3f80af6':
        """
        determines the style of the top border line of the page.
        """
        ...

    @TopBorder.setter
    def TopBorder(self, value: 'BorderLine_a3f80af6') -> None:
        ...
    @property
    def TopBorderDistance(self) -> int:
        """
        determines the top border distance of the page.
        """
        ...

    @TopBorderDistance.setter
    def TopBorderDistance(self, value: int) -> None:
        ...
    @property
    def TopMargin(self) -> int:
        """
        determines the top margin of the page.
        """
        ...

    @TopMargin.setter
    def TopMargin(self, value: int) -> None:
        ...
    @property
    def UserDefinedAttributes(self) -> 'XNameContainer_cb90e47':
        """
        contains user defined attributes.
        
        This com.sun.star.container.XNameContainer supports the service com.sun.star.xml.AttributeContainer.
        """
        ...

    @UserDefinedAttributes.setter
    def UserDefinedAttributes(self, value: 'XNameContainer_cb90e47') -> None:
        ...
    @property
    def Width(self) -> int:
        """
        contains the width of the page.
        """
        ...

    @Width.setter
    def Width(self, value: int) -> None:
        ...
    @property
    def WritingMode(self) -> int:
        """
        contains the writing direction, as represented by the com.sun.star.text.WritingMode2 constants
        """
        ...

    @WritingMode.setter
    def WritingMode(self, value: int) -> None:
        ...

