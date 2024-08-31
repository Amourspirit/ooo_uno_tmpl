# coding: utf-8
#
# Copyright 2023-2024 :Barry-Thomas-Paul: Moss
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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.presentation
from __future__ import annotations
import typing
from abc import abstractproperty, ABC
if typing.TYPE_CHECKING:
    from ..util.color import Color as Color_68e908c5
    from com.sun.star.presentation.AnimationEffect import AnimationEffectProto  # type: ignore
    from com.sun.star.presentation.ClickAction import ClickActionProto  # type: ignore
    from com.sun.star.presentation.AnimationSpeed import AnimationSpeedProto  # type: ignore

class Shape(ABC):
    """
    Service Class

    this service is supported from all shapes inside a PresentationDocument.
    
    This usually enhances objects of type com.sun.star.drawing.Shape with presentation properties.

    See Also:
        `API Shape <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1presentation_1_1Shape.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.presentation'
    __ooo_full_ns__: str = 'com.sun.star.presentation.Shape'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def Bookmark(self) -> str:
        """
        is a generic URL for the property OnClick.
        """
        ...

    @abstractproperty
    def DimColor(self) -> Color_68e908c5:
        """
        This is the color for dimming this shape.
        
        This color is used if the property com.sun.star.drawing.Shape.DimPrev is TRUE and com.sun.star.drawing.Shape.DimHide is FALSE.
        """
        ...

    @abstractproperty
    def DimHide(self) -> bool:
        """
        If this property and the property com.sun.star.drawing.Shape.DimPrev are both TRUE, the shape is hidden instead of dimmed to a color.
        """
        ...

    @abstractproperty
    def DimPrevious(self) -> bool:
        """
        If this property is TRUE, this shape is dimmed to the color of property com.sun.star.drawing.Shape.DimColor after executing its animation effect.
        """
        ...

    @abstractproperty
    def Effect(self) -> AnimationEffectProto:
        """
        selects the animation effect of this shape.
        """
        ...

    @abstractproperty
    def IsEmptyPresentationObject(self) -> bool:
        """
        If this is a default presentation object and if it is empty, this property is TRUE.
        """
        ...

    @abstractproperty
    def IsPresentationObject(self) -> bool:
        """
        If this is a presentation object, this property is TRUE.
        
        Presentation objects are objects like TitleTextShape and OutlinerShape.
        """
        ...

    @abstractproperty
    def OnClick(self) -> ClickActionProto:
        """
        selects an action performed after the user clicks on this shape.
        """
        ...

    @abstractproperty
    def PlayFull(self) -> bool:
        """
        If this property is TRUE, the sound of this shape is played in full.
        
        The default behavior is to stop the sound after completing the animation effect.
        """
        ...

    @abstractproperty
    def PresentationOrder(self) -> int:
        """
        This is the position of this shape in the order of the shapes which can be animated on its page.
        
        The animations are executed in this order, starting at the shape with the PresentationOrder \"one.\" You can change the order by changing this number. Setting it to \"one\" makes this shape the first shape in the execution order for the animation effects.
        """
        ...

    @abstractproperty
    def Sound(self) -> str:
        """
        This is the URL to a sound file that is played while the animation effect of this shape is running.
        """
        ...

    @abstractproperty
    def SoundOn(self) -> bool:
        """
        If this property is set to TRUE, a sound is played while the animation effect is executed.
        """
        ...

    @abstractproperty
    def Speed(self) -> AnimationSpeedProto:
        """
        This is the speed of the animation effect.
        """
        ...

    @abstractproperty
    def TextEffect(self) -> AnimationEffectProto:
        """
        This is the animation effect for the text inside this shape.
        """
        ...

    @abstractproperty
    def Verb(self) -> int:
        """
        specifies an \"OLE2\" verb for the ClickAction VERB in the property com.sun.star.drawing.Shape.OnClick.
        """
        ...


__all__ = ['Shape']