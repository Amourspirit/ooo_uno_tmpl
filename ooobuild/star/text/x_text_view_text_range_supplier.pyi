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

from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..awt.point import Point as Point_5fb2085e
    from .x_text_range import XTextRange as XTextRange_9a910ab7


class XTextViewTextRangeSupplier(XInterface_8f010a43):
    """
    supplies access to a document model position at a view-dependent pixel position.
    
    **since**
    
        LibreOffice 7.2

    See Also:
        `API XTextViewTextRangeSupplier <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1text_1_1XTextViewTextRangeSupplier.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.text.XTextViewTextRangeSupplier'

    def createTextRangeByPixelPosition(self, PixelPosition: Point_5fb2085e) -> XTextRange_9a910ab7:
        """
        creates the text range of the document model position at a view-dependent pixel position.
        
        Note that in case the model position is a graphic, then the model position of its anchor is returned.
        """
        ...


