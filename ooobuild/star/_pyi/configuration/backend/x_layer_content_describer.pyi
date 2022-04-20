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
# Namespace: com.sun.star.configuration.backend
from typing_extensions import Literal
import typing
from ...uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .property_info import PropertyInfo as PropertyInfo_b5d21267
    from .x_layer_handler import XLayerHandler as XLayerHandler_c5d61289

class XLayerContentDescriber(XInterface_8f010a43):
    """
    describe the contents of a layer to an XLayerHandler object.
    
    The contents of the layer is contained in the sequence of PropertyInfo structures

    See Also:
        `API XLayerContentDescriber <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1configuration_1_1backend_1_1XLayerContentDescriber.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.configuration.backend.XLayerContentDescriber']

    def describeLayer(self, aHandler: 'XLayerHandler_c5d61289', aPropertyInfos: 'typing.Tuple[PropertyInfo_b5d21267, ...]') -> None:
        """
        describes the contents of the layer to an XLayerHandler.

        Raises:
            com.sun.star.lang.NullPointerException: ``NullPointerException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
            MalformedDataException: ``MalformedDataException``
        """

