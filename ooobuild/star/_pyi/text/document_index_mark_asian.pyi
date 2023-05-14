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
# Namespace: com.sun.star.text
from abc import ABC

class DocumentIndexMarkAsian(ABC):
    """
    Service Class

    is a TextRange which is explicitly marked as an index entry for a DocumentIndex.
    
    For Asian languages the user can provide an additional string which is used for sorting. If the user does not provide these strings, they are not considered for sorting.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API DocumentIndexMarkAsian <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1text_1_1DocumentIndexMarkAsian.html>`_
    """
    @property
    def PrimaryKeyReading(self) -> str:
        """
        contains the reading of the primary key of the index entry.
        
        It is used to build a hierarchical document index.
        """
        ...
    @PrimaryKeyReading.setter
    def PrimaryKeyReading(self, value: str) -> None:
        ...
    @property
    def SecondaryKeyReading(self) -> str:
        """
        contains the reading the secondary key of the index entry.
        
        It is used to build a hierarchical document index.
        """
        ...
    @SecondaryKeyReading.setter
    def SecondaryKeyReading(self, value: str) -> None:
        ...
    @property
    def TextReading(self) -> str:
        """
        contains the reading of the string which has been chosen for the index entry.
        """
        ...
    @TextReading.setter
    def TextReading(self, value: str) -> None:
        ...

