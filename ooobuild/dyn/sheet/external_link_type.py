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
# Namespace: com.sun.star.sheet
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

    class ExternalLinkType(metaclass=UnoConstMeta, type_name="com.sun.star.sheet.ExternalLinkType", name_space="com.sun.star.sheet"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.sheet.ExternalLinkType``"""
        pass

    class ExternalLinkTypeEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.sheet.ExternalLinkType", name_space="com.sun.star.sheet"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.sheet.ExternalLinkType`` as Enum values"""
        pass

else:
    if TYPE_CHECKING:
        from com.sun.star.sheet import ExternalLinkType as ExternalLinkType
    else:
        # keep document generators happy
        from ...lo.sheet.external_link_type import ExternalLinkType as ExternalLinkType

    class ExternalLinkTypeEnum(IntEnum):
        """
        Enum of Const Class ExternalLinkType

        Constants designating the link type in ExternalLinkInfo, used with FormulaParser.ExternalLinks.
        
        **since**
        
            OOo 3.1
        """
        UNKNOWN = ExternalLinkType.UNKNOWN
        """
        Unknown element type.
        """
        DOCUMENT = ExternalLinkType.DOCUMENT
        """
        URL of an external document.
        """
        DDE = ExternalLinkType.DDE
        """
        DDE link.
        """
        SELF = ExternalLinkType.SELF
        """
        Reference to the own document.
        """
        SPECIAL = ExternalLinkType.SPECIAL
        """
        For special use cases.
        
        Behaviour is dependent on the implementation of the formula parser.
        """

__all__ = ['ExternalLinkType', 'ExternalLinkTypeEnum']
