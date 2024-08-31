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
from .x_document_index import XDocumentIndex as XDocumentIndex_c9330c5c
from ..util.x_refreshable import XRefreshable as XRefreshable_b0d60b81
if typing.TYPE_CHECKING:
    from ..container.x_index_replace import XIndexReplace as XIndexReplace_feed0dd7
    from ..graphic.x_graphic import XGraphic as XGraphic_a4da0afc
    from .x_text_columns import XTextColumns as XTextColumns_b17f0bab
    from .x_text_section import XTextSection as XTextSection_b1730b9f
    from ..util.color import Color as Color_68e908c5
    from com.sun.star.style.GraphicLocation import GraphicLocationProto  # type: ignore

class BaseIndex(XDocumentIndex_c9330c5c, XRefreshable_b0d60b81):
    """
    Service Class

    specifies the basic service of different indexes within a document.
    
    **since**
    
        LibreOffice 4.0

    See Also:
        `API BaseIndex <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1text_1_1BaseIndex.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.text'
    __ooo_full_ns__: str = 'com.sun.star.text.BaseIndex'
    __ooo_type_name__: str = 'service'

    @property
    @abstractmethod
    def BackColor(self) -> Color_68e908c5:
        """
        specifies the color of the background.
        """
        ...

    @property
    @abstractmethod
    def BackGraphic(self) -> XGraphic_a4da0afc:
        """
        contains the graphic object that is displayed as background graphic.
        
        **since**
        
            LibreOffice 6.1
        """
        ...

    @property
    @abstractmethod
    def BackGraphicFilter(self) -> str:
        """
        contains the name of the filter of the graphic file that is displayed as background graphic
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
        contains the URL of a graphic file that is displayed as background graphic
        
        Note the new behaviour since it this was deprecated: This property can only be set and only external URLs are supported (no more vnd.sun.star.GraphicObject scheme). When an URL is set, then it will load the graphic and set the BackGraphic property.
        """
        ...

    @property
    @abstractmethod
    def BackTransparent(self) -> bool:
        """
        If TRUE, the background color value in \"BackColor\" is not visible.
        """
        ...

    @property
    @abstractmethod
    def ContentSection(self) -> XTextSection_b1730b9f:
        """
        the text section containing the content of the index
        """
        ...

    @property
    @abstractmethod
    def CreateFromChapter(self) -> bool:
        """
        determines if the content of the document index is created from the complete document content or from the current chapter only.
        
        It is not available in the bibliography
        """
        ...

    @property
    @abstractmethod
    def HeaderSection(self) -> XTextSection_b1730b9f:
        """
        the text section containing the header of the index
        """
        ...

    @property
    @abstractmethod
    def IsProtected(self) -> bool:
        """
        determines if the index is protected.
        """
        ...

    @property
    @abstractmethod
    def LevelFormat(self) -> XIndexReplace_feed0dd7:
        """
        returns the interface of the level format of the index.
        
        The description of the format of the levels depends on the type of the document index.
        """
        ...

    @property
    @abstractmethod
    def ParaStyleHeading(self) -> str:
        """
        contains the name of the paragraph style that is applied to the heading.
        """
        ...

    @property
    @abstractmethod
    def ParaStyleLevel1(self) -> str:
        """
        contains the name of the paragraph style that is applied to the 1st level.
        """
        ...

    @property
    @abstractmethod
    def ParaStyleLevel10(self) -> str:
        """
        contains the name of the paragraph style that is applied to the 10th level.
        """
        ...

    @property
    @abstractmethod
    def ParaStyleLevel2(self) -> str:
        """
        contains the name of the paragraph style that is applied to the 2nd level.
        """
        ...

    @property
    @abstractmethod
    def ParaStyleLevel3(self) -> str:
        """
        contains the name of the paragraph style that is applied to the 3rd level.
        """
        ...

    @property
    @abstractmethod
    def ParaStyleLevel4(self) -> str:
        """
        contains the name of the paragraph style that is applied to the 4th level.
        """
        ...

    @property
    @abstractmethod
    def ParaStyleLevel5(self) -> str:
        """
        contains the name of the paragraph style that is applied to the 5th level.
        """
        ...

    @property
    @abstractmethod
    def ParaStyleLevel6(self) -> str:
        """
        contains the name of the paragraph style that is applied to the 6th level.
        """
        ...

    @property
    @abstractmethod
    def ParaStyleLevel7(self) -> str:
        """
        contains the name of the paragraph style that is applied to the 7th level.
        """
        ...

    @property
    @abstractmethod
    def ParaStyleLevel8(self) -> str:
        """
        contains the name of the paragraph style that is applied to the 8th level.
        """
        ...

    @property
    @abstractmethod
    def ParaStyleLevel9(self) -> str:
        """
        contains the name of the paragraph style that is applied to the 9th level.
        """
        ...

    @property
    @abstractmethod
    def ParaStyleSeparator(self) -> str:
        """
        contains the name of the paragraph style that is applied to the separator level.
        """
        ...

    @property
    @abstractmethod
    def TextColumns(self) -> XTextColumns_b17f0bab:
        """
        contains the column interface.
        """
        ...

    @property
    @abstractmethod
    def Title(self) -> str:
        """
        contains the title of the index.
        """
        ...


__all__ = ['BaseIndex']