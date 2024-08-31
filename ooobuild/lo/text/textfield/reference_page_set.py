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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.text.textfield
from __future__ import annotations
from abc import abstractproperty
from ..text_field import TextField as TextField_90260a56

class ReferencePageSet(TextField_90260a56):
    """
    Service Class

    specifies service of a text field that inserts additional page numbers.

    See Also:
        `API ReferencePageSet <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1text_1_1textfield_1_1ReferencePageSet.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.text.textfield'
    __ooo_full_ns__: str = 'com.sun.star.text.textfield.ReferencePageSet'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def NameOn(self) -> bool:
        """
        determines whether the ReferencePageGet text fields are displayed or not.
        """
        ...

    @abstractproperty
    def Offset(self) -> int:
        """
        determines an offset value to change the displayed value of a ReferencePageGet text field.
        """
        ...


__all__ = ['ReferencePageSet']

