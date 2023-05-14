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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.sheet
# Libre Office Version: 7.3
from typing_extensions import Literal
import typing
from .single_reference import SingleReference as SingleReference_e27e0d12


class ComplexReference(object):
    """
    Struct Class

    contains a reference to a cell range.

    See Also:
        `API ComplexReference <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1sheet_1_1ComplexReference.html>`_
    """
    typeName: Literal['com.sun.star.sheet.ComplexReference']

    def __init__(self, Reference1: typing.Optional[SingleReference_e27e0d12] = ..., Reference2: typing.Optional[SingleReference_e27e0d12] = ...) -> None:
        """
        Constructor

        Arguments:
            Reference1 (SingleReference, optional): Reference1 value.
            Reference2 (SingleReference, optional): Reference2 value.
        """
        ...


    @property
    def Reference1(self) -> SingleReference_e27e0d12:
        """
        is the first reference.
        """
        ...

    @Reference1.setter
    def Reference1(self, value: SingleReference_e27e0d12) -> None:
        ...

    @property
    def Reference2(self) -> SingleReference_e27e0d12:
        """
        is the second reference.
        """
        ...

    @Reference2.setter
    def Reference2(self, value: SingleReference_e27e0d12) -> None:
        ...

