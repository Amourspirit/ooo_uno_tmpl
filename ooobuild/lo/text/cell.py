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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.text
from __future__ import annotations
from ..table.cell_properties import CellProperties as CellProperties_d4360cbd
from ..table.x_cell import XCell as XCell_70d408e8
from .cell_properties import CellProperties as CellProperties_c9a70c7a
from .x_text import XText as XText_690408ca

class Cell(CellProperties_d4360cbd, CellProperties_c9a70c7a, XCell_70d408e8, XText_690408ca):
    """
    Service Class

    represents a single cell within a text table.
    
    **since**
    
        OOo 2.0

    See Also:
        `API Cell <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1text_1_1Cell.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.text'
    __ooo_full_ns__: str = 'com.sun.star.text.Cell'
    __ooo_type_name__: str = 'service'


__all__ = ['Cell']

