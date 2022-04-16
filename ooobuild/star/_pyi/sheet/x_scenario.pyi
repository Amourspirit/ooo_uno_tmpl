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
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..table.cell_range_address import CellRangeAddress as CellRangeAddress_ec450d43

class XScenario(XInterface_8f010a43):
    """
    provides access to the settings of a scenario sheet.

    See Also:
        `API XScenario <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sheet_1_1XScenario.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.sheet.XScenario']

    def addRanges(self, aRanges: 'typing.Tuple[CellRangeAddress_ec450d43, ...]') -> None:
        """
        adds more ranges to the scenario.
        """
    def apply(self) -> None:
        """
        applies the scenario.
        
        The contents of the scenario ranges are copied into the first non-scenario sheet which is in front of the sheet containing the scenario by itself.
        """
    def getIsScenario(self) -> bool:
        """
        returns TRUE if the current object is a scenario.
        """
    def getScenarioComment(self) -> str:
        """
        returns the comment for the scenario.
        """
    def setScenarioComment(self, aScenarioComment: str) -> None:
        """
        sets a new comment for the scenario.
        """

