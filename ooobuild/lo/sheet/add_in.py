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
# Libre Office Version: 7.4
# Namespace: com.sun.star.sheet
from ..lang.x_service_name import XServiceName as XServiceName_af090b54
from .x_add_in import XAddIn as XAddIn_7a560939
from .x_compatibility_names import XCompatibilityNames as XCompatibilityNames_1b100ec7

class AddIn(XServiceName_af090b54, XAddIn_7a560939, XCompatibilityNames_1b100ec7):
    """
    Service Class

    is the base for AddIn services that supply functions which can be called by other components.
    
    Any AddIn implementation must implement a service describing its specific set of functions. That service must contain the AddIn service, and the functions that are implemented, in one or more interfaces. The com.sun.star.lang.XServiceName interface must describe that service, and the XAddIn interface must describe the individual functions.
    
    Each AddIn function can take parameters of the following types:
    
    Each AddIn function must have one of the following return types:
    
    The sequences must contain arrays as described above for the parameter types. An XVolatileResult return value must contain an object implementing the VolatileResult service, that contains a volatile result. Subsequent calls with the same parameters must return the same object. An any return value can contain any of the other types.

    See Also:
        `API AddIn <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sheet_1_1AddIn.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.AddIn'
    __ooo_type_name__: str = 'service'



__all__ = ['AddIn']

