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
# Namespace: com.sun.star.graphic
from __future__ import annotations
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_graphic import XGraphic as XGraphic_a4da0afc

class XGraphicTransformer(XInterface_8f010a43):
    """
    This interface is allowing to transform a XGraphic.
    
    To transform a XGraphic, just the corresponding method has to be used, a new XGraphic instance will be returned

    See Also:
        `API XGraphicTransformer <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1graphic_1_1XGraphicTransformer.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.graphic'
    __ooo_full_ns__: str = 'com.sun.star.graphic.XGraphicTransformer'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.graphic.XGraphicTransformer'

    @abstractmethod
    def applyBrightnessContrast(self, In: XGraphic_a4da0afc, brightness: int, contrast: int, mso: bool) -> XGraphic_a4da0afc:
        """
        changes brightness/contrast

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    @abstractmethod
    def applyDuotone(self, In: XGraphic_a4da0afc, ColorOne: int, ColorTwo: int) -> XGraphic_a4da0afc:
        """
        applies Duotone effect

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    @abstractmethod
    def colorChange(self, In: XGraphic_a4da0afc, ColorFrom: int, tolerance: int, ColorTo: int, AlphaTo: int) -> XGraphic_a4da0afc:
        """
        transforms a Graphic

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...

__all__ = ['XGraphicTransformer']

