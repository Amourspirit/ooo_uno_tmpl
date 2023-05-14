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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.drawing
# Libre Office Version: 7.4
from typing_extensions import Literal
import typing


class HomogenMatrixLine(object):
    """
    Struct Class

    specifies a single line for a HomogenMatrix.

    See Also:
        `API HomogenMatrixLine <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1drawing_1_1HomogenMatrixLine.html>`_
    """
    typeName: Literal['com.sun.star.drawing.HomogenMatrixLine']

    def __init__(self, Column1: typing.Optional[float] = ..., Column2: typing.Optional[float] = ..., Column3: typing.Optional[float] = ..., Column4: typing.Optional[float] = ...) -> None:
        """
        Constructor

        Arguments:
            Column1 (float, optional): Column1 value.
            Column2 (float, optional): Column2 value.
            Column3 (float, optional): Column3 value.
            Column4 (float, optional): Column4 value.
        """
        ...


    @property
    def Column1(self) -> float:
        ...


    @property
    def Column2(self) -> float:
        ...


    @property
    def Column3(self) -> float:
        ...


    @property
    def Column4(self) -> float:
        ...


