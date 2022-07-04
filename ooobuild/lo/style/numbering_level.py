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
from abc import abstractproperty, ABC
if typing.TYPE_CHECKING:
    from ..awt.x_bitmap import XBitmap as XBitmap_70cd0909

class NumberingLevel(ABC):
    """
    Service Class

    These properties describe the numbering of a paragraph.
    
    NumberType determines the type of the numbering symbol. Depending on this setting, some of the following values will be ignored.
    
    **since**
    
        LibreOffice 6.1

    See Also:
        `API NumberingLevel <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1style_1_1NumberingLevel.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.style'
    __ooo_full_ns__: str = 'com.sun.star.style.NumberingLevel'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def BulletFontName(self) -> str:
        """
        This is the name of the font that is used for the bullet.
        """
        ...

    @abstractproperty
    def BulletId(self) -> int:
        """
        The bullet symbol with this code in the assigned font is used.
        """
        ...

    @abstractproperty
    def CharStyleName(self) -> str:
        """
        This is the name of the character style that is used for the symbol(s).
        """
        ...

    @abstractproperty
    def GraphicBitmap(self) -> 'XBitmap_70cd0909':
        """
        This is the graphic bitmap to use as a symbol.
        
        **since**
        
            LibreOffice 6.1
        """
        ...

    @abstractproperty
    def GraphicURL(self) -> str:
        """
        This is the URL of a graphic file to use as a symbol.
        
        Note the new behaviour since it this was deprecated: This property can only be set and only external URLs are supported (no more vnd.sun.star.GraphicObject scheme). When an URL is set, then it will load the graphic and set the GraphicBitmap property.
        """
        ...

    @abstractproperty
    def ListFormat(self) -> str:
        """
        Format string used to generate actual numbering.
        
        It contains placeholders (like %1%, %2%, etc) where corresponding level numberings are inserted.
        
        This is more flexible way to provide multilevel numbering with complex format string. This property is a replacement for Prefix and Suffix: if ListFormat is provided, they are not used anymore.
        
        Example: ListFormat \"(%1% %2%.%3%)\" can be resolved to numbering in actual multilevel list like \"(4 1.3)\".
        
        **since**
        
            LibreOffice 7.2
        """
        ...

    @abstractproperty
    def NumberingType(self) -> int:
        """
        specifies the type of numbering.
        """
        ...

    @abstractproperty
    def ParentNumbering(self) -> int:
        """
        specifies the number of higher numbering levels that are included in the representation of the current number.
        """
        ...

    @abstractproperty
    def Prefix(self) -> str:
        """
        This prefix is inserted in front of the numbering symbol(s).
        """
        ...

    @abstractproperty
    def StartWith(self) -> int:
        """
        This specifies the start value for the numbering.
        """
        ...

    @abstractproperty
    def Suffix(self) -> str:
        """
        This suffix is inserted after the numbering symbol(s).
        """
        ...



__all__ = ['NumberingLevel']

