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
# Namespace: com.sun.star.beans
import typing
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_hierarchical_property_set_info import XHierarchicalPropertySetInfo as XHierarchicalPropertySetInfo_ae271245


class XMultiHierarchicalPropertySet(XInterface_8f010a43):
    """
    provides access to multiple properties which form a hierarchy.

    See Also:
        `API XMultiHierarchicalPropertySet <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1beans_1_1XMultiHierarchicalPropertySet.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.beans.XMultiHierarchicalPropertySet']

    def getHierarchicalPropertySetInfo(self) -> 'XHierarchicalPropertySetInfo_ae271245':
        """
        retrieve information about the hierarchy of properties
        """
        ...
    def getHierarchicalPropertyValues(self, aPropertyNames: 'typing.Tuple[str, ...]') -> 'typing.Tuple[object, ...]':
        """
        The order of the values in the returned sequence will be the same as the order of the names in the argument.
        
        Unknown properties are ignored, in their place NULL will be returned.

        Raises:
            : ````
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
        ...
    def setHierarchicalPropertyValues(self, aHierarchicalPropertyNames: 'typing.Tuple[str, ...]', Values: 'typing.Tuple[object, ...]') -> None:
        """
        sets the values of the properties with the specified nested names.
        
        The values of the properties must change before bound events are fired. The values of constrained properties should change after the vetoable events are fired, if no exception occurs.
        
        Unknown properties are ignored.

        Raises:
            com.sun.star.beans.PropertyVetoException: ``PropertyVetoException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
        ...


