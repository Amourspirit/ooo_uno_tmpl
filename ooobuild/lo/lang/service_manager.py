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
# Namespace: com.sun.star.lang
from __future__ import annotations
import typing
from abc import abstractproperty
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
from ..container.x_content_enumeration_access import XContentEnumerationAccess as XContentEnumerationAccess_c71012d7
from ..container.x_set import XSet as XSet_90c40a4f
from .multi_service_factory import MultiServiceFactory as MultiServiceFactory_b940e5e
from .x_component import XComponent as XComponent_98dc0ab5
if typing.TYPE_CHECKING:
    from ..uno.x_component_context import XComponentContext as XComponentContext_e2e10d4a

class ServiceManager(MultiServiceFactory_b940e5e, XPropertySet_bc180bfa, XContentEnumerationAccess_c71012d7, XSet_90c40a4f, XComponent_98dc0ab5):
    """
    Service Class

    Provides a collection of implementations for services.
    
    This is a singleton you commonly find in your component context under key /singletons/com.sun.star.lang.theServiceManager.
    
    The factories are accessed with a service name. It is possible to access the factories with their implementation names, but you should avoid this.
    
    Service factories added via com.sun.star.container.XSet should support the following interfaces:
    
    Since LibreOffice 3.6, in addition to instances of XServiceInfo et al, the com.sun.star.container.XSet of at least the default C++ service manager implementation now also supports sequences of com.sun.star.beans.NamedValue in insert and remove. The sequence elements must each have a Name of uri and a string Value that is the URI of a service rdb. It is legal for there to be no such uri elements. For insert, there can additionally be an optional element with a Name of component-context and a value that is a non-null reference of type com.sun.star.uno.XComponentContext that shall be used instead of this service manager's default component context when loading the corresponding implementations.

    See Also:
        `API ServiceManager <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1lang_1_1ServiceManager.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.lang'
    __ooo_full_ns__: str = 'com.sun.star.lang.ServiceManager'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def DefaultContext(self) -> XComponentContext_e2e10d4a:
        """
        specifies the default component context to be used, if instantiating services via XMultiServiceFactory
        """
        ...


__all__ = ['ServiceManager']

