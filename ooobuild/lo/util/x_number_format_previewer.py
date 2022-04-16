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
# Libre Office Version: 7.3
# Namespace: com.sun.star.util
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..lang.locale import Locale as Locale_70d308fa
    from .color import Color as Color_68e908c5

class XNumberFormatPreviewer(XInterface_8f010a43):
    """
    represents a number formatter which can preview number formats without inserting them.

    See Also:
        `API XNumberFormatPreviewer <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1util_1_1XNumberFormatPreviewer.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.util'
    __ooo_full_ns__: str = 'com.sun.star.util.XNumberFormatPreviewer'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.util.XNumberFormatPreviewer'

    @abstractmethod
    def convertNumberToPreviewString(self, aFormat: str, fValue: float, nLocale: 'Locale_70d308fa', bAllowEnglish: bool) -> str:
        """
        formats a value using a format string, without inserting a number format into the list.

        Raises:
            com.sun.star.util.MalformedNumberFormatException: ``MalformedNumberFormatException``
        """
    @abstractmethod
    def queryPreviewColorForNumber(self, aFormat: str, fValue: float, nLocale: 'Locale_70d308fa', bAllowEnglish: bool, aDefaultColor: 'Color_68e908c5') -> 'Color_68e908c5':
        """
        returns the color which is to be used for a number.

        Raises:
            com.sun.star.util.MalformedNumberFormatException: ``MalformedNumberFormatException``
        """

__all__ = ['XNumberFormatPreviewer']

