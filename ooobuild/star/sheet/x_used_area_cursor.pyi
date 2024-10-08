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
# Namespace: com.sun.star.sheet
from __future__ import annotations
import typing

from ..uno.x_interface import XInterface as XInterface_8f010a43


class XUsedAreaCursor(XInterface_8f010a43):
    """
    provides methods to find the used area of the entire sheet.
    
    The used area is the smallest cell range that contains all cells of the spreadsheet with any contents (values, text, formulas) or visible formatting (borders and background color).

    See Also:
        `API XUsedAreaCursor <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sheet_1_1XUsedAreaCursor.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.sheet.XUsedAreaCursor'

    def gotoEndOfUsedArea(self, bExpand: bool) -> None:
        """
        points the cursor to the end of the used area.
        """
        ...
    def gotoStartOfUsedArea(self, bExpand: bool) -> None:
        """
        points the cursor to the start of the used area.
        """
        ...


