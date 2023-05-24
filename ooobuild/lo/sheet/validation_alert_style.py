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
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.sheet
# Libre Office Version: 7.4
from typing import cast
from enum import Enum
from com.sun.star.sheet.ValidationAlertStyle import ValidationAlertStyleProto

class ValidationAlertStyle(Enum):
    """
    Enum Class


    See Also:
        `API ValidationAlertStyle <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1sheet.html#aecf58149730f4c8c5c18c70f3c7c5db7>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.ValidationAlertStyle'
    __ooo_type_name__: str = 'enum'

    @property
    def typeName(self) -> str:
        return 'com.sun.star.sheet.ValidationAlertStyle'

    INFO = cast(ValidationAlertStyleProto, 'INFO')
    """
    information message is shown and the user is asked whether the change will be accepted (defaulted to \"Yes\").
    """
    MACRO = cast(ValidationAlertStyleProto, 'MACRO')
    """
    macro is executed.
    """
    STOP = cast(ValidationAlertStyleProto, 'STOP')
    """
    error message is shown and the change is rejected.
    """
    WARNING = cast(ValidationAlertStyleProto, 'WARNING')
    """
    warning message is shown and the user is asked whether the change will be accepted (defaulted to \"No\").
    """

__all__ = ['ValidationAlertStyle']

