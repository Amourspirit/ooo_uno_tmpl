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
# Namespace: com.sun.star.text
from .base_index_mark import BaseIndexMark as BaseIndexMark_bbb30bcb

class DocumentIndexMark(BaseIndexMark_bbb30bcb):
    """
    Service Class

    is a TextRange which is explicitly marked as an index entry for a DocumentIndex.

    See Also:
        `API DocumentIndexMark <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1text_1_1DocumentIndexMark.html>`_
    """
    @property
    def IsMainEntry(self) -> bool:
        """
        determines if this entry is a main entry.
        
        In a document index this entry will be emphasized by assigning a character style to it.
        """
        ...
    @property
    def PrimaryKey(self) -> str:
        """
        contains the primary key of the index entry.
        
        It is used to build a hierarchical document index.
        """
        ...
    @property
    def SecondaryKey(self) -> str:
        """
        contains the secondary key of the index entry.
        
        It is used to build a hierarchical document index.
        """
        ...

