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
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.ucb
# Libre Office Version: 2024.2
from __future__ import annotations
from enum import Enum


class FolderListCommand(Enum):
    """
    Enum Class


    See Also:
        `API FolderListCommand <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1ucb.html#aa1260fc093737bd1d1134fba75333247>`_
    """
    __ooo_ns__: str = "com.sun.star.ucb"
    __ooo_full_ns__: str = "com.sun.star.ucb.FolderListCommand"
    __ooo_type_name__: str = "enum"

    @property
    def typeName(self) -> str:
        return "com.sun.star.ucb.FolderListCommand"

    GET = "GET"
    """
    Get a list of all folders.
    
    HTTP request method as defined in RFC 2616: Hypertext Transfer Protocol – HTTP/1.1
    """
    GET_SUBSCRIBED = "GET_SUBSCRIBED"
    """
    Get a list of subscribed folders.
    """
    SET = "SET"
    """
    Set a list of folders.
    """

__all__ = ["FolderListCommand"]

