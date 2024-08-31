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
# Namespace: com.sun.star.system
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

    class SimpleMailClientFlags(metaclass=UnoConstMeta, type_name="com.sun.star.system.SimpleMailClientFlags", name_space="com.sun.star.system"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.system.SimpleMailClientFlags``"""
        pass

    class SimpleMailClientFlagsEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.system.SimpleMailClientFlags", name_space="com.sun.star.system"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.system.SimpleMailClientFlags`` as Enum values"""
        pass

else:
    if TYPE_CHECKING:
        from com.sun.star.system import SimpleMailClientFlags as SimpleMailClientFlags
    else:
        # keep document generators happy
        from ...lo.system.simple_mail_client_flags import SimpleMailClientFlags as SimpleMailClientFlags

    class SimpleMailClientFlagsEnum(IntEnum):
        """
        Enum of Const Class SimpleMailClientFlags

        These constants are used to specify how the SimpleMailClient Service should behave.
        """
        DEFAULTS = SimpleMailClientFlags.DEFAULTS
        """
        Uses the default settings when sending a mail, e.g.
        
        launches the current configured system mail client.
        """
        NO_USER_INTERFACE = SimpleMailClientFlags.NO_USER_INTERFACE
        """
        Does not show the current configured system mail client, but sends the mail without any further user interaction.
        
        If this flag is specified, a recipient address must have been specified for the given XSimpleMailMessage object given to the method com.sun.star.system.XSimpleMailClient.sendSimpleMailMessage().
        """
        NO_LOGON_DIALOG = SimpleMailClientFlags.NO_LOGON_DIALOG
        """
        No logon dialog should be displayed to prompt the user for logon information if necessary.
        
        When this flag is specified and the user needs to logon in order to send a simple mail message via the method com.sun.star.system.XSimpleMailClient.sendSimpleMailMessage(), an Exception will be thrown.
        """

__all__ = ['SimpleMailClientFlags', 'SimpleMailClientFlagsEnum']
