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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.sdbcx
import uno
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    # document generators will most likely not see this.
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class CheckOption(metaclass=UnoConstMeta, type_name="com.sun.star.sdbcx.CheckOption", name_space="com.sun.star.sdbcx"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.sdbcx.CheckOption``"""
        pass

    class CheckOptionEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.sdbcx.CheckOption", name_space="com.sun.star.sdbcx"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.sdbcx.CheckOption`` as Enum values"""
        pass

else:
    if TYPE_CHECKING:
        from com.sun.star.sdbcx import CheckOption as CheckOption
    else:
        # keep document generators happy
        from ...lo.sdbcx.check_option import CheckOption as CheckOption

    class CheckOptionEnum(IntEnum):
        """
        Enum of Const Class CheckOption

        determines the check option for a view.
        """
        NONE = CheckOption.NONE
        """
        indicates that no value checking is applied during updates of view data.
        """
        CASCADE = CheckOption.CASCADE
        """
        indicates that the value checking is applied for the view and all base views.
        """
        LOCAL = CheckOption.LOCAL
        """
        indicates that the value checking is applied only for the view.
        """

__all__ = ['CheckOption', 'CheckOptionEnum']
