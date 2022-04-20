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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.drawing
from typing_extensions import Literal
from ..uno.x_interface import XInterface as XInterface_8f010a43

class XShapeDescriptor(XInterface_8f010a43):
    """
    offers some settings which are allowed even for objects which are not yet inserted into a draw page.
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API XShapeDescriptor <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1drawing_1_1XShapeDescriptor.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.drawing.XShapeDescriptor']

    def getShapeType(self) -> str:
        """
        """

