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
# Namespace: com.sun.star.sheet
from __future__ import annotations
from abc import abstractmethod
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
from ..container.x_named import XNamed as XNamed_a6520b08
from .x_scenario import XScenario as XScenario_99ac0aad
from .x_scenario_enhanced import XScenarioEnhanced as XScenarioEnhanced_fca20dc3

class Scenario(XPropertySet_bc180bfa, XNamed_a6520b08, XScenario_99ac0aad, XScenarioEnhanced_fca20dc3):
    """
    Service Class

    represents a scenario in a spreadsheet document.

    See Also:
        `API Scenario <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sheet_1_1Scenario.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.Scenario'
    __ooo_type_name__: str = 'service'

    @property
    @abstractmethod
    def BorderColor(self) -> int:
        """
        specifies the color of the border of the scenario.
        """
        ...

    @property
    @abstractmethod
    def CopyBack(self) -> bool:
        """
        specifies if the data should be copied back into the scenario.
        """
        ...

    @property
    @abstractmethod
    def CopyFormulas(self) -> bool:
        """
        specifies if the formulas are copied or only the results.
        """
        ...

    @property
    @abstractmethod
    def CopyStyles(self) -> bool:
        """
        specifies if the styles are copied.
        """
        ...

    @property
    @abstractmethod
    def IsActive(self) -> bool:
        """
        specifies if the scenario is active.
        """
        ...

    @property
    @abstractmethod
    def PrintBorder(self) -> bool:
        """
        specifies if the scenario prints a border.
        """
        ...

    @property
    @abstractmethod
    def Protected(self) -> bool:
        """
        specifies if the scenario is protected.
        """
        ...

    @property
    @abstractmethod
    def ShowBorder(self) -> bool:
        """
        specifies if the scenario shows a border.
        """
        ...


__all__ = ['Scenario']

