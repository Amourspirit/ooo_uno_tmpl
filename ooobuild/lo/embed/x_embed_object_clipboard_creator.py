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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.embed
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73
    from .inserted_object_info import InsertedObjectInfo as InsertedObjectInfo_a0e0e26
    from .x_storage import XStorage as XStorage_8e460a32

class XEmbedObjectClipboardCreator(XInterface_8f010a43):
    """
    allows to create and initialize a new embedded object from clipboard.
    
    This interface contains methods that can help to create and initialize an embedded object based on system clipboard.

    See Also:
        `API XEmbedObjectClipboardCreator <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1embed_1_1XEmbedObjectClipboardCreator.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.embed'
    __ooo_full_ns__: str = 'com.sun.star.embed.XEmbedObjectClipboardCreator'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.embed.XEmbedObjectClipboardCreator'

    @abstractmethod
    def createInstanceInitFromClipboard(self, xStorage: 'XStorage_8e460a32', sEntryName: str, aObjectArgs: 'typing.Tuple[PropertyValue_c9610c73, ...]') -> 'InsertedObjectInfo_a0e0e26':
        """
        creates a new object and initializes it from the system clipboard.
        
        In case specified entry exists it's contents are ignored and will be overwritten on storing.
        
        The clipboard can provide a number of choices that are container related. This information will be returned in the InsertedObjectInfo object.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.io.IOException: ``IOException``
            com.sun.star.uno.Exception: ``Exception``
        """

__all__ = ['XEmbedObjectClipboardCreator']
