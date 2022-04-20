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
# Libre Office Version: 7.2
# Namespace: com.sun.star.reflection
from typing_extensions import Literal
import typing
from .x_type_description import XTypeDescription as XTypeDescription_3c210fb1

class XUnionTypeDescription(XTypeDescription_3c210fb1):
    """
    Deprecated, UNOIDL does not have a union concept.
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API XUnionTypeDescription <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1reflection_1_1XUnionTypeDescription.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.reflection.XUnionTypeDescription']

    def getDefaultDiscriminant(self) -> object:
        """
        Returns the default discriminant value.
        """
    def getDefaultMemberType(self) -> 'XTypeDescription_3c210fb1':
        """
        Returns the type of the default value.
        """
    def getDiscriminantType(self) -> 'XTypeDescription_3c210fb1':
        """
        Returns the (ordinal) discriminant type.
        """
    def getDiscriminants(self) -> 'typing.Tuple[object, ...]':
        """
        Returns discriminants of all members in order of IDL declaration.
        """
    def getMemberNames(self) -> 'typing.Tuple[str, ...]':
        """
        Returns names of all members in order of IDL declaration.
        """
    def getMemberTypes(self) -> 'typing.Tuple[XTypeDescription_3c210fb1, ...]':
        """
        Returns types of all members in order of IDL declaration.
        """

