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
# Const
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.beans
from typing_extensions import Literal
"""
Const

These values are used to specify the behavior of a Property.

**since**

    OOo 1.1.2

See Also:
    `API PropertyAttribute <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1beans_1_1PropertyAttribute.html>`_
"""
MAYBEVOID: Literal[1]
"""
indicates that a property value can be void.

It does not mean that the type of the property is void!
"""
BOUND: Literal[2]
"""
indicates that a PropertyChangeEvent will be fired to all registered XPropertyChangeListeners whenever the value of this property changes.
"""
CONSTRAINED: Literal[4]
"""
indicates that a PropertyChangeEvent will be fired to all registered XVetoableChangeListeners whenever the value of this property is about to change.
"""
TRANSIENT: Literal[8]
"""
indicates that the value of the property is not persistent.
"""
READONLY: Literal[16]
"""
indicates that the value of the property is read-only.
"""
MAYBEAMBIGUOUS: Literal[32]
"""
indicates that the value of the property can be ambiguous.
"""
MAYBEDEFAULT: Literal[64]
"""
indicates that the property can be set to default.
"""
REMOVABLE: Literal[128]
"""
indicates that the property can be removed (i.e., by calling XPropertyContainer.removeProperty()).
"""
REMOVEABLE: Literal[128]
OPTIONAL: Literal[256]
"""
indicates that a property is optional.

This attribute is not of interest for concrete property implementations. It's needed for property specifications inside service specifications in UNOIDL.

**since**

    OOo 1.1.2
"""
