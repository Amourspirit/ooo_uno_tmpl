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
# Namespace: com.sun.star.ucb
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.ucb import OpenMode as OpenMode
    if hasattr(OpenMode, '_constants') and isinstance(OpenMode._constants, dict):
        OpenMode._constants['__ooo_ns__'] = 'com.sun.star.ucb'
        OpenMode._constants['__ooo_full_ns__'] = 'com.sun.star.ucb.OpenMode'
        OpenMode._constants['__ooo_type_name__'] = 'const'
    def build_enum():
        global OpenModeEnum
        ls = [f for f in dir(OpenMode) if not callable(getattr(OpenMode, f)) and not f.startswith('__')]
        _dict = {}
        for name in ls:
            _dict[name] = getattr(OpenMode, name)
        OpenModeEnum = IntEnum('OpenModeEnum', _dict)
    build_enum()
else:
    from ...lo.ucb.open_mode import OpenMode as OpenMode

    class OpenModeEnum(IntEnum):
        """
        Enum of Const Class OpenMode

        These are the possible values for OpenCommandArgument.Mode.
        """
        ALL = OpenMode.ALL
        """
        open a folder, include all children in result set (documents and folders).
        """
        FOLDERS = OpenMode.FOLDERS
        """
        open a folder, include only children, that are folders, in result set.
        """
        DOCUMENTS = OpenMode.DOCUMENTS
        """
        open a folder, include only children, that are documents, in result set.
        """
        DOCUMENT = OpenMode.DOCUMENT
        """
        open a document.
        
        There are no special requirements for data access sharing.
        
        Note: There must be a data sink supplied in the OpenCommandArgument struct, if this value is set. This sink will be used by the content implementation to supply the document data.
        """
        DOCUMENT_SHARE_DENY_NONE = OpenMode.DOCUMENT_SHARE_DENY_NONE
        """
        open a document.
        
        Allow shared read and write access.
        
        Note: There must be a data sink supplied in the OpenCommandArgument struct, if this value is set. This sink will be used by the content implementation to supply the document data.
        """
        DOCUMENT_SHARE_DENY_WRITE = OpenMode.DOCUMENT_SHARE_DENY_WRITE
        """
        open a document.
        
        Deny shared write access.
        
        Note: There must be a data sink supplied in the OpenCommandArgument struct, if this value is set. This sink will be used by the content implementation to supply the document data.
        """

__all__ = ['OpenMode', 'OpenModeEnum']