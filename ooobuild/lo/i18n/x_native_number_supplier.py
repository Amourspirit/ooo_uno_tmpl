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
# Namespace: com.sun.star.i18n
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .native_number_xml_attributes import NativeNumberXmlAttributes as NativeNumberXmlAttributes_5e4f1070
    from ..lang.locale import Locale as Locale_70d308fa

class XNativeNumberSupplier(XInterface_8f010a43):
    """
    Methods to convert between strings of ASCII Arabic digits and native numeral strings.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API XNativeNumberSupplier <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1i18n_1_1XNativeNumberSupplier.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.i18n'
    __ooo_full_ns__: str = 'com.sun.star.i18n.XNativeNumberSupplier'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.i18n.XNativeNumberSupplier'

    @abstractmethod
    def convertFromXmlAttributes(self, aAttr: 'NativeNumberXmlAttributes_5e4f1070') -> int:
        """
        Convert XML attributes to a NatNum value.
        """
        ...
    @abstractmethod
    def convertToXmlAttributes(self, aLocale: 'Locale_70d308fa', nNativeNumberMode: int) -> 'NativeNumberXmlAttributes_5e4f1070':
        """
        Convert a specific NatNum/Locale combination to attributes used in the XML file format.
        """
        ...
    @abstractmethod
    def getNativeNumberString(self, aNumberString: str, aLocale: 'Locale_70d308fa', nNativeNumberMode: int) -> str:
        """
        Returns native number string for given number string.
        """
        ...
    @abstractmethod
    def isValidNatNum(self, aLocale: 'Locale_70d308fa', nNativeNumberMode: int) -> bool:
        """
        Check if the NatNum is valid for the given locale.
        """
        ...

__all__ = ['XNativeNumberSupplier']

