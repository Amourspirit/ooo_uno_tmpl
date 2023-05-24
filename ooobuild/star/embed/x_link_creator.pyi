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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.embed
from __future__ import annotations
import typing

from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73
    from .x_storage import XStorage as XStorage_8e460a32


class XLinkCreator(XInterface_8f010a43):
    """
    allows to create and initialize a new link.
    
    Methods of this interface does not require specification of the object type, it will be detected.

    See Also:
        `API XLinkCreator <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1embed_1_1XLinkCreator.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.embed.XLinkCreator'

    def createInstanceLink(self, xStorage: XStorage_8e460a32, sEntryName: str, aArgs: typing.Tuple[PropertyValue_c9610c73, ...], aObjectArgs: typing.Tuple[PropertyValue_c9610c73, ...]) -> XInterface_8f010a43:
        """
        creates a new object based on com.sun.star.document.MediaDescriptor and initializes it as a link.
        
        In case the entry exists already all its contents will be ignored and rewritten on storing of the object.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.io.IOException: ``IOException``
            com.sun.star.uno.Exception: ``Exception``
        """
        ...


