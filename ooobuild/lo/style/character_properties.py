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
# Namespace: com.sun.star.style
from __future__ import annotations
import typing
from abc import abstractmethod, ABC
if typing.TYPE_CHECKING:
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73
    from ..container.x_name_container import XNameContainer as XNameContainer_cb90e47
    from ..lang.locale import Locale as Locale_70d308fa
    from ..table.border_line2 import BorderLine2 as BorderLine2_af200b28
    from ..table.shadow_format import ShadowFormat as ShadowFormat_bb840bdf
    from ..util.color import Color as Color_68e908c5
    from com.sun.star.awt.FontSlant import FontSlantProto  # type: ignore

class CharacterProperties(ABC):
    """
    Service Class

    This is a set of properties to describe the style of characters.
    
    **since**
    
        LibreOffice 4.2

    See Also:
        `API CharacterProperties <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1style_1_1CharacterProperties.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.style'
    __ooo_full_ns__: str = 'com.sun.star.style.CharacterProperties'
    __ooo_type_name__: str = 'service'

    @property
    @abstractmethod
    def CharAutoKerning(self) -> bool:
        """
        This optional property determines whether the kerning tables from the current font are used.
        
        Automatic kerning applies a spacing in between certain pairs of characters to make the text look better.
        """
        ...

    @property
    @abstractmethod
    def CharBackColor(self) -> Color_68e908c5:
        """
        This optional property contains the text background color.
        """
        ...

    @property
    @abstractmethod
    def CharBackTransparent(self) -> bool:
        """
        This property determines if the text background color is set to transparent.
        """
        ...

    @property
    @abstractmethod
    def CharBorderDistance(self) -> int:
        """
        This property contains the distance from the border to the object.
        
        **since**
        
            LibreOffice 4.2
        """
        ...

    @property
    @abstractmethod
    def CharBottomBorder(self) -> BorderLine2_af200b28:
        """
        This property contains the bottom border of the object.
        
        **since**
        
            LibreOffice 4.2
        """
        ...

    @property
    @abstractmethod
    def CharBottomBorderDistance(self) -> int:
        """
        This property contains the distance from the bottom border to the object.
        
        **since**
        
            LibreOffice 4.2
        """
        ...

    @property
    @abstractmethod
    def CharCaseMap(self) -> int:
        """
        This optional property contains the value of the case-mapping of the text for formatting and displaying.
        """
        ...

    @property
    @abstractmethod
    def CharColor(self) -> Color_68e908c5:
        """
        This property contains the value of the text color.
        """
        ...

    @property
    @abstractmethod
    def CharColorTheme(self) -> int:
        """
        If available, keeps the color theme index, so that the character can be re-colored easily based on a theme.
        
        **since**
        
            LibreOffice 7.3
        """
        ...

    @property
    @abstractmethod
    def CharColorTintOrShade(self) -> int:
        """
        Tint or shade of the character color.
        
        **since**
        
            LibreOffice 7.3
        """
        ...

    @property
    @abstractmethod
    def CharCombineIsOn(self) -> bool:
        """
        This optional property determines whether text is formatted in two lines.
        
        It is linked to the properties CharCombinePrefix and CharCombineSuffix.
        """
        ...

    @property
    @abstractmethod
    def CharCombinePrefix(self) -> str:
        """
        This optional property contains the prefix (usually parenthesis) before text that is formatted in two lines.
        
        It is linked to the properties CharCombineIsOn and CharCombineSuffix.
        """
        ...

    @property
    @abstractmethod
    def CharCombineSuffix(self) -> str:
        """
        This optional property contains the suffix (usually parenthesis) after text that is formatted in two lines.
        
        It is linked to the properties CharCombineIsOn and CharCombinePrefix.
        """
        ...

    @property
    @abstractmethod
    def CharContoured(self) -> bool:
        """
        This optional property specifies if the characters are formatted and displayed with a contour effect.
        """
        ...

    @property
    @abstractmethod
    def CharCrossedOut(self) -> bool:
        """
        This property is TRUE if the characters are crossed out.
        """
        ...

    @property
    @abstractmethod
    def CharEmphasis(self) -> int:
        """
        This optional property contains the font emphasis value.
        """
        ...

    @property
    @abstractmethod
    def CharEscapement(self) -> int:
        """
        specifies the percentage by which to raise/lower superscript/subscript characters.
        
        Negative values denote subscripts and positive values superscripts.
        """
        ...

    @property
    @abstractmethod
    def CharEscapementHeight(self) -> int:
        """
        This is the relative height used for subscript or superscript characters in units of percent.
        
        The value 100 denotes the original height of the characters.
        """
        ...

    @property
    @abstractmethod
    def CharFlash(self) -> bool:
        """
        If this optional property is TRUE, then the characters are flashing.
        """
        ...

    @property
    @abstractmethod
    def CharFontCharSet(self) -> int:
        """
        This property contains the text encoding of the font.
        """
        ...

    @property
    @abstractmethod
    def CharFontFamily(self) -> int:
        """
        This property contains font family.
        """
        ...

    @property
    @abstractmethod
    def CharFontName(self) -> str:
        """
        This property specifies the name of the font style.
        
        It may contain more than one name separated by comma.
        """
        ...

    @property
    @abstractmethod
    def CharFontPitch(self) -> int:
        """
        This property contains the font pitch.
        """
        ...

    @property
    @abstractmethod
    def CharFontStyleName(self) -> str:
        """
        This property contains the name of the font style.
        
        This property may be empty.
        """
        ...

    @property
    @abstractmethod
    def CharFontType(self) -> int:
        """
        This optional property specifies the fundamental technology of the font.
        """
        ...

    @property
    @abstractmethod
    def CharHeight(self) -> float:
        """
        This value contains the height of the characters in point.
        """
        ...

    @property
    @abstractmethod
    def CharHidden(self) -> bool:
        """
        If this optional property is TRUE, then the characters are invisible.
        
        **since**
        
            OOo 2.0
        """
        ...

    @property
    @abstractmethod
    def CharHighlight(self) -> Color_68e908c5:
        """
        Determines the color of the highlight.
        
        **since**
        
            LibreOffice 4.2
        """
        ...

    @property
    @abstractmethod
    def CharInteropGrabBag(self) -> typing.Tuple[PropertyValue_c9610c73, ...]:
        """
        Grab bag of character properties, used as a string-any map for interim interop purposes.
        
        This property is intentionally not handled by the ODF filter. Any member that should be handled there should be first moved out from this grab bag to a separate property.
        
        **since**
        
            LibreOffice 4.3
        """
        ...

    @property
    @abstractmethod
    def CharKeepTogether(self) -> bool:
        """
        This optional property marks a range of characters to prevent it from being broken into two lines.
        
        A line break is applied before the range of characters if the layout makes a break necessary within the range.
        """
        ...

    @property
    @abstractmethod
    def CharKerning(self) -> int:
        """
        This optional property contains the value of the kerning of the characters.
        """
        ...

    @property
    @abstractmethod
    def CharLeftBorder(self) -> BorderLine2_af200b28:
        """
        This property contains the left border of the object.
        
        **since**
        
            LibreOffice 4.2
        """
        ...

    @property
    @abstractmethod
    def CharLeftBorderDistance(self) -> int:
        """
        This property contains the distance from the left border to the object.
        
        **since**
        
            LibreOffice 4.2
        """
        ...

    @property
    @abstractmethod
    def CharLocale(self) -> Locale_70d308fa:
        """
        This property contains the value of the locale.
        """
        ...

    @property
    @abstractmethod
    def CharNoHyphenation(self) -> bool:
        """
        This optional property determines if the word can be hyphenated at the character by automatic hyphenation.
        
        Setting to true will disable hyphenation enabled by ParaIsHyphenation.
        
        Note: implemented since LibreOffice 24.2.
        """
        ...

    @property
    @abstractmethod
    def CharNoLineBreak(self) -> bool:
        """
        This optional property marks a range of characters to ignore a line break in this area.
        
        A line break is applied behind the range of characters if the layout makes a break necessary within the range. That means that the text may go through the border.
        """
        ...

    @property
    @abstractmethod
    def CharPosture(self) -> FontSlantProto:
        """
        This property contains the value of the posture of the document.
        """
        ...

    @property
    @abstractmethod
    def CharRelief(self) -> int:
        """
        This optional property contains the relief style of the characters.
        """
        ...

    @property
    @abstractmethod
    def CharRightBorder(self) -> BorderLine2_af200b28:
        """
        This property contains the right border of the object.
        
        **since**
        
            LibreOffice 4.2
        """
        ...

    @property
    @abstractmethod
    def CharRightBorderDistance(self) -> int:
        """
        This property contains the distance from the right border to the object.
        
        **since**
        
            LibreOffice 4.2
        """
        ...

    @property
    @abstractmethod
    def CharRotation(self) -> int:
        """
        This optional property determines the rotation of a character in tenths of a degree.
        
        Depending on the implementation only certain values may be allowed.
        """
        ...

    @property
    @abstractmethod
    def CharRotationIsFitToLine(self) -> bool:
        """
        This optional property determines whether the text formatting tries to fit rotated text into the surrounded line height.
        """
        ...

    @property
    @abstractmethod
    def CharScaleWidth(self) -> int:
        """
        This optional property determines the percentage value for scaling the width of characters.
        
        The value refers to the original width which is denoted by 100, and it has to be greater than 0.
        """
        ...

    @property
    @abstractmethod
    def CharShadingValue(self) -> int:
        """
        This optional property contains the text shading value.
        """
        ...

    @property
    @abstractmethod
    def CharShadowFormat(self) -> ShadowFormat_bb840bdf:
        """
        Determines the type, color, and width of the shadow.
        
        **since**
        
            LibreOffice 4.2
        """
        ...

    @property
    @abstractmethod
    def CharShadowed(self) -> bool:
        """
        This optional property specifies if the characters are formatted and displayed with a shadow effect.
        """
        ...

    @property
    @abstractmethod
    def CharStrikeout(self) -> int:
        """
        This property determines the type of the strike out of the character.
        """
        ...

    @property
    @abstractmethod
    def CharStyleName(self) -> str:
        """
        This optional property specifies the name of the style of the font.
        """
        ...

    @property
    @abstractmethod
    def CharStyleNames(self) -> typing.Tuple[str, ...]:
        """
        This optional property specifies the names of the all styles applied to the font.
        
        It is not guaranteed that the order in the sequence reflects the order of the evaluation of the character style attributes.
        
        **since**
        
            OOo 1.1.2
        """
        ...

    @property
    @abstractmethod
    def CharTopBorder(self) -> BorderLine2_af200b28:
        """
        This property contains the top border of the object.
        
        **since**
        
            LibreOffice 4.2
        """
        ...

    @property
    @abstractmethod
    def CharTopBorderDistance(self) -> int:
        """
        This property contains the distance from the top border to the object.
        
        **since**
        
            LibreOffice 4.2
        """
        ...

    @property
    @abstractmethod
    def CharTransparence(self) -> int:
        """
        This is the transparency of the character text.
        
        The value 100 means entirely transparent, while 0 means not transparent at all.
        
        **since**
        
            LibreOffice 7.0
        """
        ...

    @property
    @abstractmethod
    def CharUnderline(self) -> int:
        """
        This property contains the value for the character underline.
        """
        ...

    @property
    @abstractmethod
    def CharUnderlineColor(self) -> Color_68e908c5:
        """
        This property contains the color of the underline for the characters.
        """
        ...

    @property
    @abstractmethod
    def CharUnderlineHasColor(self) -> bool:
        """
        This property specifies if the property CharUnderlineColor is used for an underline.
        """
        ...

    @property
    @abstractmethod
    def CharWeight(self) -> float:
        """
        This property contains the value of the font weight.
        """
        ...

    @property
    @abstractmethod
    def CharWordMode(self) -> bool:
        """
        If this property is TRUE, the underline and strike-through properties are not applied to white spaces.
        """
        ...

    @property
    @abstractmethod
    def HyperLinkName(self) -> str:
        """
        This optional property contains the name of the hyperlink.
        """
        ...

    @property
    @abstractmethod
    def HyperLinkTarget(self) -> str:
        """
        This optional property contains the name of the target for a hyperlink.
        """
        ...

    @property
    @abstractmethod
    def HyperLinkURL(self) -> str:
        """
        This optional property contains the URL of a hyperlink.
        """
        ...

    @property
    @abstractmethod
    def RubyAdjust(self) -> int:
        """
        This optional property determines the adjustment of the ruby .
        """
        ...

    @property
    @abstractmethod
    def RubyCharStyleName(self) -> str:
        """
        This optional property contains the name of the character style that is applied to RubyText.
        """
        ...

    @property
    @abstractmethod
    def RubyIsAbove(self) -> bool:
        """
        This optional property determines whether the ruby text is printed above/left or below/right of the text.
        
        This property is replaced by RubyPosition.
        """
        ...

    @property
    @abstractmethod
    def RubyPosition(self) -> int:
        """
        This optional property determines the position of the ruby .
        
        **since**
        
            LibreOffice 6.1
        """
        ...

    @property
    @abstractmethod
    def RubyText(self) -> str:
        """
        This optional property contains the text that is set as ruby.
        """
        ...

    @property
    @abstractmethod
    def TextUserDefinedAttributes(self) -> XNameContainer_cb90e47:
        """
        This property stores XML attributes.
        
        They will be saved to and restored from automatic styles inside XML files.
        """
        ...

    @property
    @abstractmethod
    def UnvisitedCharStyleName(self) -> str:
        """
        This optional property contains the character style name for unvisited hyperlinks.
        """
        ...

    @property
    @abstractmethod
    def VisitedCharStyleName(self) -> str:
        """
        This optional property contains the character style name for visited hyperlinks.
        """
        ...


__all__ = ['CharacterProperties']