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
# Namespace: com.sun.star.util
import typing
from abc import abstractmethod
from .x_replace_descriptor import XReplaceDescriptor as XReplaceDescriptor_fd510df9
if typing.TYPE_CHECKING:
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73

class XPropertyReplace(XReplaceDescriptor_fd510df9):
    """
    makes it possible to search and replace properties.

    See Also:
        `API XPropertyReplace <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1util_1_1XPropertyReplace.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.util'
    __ooo_full_ns__: str = 'com.sun.star.util.XPropertyReplace'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.util.XPropertyReplace'

    @abstractmethod
    def getReplaceAttributes(self) -> 'typing.Tuple[PropertyValue_c9610c73, ...]':
        """
        """
    @abstractmethod
    def getSearchAttributes(self) -> 'typing.Tuple[PropertyValue_c9610c73, ...]':
        """
        """
    @abstractmethod
    def getValueSearch(self) -> bool:
        """
        provides the information if specific property values are searched, or just the existence of the specified properties.
        """
    @abstractmethod
    def setReplaceAttributes(self, aSearchAttribs: 'typing.Tuple[PropertyValue_c9610c73, ...]') -> None:
        """
        sets the properties to replace the found occurrences.

        Raises:
            com.sun.star.beans.UnknownPropertyException: ``UnknownPropertyException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
    @abstractmethod
    def setSearchAttributes(self, aSearchAttribs: 'typing.Tuple[PropertyValue_c9610c73, ...]') -> None:
        """
        sets the properties to search for.

        Raises:
            com.sun.star.beans.UnknownPropertyException: ``UnknownPropertyException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
    @abstractmethod
    def setValueSearch(self, bValueSearch: bool) -> None:
        """
        specifies if specific property values are searched, or just the existence of the specified properties.
        """

__all__ = ['XPropertyReplace']
