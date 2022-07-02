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
import typing
from abc import abstractproperty
from .base_index import BaseIndex as BaseIndex_8f0d0a40
if typing.TYPE_CHECKING:
    from ..container.x_index_replace import XIndexReplace as XIndexReplace_feed0dd7

class UserIndex(BaseIndex_8f0d0a40):
    """
    Service Class

    specifies service of user defined indexes within a document.

    See Also:
        `API UserIndex <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1text_1_1UserIndex.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.text'
    __ooo_full_ns__: str = 'com.sun.star.text.UserIndex'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def CreateFromEmbeddedObjects(self) -> bool:
        """
        determines if embedded objects are included in the index.
        """
        ...

    @abstractproperty
    def CreateFromGraphicObjects(self) -> bool:
        """
        determines if graphic objects are included in the index.
        """
        ...

    @abstractproperty
    def CreateFromMarks(self) -> bool:
        """
        determines if the document index marks are included in this index.
        """
        ...

    @abstractproperty
    def CreateFromTables(self) -> bool:
        """
        determines if tables are included in the index.
        """
        ...

    @abstractproperty
    def CreateFromTextFrames(self) -> bool:
        """
        determines if text frames are included in the index.
        """
        ...

    @abstractproperty
    def LevelParagraphStyles(self) -> 'XIndexReplace_feed0dd7':
        """
        contains the interface to access the paragraph style names that are included in this index.
        """
        ...

    @abstractproperty
    def UseLevelFromSource(self) -> bool:
        """
        determines if the outline level of the location of the indexed object is used as index level of the index entry.
        """
        ...

    @abstractproperty
    def UserIndexName(self) -> str:
        """
        contains the name of the user index.
        """
        ...



__all__ = ['UserIndex']

