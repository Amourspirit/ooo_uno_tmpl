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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.animations
from typing_extensions import Literal


class AnimationFill:
    """
    Const Class

    This constants are used for the members fill() and fillDefault() of the an XTimeContainer.

    See Also:
        `API AnimationFill <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1animations_1_1AnimationFill.html>`_
    """
    DEFAULT: Literal[0]
    """
    The fill behavior for the element is determined by the value of the XTiming.FillDefault attribute.
    
    This is the default value for the XTiming.Fill... If the application of fillDefault to an element would result in the element having a value of fill that is not allowed on that element, the element will instead have a fill value of AnimationFill.AUTO.
    """
    INHERIT: Literal[0]
    """
    Specifies that the value of this attribute (and of the fill behavior) are inherited from the XTiming.FillDefault value of the parent element.
    
    If there is no parent element, the value is AnimationFill.AUTO. This is the default value for the XTiming.FillDefault.
    """
    REMOVE: Literal[1]
    """
    Specifies that the element will not extend past the end of the last instance of the simple duration.
    """
    FREEZE: Literal[2]
    """
    Specifies that the element will extend past the end of the last instance of the simple duration by \"freezing\" the element state at that point.
    
    The parent time container of the element determines how long the element is frozen (as described immediately below).
    """
    HOLD: Literal[3]
    """
    Setting this to \"hold\" has the same effect as setting to \"freeze\", except that the element is always frozen to extend to the end of the simple duration of the parent time container of the element (independent of the type of time container).
    
    For profiles that support a layered layout model (e.g., SMIL 2.0 Language Profile), held elements (elements with fill=\"hold\") will refresh their display area when a layer is added on top then later removed.
    """
    TRANSITION: Literal[4]
    """
    Setting this to \"transition\" has the same effect as setting to \"freeze\", except that the element is removed at the end of the transition.
    
    This value is only allowed on elements with media directly associated with them. If specified on any other element (e.g. a time container element in the SMIL language profile), the attribute is ignored. See the SMIL Transitions module.
    """
    AUTO: Literal[5]
    """
    The fill behavior for this element depends on whether the element specifies any of the attributes that define the simple or active duration:
    """
