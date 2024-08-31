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
# Namespace: com.sun.star.xml.crypto
from __future__ import annotations
from .xnss_initializer import XNSSInitializer as XNSSInitializer_27f70ef8

class NSSInitializer(XNSSInitializer_27f70ef8):
    """
    Service Class

    This service has a particular lifecycle.
    
    If you create an instance, the NSS backend is not initialized, until some of the crypto functions are called. As a result you can effectively change the user setting to the NSS path until NSS is really used.
    
    After the first usage you have to restart LibreOffice to activate a new NSS path.
    
    **since**
    
        LibreOffice 4.0

    See Also:
        `API NSSInitializer <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1xml_1_1crypto_1_1NSSInitializer.html>`_
    """
    ...

