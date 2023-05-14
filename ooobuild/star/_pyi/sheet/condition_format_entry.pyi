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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.sheet
from .x_condition_entry import XConditionEntry as XConditionEntry_e2340d32

class ConditionFormatEntry(XConditionEntry_e2340d32):
    """
    Service Class


    See Also:
        `API ConditionFormatEntry <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sheet_1_1ConditionFormatEntry.html>`_
    """
    @property
    def Formula1(self) -> str:
        """
        """
        ...

    @Formula1.setter
    def Formula1(self, value: str) -> None:
        ...
    @property
    def Formula2(self) -> str:
        """
        """
        ...

    @Formula2.setter
    def Formula2(self, value: str) -> None:
        ...
    @property
    def Operator(self) -> int:
        """
        See com.sun.star.sheet.ConditionFormatOperator for valid values.
        """
        ...

    @Operator.setter
    def Operator(self, value: int) -> None:
        ...
    @property
    def StyleName(self) -> str:
        """
        """
        ...

    @StyleName.setter
    def StyleName(self, value: str) -> None:
        ...

