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
# Namespace: com.sun.star.sheet
# Libre Office Version: 7.2
from enum import Enum


class DataPilotFieldOrientation(Enum):
    """
    Enum Class

    

    See Also:
        `API DataPilotFieldOrientation <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1sheet.html#a686c797e7cb837947558aa11c946245a>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.DataPilotFieldOrientation'
    __ooo_type_name__: str = 'enum'

    @property
    def typeName(self) -> str:
        return 'com.sun.star.sheet.DataPilotFieldOrientation'

    COLUMN = 'COLUMN'
    """
    the field is used as a column field.
    
    is applied to the columns.
    """
    DATA = 'DATA'
    """
    the field is used as a data field.
    """
    HIDDEN = 'HIDDEN'
    """
    the field is not used in the table.
    """
    PAGE = 'PAGE'
    """
    the field is used as a page field.
    """
    ROW = 'ROW'
    """
    the field is used as a row field.
    
    is applied to the rows.
    """

__all__ = ['DataPilotFieldOrientation']

