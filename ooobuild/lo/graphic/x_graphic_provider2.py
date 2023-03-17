# coding: utf-8
#
# Copyright 2022 :Barry-Thomas-Paul: Moss
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
import typing
from abc import abstractmethod
from .x_graphic_provider import XGraphicProvider as XGraphicProvider_b5b0e47
if typing.TYPE_CHECKING:
    from ..beans.property_values import PropertyValues as PropertyValues_d6470ce6
    from .x_graphic import XGraphic as XGraphic_a4da0afc

class XGraphicProvider2(XGraphicProvider_b5b0e47):
    """
    This interface allows operations on multiple graphics with one method call.
    
    **since**
    
        LibreOffice 6.0

    See Also:
        `API XGraphicProvider2 <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1graphic_1_1XGraphicProvider2.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.graphic'
    __ooo_full_ns__: str = 'com.sun.star.graphic.XGraphicProvider2'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.graphic.XGraphicProvider2'

    @abstractmethod
    def queryGraphics(self, MediaPropertiesSeq: 'typing.Tuple[PropertyValues_d6470ce6, ...]') -> 'typing.Tuple[XGraphic_a4da0afc, ...]':
        """
        Calling this method returns XGraphic interfaces that hold loaded graphics.
        
        **since**
        
            LibreOffice 6.0

        Raises:
            com.sun.star.io.IOException: ``IOException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
        ...

__all__ = ['XGraphicProvider2']

