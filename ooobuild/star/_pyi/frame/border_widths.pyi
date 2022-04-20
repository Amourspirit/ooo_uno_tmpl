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
# Namespace: com.sun.star.frame
# Libre Office Version: 7.2
from typing_extensions import Literal
import typing


class BorderWidths(object):
    """
    Struct Class

    specifies a border area by offsets from each side.

    See Also:
        `API BorderWidths <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1frame_1_1BorderWidths.html>`_
    """
    typeName: Literal['com.sun.star.frame.BorderWidths']

    def __init__(self, Left: typing.Optional[int] = ..., Top: typing.Optional[int] = ..., Right: typing.Optional[int] = ..., Bottom: typing.Optional[int] = ...) -> None:
        """
        Constructor

        Arguments:
            Left (int, optional): Left value.
            Top (int, optional): Top value.
            Right (int, optional): Right value.
            Bottom (int, optional): Bottom value.
        """


    @property
    def Left(self) -> int:
        """
        specifies the offset from left border.
        """


    @property
    def Top(self) -> int:
        """
        specifies the offset from top border.
        """


    @property
    def Right(self) -> int:
        """
        specifies the offset from right border.
        """


    @property
    def Bottom(self) -> int:
        """
        specifies the offset from bottom border.
        """


