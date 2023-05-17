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
# Namespace: com.sun.star.drawing
# Libre Office Version: 7.4
from __future__ import annotations
import uno
from typing import Any, cast, TYPE_CHECKING


if TYPE_CHECKING:

    from com.sun.star.drawing.NormalsKind import FLAT as NORMALS_KIND_FLAT
    from com.sun.star.drawing.NormalsKind import SPECIFIC as NORMALS_KIND_SPECIFIC
    from com.sun.star.drawing.NormalsKind import SPHERE as NORMALS_KIND_SPHERE

    class NormalsKind(uno.Enum):
        """
        Enum Class


        See Also:
            `API NormalsKind <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1drawing.html#a2f040e92a1488875fb14c6ecc377630b>`_
        """

        def __init__(self, value: Any) -> None:
            super().__init__('com.sun.star.drawing.NormalsKind', value)

        __ooo_ns__: str = 'com.sun.star.drawing'
        __ooo_full_ns__: str = 'com.sun.star.drawing.NormalsKind'
        __ooo_type_name__: str = 'enum'

        FLAT = cast("NormalsKind", NORMALS_KIND_FLAT)
        """
        forces one normal per flat part.
        
        With FLAT shading, the faces of the object are rendered in a solid color.
        """
        SPECIFIC = cast("NormalsKind", NORMALS_KIND_SPECIFIC)
        """
        does not produce standard normals, but leaves the object-specific ones untouched.
        """
        SPHERE = cast("NormalsKind", NORMALS_KIND_SPHERE)
        """
        forces normals to think that the object is a sphere.
        
        This value forces projection to wrapping in X and/or Y.
        """

else:

    from ooo.helper.enum_helper import UnoEnumMeta
    class NormalsKind(metaclass=UnoEnumMeta, type_name="com.sun.star.drawing.NormalsKind", name_space="com.sun.star.drawing"):
        """Dynamically created class that represents ``com.sun.star.drawing.NormalsKind`` Enum. Class loosely mimics Enum"""
        pass

__all__ = ['NormalsKind']
