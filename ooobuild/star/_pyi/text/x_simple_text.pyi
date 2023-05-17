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
import typing
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from .x_text_range import XTextRange as XTextRange_9a910ab7
if typing.TYPE_CHECKING:
    from .x_text_cursor import XTextCursor as XTextCursor_a60c0b48


class XSimpleText(XTextRange_9a910ab7):
    """
    is the main interface for a distinct text unit, i.e.
    
    the main text of a document, the text for headers and footers or for single cells of a table.

    See Also:
        `API XSimpleText <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1text_1_1XSimpleText.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.text.XSimpleText']

    def createTextCursor(self) -> 'XTextCursor_a60c0b48':
        """
        """
        ...
    def createTextCursorByRange(self, aTextPosition: 'XTextRange_9a910ab7') -> 'XTextCursor_a60c0b48':
        """
        The initial position is set to aTextPosition.
        """
        ...
    def insertControlCharacter(self, xRange: 'XTextRange_9a910ab7', nControlCharacter: int, bAbsorb: bool) -> None:
        """
        inserts a control character (like a paragraph break or a hard space) into the text.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    def insertString(self, xRange: 'XTextRange_9a910ab7', aString: str, bAbsorb: bool) -> None:
        """
        inserts a string of characters into the text.
        
        The string may contain the following white spaces:
        
        If the parameter bAbsorb() was TRUE the text range will contain the new inserted string, otherwise the range (and it's text) will remain unchanged.
        """
        ...


