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
# Namespace: com.sun.star.text
from __future__ import annotations
import typing
from abc import abstractproperty, ABC
if typing.TYPE_CHECKING:
    from ..awt.font_descriptor import FontDescriptor as FontDescriptor_bc110c0a
    from ..awt.size import Size as Size_576707ef
    from ..awt.x_bitmap import XBitmap as XBitmap_70cd0909
    from ..util.color import Color as Color_68e908c5

class NumberingLevel(ABC):
    """
    Service Class

    provides access to a numbering level as part of the Numbering Rules.
    
    **since**
    
        LibreOffice 3.6

    See Also:
        `API NumberingLevel <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1text_1_1NumberingLevel.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.text'
    __ooo_full_ns__: str = 'com.sun.star.text.NumberingLevel'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def Adjust(self) -> int:
        """
        adjusts the numbering (HoriOrientation_LEFT/RIGHT/CENTER)
        """
        ...

    @abstractproperty
    def BulletChar(self) -> str:
        """
        contains the symbol in the given font.
        
        This is only valid if the numbering type is com.sun.star.style.NumberingType.CHAR_SPECIAL.
        """
        ...

    @abstractproperty
    def BulletColor(self) -> Color_68e908c5:
        """
        contains the color for the symbol.
        
        This is only valid if the numbering type is com.sun.star.style.NumberingType.CHAR_SPECIAL.
        """
        ...

    @abstractproperty
    def BulletFont(self) -> FontDescriptor_bc110c0a:
        """
        the font used to paint the bullet.
        """
        ...

    @abstractproperty
    def BulletFontName(self) -> str:
        """
        the name of the font for the symbol.
        
        This is only valid if the numbering type is com.sun.star.style.NumberingType.CHAR_SPECIAL.
        """
        ...

    @abstractproperty
    def BulletId(self) -> int:
        """
        the ID of the symbol in the given font.
        
        This is only valid if the numbering type is com.sun.star.style.NumberingType.CHAR_SPECIAL.
        """
        ...

    @abstractproperty
    def BulletRelSize(self) -> int:
        """
        contains the size of the symbol relative to the high of the paragraph.
        
        This is only valid if the numbering type is com.sun.star.style.NumberingType.CHAR_SPECIAL.
        """
        ...

    @abstractproperty
    def CharStyleName(self) -> str:
        """
        Name of the character style that is used for the numbering symbol.
        """
        ...

    @abstractproperty
    def FirstLineIndent(self) -> int:
        """
        additional line indent for the first text line
        """
        ...

    @abstractproperty
    def FirstLineOffset(self) -> int:
        """
        specifies the offset between the beginning of the first line and the beginning of the following lines of the paragraph.
        """
        ...

    @abstractproperty
    def GraphicBitmap(self) -> XBitmap_70cd0909:
        """
        the graphic file that is used as the numbering symbol.
        
        This is only valid if the numbering type is com.sun.star.style.NumberingType.BITMAP.
        """
        ...

    @abstractproperty
    def GraphicSize(self) -> Size_576707ef:
        """
        size of the graphic that is used as bullet.
        """
        ...

    @abstractproperty
    def GraphicURL(self) -> str:
        """
        the URL of the graphic file that is used as the numbering symbol.
        
        This is only valid if the numbering type is com.sun.star.style.NumberingType.BITMAP.
        
        Note the new behaviour since it this was deprecated: This property can only be set and only external URLs are supported (no more vnd.sun.star.GraphicObject scheme). When an URL is set, then it will load the bitmap and set the GraphicBitmap property.
        """
        ...

    @abstractproperty
    def HeadingStyleName(self) -> str:
        """
        contains the name of the paragraph style that is interpreted as the header of this level.
        
        It is only contained in the levels of chapter numbering rules.
        """
        ...

    @abstractproperty
    def IndentAt(self) -> int:
        """
        indentation of the text lines
        """
        ...

    @abstractproperty
    def LabelFollowedBy(self) -> int:
        """
        character following the list label
        """
        ...

    @abstractproperty
    def LeftMargin(self) -> int:
        """
        specifies the left margin of the numbering
        """
        ...

    @abstractproperty
    def ListtabStopPosition(self) -> int:
        """
        list tab position
        """
        ...

    @abstractproperty
    def NumberingType(self) -> int:
        """
        specifies the type of numbering.
        """
        ...

    @abstractproperty
    def ParagraphStyleName(self) -> str:
        """
        contains the name of the paragraph style that should use this numbering.
        
        This is ignored for chapter numbering rules, use HeadingStyleName.
        
        **since**
        
            LibreOffice 3.6
        """
        ...

    @abstractproperty
    def ParentNumbering(self) -> int:
        """
        number of upper levels that are included in the current numbering symbol.
        """
        ...

    @abstractproperty
    def PositionAndSpaceMode(self) -> int:
        """
        position and space mode
        """
        ...

    @abstractproperty
    def Prefix(self) -> str:
        """
        the prefix of the numbering symbol.
        """
        ...

    @abstractproperty
    def StartWith(self) -> int:
        """
        specifies the start value for the numbering.
        
        This property is only valid if the numbering type is not com.sun.star.style.NumberingType.BITMAP or com.sun.star.style.NumberingType.CHAR_SPECIAL.
        """
        ...

    @abstractproperty
    def Suffix(self) -> str:
        """
        the suffix of the numbering symbol.
        """
        ...

    @abstractproperty
    def SymbolTextDistance(self) -> int:
        """
        specifies the distance between the numbering symbol and the text of the paragraph.
        """
        ...

    @abstractproperty
    def VertOrient(self) -> int:
        """
        contains the vertical orientation of a graphic.
        
        It is set using com.sun.star.text.VertOrientation.
        """
        ...


__all__ = ['NumberingLevel']

