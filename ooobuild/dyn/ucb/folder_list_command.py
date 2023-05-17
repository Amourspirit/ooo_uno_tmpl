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
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.ucb
# Libre Office Version: 7.4
from __future__ import annotations
import uno
from typing import Any, TYPE_CHECKING


if TYPE_CHECKING:

    from com.sun.star.ucb.FolderListCommand import GET as FOLDER_LIST_COMMAND_GET
    from com.sun.star.ucb.FolderListCommand import GET_SUBSCRIBED as FOLDER_LIST_COMMAND_GET_SUBSCRIBED
    from com.sun.star.ucb.FolderListCommand import SET as FOLDER_LIST_COMMAND_SET

    class FolderListCommand(uno.Enum):
        """
        Enum Class


        See Also:
            `API FolderListCommand <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1ucb.html#aa1260fc093737bd1d1134fba75333247>`_
        """

        def __init__(self, value: Any) -> None:
            super().__init__('com.sun.star.ucb.FolderListCommand', value)

        __ooo_ns__: str = 'com.sun.star.ucb'
        __ooo_full_ns__: str = 'com.sun.star.ucb.FolderListCommand'
        __ooo_type_name__: str = 'enum'

        GET: FolderListCommand = FOLDER_LIST_COMMAND_GET
        """
        Get a list of all folders.
        
        HTTP request method as defined in RFC 2616: Hypertext Transfer Protocol – HTTP/1.1
        """
        GET_SUBSCRIBED: FolderListCommand = FOLDER_LIST_COMMAND_GET_SUBSCRIBED
        """
        Get a list of subscribed folders.
        """
        SET: FolderListCommand = FOLDER_LIST_COMMAND_SET
        """
        Set a list of folders.
        """

else:

    from ooo.helper.enum_helper import UnoEnumMeta
    class FolderListCommand(metaclass=UnoEnumMeta, type_name="com.sun.star.ucb.FolderListCommand", name_space="com.sun.star.ucb"):
        """Dynamically created class that represents ``com.sun.star.ucb.FolderListCommand`` Enum. Class loosely mimics Enum"""
        pass

__all__ = ['FolderListCommand']
