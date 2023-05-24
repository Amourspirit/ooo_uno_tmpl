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
from ..lang.x_component import XComponent as XComponent_98dc0ab5
from ..lang.x_multi_service_factory import XMultiServiceFactory as XMultiServiceFactory_191e0eb6

class AdministrationProvider(XComponent_98dc0ab5, XMultiServiceFactory_191e0eb6):
    """
    Service Class

    manages one, or more, complete sets of configuration data for administrative purposes and serves as a factory for objects that provide access to subsets of these shared configurations.
    
    Shared sets of configuration data usually serve to provide defaults, which are used if no individual settings are present. Depending on the data store multiple layers of defaults may be combined with a user-specific layer to make up the final configuration.
    
    Many aspects of the supported behavior depend strongly on the underlying data store and on the administrative structures it defines. With some data stores this service also enables access to individual user's configuration data by an administrator.
    
    On the other hand, in the simplest model there is only a single layer of default data which is accessible through this service.
    
    An implementation is usually obtained from a com.sun.star.lang.ServiceManager. The arguments passed to com.sun.star.lang.XMultiComponentFactory.createInstanceWithArgumentsAndContext() select the configuration data source. They may also define the scope of administrable data or contain credentials to be used to authorize the administrative access. Missing parameters may be filled in from the context or the environment.
    
    A ConfigurationProvider provides access to the personal layer of configuration data of the current user context. It should in most cases be used when using the configuration data, although for most contexts an AdministrationProvider can be used as a drop-in replacement.

    See Also:
        `API AdministrationProvider <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1configuration_1_1AdministrationProvider.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.configuration'
    __ooo_full_ns__: str = 'com.sun.star.configuration.AdministrationProvider'
    __ooo_type_name__: str = 'service'


__all__ = ['AdministrationProvider']

