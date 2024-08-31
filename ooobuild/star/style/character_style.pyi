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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.style
from __future__ import annotations
from .character_properties import CharacterProperties as CharacterProperties_1d4f0ef3
from .style import Style as Style_7336094a

class CharacterStyle(CharacterProperties_1d4f0ef3, Style_7336094a):
    """
    Service Class

    specifies a style sheet for characters within a com.sun.star.text.Text.

    See Also:
        `API CharacterStyle <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1style_1_1CharacterStyle.html>`_
    """
    @property
    def CharDiffHeight(self) -> float:
        """
        This value contains the character height as difference in point to the height of the character in the parent style.
        """
        ...
    @CharDiffHeight.setter
    def CharDiffHeight(self, value: float) -> None:
        ...
    @property
    def CharDiffHeightAsian(self) -> float:
        """
        This value contains the character height as difference in point to the height of the character in the parent style in Asian text.
        """
        ...
    @CharDiffHeightAsian.setter
    def CharDiffHeightAsian(self, value: float) -> None:
        ...
    @property
    def CharDiffHeightComplex(self) -> float:
        """
        This value contains the character height as difference in point to the height of the character in the parent style in complex text.
        """
        ...
    @CharDiffHeightComplex.setter
    def CharDiffHeightComplex(self, value: float) -> None:
        ...
    @property
    def CharPropHeight(self) -> int:
        """
        This value contains the character height as percentage value relative to the height of the character in the parent style.
        """
        ...
    @CharPropHeight.setter
    def CharPropHeight(self, value: int) -> None:
        ...
    @property
    def CharPropHeightAsian(self) -> int:
        """
        This value contains the character height as percentage value relative to the height of the character in the parent style in Asian text.
        """
        ...
    @CharPropHeightAsian.setter
    def CharPropHeightAsian(self, value: int) -> None:
        ...
    @property
    def CharPropHeightComplex(self) -> int:
        """
        This value contains the character height as percentage value relative to the height of the character in the parent style in complex text.
        """
        ...
    @CharPropHeightComplex.setter
    def CharPropHeightComplex(self, value: int) -> None:
        ...

