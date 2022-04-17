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
# Libre Office Version: 7.3
# Namespace: com.sun.star.configuration.backend
from typing_extensions import Literal
import typing
from ...uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_layer import XLayer as XLayer_4cd50fcb
    from .x_updatable_layer import XUpdatableLayer as XUpdatableLayer_ec97135d

class XSingleLayerStratum(XInterface_8f010a43):
    """
    Handles access to a stratum consisting of a single layer in a configuration data repository.
    
    The interface provides timestamp-checking capabilities for efficient caching.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API XSingleLayerStratum <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1configuration_1_1backend_1_1XSingleLayerStratum.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.configuration.backend.XSingleLayerStratum']

    def getLayer(self, aComponent: str, aTimestamp: str) -> 'XLayer_4cd50fcb':
        """
        retrieves the layer data for a component, if newer than indicated.
        
        A timestamp can be provided, which is used to indicate a point in time. The layer should be returned only if is modified since that time.
        
        An empty timestamp indicates, that the layer should be retrieved irrespective of its modification time.
        
        The format and meaning of a timestamp depends on the implementation. Timestamps can be obtained using com.sun.star.util.XTimeStamped.getTimestamp().

        Raises:
            BackendAccessException: ``BackendAccessException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
    def getUpdatableLayer(self, aComponent: str) -> 'XUpdatableLayer_ec97135d':
        """
        retrieves a writable representation of the layer for a component.

        Raises:
            BackendAccessException: ``BackendAccessException``
            com.sun.star.lang.NoSupportException: ``NoSupportException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """

