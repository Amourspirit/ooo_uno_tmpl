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
# Namespace: com.sun.star.lang
import typing

from ..uno.x_interface import XInterface as XInterface_8f010a43


class XServiceInfo(XInterface_8f010a43):
    """
    Provides information regarding the implementation: which services are implemented and the name of the implementation.

    See Also:
        `API XServiceInfo <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1lang_1_1XServiceInfo.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.lang.XServiceInfo'

    def getImplementationName(self) -> str:
        """
        Provides the implementation name of the service implementation.
        """
        ...
    def getSupportedServiceNames(self) -> 'typing.Tuple[str, ...]':
        """
        Provides the supported service names of the implementation, including also indirect service names.
        """
        ...
    def supportsService(self, ServiceName: str) -> bool:
        """
        Tests whether the specified service is supported, i.e.
        
        implemented by the implementation.
        """
        ...

