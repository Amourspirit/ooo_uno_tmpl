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
# Namespace: com.sun.star.ui.test
from __future__ import annotations
import typing

from abc import ABC
if typing.TYPE_CHECKING:
    from ...beans.property_values import PropertyValues as PropertyValues_d6470ce6
    from .xui_object import XUIObject as XUIObject_ad8a0b21


class XUITest(ABC):
    """

    See Also:
        `API XUITest <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1ui_1_1test_1_1XUITest.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.ui.test.XUITest'

    def executeCommand(self, command: str) -> bool:
        """
        """
        ...
    def executeCommandWithParameters(self, command: str, propValues: PropertyValues_d6470ce6) -> bool:
        """
        """
        ...
    def executeDialog(self, command: str) -> bool:
        """
        """
        ...
    def getFloatWindow(self) -> XUIObject_ad8a0b21:
        """
        """
        ...
    def getTopFocusWindow(self) -> XUIObject_ad8a0b21:
        """
        """
        ...


