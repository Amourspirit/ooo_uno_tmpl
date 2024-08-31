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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.configuration
from __future__ import annotations
from .group_access import GroupAccess as GroupAccess_1f8f0edf
from ..container.x_name_replace import XNameReplace as XNameReplace_f0900d60

class GroupUpdate(GroupAccess_1f8f0edf, XNameReplace_f0900d60):
    """
    Service Class

    provides write access to a predefined heterogeneous group of values and nested trees as part of a hierarchy.
    
    This service extends GroupAccess to support modifying values.

    See Also:
        `API GroupUpdate <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1configuration_1_1GroupUpdate.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.configuration'
    __ooo_full_ns__: str = 'com.sun.star.configuration.GroupUpdate'
    __ooo_type_name__: str = 'service'


__all__ = ['GroupUpdate']

