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
    from .number_format_code import NumberFormatCode as NumberFormatCode_d9a00c95
    from ..lang.locale import Locale as Locale_70d308fa

class XNumberFormatCode(XInterface_8f010a43):
    """
    Access number format codes defined in locale data.

    See Also:
        `API XNumberFormatCode <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1i18n_1_1XNumberFormatCode.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.i18n'
    __ooo_full_ns__: str = 'com.sun.star.i18n.XNumberFormatCode'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.i18n.XNumberFormatCode'

    @abstractmethod
    def getAllFormatCode(self, nFormatUsage: int, rLocale: 'Locale_70d308fa') -> 'typing.Tuple[NumberFormatCode_d9a00c95, ...]':
        """
        returns all format codes for a given nFormatUsage and locale.
        """
        ...
    @abstractmethod
    def getAllFormatCodes(self, rLocale: 'Locale_70d308fa') -> 'typing.Tuple[NumberFormatCode_d9a00c95, ...]':
        """
        returns all format codes for a given locale.
        """
        ...
    @abstractmethod
    def getDefault(self, nFormatType: int, nFormatUsage: int, rLocale: 'Locale_70d308fa') -> 'NumberFormatCode_d9a00c95':
        """
        returns the default number format code of a specific category (usage group) for a given locale and format length type.
        """
        ...
    @abstractmethod
    def getFormatCode(self, nFormatIndex: int, rLocale: 'Locale_70d308fa') -> 'NumberFormatCode_d9a00c95':
        """
        returns the number format pointed to by nFormatIndex for a given locale.
        """
        ...

__all__ = ['XNumberFormatCode']

