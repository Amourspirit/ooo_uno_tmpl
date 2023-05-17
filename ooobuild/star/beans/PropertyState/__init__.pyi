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
# Namespace: com.sun.star.beans
# Libre Office Version: 7.4
from __future__ import annotations
import uno
from com.sun.star._pyi.beans.property_state import PropertyState as PyiPropertyState
"""
Enum


See Also:
    `API PropertyState <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1beans.html#a1a5ccb5c59cace4a214c1e2eae8620b0>`_
"""
typeName: str = 'com.sun.star.beans.PropertyState'

AMBIGUOUS_VALUE: PyiPropertyState = ...
"""
The value of the property is only a recommendation because there are multiple values for this property (e.g., from a multi selection).

The PropertyAttribute field in the struct Property must contain the PropertyAttribute.MAYBEAMBIGUOUS flag. The property value must be available and of the specified type. If the Attribute field in the struct Property contains PropertyAttribute.MAYBEVOID, then the value may be void.
"""
DEFAULT_VALUE: PyiPropertyState = ...
"""
The value of the property is available from a master (e.g., template).
"""
DIRECT_VALUE: PyiPropertyState = ...
"""
The value of the property is stored in the PropertySet itself.
"""

