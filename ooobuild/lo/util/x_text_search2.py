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
from .x_text_search import XTextSearch as XTextSearch_a56a0b19
if typing.TYPE_CHECKING:
    from .search_options2 import SearchOptions2 as SearchOptions2_c94e0c3a

class XTextSearch2(XTextSearch_a56a0b19):
    """
    enables an object to search in its content.
    
    Derived from com.sun.star.util.XTextSearch this interface adds simple wildcard search capabilities using com.sun.star.util.SearchOptions2 options.
    
    **since**
    
        LibreOffice 5.2

    See Also:
        `API XTextSearch2 <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1util_1_1XTextSearch2.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.util'
    __ooo_full_ns__: str = 'com.sun.star.util.XTextSearch2'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.util.XTextSearch2'

    @abstractmethod
    def setOptions2(self, options: SearchOptions2_c94e0c3a) -> None:
        """
        set the options for the forward or backward search.
        """
        ...

__all__ = ['XTextSearch2']

