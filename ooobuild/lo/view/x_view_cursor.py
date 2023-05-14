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
# Namespace: com.sun.star.view
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43

class XViewCursor(XInterface_8f010a43):
    """
    makes it possible to move a cursor up/down/left/right within laid out text.

    See Also:
        `API XViewCursor <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1view_1_1XViewCursor.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.view'
    __ooo_full_ns__: str = 'com.sun.star.view.XViewCursor'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.view.XViewCursor'

    @abstractmethod
    def goDown(self, nCount: int, bExpand: bool) -> bool:
        """
        moves the cursor the specified number of lines down.
        """
        ...
    @abstractmethod
    def goLeft(self, nCount: int, bExpand: bool) -> bool:
        """
        moves the cursor the specified number of characters to the left.
        """
        ...
    @abstractmethod
    def goRight(self, nCount: int, bExpand: bool) -> bool:
        """
        moves the cursor the specified number of characters to the right.
        """
        ...
    @abstractmethod
    def goUp(self, nCount: int, bExpand: bool) -> bool:
        """
        moves the cursor the specified number of lines up.
        """
        ...

__all__ = ['XViewCursor']

