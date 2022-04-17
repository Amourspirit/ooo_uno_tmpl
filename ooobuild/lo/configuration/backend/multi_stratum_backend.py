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
# Namespace: com.sun.star.configuration.backend
from .backend import Backend as Backend_5cb2101e
from ...lang.x_initialization import XInitialization as XInitialization_d46c0cca

class MultiStratumBackend(Backend_5cb2101e, XInitialization_d46c0cca):
    """
    Service Class

    implements Backend provides access to a configuration database composed of one or more storage backends containing settings used by software modules.

    See Also:
        `API MultiStratumBackend <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1configuration_1_1backend_1_1MultiStratumBackend.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.configuration.backend'
    __ooo_full_ns__: str = 'com.sun.star.configuration.backend.MultiStratumBackend'
    __ooo_type_name__: str = 'service'



__all__ = ['MultiStratumBackend']

