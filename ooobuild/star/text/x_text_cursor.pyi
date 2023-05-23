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

from .x_text_range import XTextRange as XTextRange_9a910ab7


class XTextCursor(XTextRange_9a910ab7):
    """
    extends a text range by method to modify its position.

    See Also:
        `API XTextCursor <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1text_1_1XTextCursor.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.text.XTextCursor'

    def collapseToEnd(self) -> None:
        """
        sets the start of the position to the end.
        """
        ...
    def collapseToStart(self) -> None:
        """
        sets the end of the position to the start.
        """
        ...
    def goLeft(self, nCount: int, bExpand: bool) -> bool:
        """
        moves the cursor the specified number of characters to the left.
        
        Note: Even if the command was not completed successfully it may be completed partially. E.g. if it was required to move 5 characters but it is only possible to move 3 FALSE will be returned and the cursor moves only those 3 characters.
        """
        ...
    def goRight(self, nCount: int, bExpand: bool) -> bool:
        """
        moves the cursor the specified number of characters to the right.
        
        Note: Even if the command was not completed successfully it may be completed partially. E.g. if it was required to move 5 characters but it is only possible to move 3 FALSE will be returned and the cursor moves only those 3 characters.
        """
        ...
    def gotoEnd(self, bExpand: bool) -> None:
        """
        moves the cursor to the end of the text.
        """
        ...
    def gotoRange(self, xRange: 'XTextRange_9a910ab7', bExpand: bool) -> None:
        """
        moves or expands the cursor to a specified TextRange.
        """
        ...
    def gotoStart(self, bExpand: bool) -> None:
        """
        moves the cursor to the start of the text.
        """
        ...
    def isCollapsed(self) -> bool:
        """
        determines if the start and end positions are the same.
        """
        ...

