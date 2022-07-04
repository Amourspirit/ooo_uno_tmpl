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
# Namespace: com.sun.star.text
# Libre Office Version: 7.3
from typing_extensions import Literal
import typing


class VertOrientationFormat(object):
    """
    Struct Class

    describes the vertical orientation of an object.
    
    If VerticalOrientation == VERT_NONE, then the value \"YPos\" describes the distance from the top of the context. Otherwise \"YPos\" is ignored.

    See Also:
        `API VertOrientationFormat <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1text_1_1VertOrientationFormat.html>`_
    """
    typeName: Literal['com.sun.star.text.VertOrientationFormat']

    def __init__(self, YPos: typing.Optional[int] = ..., VerticalOrientation: typing.Optional[int] = ..., VerticalRelation: typing.Optional[int] = ...) -> None:
        """
        Constructor

        Arguments:
            YPos (int, optional): YPos value.
            VerticalOrientation (int, optional): VerticalOrientation value.
            VerticalRelation (int, optional): VerticalRelation value.
        """
        ...


    @property
    def YPos(self) -> int:
        """
        contains the distance from top.
        
        Only valid if the property VerticalOrientation contains the value VERT_NONE.
        """
        ...


    @property
    def VerticalOrientation(self) -> int:
        """
        determines the vertical alignment of an object.
        
        The values refer to com.sun.star.VertOrientation.
        """
        ...


    @property
    def VerticalRelation(self) -> int:
        """
        determines the reference position of the vertical alignment.
        """
        ...


