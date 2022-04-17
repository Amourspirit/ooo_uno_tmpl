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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.sheet


class FilterFieldType(object):
    """
    Const Class

    
    **since**
    
        LibreOffice 7.2

    See Also:
        `API FilterFieldType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1sheet_1_1FilterFieldType.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.FilterFieldType'
    __ooo_type_name__: str = 'const'

    NUMERIC = 0
    """
    Filter by numeric value.
    """
    STRING = 1
    """
    Filter by string value.
    """
    DATE = 2
    """
    Filter by date.
    """
    TEXT_COLOR = 3
    """
    Filter by text color.
    """
    BACKGROUND_COLOR = 4
    """
    Filter by background color.
    """

__all__ = ['FilterFieldType']