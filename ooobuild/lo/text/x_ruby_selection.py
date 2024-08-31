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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.text
from __future__ import annotations
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..beans.property_values import PropertyValues as PropertyValues_d6470ce6

class XRubySelection(XInterface_8f010a43):
    """
    This interface enables the object to handle list of ruby lines (aka Furigana lines).

    See Also:
        `API XRubySelection <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1text_1_1XRubySelection.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.text'
    __ooo_full_ns__: str = 'com.sun.star.text.XRubySelection'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.text.XRubySelection'

    @abstractmethod
    def getRubyList(self, Automatic: bool) -> typing.Tuple[PropertyValues_d6470ce6, ...]:
        """
        returns a sequence of ruby elements.
        
        Each element contains at least a string that contains the selected text and the ruby text. Additional parameters can be the ruby adjustment, the name of a character style.
        """
        ...
    @abstractmethod
    def setRubyList(self, RubyList: typing.Tuple[PropertyValues_d6470ce6, ...], Automatic: bool) -> None:
        """
        applies the RubyList to the current selection.
        
        The number of elements must be equal to the number of elements that are returned by getRubyList. Automatic must be set equally, too.
        """
        ...

__all__ = ['XRubySelection']

