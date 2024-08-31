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
# Namespace: com.sun.star.view
from __future__ import annotations
import typing

from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..awt.x_control import XControl as XControl_7a9c098d
    from ..awt.x_control_model import XControlModel as XControlModel_affc0b7e


class XControlAccess(XInterface_8f010a43):
    """
    provides access to the controls in a view.

    See Also:
        `API XControlAccess <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1view_1_1XControlAccess.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.view.XControlAccess'

    def getControl(self, xModel: XControlModel_affc0b7e) -> XControl_7a9c098d:
        """
        is called to get the control from the specified control model.

        Raises:
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
        """
        ...


