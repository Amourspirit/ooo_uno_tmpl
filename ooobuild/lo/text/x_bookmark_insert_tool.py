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
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_text_content import XTextContent as XTextContent_b16e0ba5
    from .x_text_range import XTextRange as XTextRange_9a910ab7

class XBookmarkInsertTool(XInterface_8f010a43):
    """
    offers an easy way to insert bookmarks by name.

    See Also:
        `API XBookmarkInsertTool <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1text_1_1XBookmarkInsertTool.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.text'
    __ooo_full_ns__: str = 'com.sun.star.text.XBookmarkInsertTool'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.text.XBookmarkInsertTool'

    @abstractmethod
    def insertNewBookmark(self, xTextRange: 'XTextRange_9a910ab7', aName: str) -> 'XTextContent_b16e0ba5':
        """
        inserts a bookmark at the specified text position.
        """
        ...

__all__ = ['XBookmarkInsertTool']

