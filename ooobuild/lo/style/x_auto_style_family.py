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
# Libre Office Version: 7.4
# Namespace: com.sun.star.style
import typing
from abc import abstractmethod
from ..container.x_enumeration_access import XEnumerationAccess as XEnumerationAccess_4bac0ffc
if typing.TYPE_CHECKING:
    from ..beans.property_values import PropertyValues as PropertyValues_d6470ce6
    from .x_auto_style import XAutoStyle as XAutoStyle_a67a0b3b

class XAutoStyleFamily(XEnumerationAccess_4bac0ffc):
    """
    This service contains the collection of automatic style families within the container document.

    See Also:
        `API XAutoStyleFamily <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1style_1_1XAutoStyleFamily.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.style'
    __ooo_full_ns__: str = 'com.sun.star.style.XAutoStyleFamily'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.style.XAutoStyleFamily'

    @abstractmethod
    def insertStyle(self, Values: 'PropertyValues_d6470ce6') -> 'XAutoStyle_a67a0b3b':
        """
        """
        ...

__all__ = ['XAutoStyleFamily']

