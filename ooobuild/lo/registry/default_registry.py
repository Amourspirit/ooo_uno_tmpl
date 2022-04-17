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
# Namespace: com.sun.star.registry
from .x_simple_registry import XSimpleRegistry as XSimpleRegistry_10150e9c

class DefaultRegistry(XSimpleRegistry_10150e9c):
    """
    Service Class

    implicitly supports a local registry and a read-only system registry for global information.
    
    In the context of this service, the functions open, close, and destroy from XSimpleRegistry are not supported and throw an exception if they are used.
    
    Functions of XSimpleRegistry:
    
    Functions of XRegistryKey:
    
    How to find the registries:

    See Also:
        `API DefaultRegistry <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1registry_1_1DefaultRegistry.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.registry'
    __ooo_full_ns__: str = 'com.sun.star.registry.DefaultRegistry'
    __ooo_type_name__: str = 'service'



__all__ = ['DefaultRegistry']

