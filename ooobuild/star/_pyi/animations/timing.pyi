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
# Namespace: com.sun.star.animations
# Libre Office Version: 7.3
"""
Enum

ENUM Timing

See Also:
    `API Timing <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1animations.html#ad073880fe621cbabcd7a7cf904ef332f>`_
"""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ooo.stubs.uno_enum import UnoEnum

INDEFINITE: 'UnoEnum'
"""
specifies that a duration, end or start time is indefinite
"""
MEDIA: 'UnoEnum'
"""
specifies a simple duration as the intrinsic media duration.

This is only valid for elements that define media.
"""
