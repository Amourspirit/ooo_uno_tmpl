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
import typing
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from ..uno.x_interface import XInterface as XInterface_8f010a43


class XSolverDescription(XInterface_8f010a43):
    """
    gives access to user-visible strings for a solver.

    See Also:
        `API XSolverDescription <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sheet_1_1XSolverDescription.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.sheet.XSolverDescription']

    def getPropertyDescription(self, aPropertyName: str) -> str:
        """
        returns a short description for a property in the component's com.sun.star.beans.XPropertySet interface.
        """
        ...

    @property
    def ComponentDescription(self) -> str:
        """
        A user-visible name of the component.
        """
        ...
    @ComponentDescription.setter
    def ComponentDescription(self, value: str) -> None:
        ...
    @property
    def StatusDescription(self) -> str:
        """
        After calling solve, a message describing the status (explaining why no solution was found).
        """
        ...
    @StatusDescription.setter
    def StatusDescription(self, value: str) -> None:
        ...

