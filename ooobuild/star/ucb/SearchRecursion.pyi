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
# Enum
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.ucb
# Libre Office Version: 2024.2
from __future__ import annotations
from typing import Protocol, Any
from typing_extensions import Literal


class SearchRecursionProto(Protocol):
    """Protocol for SearchRecursion"""

    @property
    def typeName(self) -> Literal["com.sun.star.ucb.SearchRecursion"]:
        ...
    value: Any
    DEEP: SearchRecursionProto
    NONE: SearchRecursionProto
    ONE_LEVEL: SearchRecursionProto

DEEP: SearchRecursionProto
"""
Searches through the complete hierarchy of all sub-objects.
"""
NONE: SearchRecursionProto
"""
Does not search through any sub-objects.
"""
ONE_LEVEL: SearchRecursionProto
"""
Only searches through sub-objects of the first hierarchy level.
"""

