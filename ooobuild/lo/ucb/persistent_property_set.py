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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.ucb
from ..beans.x_property_access import XPropertyAccess as XPropertyAccess_e1d40d20
from ..beans.x_property_container import XPropertyContainer as XPropertyContainer_c600e71
from ..container.x_named import XNamed as XNamed_a6520b08
from .x_persistent_property_set import XPersistentPropertySet as XPersistentPropertySet_2b0c0f5c

class PersistentPropertySet(XPropertyAccess_e1d40d20, XPropertyContainer_c600e71, XNamed_a6520b08, XPersistentPropertySet_2b0c0f5c):
    """
    Service Class

    This service contains the interfaces to implement by objects returned by XPropertySetRegistry.openPropertySet().

    See Also:
        `API PersistentPropertySet <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1ucb_1_1PersistentPropertySet.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ucb'
    __ooo_full_ns__: str = 'com.sun.star.ucb.PersistentPropertySet'
    __ooo_type_name__: str = 'service'



__all__ = ['PersistentPropertySet']

