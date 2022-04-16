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
# Namespace: com.sun.star.style
# Libre Office Version: 7.3
from enum import Enum


class BreakType(Enum):
    """
    Enum Class

    

    See Also:
        `API BreakType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1style.html#a3ae28cb49c180ec160a0984600b2b925>`_
    """
    __ooo_ns__: str = 'com.sun.star.style'
    __ooo_full_ns__: str = 'com.sun.star.style.BreakType'
    __ooo_type_name__: str = 'enum'

    COLUMN_AFTER = 'COLUMN_AFTER'
    """
    A column break is applied after the object to which it belongs.
    """
    COLUMN_BEFORE = 'COLUMN_BEFORE'
    """
    A column break is applied before the object to which it belongs.
    """
    COLUMN_BOTH = 'COLUMN_BOTH'
    """
    A column break is applied before and after the object to which it belongs.
    """
    NONE = 'NONE'
    """
    No column or page break is applied.
    
    This value specifies that a location is not yet assigned.
    """
    PAGE_AFTER = 'PAGE_AFTER'
    """
    A page break is applied after the object to which it belongs.
    """
    PAGE_BEFORE = 'PAGE_BEFORE'
    """
    A page break is applied before the object to which it belongs.
    """
    PAGE_BOTH = 'PAGE_BOTH'
    """
    A page break is applied before and after the object to which it belongs.
    """

__all__ = ['BreakType']

