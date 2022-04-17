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
# Namespace: com.sun.star.style
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73

class XStyleLoader(XInterface_8f010a43):
    """
    enables the object to import styles from documents.

    See Also:
        `API XStyleLoader <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1style_1_1XStyleLoader.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.style.XStyleLoader']

    def getStyleLoaderOptions(self) -> 'typing.Tuple[PropertyValue_c9610c73, ...]':
        """
        """
    def loadStylesFromURL(self, URL: str, aOptions: 'typing.Tuple[PropertyValue_c9610c73, ...]') -> None:
        """
        loads styles from a document at the given URL.
        
        If OverwriteStyles is TRUE, then all styles will be loaded. Otherwise, only styles which are not already defined in this document are loaded.
        
        The sequence<PropertyValue> has the following, optional items:
        
        As the default, all supported style families are loaded and existing styles are overwritten.

        Raises:
            com.sun.star.io.IOException: ``IOException``
        """

