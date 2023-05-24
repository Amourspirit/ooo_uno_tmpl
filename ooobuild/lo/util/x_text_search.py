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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.util
from __future__ import annotations
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .search_options import SearchOptions as SearchOptions_bd140c08
    from .search_result import SearchResult as SearchResult_b1070b9b

class XTextSearch(XInterface_8f010a43):
    """
    enables an object to search in its content.

    See Also:
        `API XTextSearch <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1util_1_1XTextSearch.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.util'
    __ooo_full_ns__: str = 'com.sun.star.util.XTextSearch'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.util.XTextSearch'

    @abstractmethod
    def searchBackward(self, searchStr: str, startPos: int, endPos: int) -> SearchResult_b1070b9b:
        """
        search backward in the searchStr, starts at startPos and ends by endpos.
        
        The endpos must be lower than the startpos, because the function searches backward! The result is returned in the SearchResult.
        """
        ...
    @abstractmethod
    def searchForward(self, searchStr: str, startPos: int, endPos: int) -> SearchResult_b1070b9b:
        """
        search forward in the searchStr, starts at startPos and ends by endpos.
        
        The result is returned in the SearchResult.
        """
        ...
    @abstractmethod
    def setOptions(self, options: SearchOptions_bd140c08) -> None:
        """
        set the options for the forward or backward search.
        """
        ...

__all__ = ['XTextSearch']

