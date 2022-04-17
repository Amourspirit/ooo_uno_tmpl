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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.system
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.system import SystemShellExecuteFlags as SystemShellExecuteFlags
    if hasattr(SystemShellExecuteFlags, '_constants') and isinstance(SystemShellExecuteFlags._constants, dict):
        SystemShellExecuteFlags._constants['__ooo_ns__'] = 'com.sun.star.system'
        SystemShellExecuteFlags._constants['__ooo_full_ns__'] = 'com.sun.star.system.SystemShellExecuteFlags'
        SystemShellExecuteFlags._constants['__ooo_type_name__'] = 'const'
    def build_enum():
        global SystemShellExecuteFlagsEnum
        ls = [f for f in dir(SystemShellExecuteFlags) if not callable(getattr(SystemShellExecuteFlags, f)) and not f.startswith('__')]
        _dict = {}
        for name in ls:
            _dict[name] = getattr(SystemShellExecuteFlags, name)
        SystemShellExecuteFlagsEnum = IntEnum('SystemShellExecuteFlagsEnum', _dict)
    build_enum()
else:
    from ...lo.system.system_shell_execute_flags import SystemShellExecuteFlags as SystemShellExecuteFlags

    class SystemShellExecuteFlagsEnum(IntEnum):
        """
        Enum of Const Class SystemShellExecuteFlags

        Different settings for the SystemShellExecute service.
        
        **since**
        
            LibreOffice 3.6
        """
        DEFAULTS = SystemShellExecuteFlags.DEFAULTS
        """
        Uses the default settings for executing commands.
        """
        NO_SYSTEM_ERROR_MESSAGE = SystemShellExecuteFlags.NO_SYSTEM_ERROR_MESSAGE
        """
        Prevents the display of system error message boxes if the method com.sun.star.system.XSystemShellExecute.execute() fails.
        """
        URIS_ONLY = SystemShellExecuteFlags.URIS_ONLY
        """
        Only allows opening of absolute URI references.
        
        **since**
        
            LibreOffice 3.6
        """

__all__ = ['SystemShellExecuteFlags', 'SystemShellExecuteFlagsEnum']