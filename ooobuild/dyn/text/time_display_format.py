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
# Namespace: com.sun.star.text
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

    class TimeDisplayFormat(metaclass=UnoConstMeta, type_name="com.sun.star.text.TimeDisplayFormat", name_space="com.sun.star.text"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.text.TimeDisplayFormat``"""
        pass

    class TimeDisplayFormatEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.text.TimeDisplayFormat", name_space="com.sun.star.text"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.text.TimeDisplayFormat`` as Enum values"""
        pass

else:
    if TYPE_CHECKING:
        from com.sun.star.text import TimeDisplayFormat as TimeDisplayFormat
    else:
        # keep document generators happy
        from ...lo.text.time_display_format import TimeDisplayFormat as TimeDisplayFormat

    class TimeDisplayFormatEnum(IntEnum):
        """
        Enum of Const Class TimeDisplayFormat

        These constants define how a time field is formatted before it is displayed.
        
        The format may also depend on the system or document locale.
        
        .. deprecated::
        
            Class is deprecated.
        """
        STANDARD = TimeDisplayFormat.STANDARD
        """
        the system standard
        """
        HHMM = TimeDisplayFormat.HHMM
        """
        13:49
        """
        HHMMSS = TimeDisplayFormat.HHMMSS
        """
        13:49:20
        """
        HHMMSS00 = TimeDisplayFormat.HHMMSS00
        """
        13:49:20.30
        """
        HHMMAMPM = TimeDisplayFormat.HHMMAMPM
        """
        01:49
        """
        HHMMSSAMPM = TimeDisplayFormat.HHMMSSAMPM
        """
        01:49:20
        """
        HHMMSS00AMPM = TimeDisplayFormat.HHMMSS00AMPM
        """
        01:49:20.30
        """

__all__ = ['TimeDisplayFormat', 'TimeDisplayFormatEnum']
