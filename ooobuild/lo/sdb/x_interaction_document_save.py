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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.sdb
from __future__ import annotations
import typing
from abc import abstractmethod
from ..task.x_interaction_continuation import XInteractionContinuation as XInteractionContinuation_5af0108e
if typing.TYPE_CHECKING:
    from ..ucb.x_content import XContent as XContent_79db0975

class XInteractionDocumentSave(XInteractionContinuation_5af0108e):
    """
    An interaction continuation handing back a document name.
    
    This continuation is typically used in conjunction with a com.sun.star.sdb.DocumentSaveRequest.
    
    **since**
    
        OOo 2.0

    See Also:
        `API XInteractionDocumentSave <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sdb_1_1XInteractionDocumentSave.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sdb'
    __ooo_full_ns__: str = 'com.sun.star.sdb.XInteractionDocumentSave'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.sdb.XInteractionDocumentSave'

    @abstractmethod
    def setName(self, Name: str, Content: XContent_79db0975) -> None:
        """
        set the document name chosen by the interaction handler
        """
        ...

__all__ = ['XInteractionDocumentSave']


