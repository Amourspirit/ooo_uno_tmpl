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
    from ..beans.property_values import PropertyValues as PropertyValues_d6470ce6
    from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
    from .x_graphic import XGraphic as XGraphic_a4da0afc


class XGraphicProvider(XInterface_8f010a43):
    """
    This interface acts as the main interface to handle graphic content.
    
    It is used to load graphics, store graphics and to get information about unloaded graphics

    See Also:
        `API XGraphicProvider <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1graphic_1_1XGraphicProvider.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.graphic.XGraphicProvider'

    def queryGraphic(self, MediaProperties: PropertyValues_d6470ce6) -> XGraphic_a4da0afc:
        """
        Calling this method returns a XGraphic interface that holds the graphic content after loading the graphic.

        Raises:
            com.sun.star.io.IOException: ``IOException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
        ...
    def queryGraphicDescriptor(self, MediaProperties: PropertyValues_d6470ce6) -> XPropertySet_bc180bfa:
        """
        Calling this method returns a com.sun.star.beans.XPropertySet interface that gives access to the properties of the unloaded graphic.
        
        In most cases, this method will be used to query the mime type of the graphic and, in the case of pixel graphics, the resulting size after loading

        Raises:
            com.sun.star.io.IOException: ``IOException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
        ...
    def storeGraphic(self, Graphic: XGraphic_a4da0afc, MediaProperties: PropertyValues_d6470ce6) -> None:
        """
        Store the graphic content, represented through the XGraphic interface at the specified location.

        Raises:
            com.sun.star.io.IOException: ``IOException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
        ...


