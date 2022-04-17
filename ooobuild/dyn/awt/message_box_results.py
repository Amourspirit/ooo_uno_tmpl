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
# Namespace: com.sun.star.awt
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.awt import MessageBoxResults as MessageBoxResults
    if hasattr(MessageBoxResults, '_constants') and isinstance(MessageBoxResults._constants, dict):
        MessageBoxResults._constants['__ooo_ns__'] = 'com.sun.star.awt'
        MessageBoxResults._constants['__ooo_full_ns__'] = 'com.sun.star.awt.MessageBoxResults'
        MessageBoxResults._constants['__ooo_type_name__'] = 'const'
    def build_enum():
        global MessageBoxResultsEnum
        ls = [f for f in dir(MessageBoxResults) if not callable(getattr(MessageBoxResults, f)) and not f.startswith('__')]
        _dict = {}
        for name in ls:
            _dict[name] = getattr(MessageBoxResults, name)
        MessageBoxResultsEnum = IntEnum('MessageBoxResultsEnum', _dict)
    build_enum()
else:
    from ...lo.awt.message_box_results import MessageBoxResults as MessageBoxResults

    class MessageBoxResultsEnum(IntEnum):
        """
        Enum of Const Class MessageBoxResults

        These constants are used to specify a result of executing a XMessageBox.
        
        **since**
        
            LibreOffice 4.2
        """
        CANCEL = MessageBoxResults.CANCEL
        """
        The user canceled the XMessageBox, by pressing \"Cancel\" or \"Abort\" button.
        """
        OK = MessageBoxResults.OK
        """
        The user pressed the \"Ok\" button.
        """
        YES = MessageBoxResults.YES
        """
        The user pressed the \"Yes\" button.
        """
        NO = MessageBoxResults.NO
        """
        The user pressed the \"No\" button.
        """
        RETRY = MessageBoxResults.RETRY
        """
        The user pressed the \"Retry\" button.
        """
        IGNORE = MessageBoxResults.IGNORE
        """
        The user pressed the \"Ignore\" button.
        """

__all__ = ['MessageBoxResults', 'MessageBoxResultsEnum']