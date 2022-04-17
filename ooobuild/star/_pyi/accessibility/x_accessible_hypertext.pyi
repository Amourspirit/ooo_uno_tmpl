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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.accessibility
from typing_extensions import Literal
import typing
from .x_accessible_text import XAccessibleText as XAccessibleText_5b77105b
if typing.TYPE_CHECKING:
    from .x_accessible_hyperlink import XAccessibleHyperlink as XAccessibleHyperlink_b34c126c

class XAccessibleHypertext(XAccessibleText_5b77105b):
    """
    Implement this interface to expose the hypertext structure of a document.
    
    The XAccessibleHypertext interface is the main interface to expose hyperlinks in a document, typically a text document, that are used to reference other (parts of) documents. For supporting the XAccessibleHypertext.getLinkIndex() method of this interface and other character related methods of the XAccessibleHyperlink interface, it is necessary to also support the XAccessibleText interface.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API XAccessibleHypertext <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1accessibility_1_1XAccessibleHypertext.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.accessibility.XAccessibleHypertext']

    def getHyperLink(self, nLinkIndex: int) -> 'XAccessibleHyperlink_b34c126c':
        """
        Return the specified link.
        
        The returned XAccessibleHyperlink object encapsulates the hyperlink and provides several kinds of information describing it.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
    def getHyperLinkCount(self) -> int:
        """
        Returns the number of links and link groups contained within this hypertext document.
        """
    def getHyperLinkIndex(self, nCharIndex: int) -> int:
        """
        Returns the index of the hyperlink that is associated with this character index.
        
        In a HTML document this is the case when a <a href> tag spans (includes) the given character index.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """

