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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.style
import typing
from abc import ABC
if typing.TYPE_CHECKING:
    from ..awt.font_slant import FontSlant as FontSlant_849509ed
    from ..lang.locale import Locale as Locale_70d308fa

class CharacterPropertiesAsian(ABC):
    """
    Service Class

    This is a set of properties to describe the style of characters in Asian texts.

    See Also:
        `API CharacterPropertiesAsian <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1style_1_1CharacterPropertiesAsian.html>`_
    """
    @property
    def CharFontCharSetAsian(self) -> int:
        """
        This property contains the text encoding of the font as specified in com.sun.star.awt.CharSet.
        """
        ...
    @CharFontCharSetAsian.setter
    def CharFontCharSetAsian(self, value: int) -> None:
        ...
    @property
    def CharFontFamilyAsian(self) -> int:
        """
        This property contains font family as specified in com.sun.star.awt.FontFamily .
        """
        ...
    @CharFontFamilyAsian.setter
    def CharFontFamilyAsian(self, value: int) -> None:
        ...
    @property
    def CharFontNameAsian(self) -> str:
        """
        This property specifies the name of the font style.
        
        It may contain more than one name separated by comma.
        """
        ...
    @CharFontNameAsian.setter
    def CharFontNameAsian(self, value: str) -> None:
        ...
    @property
    def CharFontPitchAsian(self) -> int:
        """
        This property contains the font pitch as specified in com.sun.star.awt.FontPitch.
        """
        ...
    @CharFontPitchAsian.setter
    def CharFontPitchAsian(self, value: int) -> None:
        ...
    @property
    def CharFontStyleNameAsian(self) -> str:
        """
        This property contains the name of the font style.
        
        This property may be empty.
        """
        ...
    @CharFontStyleNameAsian.setter
    def CharFontStyleNameAsian(self, value: str) -> None:
        ...
    @property
    def CharHeightAsian(self) -> float:
        """
        This value contains the height of the characters in point.
        """
        ...
    @CharHeightAsian.setter
    def CharHeightAsian(self, value: float) -> None:
        ...
    @property
    def CharLocaleAsian(self) -> 'Locale_70d308fa':
        """
        contains the value of the locale.
        """
        ...
    @CharLocaleAsian.setter
    def CharLocaleAsian(self, value: 'Locale_70d308fa') -> None:
        ...
    @property
    def CharPostureAsian(self) -> 'FontSlant_849509ed':
        """
        This property contains the value of the posture of the document.
        """
        ...
    @CharPostureAsian.setter
    def CharPostureAsian(self, value: 'FontSlant_849509ed') -> None:
        ...
    @property
    def CharWeightAsian(self) -> float:
        """
        This property contains the value of the font weight.
        """
        ...
    @CharWeightAsian.setter
    def CharWeightAsian(self, value: float) -> None:
        ...

