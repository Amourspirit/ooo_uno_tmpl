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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.sheet
from __future__ import annotations
import typing
from abc import abstractmethod, abstractproperty
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .solver_constraint import SolverConstraint as SolverConstraint_f1e30dc1
    from .x_spreadsheet_document import XSpreadsheetDocument as XSpreadsheetDocument_2a1f0f30
    from ..table.cell_address import CellAddress as CellAddress_ae5f0b56

class XSolver(XInterface_8f010a43):
    """
    allows to call a solver for a model that is defined by spreadsheet cells.

    See Also:
        `API XSolver <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sheet_1_1XSolver.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.XSolver'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.sheet.XSolver'

    @abstractmethod
    def solve(self) -> None:
        """
        executes the calculation and tries to find a solution.
        """
        ...
    @abstractproperty
    def Constraints(self) -> typing.Tuple[SolverConstraint_f1e30dc1, ...]:
        """
        The constraints of the model.
        """
        ...

    @abstractproperty
    def Document(self) -> XSpreadsheetDocument_2a1f0f30:
        """
        The spreadsheet document that contains the cells.
        """
        ...

    @abstractproperty
    def Maximize(self) -> bool:
        """
        selects if the objective value is maximized or minimized.
        """
        ...

    @abstractproperty
    def Objective(self) -> CellAddress_ae5f0b56:
        """
        The address of the cell that contains the objective value.
        """
        ...

    @abstractproperty
    def ResultValue(self) -> float:
        """
        contains the objective value for the solution, if a solution was found.
        """
        ...

    @abstractproperty
    def Solution(self) -> typing.Tuple[float, ...]:
        """
        contains the solution's value for each of the variables, if a solution was found.
        """
        ...

    @abstractproperty
    def Success(self) -> bool:
        """
        contains TRUE if a solution was found.
        """
        ...

    @abstractproperty
    def Variables(self) -> typing.Tuple[CellAddress_ae5f0b56, ...]:
        """
        The addresses of the cells that contain the variables.
        """
        ...


__all__ = ['XSolver']

