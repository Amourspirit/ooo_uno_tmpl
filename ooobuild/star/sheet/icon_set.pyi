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
# Namespace: com.sun.star.sheet
import typing
from .x_condition_entry import XConditionEntry as XConditionEntry_e2340d32
if typing.TYPE_CHECKING:
    from .x_icon_set_entry import XIconSetEntry as XIconSetEntry_c7620c40

class IconSet(XConditionEntry_e2340d32):
    """
    Service Class


    See Also:
        `API IconSet <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sheet_1_1IconSet.html>`_
    """
    @property
    def IconSetEntries(self) -> 'typing.Tuple[XIconSetEntry_c7620c40, ...]':
        """
        """
        ...
    @IconSetEntries.setter
    def IconSetEntries(self, value: 'typing.Tuple[XIconSetEntry_c7620c40, ...]') -> None:
        ...
    @property
    def Icons(self) -> int:
        """
        See com.sun.star.sheet.IconSetType for possible values.
        """
        ...
    @Icons.setter
    def Icons(self, value: int) -> None:
        ...
    @property
    def Reverse(self) -> bool:
        """
        """
        ...
    @Reverse.setter
    def Reverse(self, value: bool) -> None:
        ...
    @property
    def ShowValue(self) -> bool:
        """
        """
        ...
    @ShowValue.setter
    def ShowValue(self, value: bool) -> None:
        ...
