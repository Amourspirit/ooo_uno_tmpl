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
# Namespace: com.sun.star.linguistic2
# Libre Office Version: 7.4
from __future__ import annotations
from enum import Enum


class ConversionDirection(Enum):
    """
    Enum Class


    See Also:
        `API ConversionDirection <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1linguistic2.html#a884af1a9fc4a39bcfd381c3acaa30997>`_
    """
    __ooo_ns__: str = "com.sun.star.linguistic2"
    __ooo_full_ns__: str = "com.sun.star.linguistic2.ConversionDirection"
    __ooo_type_name__: str = "enum"

    @property
    def typeName(self) -> str:
        return "com.sun.star.linguistic2.ConversionDirection"

    FROM_LEFT = "FROM_LEFT"
    """
    the text to be looked for should match the left part of a dictionary entry.
    """
    FROM_RIGHT = "FROM_RIGHT"
    """
    the text to be looked for should match the right part of a dictionary entry.
    """

__all__ = ["ConversionDirection"]

