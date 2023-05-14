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
# Namespace: com.sun.star.frame.status
# Libre Office Version: 7.4
from typing_extensions import Literal
import typing


class LeftRightMarginScale(object):
    """
    Struct Class

    specifies a left and right margin.
    
    **since**
    
        LibreOffice 5.3

    See Also:
        `API LeftRightMarginScale <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1frame_1_1status_1_1LeftRightMarginScale.html>`_
    """
    typeName: Literal['com.sun.star.frame.status.LeftRightMarginScale']

    def __init__(self, TextLeft: typing.Optional[int] = ..., Left: typing.Optional[int] = ..., Right: typing.Optional[int] = ..., FirstLine: typing.Optional[int] = ..., ScaleLeft: typing.Optional[int] = ..., ScaleRight: typing.Optional[int] = ..., ScaleFirstLine: typing.Optional[int] = ..., AutoFirstLine: typing.Optional[bool] = ...) -> None:
        """
        Constructor

        Arguments:
            TextLeft (int, optional): TextLeft value.
            Left (int, optional): Left value.
            Right (int, optional): Right value.
            FirstLine (int, optional): FirstLine value.
            ScaleLeft (int, optional): ScaleLeft value.
            ScaleRight (int, optional): ScaleRight value.
            ScaleFirstLine (int, optional): ScaleFirstLine value.
            AutoFirstLine (bool, optional): AutoFirstLine value.
        """
        ...


    @property
    def TextLeft(self) -> int:
        """
        specifies a left text margin in 1/100th mm.
        """
        ...


    @property
    def Left(self) -> int:
        """
        specifies a left margin in 1/100th mm.
        """
        ...


    @property
    def Right(self) -> int:
        """
        specifies a right margin in 1/100th mm.
        """
        ...


    @property
    def FirstLine(self) -> int:
        """
        specifies a first line indent relative to TextLeft in 1/100th mm.
        """
        ...


    @property
    def ScaleLeft(self) -> int:
        """
        specifies a scale value for the left margin in percent.
        """
        ...


    @property
    def ScaleRight(self) -> int:
        """
        specifies a scale value for the right margin in percent.
        """
        ...


    @property
    def ScaleFirstLine(self) -> int:
        """
        specifies a scale value for the first line margin in percent.
        """
        ...


    @property
    def AutoFirstLine(self) -> bool:
        """
        specifies if the automatic calculation of the first line indent occurs.
        """
        ...


