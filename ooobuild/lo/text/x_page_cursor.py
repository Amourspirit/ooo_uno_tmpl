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
# Namespace: com.sun.star.text
from __future__ import annotations
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43

class XPageCursor(XInterface_8f010a43):
    """
    makes it possible to perform cursor movements between pages.

    See Also:
        `API XPageCursor <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1text_1_1XPageCursor.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.text'
    __ooo_full_ns__: str = 'com.sun.star.text.XPageCursor'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.text.XPageCursor'

    @abstractmethod
    def getPage(self) -> int:
        """
        """
        ...
    @abstractmethod
    def jumpToEndOfPage(self) -> bool:
        """
        moves the cursor to the end of the current page.
        """
        ...
    @abstractmethod
    def jumpToFirstPage(self) -> bool:
        """
        moves the cursor to the first page.
        """
        ...
    @abstractmethod
    def jumpToLastPage(self) -> bool:
        """
        moves the cursor to the last page.
        """
        ...
    @abstractmethod
    def jumpToNextPage(self) -> bool:
        """
        moves the cursor to the next page.
        """
        ...
    @abstractmethod
    def jumpToPage(self, nPage: int) -> bool:
        """
        moves the cursor to the specified page.
        """
        ...
    @abstractmethod
    def jumpToPreviousPage(self) -> bool:
        """
        moves the cursor to the previous page.
        """
        ...
    @abstractmethod
    def jumpToStartOfPage(self) -> bool:
        """
        moves the cursor to the start of the current page.
        """
        ...

__all__ = ['XPageCursor']

