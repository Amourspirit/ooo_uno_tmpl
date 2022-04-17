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
# Namespace: com.sun.star.sdb.application
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.sdb.application import CopyTableContinuation as CopyTableContinuation
    if hasattr(CopyTableContinuation, '_constants') and isinstance(CopyTableContinuation._constants, dict):
        CopyTableContinuation._constants['__ooo_ns__'] = 'com.sun.star.sdb.application'
        CopyTableContinuation._constants['__ooo_full_ns__'] = 'com.sun.star.sdb.application.CopyTableContinuation'
        CopyTableContinuation._constants['__ooo_type_name__'] = 'const'
    def build_enum():
        global CopyTableContinuationEnum
        ls = [f for f in dir(CopyTableContinuation) if not callable(getattr(CopyTableContinuation, f)) and not f.startswith('__')]
        _dict = {}
        for name in ls:
            _dict[name] = getattr(CopyTableContinuation, name)
        CopyTableContinuationEnum = IntEnum('CopyTableContinuationEnum', _dict)
    build_enum()
else:
    from ....lo.sdb.application.copy_table_continuation import CopyTableContinuation as CopyTableContinuation

    class CopyTableContinuationEnum(IntEnum):
        """
        Enum of Const Class CopyTableContinuation

        specifies the possible continuations when copying a table row via a CopyTableWizard failed.
        """
        Proceed = CopyTableContinuation.Proceed
        """
        indicates the error should be ignored, and copying should be continued.
        """
        CallNextHandler = CopyTableContinuation.CallNextHandler
        """
        is used to indicate the next registered XCopyTableListener should be called.
        """
        Cancel = CopyTableContinuation.Cancel
        """
        cancels the whole copying process
        """
        AskUser = CopyTableContinuation.AskUser
        """
        asks the user how the handle the error.
        
        The user can choose between ignoring the error and canceling the copy operation.
        """

__all__ = ['CopyTableContinuation', 'CopyTableContinuationEnum']
