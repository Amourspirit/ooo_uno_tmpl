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
# Libre Office Version: 7.2
# Namespace: com.sun.star.configuration
from .simple_set_access import SimpleSetAccess as SimpleSetAccess_5ea81068
from ..container.x_name_container import XNameContainer as XNameContainer_cb90e47
from ..lang.x_multi_service_factory import XMultiServiceFactory as XMultiServiceFactory_191e0eb6
from ..lang.x_single_service_factory import XSingleServiceFactory as XSingleServiceFactory_27210f0d

class SimpleSetUpdate(SimpleSetAccess_5ea81068, XNameContainer_cb90e47, XMultiServiceFactory_191e0eb6, XSingleServiceFactory_27210f0d):
    """
    Service Class

    provides write access to a dynamic, homogeneous, non-hierarchical set of values or objects.
    
    Allows adding and removing elements. Helps create new elements to be added.
    
    This service extends SimpleSetAccess to support modifying the container. Any child objects shall in turn support modifying access.

    See Also:
        `API SimpleSetUpdate <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1configuration_1_1SimpleSetUpdate.html>`_
    """


