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
# Namespace: com.sun.star.beans
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .property import Property as Property_8f4e0a76

class XPropertySetInfo(XInterface_8f010a43):
    """
    specifies a set of properties.
    
    There are three kinds of properties:
    
    The specification only describes the properties, it does not contain any values.

    See Also:
        `API XPropertySetInfo <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1beans_1_1XPropertySetInfo.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.beans.XPropertySetInfo']

    def getProperties(self) -> 'typing.Tuple[Property_8f4e0a76, ...]':
        """
        """
    def getPropertyByName(self, aName: str) -> 'Property_8f4e0a76':
        """

        Raises:
            com.sun.star.beans.UnknownPropertyException: ``UnknownPropertyException``
        """
    def hasPropertyByName(self, Name: str) -> bool:
        """
        """

