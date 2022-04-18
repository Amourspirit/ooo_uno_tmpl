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
# Const
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.awt
from typing_extensions import Literal
"""
Const

defines modes how an image is drawn onto a device

**since**

    LibreOffice 4.1

See Also:
    `API ImageDrawMode <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1awt_1_1ImageDrawMode.html>`_
"""
NONE: Literal[0]
"""
the image is drawn as is, without any color transformation.
"""
DISABLE: Literal[1]
"""
the image is drawn as if it represented a feature whose state is disabled.
"""
HIGHLIGHT: Literal[2]
"""
the image is drawn as being highlighted.

See com.sun.star.awt.XStyleSettings.HighlightColor.
"""
DEACTIVE: Literal[4]
"""
the image is drawn as being deactivated.

See com.sun.star.awt.XStyleSettings.DeactiveColor.
"""
SEMITRANSPARENT: Literal[16]
"""
the image is drawn semi-transparent.
"""

