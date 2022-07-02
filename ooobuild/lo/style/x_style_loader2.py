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
# Libre Office Version: 7.2
# Namespace: com.sun.star.style
import typing
from abc import abstractmethod
from .x_style_loader import XStyleLoader as XStyleLoader_be2a0bf9
if typing.TYPE_CHECKING:
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73
    from ..lang.x_component import XComponent as XComponent_98dc0ab5

class XStyleLoader2(XStyleLoader_be2a0bf9):
    """
    extends XStyleLoader interface to import styles from an already opened component.
    
    **since**
    
        LibreOffice 4.4

    See Also:
        `API XStyleLoader2 <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1style_1_1XStyleLoader2.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.style'
    __ooo_full_ns__: str = 'com.sun.star.style.XStyleLoader2'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.style.XStyleLoader2'

    @abstractmethod
    def loadStylesFromDocument(self, aSourceComponent: 'XComponent_98dc0ab5', aOptions: 'typing.Tuple[PropertyValue_c9610c73, ...]') -> None:
        """
        loads styles from a given document
        
        As the default, all supported style families are loaded and existing styles are overwritten.

        Raises:
            com.sun.star.io.IOException: ``IOException``
        """
        ...

__all__ = ['XStyleLoader2']

