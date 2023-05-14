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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.animations
from typing_extensions import Literal
import typing
from ..container.x_child import XChild as XChild_a6390b07
if typing.TYPE_CHECKING:
    from ..beans.named_value import NamedValue as NamedValue_a37a0af3

class XAnimationNode(XChild_a6390b07):
    """

    See Also:
        `API XAnimationNode <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1animations_1_1XAnimationNode.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.animations.XAnimationNode']

    @property
    def UserData(self) -> 'typing.Tuple[NamedValue_a37a0af3, ...]':
        """
        """
        ...

    @UserData.setter
    def UserData(self, value: 'typing.Tuple[NamedValue_a37a0af3, ...]') -> None:
        ...

    @property
    def Acceleration(self) -> float:
        """
        defines the acceleration for this element.
        
        Element time will accelerate from a rate of 0 at the beginning up to a run rate, over the course of the specified proportion of the simple duration.
        
        Acceleration is a value between 0 (no acceleration) and 1 (acceleration until end of the elements duration).
        """
        ...

    @Acceleration.setter
    def Acceleration(self, value: float) -> None:
        ...
    @property
    def AutoReverse(self) -> bool:
        """
        defines the auto reverse settings for this element.
        
        AutoReverse is
        """
        ...

    @AutoReverse.setter
    def AutoReverse(self, value: bool) -> None:
        ...
    @property
    def Begin(self) -> object:
        """
        a sequence of values that define the beginning of this element Begin is
        """
        ...

    @Begin.setter
    def Begin(self, value: object) -> None:
        ...
    @property
    def Decelerate(self) -> float:
        """
        defines the deceleration for this element.
        
        Element time will deceleration from a run rate to a rate of 0 at the ending, over the course of the specified proportion of the simple duration.
        
        Decelerate is a value between 0 (no deceleration) and 1 (deceleration from beginning of the elements duration).
        """
        ...

    @Decelerate.setter
    def Decelerate(self, value: float) -> None:
        ...
    @property
    def Duration(self) -> object:
        """
        defines the length of the simple duration.
        
        Duration is
        """
        ...

    @Duration.setter
    def Duration(self, value: object) -> None:
        ...
    @property
    def End(self) -> object:
        """
        a sequence of values that define the ending of this element End is
        """
        ...

    @End.setter
    def End(self, value: object) -> None:
        ...
    @property
    def EndSync(self) -> object:
        """
        controls the implicit duration of time containers, as a function of the children.
        
        The EndSync attribute is only valid for par and excl time container elements, and media elements with timed children (e.g. animate or area elements).
        
        EndSync is either a short constant from EndSync, an interface reference to a child XTimeContainer or VOID.
        """
        ...

    @EndSync.setter
    def EndSync(self, value: object) -> None:
        ...
    @property
    def Fill(self) -> int:
        """
        the attribute that specify the behavior how an element should be extended beyond the active duration by freezing the final state of the element.
        
        Fill is a value from AnimationFill.
        """
        ...

    @Fill.setter
    def Fill(self, value: int) -> None:
        ...
    @property
    def FillDefault(self) -> int:
        """
        the default value for the fill behavior for this element and all descendants.
        
        FillDefault is
        """
        ...

    @FillDefault.setter
    def FillDefault(self, value: int) -> None:
        ...
    @property
    def RepeatCount(self) -> object:
        """
        the number of iterations of the simple duration.
        
        RepeatCount is
        """
        ...

    @RepeatCount.setter
    def RepeatCount(self, value: object) -> None:
        ...
    @property
    def RepeatDuration(self) -> object:
        """
        the total duration for repeat.
        
        RepeatDuration is
        """
        ...

    @RepeatDuration.setter
    def RepeatDuration(self, value: object) -> None:
        ...
    @property
    def Restart(self) -> int:
        """
        defines the restart behavior of this element.
        
        Restart is a short value from AnimationRestart.
        """
        ...

    @Restart.setter
    def Restart(self, value: int) -> None:
        ...
    @property
    def RestartDefault(self) -> int:
        """
        defines the default restart behavior for this element and all descendants.
        """
        ...

    @RestartDefault.setter
    def RestartDefault(self, value: int) -> None:
        ...
    @property
    def Type(self) -> int:
        """
        a value from AnimationNodeType.
        """
        ...

    @Type.setter
    def Type(self, value: int) -> None:
        ...

