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
# Namespace: com.sun.star.embed
import typing
from .xole_simple_storage import XOLESimpleStorage as XOLESimpleStorage_f6db0d7c
if typing.TYPE_CHECKING:
    from ..io.x_input_stream import XInputStream as XInputStream_98d40ab4
    from ..io.x_stream import XStream as XStream_678908a4

class OLESimpleStorage(XOLESimpleStorage_f6db0d7c):
    """
    Service Class

    This service provides a simple functionality to allow read/write the storages in OLE storage format.

    See Also:
        `API OLESimpleStorage <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1embed_1_1OLESimpleStorage.html>`_
    """
    def createFromInputStream(self, xInputStream: 'XInputStream_98d40ab4', bNoTempCopy: bool) -> None:
        """
        is used to initialize the object on it's creation.
        """
        ...
    def createFromStream(self, xStream: 'XStream_678908a4', bNoTempCopy: bool) -> None:
        """
        is used to initialize the object on it's creation.
        """
        ...

