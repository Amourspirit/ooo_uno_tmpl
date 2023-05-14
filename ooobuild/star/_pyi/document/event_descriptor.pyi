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
# Namespace: com.sun.star.document
from abc import ABC

class EventDescriptor(ABC):
    """
    Service Class

    specifies an event binding for a document or a document content

    See Also:
        `API EventDescriptor <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1document_1_1EventDescriptor.html>`_
    """
    @property
    def EventType(self) -> str:
        """
        specifies the type of the event handler
        
        Usually this is one of the following:
        
        This list is extensible.
        """
        ...

    @EventType.setter
    def EventType(self, value: str) -> None:
        ...
    @property
    def Script(self) -> str:
        """
        specifies the script source code
        """
        ...

    @Script.setter
    def Script(self, value: str) -> None:
        ...

