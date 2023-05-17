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
# Namespace: com.sun.star.i18n
import typing
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

import uno
from .x_text_conversion import XTextConversion as XTextConversion_cd640c6b
if typing.TYPE_CHECKING:
    from ..lang.locale import Locale as Locale_70d308fa


class XExtendedTextConversion(XTextConversion_cd640c6b):
    """
    This interface provides Text Conversion service.
    
    It is derived from com.sun.star.i18n.XTextConversion and provides a new conversion function containing position map (offset) between original and converted string.
    
    **since**
    
        OOo 2.0

    See Also:
        `API XExtendedTextConversion <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1i18n_1_1XExtendedTextConversion.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.i18n.XExtendedTextConversion']

    def getConversionWithOffset(self, aText: str, nStartPos: int, nLength: int, aLocale: 'Locale_70d308fa', nTextConversionType: int, nTextConversionOptions: int, rOffset: uno.ByteSequence) -> str:
        """
        The functionality of this method is same as com.sun.star.i18n.XTextConversion.getConversion(), except an additional output parameter rOffset.

        * ``rOffset`` is an out direction argument.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.lang.NoSupportException: ``NoSupportException``
        """
        ...


