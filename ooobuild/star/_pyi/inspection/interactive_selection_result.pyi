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
# Enum
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.inspection
# Libre Office Version: 7.4
from __future__ import annotations
import uno


class InteractiveSelectionResult(uno.Enum):
    """
    Enum


    See Also:
        `API InteractiveSelectionResult <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1inspection.html#a2c7cbb6dbe76b989188c75ba8e400876>`_
    """
    typeName: str = 'com.sun.star.inspection.InteractiveSelectionResult'

    Cancelled: PyiInteractiveSelectionResult = ...
    """
    The interactive selection of a property value was canceled.
    """
    ObtainedValue: PyiInteractiveSelectionResult = ...
    """
    The interactive selection of a property value succeeded, a new property value has been obtained, but not yet set at the inspected component.
    
    In this case, the obtained value is passed to the caller of XPropertyHandler.onInteractivePropertySelection(), which is responsible for forwarding this value to the inspected component.
    """
    Pending: PyiInteractiveSelectionResult = ...
    """
    The interactive selection of a property value is still pending.
    """
    Success: PyiInteractiveSelectionResult = ...
    """
    The interactive selection of a property value succeeded, and the new property value chosen by the user has already been set at the inspected component.
    """

