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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.sheet
from typing_extensions import Literal
from ..uno.x_interface import XInterface as XInterface_8f010a43

class XArrayFormulaRange(XInterface_8f010a43):
    """
    provides handling of array formulas in a cell range.

    See Also:
        `API XArrayFormulaRange <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sheet_1_1XArrayFormulaRange.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.sheet.XArrayFormulaRange']

    def getArrayFormula(self) -> str:
        """
        returns the array formula of the range or an empty string, if the range does not contain an array formula.
        """
    def setArrayFormula(self, aFormula: str) -> None:
        """
        applies the array formula to the entire cell range.
        """
