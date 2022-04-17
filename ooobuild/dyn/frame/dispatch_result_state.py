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
# Namespace: com.sun.star.frame
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.frame import DispatchResultState as DispatchResultState
    if hasattr(DispatchResultState, '_constants') and isinstance(DispatchResultState._constants, dict):
        DispatchResultState._constants['__ooo_ns__'] = 'com.sun.star.frame'
        DispatchResultState._constants['__ooo_full_ns__'] = 'com.sun.star.frame.DispatchResultState'
        DispatchResultState._constants['__ooo_type_name__'] = 'const'
    def build_enum():
        global DispatchResultStateEnum
        ls = [f for f in dir(DispatchResultState) if not callable(getattr(DispatchResultState, f)) and not f.startswith('__')]
        _dict = {}
        for name in ls:
            _dict[name] = getattr(DispatchResultState, name)
        DispatchResultStateEnum = IntEnum('DispatchResultStateEnum', _dict)
    build_enum()
else:
    from ...lo.frame.dispatch_result_state import DispatchResultState as DispatchResultState

    class DispatchResultStateEnum(IntEnum):
        """
        Enum of Const Class DispatchResultState

        possible values for DispatchResultEvent
        """
        FAILURE = DispatchResultState.FAILURE
        """
        indicates: dispatch failed
        """
        SUCCESS = DispatchResultState.SUCCESS
        """
        indicates: dispatch was successful
        """
        DONTKNOW = DispatchResultState.DONTKNOW
        """
        indicates: result isn't defined
        """

__all__ = ['DispatchResultState', 'DispatchResultStateEnum']