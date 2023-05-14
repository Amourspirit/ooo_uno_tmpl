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


class LeftRightMargin(object):
    """
    Struct Class

    specifies a left and right margin.
    
    **since**
    
        OOo 2.0

    See Also:
        `API LeftRightMargin <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1frame_1_1status_1_1LeftRightMargin.html>`_
    """
    typeName: Literal['com.sun.star.frame.status.LeftRightMargin']

    def __init__(self, Left: typing.Optional[int] = ..., Right: typing.Optional[int] = ...) -> None:
        """
        Constructor

        Arguments:
            Left (int, optional): Left value.
            Right (int, optional): Right value.
        """
        ...


    @property
    def Left(self) -> int:
        """
        specifies a left side margin in 1/100th mm.
        """
        ...


    @property
    def Right(self) -> int:
        """
        specifies a right side margin in 1/100th mm.
        """
        ...


