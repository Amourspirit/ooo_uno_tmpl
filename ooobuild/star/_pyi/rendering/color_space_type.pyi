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
# Libre Office Version: 7.2
# Namespace: com.sun.star.rendering
from typing_extensions import Literal
"""
Const

Categories for color spaces.

See Also:
    `API ColorSpaceType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1rendering_1_1ColorSpaceType.html>`_
"""
DEVICE_COLOR: Literal[0]
"""
Unspecified device color space - use conversion functions to convert to standard color spaces.
"""
GREY: Literal[1]
"""
Grey-value color space.

Use this for monochrome images.
"""
RGB: Literal[2]
"""
RGB color space.
"""
CMYK: Literal[3]
"""
CMYK color space.

See Wikipedia for a thorough explanation.
"""
CMYKOG: Literal[4]
"""
CMYKOG color space.

See Wikipedia for a thorough explanation.
"""
CIEXYZ: Literal[5]
"""
Standard CieXYZ color space.

See Wikipedia for a thorough explanation.
"""
CIELAB: Literal[6]
"""
Standard CieLab color space.

See Wikipedia for a thorough explanation. Preferable over CIEXYZ if perceptual uniformity is an issue.
"""
SRGB: Literal[7]
"""
Standard sRGB color space.

See Wikipedia for a thorough explanation.
"""
HSV: Literal[8]
"""
HSV color space.

Hue saturation value. See Wikipedia for a thorough explanation.
"""
HSL: Literal[9]
"""
HSL color space.

Hue saturation lightness. See Wikipedia for a thorough explanation
"""
YCBCR: Literal[10]
"""
YCbCr color space.

See Wikipedia for a thorough explanation. This color space is common for digital video.
"""
INDEXED: Literal[11]
"""
Indexed color space.

The color components of this color space are in fact indices into a color map.
"""

