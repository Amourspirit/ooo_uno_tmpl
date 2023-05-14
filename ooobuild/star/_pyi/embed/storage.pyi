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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.embed
from .base_storage import BaseStorage as BaseStorage_ae680b55
from .x_encryption_protected_source import XEncryptionProtectedSource as XEncryptionProtectedSource_8cdf11a3
from .x_transacted_object import XTransactedObject as XTransactedObject_fb510dbd
from .x_transaction_broadcaster import XTransactionBroadcaster as XTransactionBroadcaster_576e104d

class Storage(BaseStorage_ae680b55, XEncryptionProtectedSource_8cdf11a3, XTransactedObject_fb510dbd, XTransactionBroadcaster_576e104d):
    """
    Service Class

    This is a service that allows to get access to a package using storage hierarchy.
    
    A root storage should be retrieved by using StorageFactory service. Substorages are created through XStorage interface of a parent storage.

    See Also:
        `API Storage <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1embed_1_1Storage.html>`_
    """
    @property
    def HasEncryptedEntries(self) -> bool:
        """
        allows to detect if the storage contains encrypted entries.
        
        In case it is set to TRUE the storage itself and/or a tree of substorages contain encrypted streams. Usually in case this property is supported the implementation supports XEncryptionProtectedSource interface.
        """
        ...
    @HasEncryptedEntries.setter
    def HasEncryptedEntries(self, value: bool) -> None:
        ...
    @property
    def HasNonEncryptedEntries(self) -> bool:
        """
        allows to detect if the storage contains non-encrypted entries.
        
        In case it is set to TRUE the storage itself and/or a tree of substorages contains non-encrypted streams. Usually in case this property is supported the implementation supports XEncryptionProtectedSource interface.
        """
        ...
    @HasNonEncryptedEntries.setter
    def HasNonEncryptedEntries(self, value: bool) -> None:
        ...
    @property
    def IsRoot(self) -> bool:
        """
        allows to detect whether the storage is a root one.
        """
        ...
    @IsRoot.setter
    def IsRoot(self, value: bool) -> None:
        ...
    @property
    def MediaType(self) -> str:
        """
        allows to get and set the media type of the storage.
        """
        ...
    @MediaType.setter
    def MediaType(self, value: str) -> None:
        ...
    @property
    def MediaTypeFallbackIsUsed(self) -> bool:
        """
        allows to detect whether mediatype is detected by using fallback approach.
        
        Can be set to true if the mediatype can not be detected in standard way, but there is a fallback solution allows to do it.
        
        Usually means that the document validity is questionable, although the package itself is not corrupted. The decision about document validity in this case is in application hands. It is up to user of the storage to decide whether he accepts the fallback approach for an implementation of this service, outputs a warning or an error.
        """
        ...
    @MediaTypeFallbackIsUsed.setter
    def MediaTypeFallbackIsUsed(self, value: bool) -> None:
        ...
    @property
    def RepairPackage(self) -> bool:
        """
        allows to detect whether storage is open in \"repair package\" mode or not.
        """
        ...
    @RepairPackage.setter
    def RepairPackage(self, value: bool) -> None:
        ...
    @property
    def Version(self) -> str:
        """
        allows to get and set the version of the format related to the MediaType.
        """
        ...
    @Version.setter
    def Version(self, value: str) -> None:
        ...

