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
# Namespace: com.sun.star.auth
from .xsso_password_cache import XSSOPasswordCache as XSSOPasswordCache_ec0f0d2e

class SSOPasswordCache(XSSOPasswordCache_ec0f0d2e):
    """
    Service Class

    provided as a convenience for simple username/password based Single Sign-on implementations which don't provide some sort of authentication information repository.
    
    provides access to a cache which maps usernames to associated passwords. Individual cache entries may be persisted.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API SSOPasswordCache <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1auth_1_1SSOPasswordCache.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.auth'
    __ooo_full_ns__: str = 'com.sun.star.auth.SSOPasswordCache'
    __ooo_type_name__: str = 'service'



__all__ = ['SSOPasswordCache']

