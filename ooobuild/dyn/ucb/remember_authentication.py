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
# Namespace: com.sun.star.ucb
# Libre Office Version: 7.4
from __future__ import annotations
import uno
from typing import Any, TYPE_CHECKING


if TYPE_CHECKING:

    from com.sun.star.ucb.RememberAuthentication import NO as REMEMBER_AUTHENTICATION_NO
    from com.sun.star.ucb.RememberAuthentication import PERSISTENT as REMEMBER_AUTHENTICATION_PERSISTENT
    from com.sun.star.ucb.RememberAuthentication import SESSION as REMEMBER_AUTHENTICATION_SESSION

    class RememberAuthentication(uno.Enum):
        """
        Enum Class


        See Also:
            `API RememberAuthentication <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1ucb.html#a7b9847f348fd7f6a0fc461f821c08173>`_
        """

        def __init__(self, value: Any) -> None:
            super().__init__('com.sun.star.ucb.RememberAuthentication', value)

        __ooo_ns__: str = 'com.sun.star.ucb'
        __ooo_full_ns__: str = 'com.sun.star.ucb.RememberAuthentication'
        __ooo_type_name__: str = 'enum'

        NO: RememberAuthentication = REMEMBER_AUTHENTICATION_NO
        """
        Do not remember the authentication data (use it once and immediately forget about it).
        """
        PERSISTENT: RememberAuthentication = REMEMBER_AUTHENTICATION_PERSISTENT
        """
        Remember the authentication data \"forever\".
        """
        SESSION: RememberAuthentication = REMEMBER_AUTHENTICATION_SESSION
        """
        Remember the authentication data, but only until the end of the current session.
        """

else:

    from ooo.helper.enum_helper import UnoEnumMeta
    class RememberAuthentication(metaclass=UnoEnumMeta, type_name="com.sun.star.ucb.RememberAuthentication", name_space="com.sun.star.ucb"):
        """Dynamically created class that represents ``com.sun.star.ucb.RememberAuthentication`` Enum. Class loosely mimics Enum"""
        pass

__all__ = ['RememberAuthentication']
