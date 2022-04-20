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
# Namespace: com.sun.star.rendering
# Libre Office Version: 7.2
from typing_extensions import Literal
import typing
from ..geometry.real_size2_d import RealSize2D as RealSize2D_ca1a0c09


class AnimationAttributes(object):
    """
    Struct Class

    This structure contains attributes needed to run an animation.
    
    **since**
    
        OOo 2.0

    See Also:
        `API AnimationAttributes <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1rendering_1_1AnimationAttributes.html>`_
    """
    typeName: Literal['com.sun.star.rendering.AnimationAttributes']

    def __init__(self, Duration: typing.Optional[float] = ..., RepeatMode: typing.Optional[int] = ..., UntransformedSize: typing.Optional[RealSize2D_ca1a0c09] = ...) -> None:
        """
        Constructor

        Arguments:
            Duration (float, optional): Duration value.
            RepeatMode (int, optional): RepeatMode value.
            UntransformedSize (RealSize2D, optional): UntransformedSize value.
        """


    @property
    def Duration(self) -> float:
        """
        Preferred duration of the animation sequence in seconds.
        """


    @property
    def RepeatMode(self) -> int:
        """
        Repeat mode of the animation sequence.
        
        This value determines how the [0,1] parameter space of the animation should be swept through. Permissible values are given in AnimationRepeat.
        """


    @property
    def UntransformedSize(self) -> RealSize2D_ca1a0c09:
        """
        Size of the untransformed animation sequence.
        
        This value specifies the size of the animation when rendered with the identity view transform. This permits e.g. XSprite implementations to cache rendered animation content in finite-sized bitmaps.
        """


