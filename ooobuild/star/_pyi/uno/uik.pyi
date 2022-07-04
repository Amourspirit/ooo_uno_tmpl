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
# Namespace: com.sun.star.uno
# Libre Office Version: 7.3
from typing_extensions import Literal
import typing


class Uik(object):
    """
    Struct Class

    Specifies a universal interface key (globally unique).
    
    This struct is deprecated. Uiks are not used anymore.
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API Uik <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1uno_1_1Uik.html>`_
    """
    typeName: Literal['com.sun.star.uno.Uik']

    def __init__(self, Data1: typing.Optional[int] = ..., Data2: typing.Optional[int] = ..., Data3: typing.Optional[int] = ..., Data4: typing.Optional[int] = ..., Data5: typing.Optional[int] = ...) -> None:
        """
        Constructor

        Arguments:
            Data1 (int, optional): Data1 value.
            Data2 (int, optional): Data2 value.
            Data3 (int, optional): Data3 value.
            Data4 (int, optional): Data4 value.
            Data5 (int, optional): Data5 value.
        """
        ...


    @property
    def Data1(self) -> int:
        """
        specifies a 4 byte data block.
        """
        ...


    @property
    def Data2(self) -> int:
        """
        specifies a 2 byte data block.
        """
        ...


    @property
    def Data3(self) -> int:
        """
        specifies a 2 byte data block.
        """
        ...


    @property
    def Data4(self) -> int:
        """
        specifies a 4 byte data block.
        """
        ...


    @property
    def Data5(self) -> int:
        """
        specifies a 4 byte data block.
        """
        ...


