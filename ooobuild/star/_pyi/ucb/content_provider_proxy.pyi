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
# Namespace: com.sun.star.ucb
from .x_content_provider import XContentProvider as XContentProvider_d4150cc0
from .x_content_provider_supplier import XContentProviderSupplier as XContentProviderSupplier_48e61014
from .x_parameterized_content_provider import XParameterizedContentProvider as XParameterizedContentProvider_9dc6120d

class ContentProviderProxy(XContentProvider_d4150cc0, XContentProviderSupplier_48e61014, XParameterizedContentProvider_9dc6120d):
    """
    Service Class

    is a proxy for a content provider.
    
    Implementing a content provider proxy can be useful if the creation of the real content provider object shall be deferred for some reason (i.e. performance) until the first method gets called on it. Instead of instantiating and registering the real provider at the UCB, a proxy for the real provider can be created and registered at the UCB.

    See Also:
        `API ContentProviderProxy <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1ucb_1_1ContentProviderProxy.html>`_
    """
    ...

