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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.xml.sax
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

    class FastToken(metaclass=UnoConstMeta, type_name="com.sun.star.xml.sax.FastToken", name_space="com.sun.star.xml.sax"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.xml.sax.FastToken``"""
        pass

    class FastTokenEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.xml.sax.FastToken", name_space="com.sun.star.xml.sax"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.xml.sax.FastToken`` as Enum values"""
        pass

else:
    if TYPE_CHECKING:
        from com.sun.star.xml.sax import FastToken as FastToken
    else:
        # keep document generators happy
        from ....lo.xml.sax.fast_token import FastToken as FastToken

    class FastTokenEnum(IntEnum):
        """
        Enum of Const Class FastToken

        """
        DONTKNOW = FastToken.DONTKNOW
        """
        specifies an unknown token.
        """
        NAMESPACE = FastToken.NAMESPACE
        """
        specifies the first namespace token
        """

__all__ = ['FastToken', 'FastTokenEnum']
