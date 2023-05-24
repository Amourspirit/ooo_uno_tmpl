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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.configuration
from __future__ import annotations
from .hierarchy_access import HierarchyAccess as HierarchyAccess_5e871071
from .simple_set_access import SimpleSetAccess as SimpleSetAccess_5ea81068

class SetAccess(HierarchyAccess_5e871071, SimpleSetAccess_5ea81068):
    """
    Service Class

    provides access to a dynamic, homogeneous set of values or nested trees within a hierarchy.
    
    Also provides information about the template for elements. Allows normalizing externally generated names.
    
    Sets are dynamic containers within the hierarchy.
    
    The number and names of contained elements are not fixed in advance, but all elements have to be of one predetermined type.

    See Also:
        `API SetAccess <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1configuration_1_1SetAccess.html>`_
    """
    ...

