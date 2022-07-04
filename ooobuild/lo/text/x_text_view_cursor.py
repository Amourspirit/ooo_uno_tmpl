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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.text
import typing
from abc import abstractmethod
from .x_text_cursor import XTextCursor as XTextCursor_a60c0b48
if typing.TYPE_CHECKING:
    from ..awt.point import Point as Point_5fb2085e

class XTextViewCursor(XTextCursor_a60c0b48):
    """
    describes a cursor in a text document's view.

    See Also:
        `API XTextViewCursor <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1text_1_1XTextViewCursor.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.text'
    __ooo_full_ns__: str = 'com.sun.star.text.XTextViewCursor'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.text.XTextViewCursor'

    @abstractmethod
    def getPosition(self) -> 'Point_5fb2085e':
        """
        """
        ...
    @abstractmethod
    def isVisible(self) -> bool:
        """
        """
        ...
    @abstractmethod
    def setVisible(self, bVisible: bool) -> None:
        """
        shows or hides this cursor for the user.
        """
        ...

__all__ = ['XTextViewCursor']

