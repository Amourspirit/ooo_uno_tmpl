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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.text
from __future__ import annotations
import typing
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
if typing.TYPE_CHECKING:
    from .x_dependent_text_field import XDependentTextField as XDependentTextField_c3d0e45

class TextFieldMaster(XPropertySet_bc180bfa):
    """
    Service Class

    A TextFieldMaster specifies important data for its DependentTextFields.

    See Also:
        `API TextFieldMaster <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1text_1_1TextFieldMaster.html>`_
    """
    @property
    def DependentTextFields(self) -> typing.Tuple[XDependentTextField_c3d0e45, ...]:
        """
        contains a sequence of all fields that depend on this master.
        """
        ...
    @DependentTextFields.setter
    def DependentTextFields(self, value: typing.Tuple[XDependentTextField_c3d0e45, ...]) -> None:
        ...
    @property
    def InstanceName(self) -> str:
        """
        contains the instance name as it is used in the com.sun.star.text.XTextFieldsSupplier.
        """
        ...
    @InstanceName.setter
    def InstanceName(self, value: str) -> None:
        ...
    @property
    def Name(self) -> str:
        """
        determines the name of the field master.
        
        The name is void as long as the instance is not member of the document structure. When the value is being set the instance is inserted into the document and the name cannot be changed afterwards. That does not apply to the Database text field master.
        """
        ...
    @Name.setter
    def Name(self, value: str) -> None:
        ...

