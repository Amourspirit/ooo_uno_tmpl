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


class FontType(object):
    """
    Const

    These values are used to specify the technology of the font representation.
    
    They may be expanded in future versions.

    See Also:
        `API FontType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1awt_1_1FontType.html>`_
    """
    DONTKNOW: Literal[0]
    """
    The type of the font is not known.
    """
    RASTER: Literal[1]
    """
    specifies a raster font.
    """
    DEVICE: Literal[2]
    """
    specifies a device font.
    """
    SCALABLE: Literal[4]
    """
    specifies a scalable font.
    """

