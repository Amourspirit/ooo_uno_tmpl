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
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.ucb
# Libre Office Version: 7.4
from __future__ import annotations
import uno
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import UnoEnumMeta
    class VerificationMode(metaclass=UnoEnumMeta, type_name="com.sun.star.ucb.VerificationMode", name_space="com.sun.star.ucb"):
        """Dynamically created class that represents ``com.sun.star.ucb.VerificationMode`` Enum. Class loosely mimics Enum"""
        pass
else:
    from ...lo.ucb.verification_mode import VerificationMode as VerificationMode

__all__ = ["VerificationMode"]
