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
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.awt
# Libre Office Version: 2024.2
from __future__ import annotations
from enum import Enum


class PushButtonType(Enum):
    """
    Enum Class


    See Also:
        `API PushButtonType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1awt.html#aa4e49c7e6c5bf2b4d010ad4a50b90ec0>`_
    """
    __ooo_ns__: str = "com.sun.star.awt"
    __ooo_full_ns__: str = "com.sun.star.awt.PushButtonType"
    __ooo_type_name__: str = "enum"

    @property
    def typeName(self) -> str:
        return "com.sun.star.awt.PushButtonType"

    CANCEL = "CANCEL"
    """
    acts like a cancel button.
    """
    HELP = "HELP"
    """
    acts like a help button.
    """
    OK = "OK"
    """
    acts like an OK button.
    """
    STANDARD = "STANDARD"
    """
    acts like a standard push button.
    """

__all__ = ["PushButtonType"]

