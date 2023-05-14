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
from .homogen_matrix_line4 import HomogenMatrixLine4 as HomogenMatrixLine4_2b170ef2


class HomogenMatrix4(object):
    """
    Struct Class

    specifies a homogeneous matrix by four homogeneous lines.

    See Also:
        `API HomogenMatrix4 <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1drawing_1_1HomogenMatrix4.html>`_
    """
    typeName: Literal['com.sun.star.drawing.HomogenMatrix4']

    def __init__(self, Line1: typing.Optional[HomogenMatrixLine4_2b170ef2] = ..., Line2: typing.Optional[HomogenMatrixLine4_2b170ef2] = ..., Line3: typing.Optional[HomogenMatrixLine4_2b170ef2] = ..., Line4: typing.Optional[HomogenMatrixLine4_2b170ef2] = ...) -> None:
        """
        Constructor

        Arguments:
            Line1 (HomogenMatrixLine4, optional): Line1 value.
            Line2 (HomogenMatrixLine4, optional): Line2 value.
            Line3 (HomogenMatrixLine4, optional): Line3 value.
            Line4 (HomogenMatrixLine4, optional): Line4 value.
        """
        ...


    @property
    def Line1(self) -> HomogenMatrixLine4_2b170ef2:
        ...


    @property
    def Line2(self) -> HomogenMatrixLine4_2b170ef2:
        ...


    @property
    def Line3(self) -> HomogenMatrixLine4_2b170ef2:
        ...


    @property
    def Line4(self) -> HomogenMatrixLine4_2b170ef2:
        ...


