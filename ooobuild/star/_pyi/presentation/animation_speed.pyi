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
# Enum
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.presentation
# Libre Office Version: 7.2
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    import uno
from enum import Enum

class AnimationSpeed(Enum):
    """
    Enum

    

    See Also:
        `API AnimationSpeed <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1presentation.html#a07b64dc4a366b20ad5052f974ffdbf62>`_
    """
    typeName: str = 'com.sun.star.presentation.AnimationSpeed'

    FAST: 'uno.Enum'
    """
    set the speed from the animation/fade to fast.
    """
    MEDIUM: 'uno.Enum'
    """
    set the speed from the animation/fade to medium.
    """
    SLOW: 'uno.Enum'
    """
    set the speed from the animation/fade to slow.
    """

