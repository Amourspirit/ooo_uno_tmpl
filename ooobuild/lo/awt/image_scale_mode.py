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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.awt


class ImageScaleMode(object):
    """
    Const Class

    defines modes how an image displayed in a given area should be scaled to fit this area

    See Also:
        `API ImageScaleMode <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1awt_1_1ImageScaleMode.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt'
    __ooo_full_ns__: str = 'com.sun.star.awt.ImageScaleMode'
    __ooo_type_name__: str = 'const'

    NONE = 0
    """
    specifies that no scaling should happen at all
    """
    ISOTROPIC = 1
    """
    specifies that the image should be scaled up or down to the size of the surrounding area isotropically, i.e.
    
    by keeping its aspect ratio.
    """
    ANISOTROPIC = 2
    """
    specifies that the image should be scaled up or down to the size of the surrounding area anisotropically.
    
    The image will finally cover all of the surrounding area, but its dimensions might be distorted.
    """

__all__ = ['ImageScaleMode']
