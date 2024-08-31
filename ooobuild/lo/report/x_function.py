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
# Namespace: com.sun.star.report
from __future__ import annotations
from abc import abstractmethod
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
from ..container.x_child import XChild as XChild_a6390b07
from ..lang.x_component import XComponent as XComponent_98dc0ab5

class XFunction(XPropertySet_bc180bfa, XChild_a6390b07, XComponent_98dc0ab5):
    """
    specifies a format condition for a control.

    See Also:
        `API XFunction <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1report_1_1XFunction.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.report'
    __ooo_full_ns__: str = 'com.sun.star.report.XFunction'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.report.XFunction'

    @property
    @abstractmethod
    def DeepTraversing(self) -> bool:
        """
        specifies if sub reports should be traversed as well.
        """
        ...

    @property
    @abstractmethod
    def Formula(self) -> str:
        """
        defines the formula of this function
        """
        ...

    @property
    @abstractmethod
    def InitialFormula(self) -> object:
        """
        defines the formula for the initial value
        """
        ...

    @property
    @abstractmethod
    def Name(self) -> str:
        """
        defines the name of the function
        """
        ...

    @property
    @abstractmethod
    def PreEvaluated(self) -> bool:
        """
        specifies if the function should be evaluated before the report element will be executed.
        """
        ...


__all__ = ['XFunction']

