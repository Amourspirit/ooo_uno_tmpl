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
# Namespace: com.sun.star.drawing
# Libre Office Version: 7.3
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    import uno
"""
Enum



See Also:
    `API TextureProjectionMode <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1drawing.html#ae1e109a5c70543e3b92db3b854fd3acb>`_
"""
typeName: str = 'com.sun.star.drawing.TextureProjectionMode'

OBJECTSPECIFIC: 'uno.Enum'
"""
This value specifies that the standard object projection method is used.
"""
PARALLEL: 'uno.Enum'
"""
the 3D objects are drawn in the parallel projection.

This value specifies a flat parallel projection in the specified degree of freedom (X or Y).
"""
SPHERE: 'uno.Enum'
"""
forces normals to think that the object is a sphere.

This value forces projection to wrapping in X and/or Y.
"""

