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
# Namespace: com.sun.star.script
import typing
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from abc import ABC
if typing.TYPE_CHECKING:
    from ..lang.x_service_info import XServiceInfo as XServiceInfo_af180b5f
    from ..lang.x_type_provider import XTypeProvider as XTypeProvider_bbb40bef


class XServiceDocumenter(ABC):
    """
    provides documentation for UNO services
    
    **since**
    
        LibreOffice 5.1

    See Also:
        `API XServiceDocumenter <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1script_1_1XServiceDocumenter.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.script.XServiceDocumenter']

    def showCoreDocs(self, xService: 'XServiceInfo_af180b5f') -> None:
        """
        """
        ...
    def showInterfaceDocs(self, xTypeProvider: 'XTypeProvider_bbb40bef') -> None:
        """
        """
        ...
    def showServiceDocs(self, xService: 'XServiceInfo_af180b5f') -> None:
        """
        """
        ...

    @property
    def CoreBaseUrl(self) -> str:
        """
        """
        ...
    @CoreBaseUrl.setter
    def CoreBaseUrl(self, value: str) -> None:
        ...
    @property
    def ServiceBaseUrl(self) -> str:
        """
        """
        ...
    @ServiceBaseUrl.setter
    def ServiceBaseUrl(self, value: str) -> None:
        ...

