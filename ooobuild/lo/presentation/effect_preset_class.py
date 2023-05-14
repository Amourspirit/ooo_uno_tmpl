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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.presentation


class EffectPresetClass(object):
    """
    Const Class

    This constants defines the class for a preset animation effect.
    
    This is stored with the name preset-class inside the com.sun.star.animations.XAnimationNode.UserData sequence. This does not manipulate the timing or synchronization. It can be used to quickly identify preset animations inside an animation hierarchy.

    See Also:
        `API EffectPresetClass <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1presentation_1_1EffectPresetClass.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.presentation'
    __ooo_full_ns__: str = 'com.sun.star.presentation.EffectPresetClass'
    __ooo_type_name__: str = 'const'

    CUSTOM = 0
    ENTRANCE = 1
    EXIT = 2
    EMPHASIS = 3
    MOTIONPATH = 4
    OLEACTION = 5
    MEDIACALL = 6

__all__ = ['EffectPresetClass']
