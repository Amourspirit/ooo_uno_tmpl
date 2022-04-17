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
# Libre Office Version: 7.3
from enum import Enum


class CellDeleteMode(Enum):
    """
    Enum Class

    

    See Also:
        `API CellDeleteMode <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1sheet.html#af2bbbff47b7abe36f258e59b1351e422>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.CellDeleteMode'
    __ooo_type_name__: str = 'enum'

    COLUMNS = 'COLUMNS'
    """
    entire columns to the right of the deleted cells are moved left.
    
    entire columns to the right of the inserted cells are moved right.
    """
    LEFT = 'LEFT'
    """
    selects the left border.
    
    the cells to the right of the deleted cells are moved left.
    """
    NONE = 'NONE'
    """
    no cells are moved.
    
    sheet is not linked.
    
    new values are used without changes.
    
    nothing is calculated.
    
    nothing is imported.
    
    no condition is specified.
    """
    ROWS = 'ROWS'
    """
    entire rows below the deleted cells are moved up.
    
    entire rows below the inserted cells are moved down.
    """
    UP = 'UP'
    """
    the cells below the deleted cells are moved up.
    """

__all__ = ['CellDeleteMode']
