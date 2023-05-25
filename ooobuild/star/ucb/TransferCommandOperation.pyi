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
# Enum
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.ucb
# Libre Office Version: 7.4
from __future__ import annotations
from typing import Protocol, Any
from typing_extensions import Literal


class TransferCommandOperationProto(Protocol):
    """Protocol for TransferCommandOperation"""

    @property
    def typeName(self) -> Literal["com.sun.star.ucb.TransferCommandOperation"]:
        ...
    value: Any
    COPY: TransferCommandOperationProto
    LINK: TransferCommandOperationProto
    MOVE: TransferCommandOperationProto

COPY: TransferCommandOperationProto
"""
Copy the source to the target folder.

WebDAV methods as defined in HTTP Extensions for Web Distributed Authoring and Versioning (WebDAV)
"""
LINK: TransferCommandOperationProto
"""
Create a link in the target folder.

The link's target is the source object.
"""
MOVE: TransferCommandOperationProto
"""
Move the source to the target folder.

WebDAV methods as defined in HTTP Extensions for Web Distributed Authoring and Versioning (WebDAV)
"""

