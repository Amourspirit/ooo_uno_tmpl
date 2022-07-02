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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.container
import typing
from .x_enumerable_map import XEnumerableMap as XEnumerableMap_dc50e41

class EnumerableMap(XEnumerableMap_dc50e41):
    """
    Service Class

    provides a default XEnumerableMap implementation
    
    For the keys put into the map using XMap.put() or createImmutable(), the following rules apply:
    
    For the values put into the map using XMap.put() or createImmutable(), the following rules apply:
    
    The factory methods of the XEnumerableMap interface support both isolated and non-isolated enumerators. The latter one will be automatically disposed when the map changes after enumerator creation, so every attempt to use them will result in a com.sun.star.lang.DisposedException being thrown.

    See Also:
        `API EnumerableMap <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1container_1_1EnumerableMap.html>`_
    """
    def create(self, KeyType: object, ValueType: object) -> None:
        """
        creates an instance mapping from the given key type to the given value type

        Raises:
            com.sun.star.beans.IllegalTypeException: ``IllegalTypeException``
        """
        ...
    def createImmutable(self, KeyType: object, ValueType: object, Values: 'typing.Tuple[typing.Tuple[object, object], ...]') -> None:
        """
        creates an instance mapping from the given key type to the given value type
        
        The resulting map is immutable, so later alter operations on it will fail with a com.sun.star.lang.NoSupportException.

        Raises:
            com.sun.star.beans.IllegalTypeException: ``IllegalTypeException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...


