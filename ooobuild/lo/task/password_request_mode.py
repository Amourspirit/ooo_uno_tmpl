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
# Namespace: com.sun.star.task
# Libre Office Version: 7.4
from __future__ import annotations
from typing import cast, TYPE_CHECKING
from enum import Enum
if TYPE_CHECKING:
    from com.sun.star.task.PasswordRequestMode import PasswordRequestModeProto

class PasswordRequestMode(Enum):
    """
    Enum Class


    See Also:
        `API PasswordRequestMode <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1task.html#a921a6f0fb0abf824f006cab79dbc54d0>`_
    """
    __ooo_ns__: str = 'com.sun.star.task'
    __ooo_full_ns__: str = 'com.sun.star.task.PasswordRequestMode'
    __ooo_type_name__: str = 'enum'

    @property
    def typeName(self) -> str:
        return 'com.sun.star.task.PasswordRequestMode'

    PASSWORD_CREATE = cast("PasswordRequestModeProto", 'PASSWORD_CREATE')
    """
    Password creation.
    """
    PASSWORD_ENTER = cast("PasswordRequestModeProto", 'PASSWORD_ENTER')
    """
    Ask for a password.
    """
    PASSWORD_REENTER = cast("PasswordRequestModeProto", 'PASSWORD_REENTER')
    """
    Wrong password was entered, ask again.
    """

__all__ = ['PasswordRequestMode']

