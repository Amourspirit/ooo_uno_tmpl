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
# Namespace: com.sun.star.xsd
from abc import abstractmethod, abstractproperty
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa

class XDataType(XPropertySet_bc180bfa):
    """
    specifies an XSD compliant simple data type

    See Also:
        `API XDataType <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1xsd_1_1XDataType.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.xsd'
    __ooo_full_ns__: str = 'com.sun.star.xsd.XDataType'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.xsd.XDataType'

    @abstractmethod
    def explainInvalid(self, value: str) -> str:
        """
        TODO.
        """
        ...
    @abstractmethod
    def validate(self, value: str) -> bool:
        """
        TODO.
        """
        ...
    @abstractproperty
    def IsBasic(self) -> bool:
        """
        specifies whether the type is a basic type
        
        Basic types are built into the type system, and cannot be changed by the user.
        """
        ...

    @abstractproperty
    def Name(self) -> str:
        """
        provides access to the name of the type
        """
        ...

    @abstractproperty
    def Pattern(self) -> str:
        """
        specifies the pattern which strings conforming to this type comply to
        
        See http://www.w3.org/TR/xmlschema-2/#rf-pattern
        """
        ...

    @abstractproperty
    def TypeClass(self) -> int:
        """
        class of the type
        """
        ...

    @abstractproperty
    def WhiteSpaceTreatment(self) -> int:
        """
        specifies how strings of this data type are to be processed, with respect to white spaces
        
        See http://www.w3.org/TR/xmlschema-2/#rf-whiteSpace
        """
        ...


__all__ = ['XDataType']

