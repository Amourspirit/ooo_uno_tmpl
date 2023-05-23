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
# Namespace: com.sun.star.sdbcx
from __future__ import annotations
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43

class XRowLocate(XInterface_8f010a43):
    """
    is used to identify rows within a result set and to find rows by a bookmark.
    
    Bookmarks are only valid in the scope of the current result set and are not interchangeable between result sets. A bookmark could be a complex data structure, so it could not be compared in a safe way. Because of that, a provider has to implement the compare method for bookmarks.

    See Also:
        `API XRowLocate <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sdbcx_1_1XRowLocate.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sdbcx'
    __ooo_full_ns__: str = 'com.sun.star.sdbcx.XRowLocate'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.sdbcx.XRowLocate'

    @abstractmethod
    def compareBookmarks(self, first: object, second: object) -> int:
        """
        compares two bookmarks and returns an indication of their relative values.
        
        The bookmarks must apply to the same ResultSet. You cannot reliably compare bookmarks from different ResultSets, even if they were created from the same source or statement. A bookmark that is not valid, or incorrectly formed, will cause an exception.

        Raises:
            com.sun.star.sdbc.SQLException: ``SQLException``
        """
        ...
    @abstractmethod
    def getBookmark(self) -> object:
        """
        returns the bookmark of the current row of a result set.

        Raises:
            com.sun.star.sdbc.SQLException: ``SQLException``
        """
        ...
    @abstractmethod
    def hasOrderedBookmarks(self) -> bool:
        """
        determines whether the bookmarks of a result set are ordered or not.

        Raises:
            com.sun.star.sdbc.SQLException: ``SQLException``
        """
        ...
    @abstractmethod
    def hashBookmark(self, bookmark: object) -> int:
        """
        returns the hash value for a specified bookmark.

        Raises:
            com.sun.star.sdbc.SQLException: ``SQLException``
        """
        ...
    @abstractmethod
    def moveRelativeToBookmark(self, bookmark: object, rows: int) -> bool:
        """
        moves the cursor a relative number of rows, either positive or negative starting at a given bookmark position.
        
        If the bookmark could not be located, a result set will be positioned after the last record. If the bookmark is invalid, or not generated by the current result set, then the behavior is not defined, even an abnormal termination is possible.

        Raises:
            com.sun.star.sdbc.SQLException: ``SQLException``
        """
        ...
    @abstractmethod
    def moveToBookmark(self, bookmark: object) -> bool:
        """
        moves the cursor to the row identified by a valid bookmark.
        
        If the bookmark could not be located, a result set will be positioned after the last record. If the bookmark is invalid, or not generated by the current result set, then the behavior is not defined, even an abnormal termination is possible.

        Raises:
            com.sun.star.sdbc.SQLException: ``SQLException``
        """
        ...

__all__ = ['XRowLocate']

