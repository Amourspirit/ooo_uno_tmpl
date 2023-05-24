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
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.ucb
# Libre Office Version: 7.4
from __future__ import annotations
from typing import cast, TYPE_CHECKING
from enum import Enum
if TYPE_CHECKING:
    from com.sun.star.ucb.OutgoingMessageState import OutgoingMessageStateProto

class OutgoingMessageState(Enum):
    """
    Enum Class


    See Also:
        `API OutgoingMessageState <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1ucb.html#a8dec3ee1933cc93724b3764b124b8cc1>`_
    """
    __ooo_ns__: str = 'com.sun.star.ucb'
    __ooo_full_ns__: str = 'com.sun.star.ucb.OutgoingMessageState'
    __ooo_type_name__: str = 'enum'

    @property
    def typeName(self) -> str:
        return 'com.sun.star.ucb.OutgoingMessageState'

    COMPLETELY_LOCALLY_SENT = cast("OutgoingMessageStateProto", 'COMPLETELY_LOCALLY_SENT')
    """
    Message has been sent upstream to all recipients.
    """
    CONFIRMED = cast("OutgoingMessageStateProto", 'CONFIRMED')
    """
    Recipient confirmed reading.
    """
    EXTERNAL_ERROR = cast("OutgoingMessageStateProto", 'EXTERNAL_ERROR')
    """
    Global fatal error (e.g.
    
    last member in SMTP chain could not deliver the message).
    """
    NONRECOVERABLE_LOCAL_ERROR = cast("OutgoingMessageStateProto", 'NONRECOVERABLE_LOCAL_ERROR')
    """
    Local fatal error (e.g.
    
    first SMTP server upstream did not accept the message).
    """
    PARTIALLY_LOCALLY_SENT = cast("OutgoingMessageStateProto", 'PARTIALLY_LOCALLY_SENT')
    """
    Message has been sent upstream to some recipients.
    """
    RECOVERABLE_LOCAL_ERROR = cast("OutgoingMessageStateProto", 'RECOVERABLE_LOCAL_ERROR')
    """
    Local, non-fatal error (e.g.
    
    network temporarily not available).
    """
    WAITING_CONFIRMATION = cast("OutgoingMessageStateProto", 'WAITING_CONFIRMATION')
    """
    Message was sent; we are waiting for confirmation.
    """
    WRITTEN = cast("OutgoingMessageStateProto", 'WRITTEN')
    """
    Message has just been placed into the out tray.
    """

__all__ = ['OutgoingMessageState']

