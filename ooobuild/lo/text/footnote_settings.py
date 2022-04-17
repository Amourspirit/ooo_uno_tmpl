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
# Namespace: com.sun.star.text
from abc import abstractproperty, ABC

class FootnoteSettings(ABC):
    """
    Service Class

    provides access to the settings of footnotes or endnotes in a (text) document.
    
    **since**
    
        OOo 2.0

    See Also:
        `API FootnoteSettings <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1text_1_1FootnoteSettings.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.text'
    __ooo_full_ns__: str = 'com.sun.star.text.FootnoteSettings'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def AnchorCharStyleName(self) -> str:
        """
        contains the name of the character style that is used for footnote/endnote anchor in the text.
        
        **since**
        
            OOo 2.0
        """

    @abstractproperty
    def BeginNotice(self) -> str:
        """
        contains the string at the restart of the footnote text after a break.
        
        For footnotes only.
        """

    @abstractproperty
    def CharStyleName(self) -> str:
        """
        contains the name of the character style that is used for the label in front of the footnote/endnote text.
        """

    @abstractproperty
    def EndNotice(self) -> str:
        """
        contains the string at the end of a footnote part in front of a break.
        
        For footnotes only.
        """

    @abstractproperty
    def FootnoteCounting(self) -> int:
        """
        contains the type of the counting of the footnote numbers.
        
        For footnotes only.
        """

    @abstractproperty
    def NumberingType(self) -> int:
        """
        contains the numbering type for the numbering of the footnotes/endnotes.
        """

    @abstractproperty
    def PageStyleName(self) -> str:
        """
        contains the page style that is used for the page that contains the footnote/endnote texts
        """

    @abstractproperty
    def ParaStyleName(self) -> str:
        """
        contains the paragraph style that is used for the footnote/endnote text.
        """

    @abstractproperty
    def PositionEndOfDoc(self) -> bool:
        """
        If TRUE, the footnote text is shown at the end of the document.
        
        For footnotes only.
        """

    @abstractproperty
    def Prefix(self) -> str:
        """
        contains the prefix for the footnote/endnote symbol.
        """

    @abstractproperty
    def StartAt(self) -> int:
        """
        contains the first number of the automatic numbering of footnotes/endnotes.
        """

    @abstractproperty
    def Suffix(self) -> str:
        """
        contains the suffix for the footnote/endnote symbol.
        """



__all__ = ['FootnoteSettings']
