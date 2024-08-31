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
# Namespace: com.sun.star.sheet
from __future__ import annotations
from abc import abstractproperty
from .x_condition_entry import XConditionEntry as XConditionEntry_e2340d32

class DateCondition(XConditionEntry_e2340d32):
    """
    Service Class


    See Also:
        `API DateCondition <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sheet_1_1DateCondition.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.DateCondition'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def DateType(self) -> int:
        """
        See com.sun.star.sheet.DateType for possible values.
        """
        ...

    @abstractproperty
    def StyleName(self) -> str:
        """
        """
        ...


__all__ = ['DateCondition']

