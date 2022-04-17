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
# Namespace: com.sun.star.ui.dialogs
from typing_extensions import Literal
import typing
from ...uno.x_interface import XInterface as XInterface_8f010a43

class XControlInformation(XInterface_8f010a43):
    """
    Interface to query for controls and control properties supported by the implementing instance.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API XControlInformation <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1ui_1_1dialogs_1_1XControlInformation.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.ui.dialogs.XControlInformation']

    def getSupportedControlProperties(self, aControlName: str) -> 'typing.Tuple[str, ...]':
        """
        Returns a sequence with properties supported by the specified control.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
    def getSupportedControls(self) -> 'typing.Tuple[str, ...]':
        """
        Query for the supported controls of a service instance.
        """
    def isControlPropertySupported(self, aControlName: str, aControlProperty: str) -> bool:
        """
        Returns whether control property is supported by a control.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
    def isControlSupported(self, aControlName: str) -> bool:
        """
        Returns whether the specified control is supported or not.
        """

