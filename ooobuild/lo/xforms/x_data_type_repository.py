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
# Namespace: com.sun.star.xforms
import typing
from abc import abstractmethod
from ..container.x_enumeration_access import XEnumerationAccess as XEnumerationAccess_4bac0ffc
from ..container.x_name_access import XNameAccess as XNameAccess_e2ab0cf6
if typing.TYPE_CHECKING:
    from ..xsd.x_data_type import XDataType as XDataType_83f209cb

class XDataTypeRepository(XEnumerationAccess_4bac0ffc, XNameAccess_e2ab0cf6):
    """
    specifies a repository of XSD data types
    
    The elements of the repository are instances supporting the com.sun.star.xsd.XDataType interface.

    See Also:
        `API XDataTypeRepository <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1xforms_1_1XDataTypeRepository.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.xforms'
    __ooo_full_ns__: str = 'com.sun.star.xforms.XDataTypeRepository'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.xforms.XDataTypeRepository'

    @abstractmethod
    def cloneDataType(self, sourceName: str, newName: str) -> 'XDataType_83f209cb':
        """
        creates a clone of the given data type, and inserts it into the repository

        Raises:
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
            com.sun.star.container.ElementExistException: ``ElementExistException``
        """
    @abstractmethod
    def getBasicDataType(self, dataTypeClass: int) -> 'XDataType_83f209cb':
        """
        retrieves the basic type for the given type class

        Raises:
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
        """
    @abstractmethod
    def getDataType(self, typeName: str) -> 'XDataType_83f209cb':
        """

        Raises:
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
        """
    @abstractmethod
    def revokeDataType(self, typeName: str) -> None:
        """
        removes a data type given by name from the repository

        Raises:
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
            com.sun.star.util.VetoException: ``VetoException``
        """

__all__ = ['XDataTypeRepository']

