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
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.reflection
# Libre Office Version: 7.2
from enum import Enum


class FieldAccessMode(Enum):
    """
    Enum Class

    

    See Also:
        `API FieldAccessMode <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1reflection.html#a95a71baf95250ba8716608067ba245f9>`_
    """
    __ooo_ns__: str = 'com.sun.star.reflection'
    __ooo_full_ns__: str = 'com.sun.star.reflection.FieldAccessMode'
    __ooo_type_name__: str = 'enum'

    @property
    def typeName(self) -> str:
        return 'com.sun.star.reflection.FieldAccessMode'

    CONST = 'CONST'
    """
    Deprecated.
    
    Not used anymore.
    """
    READONLY = 'READONLY'
    """
    readable only
    """
    READWRITE = 'READWRITE'
    """
    readable and writeable
    """
    WRITEONLY = 'WRITEONLY'
    """
    writeable only
    """

__all__ = ['FieldAccessMode']

