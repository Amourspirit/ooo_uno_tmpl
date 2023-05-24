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
# Namespace: com.sun.star.graphic
from __future__ import annotations
import typing

from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73
    from .x_primitive2_d import XPrimitive2D as XPrimitive2D_d5730c6d
    from ..util.x_binary_data_container import XBinaryDataContainer as XBinaryDataContainer_19270ea0


class XPdfDecomposer(XInterface_8f010a43):
    """
    XPdfDecomposer interface.
    
    This renders a PDF data into a bitmap and returns it as a primitive.
    
    **since**
    
        LibreOffice 7.0

    See Also:
        `API XPdfDecomposer <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1graphic_1_1XPdfDecomposer.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.graphic.XPdfDecomposer'

    def getDecomposition(self, xDataContainer: XBinaryDataContainer_19270ea0, xDecompositionParameters: typing.Tuple[PropertyValue_c9610c73, ...]) -> typing.Tuple[XPrimitive2D_d5730c6d, ...]:
        """
        Retrieve decomposed list - in this case a bitmap with the rendered PDF.
        
        sal_Int32 PageIndex - which page to use
        """
        ...


