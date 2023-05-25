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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.sheet
from __future__ import annotations
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43

class XCellRangeFormula(XInterface_8f010a43):
    """
    allows to get and set cell contents (values, text or formulas) for a cell range.
    
    The outer sequence represents the rows and the inner sequence the columns of the array.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API XCellRangeFormula <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sheet_1_1XCellRangeFormula.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.XCellRangeFormula'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.sheet.XCellRangeFormula'

    @abstractmethod
    def getFormulaArray(self) -> typing.Tuple[typing.Tuple[str, ...], ...]:
        """
        gets an array from the contents of the cell range.
        
        Each element of the result contains the same string that would be returned by com.sun.star.table.XCell.getFormula() for the corresponding cell.
        """
        ...
    @abstractmethod
    def setFormulaArray(self, aArray: typing.Tuple[typing.Tuple[str, ...], ...]) -> None:
        """
        fills the cell range with values from an array.
        
        The size of the array must be the same as the size of the cell range. Each element of the array is interpreted the same way as the argument to a com.sun.star.table.XCell.setFormula() call for the corresponding cell.
        """
        ...

__all__ = ['XCellRangeFormula']


