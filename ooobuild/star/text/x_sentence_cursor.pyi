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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.text
from __future__ import annotations
import typing

from .x_text_cursor import XTextCursor as XTextCursor_a60c0b48


class XSentenceCursor(XTextCursor_a60c0b48):
    """
    makes it possible to perform cursor movements through sentences.

    See Also:
        `API XSentenceCursor <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1text_1_1XSentenceCursor.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.text.XSentenceCursor'

    def gotoEndOfSentence(self, Expand: bool) -> bool:
        """
        moves the cursor to the end of the current sentence.
        """
        ...
    def gotoNextSentence(self, Expand: bool) -> bool:
        """
        moves the cursor to the start of the next sentence.
        """
        ...
    def gotoPreviousSentence(self, Expand: bool) -> bool:
        """
        moves the cursor to the start of the previous sentence.
        """
        ...
    def gotoStartOfSentence(self, Expand: bool) -> bool:
        """
        moves the cursor to the start of the current sentence.
        """
        ...
    def isEndOfSentence(self) -> bool:
        """
        determines if the cursor is positioned at the end of a sentence.
        """
        ...
    def isStartOfSentence(self) -> bool:
        """
        determines if the cursor is positioned at the start of a sentence.
        """
        ...


