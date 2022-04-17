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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.embed
import typing
from abc import ABC
if typing.TYPE_CHECKING:
    from .x_storage import XStorage as XStorage_8e460a32
    from ..frame.x_dispatch_provider_interceptor import XDispatchProviderInterceptor as XDispatchProviderInterceptor_afda1275

class EmbeddedObjectDescriptor(ABC):
    """
    Service Class

    describes properties of an embedded object
    
    This service may be represented by a com.sun.star.beansPropertyValue[]. Such descriptors will be passed to different functions, included into possible load/save processes. Every member of such process can use this descriptor and may change it to actualize the information about the object. So this descriptor should be used as an in/out parameter.

    See Also:
        `API EmbeddedObjectDescriptor <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1embed_1_1EmbeddedObjectDescriptor.html>`_
    """
    @property
    def OutplaceDispatchInterceptor(self) -> 'XDispatchProviderInterceptor_afda1275':
        """
        allows to provide a dispatch interceptor for outplace activation.
        """
    @property
    def RecoveryStorage(self) -> 'XStorage_8e460a32':
        """
        denotes the storage from which the embedded object is to be recovered.
        
        Upon activating the embedded object, it is normally loaded from a storage as denoted by the parameters to the XEmbedObjectCreator method calls.
        
        You can pass a non-NULL RecoveryStorage in the object descriptor if you wish to load the embedded object from an alternate storage.
        
        The object will still be based on the storage denoted in the XEmbedObjectCreator method call, i.e., subsequent save operations will still use that storage. RecoveryStorage is used at loading time only, and then discarded.
        """
    @property
    def StoreVisualReplacement(self) -> bool:
        """
        lets the graphical representation of embedded document be stored.
        
        Setting of this property to true tells the embedded object that controls the document to store or not to store the graphical representation of the document into the object persistence. If this property is not set the object makes the decision itself.
        """


