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
# Namespace: com.sun.star.text.fieldmaster
from __future__ import annotations
import typing
from ..text_field_master import TextFieldMaster as TextFieldMaster_d6410cc2
if typing.TYPE_CHECKING:
    from ...beans.property_values import PropertyValues as PropertyValues_d6470ce6
    from ...lang.locale import Locale as Locale_70d308fa

class Bibliography(TextFieldMaster_d6410cc2):
    """
    Service Class

    specifies service of a Bibliography field master.

    See Also:
        `API Bibliography <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1text_1_1fieldmaster_1_1Bibliography.html>`_
    """
    @property
    def BracketAfter(self) -> str:
        """
        determines the closing bracket used to display the bibliography text fields.
        """
        ...
    @BracketAfter.setter
    def BracketAfter(self, value: str) -> None:
        ...
    @property
    def BracketBefore(self) -> str:
        """
        determines the opening bracket used to display the bibliography text fields.
        """
        ...
    @BracketBefore.setter
    def BracketBefore(self, value: str) -> None:
        ...
    @property
    def IsNumberEntries(self) -> bool:
        """
        determines whether the bibliography text fields are numbered.
        
        If FALSE the short name of the bibliography entry is displayed instead.
        """
        ...
    @IsNumberEntries.setter
    def IsNumberEntries(self, value: bool) -> None:
        ...
    @property
    def IsSortByPosition(self) -> bool:
        """
        determines whether the bibliography entries in a bibliography index are sorted by the document position.
        
        If FALSE the SortKey property determines the sorting of the entries.
        """
        ...
    @IsSortByPosition.setter
    def IsSortByPosition(self, value: bool) -> None:
        ...
    @property
    def Locale(self) -> Locale_70d308fa:
        """
        contains the locale of the field master
        """
        ...
    @Locale.setter
    def Locale(self, value: Locale_70d308fa) -> None:
        ...
    @property
    def SortAlgorithm(self) -> str:
        """
        contains the name of the sort algorithm that is used to sort the text fields.
        """
        ...
    @SortAlgorithm.setter
    def SortAlgorithm(self, value: str) -> None:
        ...
    @property
    def SortKeys(self) -> typing.Tuple[PropertyValues_d6470ce6, ...]:
        """
        determines the sorting of the bibliography entries in a bibliography index.
        
        This property is used if the property IsSortByPosition is not set. Each contained element of the sequence is a sequence of the following two properties:
        """
        ...
    @SortKeys.setter
    def SortKeys(self, value: typing.Tuple[PropertyValues_d6470ce6, ...]) -> None:
        ...

