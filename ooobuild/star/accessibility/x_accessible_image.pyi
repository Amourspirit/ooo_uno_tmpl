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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.accessibility
from __future__ import annotations
import typing

from ..uno.x_interface import XInterface as XInterface_8f010a43


class XAccessibleImage(XInterface_8f010a43):
    """
    Implement this interface to represent images and icons.
    
    This interface is used for a representation of images like icons of buttons. The corresponding interface of the Java Accessibility API is AccessibleIcon. This interface lets you retrieve an image's size and description.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API XAccessibleImage <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1accessibility_1_1XAccessibleImage.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.accessibility.XAccessibleImage'

    def getAccessibleImageDescription(self) -> str:
        """
        Returns the localized description of the image.
        
        It depends on the usage of an image whether the description should express the image's function (e.g. for icons) or the actual content of the image (e.g. for image maps or non-iconic images embedded into a document.)
        """
        ...
    def getAccessibleImageHeight(self) -> int:
        """
        Returns the height of the image.
        
        The height is returned in units specified by the parents coordinate system.
        """
        ...
    def getAccessibleImageWidth(self) -> int:
        """
        Returns the width of the image.
        
        The width is returned in units specified by the parents coordinate system.
        """
        ...


