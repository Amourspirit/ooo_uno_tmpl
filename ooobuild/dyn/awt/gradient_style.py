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
# Namespace: com.sun.star.awt
# Libre Office Version: 7.4
from __future__ import annotations
import uno
from typing import TYPE_CHECKING


if TYPE_CHECKING:

    class GradientStyle(uno.Enum):
        """
        Enum Class


        See Also:
            `API GradientStyle <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1awt.html#aa6b9d577a1700f29923f49f7b77d165f>`_
        """
        __ooo_ns__: str = ...
        __ooo_full_ns__: str = ...
        __ooo_type_name__: str = ...

        @property
        def typeName(self) -> str:
            ...

        AXIAL: GradientStyle = ...
        """
        specifies an axial gradient.
        """
        ELLIPTICAL: GradientStyle = ...
        """
        specifies an elliptical gradient.
        """
        LINEAR: GradientStyle = ...
        """
        specifies a linear gradient.
        """
        RADIAL: GradientStyle = ...
        """
        specifies a radial gradient.
        """
        RECT: GradientStyle = ...
        """
        specifies a gradient in the shape of a rectangle.
        """
        SQUARE: GradientStyle = ...
        """
        specifies a gradient in the shape of a square.
        """

else:

    from ooo.helper.enum_helper import UnoEnumMeta
    class GradientStyle(metaclass=UnoEnumMeta, type_name="com.sun.star.awt.GradientStyle", name_space="com.sun.star.awt"):
        """Dynamically created class that represents ``com.sun.star.awt.GradientStyle`` Enum. Class loosely mimics Enum"""
        pass

__all__ = ['GradientStyle']

