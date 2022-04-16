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
# Namespace: com.sun.star.style
import typing
from abc import abstractmethod
from ..beans.x_multi_property_set import XMultiPropertySet as XMultiPropertySet_fd880e05
from ..beans.x_multi_property_states import XMultiPropertyStates as XMultiPropertyStates_2a3e0f4d
if typing.TYPE_CHECKING:
    from ..beans.property_values import PropertyValues as PropertyValues_d6470ce6

class XAutoStyle(XMultiPropertySet_fd880e05, XMultiPropertyStates_2a3e0f4d):
    """
    This interface allows access to a single automatic style.

    See Also:
        `API XAutoStyle <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1style_1_1XAutoStyle.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.style'
    __ooo_full_ns__: str = 'com.sun.star.style.XAutoStyle'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.style.XAutoStyle'

    @abstractmethod
    def getProperties(self) -> 'PropertyValues_d6470ce6':
        """
        returns a sequence of all properties that are set in the style
        """

__all__ = ['XAutoStyle']

