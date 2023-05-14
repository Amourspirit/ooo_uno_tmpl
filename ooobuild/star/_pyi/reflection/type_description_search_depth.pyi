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
# Enum
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.reflection
# Libre Office Version: 7.4
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    import uno
from enum import Enum

class TypeDescriptionSearchDepth(Enum):
    """
    Enum

    

    See Also:
        `API TypeDescriptionSearchDepth <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1reflection.html#a19627c9e2873087a7d672cd9e0913000>`_
    """
    typeName: str = 'com.sun.star.reflection.TypeDescriptionSearchDepth'

    INFINITE: 'uno.Enum'
    """
    Infinite search depth.
    
    Search through all children including direct children, grand children, grand children's children, ...
    """
    ONE: 'uno.Enum'
    """
    Search only through direct children.
    """

