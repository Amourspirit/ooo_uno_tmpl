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
# Namespace: com.sun.star.configuration.backend
from __future__ import annotations
from .x_schema import XSchema as XSchema_5ce7101f

class Schema(XSchema_5ce7101f):
    """
    Service Class

    provides read only access to a configuration component schema.
    
    A component is a set of hierarchically organized and semantically related configuration settings, e.g StarWriter settings.
    
    A component schema contains two separate sections, one which describes the templates to be used in the dynamic containers (sets) of the component and one which describes the component's data structure.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API Schema <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1configuration_1_1backend_1_1Schema.html>`_
    """
    @property
    def URL(self) -> str:
        """
        The URL of the layer data.
        
        **since**
        
            OOo 2.0
        """
        ...
    @URL.setter
    def URL(self, value: str) -> None:
        ...

