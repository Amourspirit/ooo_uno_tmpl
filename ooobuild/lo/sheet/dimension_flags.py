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


class DimensionFlags(object):
    """
    Const Class

    used to specify flags for a dimension in a data pilot source.

    See Also:
        `API DimensionFlags <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1sheet_1_1DimensionFlags.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.DimensionFlags'
    __ooo_type_name__: str = 'const'

    NO_COLUMN_ORIENTATION = 1
    """
    The dimension cannot be used in column orientation.
    """
    NO_ROW_ORIENTATION = 2
    """
    The dimension cannot be used in row orientation.
    """
    NO_PAGE_ORIENTATION = 4
    """
    The dimension cannot be used in page orientation.
    """
    NO_DATA_ORIENTATION = 8
    """
    The dimension cannot be used in data orientation.
    """

__all__ = ['DimensionFlags']
