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
# Namespace: com.sun.star.view
import typing
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from ..uno.x_interface import XInterface as XInterface_8f010a43


class XLineCursor(XInterface_8f010a43):
    """
    makes it possible to move a cursor by lines within laid out text.

    See Also:
        `API XLineCursor <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1view_1_1XLineCursor.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.view.XLineCursor']

    def gotoEndOfLine(self, bExpand: bool) -> None:
        """
        moves the cursor to the end of the current line.
        """
        ...
    def gotoStartOfLine(self, bExpand: bool) -> None:
        """
        moves the cursor to the start of the current line.
        """
        ...
    def isAtEndOfLine(self) -> bool:
        """
        determines if the cursor is positioned at the end of a line.
        """
        ...
    def isAtStartOfLine(self) -> bool:
        """
        determines if the cursor is positioned at the start of a line.
        """
        ...


