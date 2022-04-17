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
# Namespace: com.sun.star.document
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73

class XDocumentInsertable(XInterface_8f010a43):
    """
    makes it possible to import a document from a given URL into this document.

    See Also:
        `API XDocumentInsertable <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1document_1_1XDocumentInsertable.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.document.XDocumentInsertable']

    def insertDocumentFromURL(self, aURL: str, aOptions: 'typing.Tuple[PropertyValue_c9610c73, ...]') -> None:
        """
        inserts the document that is specified by the URL.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.io.IOException: ``IOException``
        """
