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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.text
from __future__ import annotations
import typing

import uno
from .x_text_markup import XTextMarkup as XTextMarkup_a5d60b3a
if typing.TYPE_CHECKING:
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73
    from ..lang.locale import Locale as Locale_70d308fa


class XFlatParagraph(XTextMarkup_a5d60b3a):
    """
    provides functionality to ...
    
    **since**
    
        OOo 3.0

    See Also:
        `API XFlatParagraph <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1text_1_1XFlatParagraph.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.text.XFlatParagraph'

    def changeAttributes(self, nPos: int, nLen: int, aAttributes: typing.Tuple[PropertyValue_c9610c73, ...]) -> None:
        """
        replace the attributes of the specific text with the given set of attributes.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    def changeText(self, nPos: int, nLen: int, NewText: str, aAttributes: typing.Tuple[PropertyValue_c9610c73, ...]) -> None:
        """
        replace the specific text with new text.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    def getLanguageOfText(self, nPos: int, nLen: int) -> Locale_70d308fa:
        """
        get the language of the specific text

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    def getLanguagePortions(self) -> uno.ByteSequence:
        """
        get a list of indexes that separate each two different languages
        """
        ...
    def getPrimaryLanguageOfText(self, nPos: int, nLen: int) -> Locale_70d308fa:
        """
        get the single most probable language of the specific text, especially after getLanguageOfText fails

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    def getText(self) -> str:
        """
        get the content of the paragraph
        """
        ...
    def isChecked(self, nType: int) -> bool:
        """
        returns whether the respective text node has already been processed
        """
        ...
    def isModified(self) -> bool:
        """
        check whether the content has been modified
        """
        ...
    def setChecked(self, nType: int, bVal: bool) -> None:
        """
        change the \"checked\" flag of the respective text node, i.e., mark the text node as \"processed\"
        """
        ...


