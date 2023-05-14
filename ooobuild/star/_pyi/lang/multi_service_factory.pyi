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
# Namespace: com.sun.star.lang
from .x_multi_component_factory import XMultiComponentFactory as XMultiComponentFactory_381b0f98
from .x_multi_service_factory import XMultiServiceFactory as XMultiServiceFactory_191e0eb6

class MultiServiceFactory(XMultiComponentFactory_381b0f98, XMultiServiceFactory_191e0eb6):
    """
    Service Class

    Provides a collection of implementations of services.
    
    The factories for instantiating objects of implementations are accessed via a service name.
    
    The com.sun.star.container.XContentEnumerationAccess interface can be supported optionally. If it is supported, it is possible to enumerate all implementations that support the service specified with the argument of com.sun.star.container.XContentEnumerationAccess.createContentEnumeration(). The enumerator returns interfaces. The type of the interface is not specified. Commonly this is XSingleComponentFactory.

    See Also:
        `API MultiServiceFactory <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1lang_1_1MultiServiceFactory.html>`_
    """
    ...

