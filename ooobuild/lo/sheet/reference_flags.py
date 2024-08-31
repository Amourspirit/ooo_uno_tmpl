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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.sheet


class ReferenceFlags(object):
    """
    Const Class

    defines flags for references.
    
    The values can be combined.

    See Also:
        `API ReferenceFlags <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1sheet_1_1ReferenceFlags.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.ReferenceFlags'
    __ooo_type_name__: str = 'const'

    COLUMN_RELATIVE = 1
    """
    selects a relative column reference.
    """
    COLUMN_DELETED = 2
    """
    marks a deleted column reference.
    """
    ROW_RELATIVE = 4
    """
    selects a relative row reference.
    """
    ROW_DELETED = 8
    """
    marks a deleted row reference.
    """
    SHEET_RELATIVE = 16
    """
    selects a relative sheet reference.
    """
    SHEET_DELETED = 32
    """
    marks a deleted sheet reference.
    """
    SHEET_3D = 64
    """
    selects a 3D sheet reference.
    """
    RELATIVE_NAME = 128
    """
    marks a reference from a relative range name.
    """

__all__ = ['ReferenceFlags']
