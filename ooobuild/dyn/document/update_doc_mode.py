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
# Libre Office Version: 7.2
# Namespace: com.sun.star.document
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class UpdateDocMode(metaclass=UnoConstMeta, type_name="com.sun.star.document.UpdateDocMode", name_space="com.sun.star.document"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.document.UpdateDocMode``"""
        pass

    class UpdateDocModeEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.document.UpdateDocMode", name_space="com.sun.star.document"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.document.UpdateDocMode`` as Enum values"""
        pass

else:
    from ...lo.document.update_doc_mode import UpdateDocMode as UpdateDocMode

    class UpdateDocModeEnum(IntEnum):
        """
        Enum of Const Class UpdateDocMode

        Specify the way a document can be updated.
        
        **since**
        
            OOo 1.1.2
        """
        NO_UPDATE = UpdateDocMode.NO_UPDATE
        """
        Do not update document.
        """
        QUIET_UPDATE = UpdateDocMode.QUIET_UPDATE
        """
        Update document if it does not require a dialog.
        
        Otherwise do not update. For example a link to a database can require a dialog to get password for an update.
        """
        ACCORDING_TO_CONFIG = UpdateDocMode.ACCORDING_TO_CONFIG
        """
        Produce update according to configuration settings.
        
        If there are no settings use dialog.
        """
        FULL_UPDATE = UpdateDocMode.FULL_UPDATE
        """
        Update document even if it does require a dialog.
        """

__all__ = ['UpdateDocMode', 'UpdateDocModeEnum']
