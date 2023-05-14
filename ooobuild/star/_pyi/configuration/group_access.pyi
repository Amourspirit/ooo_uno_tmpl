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
from .hierarchy_access import HierarchyAccess as HierarchyAccess_5e871071
from .property_hierarchy import PropertyHierarchy as PropertyHierarchy_83841184

class GroupAccess(HierarchyAccess_5e871071, PropertyHierarchy_83841184):
    """
    Service Class

    provides access to a predefined heterogeneous group of values and nested trees as part of a hierarchy.
    
    Provides access to, and information about, its children and descendants viewed either as properties or as contained elements.
    
    Groups are static collections within the hierarchy.
    
    The number and names of contained elements are fixed in advance and each child may have a different type.
    
    This service subsumes two alternate ways of accessing child and descendent elements. These strongly overlap, supporting the basic identity xGroup.getPropertyValue( aName ) == xGroup.getByName( aName ).

    See Also:
        `API GroupAccess <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1configuration_1_1GroupAccess.html>`_
    """
    ...

