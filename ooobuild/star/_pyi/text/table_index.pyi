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
# Namespace: com.sun.star.text
from .base_index import BaseIndex as BaseIndex_8f0d0a40

class TableIndex(BaseIndex_8f0d0a40):
    """
    Service Class

    specifies service of table indexes within a document.

    See Also:
        `API TableIndex <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1text_1_1TableIndex.html>`_
    """
    @property
    def CreateFromLabels(self) -> bool:
        """
        determines if the name or the label of an object is used to create the index.
        """
        ...

    @CreateFromLabels.setter
    def CreateFromLabels(self, value: bool) -> None:
        ...
    @property
    def LabelCategory(self) -> str:
        """
        determines the name of the sequence field that is evaluated to create the index.
        """
        ...

    @LabelCategory.setter
    def LabelCategory(self, value: str) -> None:
        ...
    @property
    def LabelDisplayType(self) -> int:
        """
        determines the way the paragraph containing a label is included in the index.
        """
        ...

    @LabelDisplayType.setter
    def LabelDisplayType(self, value: int) -> None:
        ...

