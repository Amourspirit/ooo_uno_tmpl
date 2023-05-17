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
# Enum
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.awt
# Libre Office Version: 7.4
from __future__ import annotations
import uno


class RasterOperation(uno.Enum):
    """
    Enum


    See Also:
        `API RasterOperation <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1awt.html#a54da390665a5b42acc81143cd24926fd>`_
    """
    typeName: str = 'com.sun.star.awt.RasterOperation'

    ALLBITS: PyiRasterOperation = ...
    """
    All bits which are affected by this operation are set to 1.
    """
    INVERT: PyiRasterOperation = ...
    """
    All bits which are affected by this operation are inverted.
    """
    OVERPAINT: PyiRasterOperation = ...
    """
    sets all pixel as written in the output operation.
    """
    XOR: PyiRasterOperation = ...
    """
    uses the pixel written as one and the current pixel as the other operator of an exclusive or-operation.
    """
    ZEROBITS: PyiRasterOperation = ...
    """
    All bits which are affected by this operation are set to 0.
    """

