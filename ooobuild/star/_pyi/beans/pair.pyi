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
# Namespace: com.sun.star.beans
# Libre Office Version: 7.2
from typing_extensions import Literal
import typing


class Pair(object):
    """
    Struct Class

    A tuple, or pair.
    
    This structure allows for conveniently packing together two values of any type, and could be useful as the result type of methods.
    
    **since**
    
        OOo 3.0

    See Also:
        `API Pair <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1beans_1_1Pair_3_01T_00_01U_01_4.html>`_
    """
    typeName: Literal['com.sun.star.beans.Pair']

    def __init__(self, First: typing.Optional[object] = ..., Second: typing.Optional[object] = ...) -> None:
        """
        Constructor

        Arguments:
            First (object, optional): First value.
            Second (object, optional): Second value.
        """


    @property
    def First(self) -> object:
        """
        first object.
        """


    @property
    def Second(self) -> object:
        """
        second object.
        """


