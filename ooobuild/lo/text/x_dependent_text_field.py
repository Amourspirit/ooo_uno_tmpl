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
from .x_text_field import XTextField as XTextField_9a630aae
if typing.TYPE_CHECKING:
    from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa

class XDependentTextField(XTextField_9a630aae):
    """
    makes it possible to attach this TextField to a TextFieldMaster.

    See Also:
        `API XDependentTextField <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1text_1_1XDependentTextField.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.text'
    __ooo_full_ns__: str = 'com.sun.star.text.XDependentTextField'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.text.XDependentTextField'

    @abstractmethod
    def attachTextFieldMaster(self, xFieldMaster: 'XPropertySet_bc180bfa') -> None:
        """
        method must be called to attach the TextFieldMaster to this TextField.
        
        A TextFieldMaster can only be assigned once.
        
        Example: Create and insert a user field (with a UserField):

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    @abstractmethod
    def getTextFieldMaster(self) -> 'XPropertySet_bc180bfa':
        """
        """
        ...

__all__ = ['XDependentTextField']

