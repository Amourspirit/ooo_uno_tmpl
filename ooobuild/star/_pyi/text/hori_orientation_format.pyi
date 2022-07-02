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
# Libre Office Version: 7.2
from typing_extensions import Literal
import typing


class HoriOrientationFormat(object):
    """
    Struct Class

    describes the horizontal orientation of an object.
    
    If HorizontalOrientation == HORI_NONE, then the value \"XPos\" describes the distance from the left border of the context. Otherwise \"XPos\" is ignored.
    
    The following flags are used to adapt the position of the object to odd and even pages. If \"PositionToggle\" is set, then the horizontal position is mirrored.

    See Also:
        `API HoriOrientationFormat <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1text_1_1HoriOrientationFormat.html>`_
    """
    typeName: Literal['com.sun.star.text.HoriOrientationFormat']

    def __init__(self, XPos: typing.Optional[int] = ..., HorizontalOrientation: typing.Optional[int] = ..., HorizontalRelation: typing.Optional[int] = ..., PositionToggle: typing.Optional[bool] = ...) -> None:
        """
        Constructor

        Arguments:
            XPos (int, optional): XPos value.
            HorizontalOrientation (int, optional): HorizontalOrientation value.
            HorizontalRelation (int, optional): HorizontalRelation value.
            PositionToggle (bool, optional): PositionToggle value.
        """
        ...


    @property
    def XPos(self) -> int:
        """
        contains the distance from the left border.
        
        Only valid if the property HorizontalOrientation contains the value HORI_NONE.
        """
        ...


    @property
    def HorizontalOrientation(self) -> int:
        """
        determines the horizontal alignment of an object.
        
        The values refer to com.sun.star.HoriOrientation.
        """
        ...


    @property
    def HorizontalRelation(self) -> int:
        """
        determines the reference position of the horizontal alignment.
        """
        ...


    @property
    def PositionToggle(self) -> bool:
        """
        determines if the orientation toggles between left and right pages.
        """
        ...


