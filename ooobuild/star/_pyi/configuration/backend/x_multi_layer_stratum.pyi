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
    from .x_layer import XLayer as XLayer_4cd50fcb
    from .x_updatable_layer import XUpdatableLayer as XUpdatableLayer_ec97135d

class XMultiLayerStratum(XInterface_8f010a43):
    """
    Handles access to a stratum consisting of multiple layers in a single configuration data repository.
    
    The interface provides access to data for multiple entities and timestamp-checking capabilities for efficient caching.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API XMultiLayerStratum <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1configuration_1_1backend_1_1XMultiLayerStratum.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.configuration.backend.XMultiLayerStratum']

    def getLayer(self, aLayerId: str, aTimestamp: str) -> 'XLayer_4cd50fcb':
        """
        retrieves a layer associated to a layer id, if newer than indicated.
        
        A timestamp can be provided, which is used to indicate a point in time. The layer should be returned only if is modified since that time.
        
        Layer ids can be obtained from XMultiLayerStratum.listLayerIds() or XMultiLayerStratum.getUpdateLayerId().
        
        An empty timestamp indicates, that the layer should be retrieved irrespective of its modification time.
        
        The format and meaning of a timestamp depends on the implementation. Timestamps can be obtained using com.sun.star.util.XTimeStamped.getTimestamp().

        Raises:
            BackendAccessException: ``BackendAccessException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    def getLayers(self, aLayerIds: 'typing.Tuple[str, ...]', aTimestamp: str) -> 'typing.Tuple[XLayer_4cd50fcb, ...]':
        """
        retrieves the layers associated to a series of layer ids, if newer than indicated.
        
        A timestamp can be provided, which is used to indicate a point in time. Only layers that are modified since that time should be returned. The same timestamp is used for all layers.
        
        Layer ids can be obtained from XMultiLayerStratum.listLayerIds().
        
        An empty timestamp indicates, that the layers should be retrieved irrespective of their modification time.
        
        The format and meaning of a timestamp depends on the implementation. Timestamps can be obtained using com.sun.star.util.XTimeStamped.getTimestamp().
        
        The list has the same length as aLayerIds. Each layer object is associated to the layer id in the corresponding position.
        
        For layers that are newer than indicated by the timestamp, the list contains a NULL element.

        Raises:
            BackendAccessException: ``BackendAccessException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    def getMultipleLayers(self, aLayerIds: 'typing.Tuple[str, ...]', aTimestamps: 'typing.Tuple[str, ...]') -> 'typing.Tuple[XLayer_4cd50fcb, ...]':
        """
        retrieves the layers associated to a series of layer ids, if newer than indicated for each layer.
        
        For each layer an individual timestamp can be provided, which is used to indicate the last known version of the layer. Only layers that are modified since that time should be returned.
        
        Layer ids can be obtained from XMultiLayerStratum.listLayerIds().
        
        This list must have the same length as aLayerIds. Timestamps are matched to layer ids by their position.
        
        An empty timestamp indicates, that the associated layer should be retrieved irrespective of its modification time.
        
        The format and meaning of a timestamp depends on the implementation. Timestamps can be obtained using com.sun.star.util.XTimeStamped.getTimestamp().
        
        The list has the same length as aLayerIds. Each layer object is associated to the layer id in the corresponding position.
        
        For layers that are newer than indicated by the corresponding timestamp, the list contains a NULL element.

        Raises:
            BackendAccessException: ``BackendAccessException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    def getUpdatableLayer(self, aLayerId: str) -> 'XUpdatableLayer_ec97135d':
        """
        retrieves a writable representation of the layer associated to a layer id.
        
        A layer id for writing can be obtained from XMultiLayerStratum.getUpdateLayerId().

        Raises:
            BackendAccessException: ``BackendAccessException``
            com.sun.star.lang.NoSupportException: ``NoSupportException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    def getUpdateLayerId(self, aComponent: str, aEntity: str) -> str:
        """
        identifies the layer which should be modified to update data of a component on behalf of an entity.
        
        The layer id returned is one of the layer ids obtained from XMultiLayerStratum.listLayerIds() for the same component and entity.

        Raises:
            BackendAccessException: ``BackendAccessException``
            com.sun.star.lang.NoSupportException: ``NoSupportException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    def listLayerIds(self, aComponent: str, aEntity: str) -> 'typing.Tuple[str, ...]':
        """
        identifies the layers within this stratum which should be read and merged to determine data of a component for an entity
        
        The list is ordered by priority. Typically the most general layers (global defaults, entire organization) are first, more specific layers (associated to specific groups or roles) are next and the entity's own data is last.

        Raises:
            BackendAccessException: ``BackendAccessException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...


