# coding: utf-8
#
# Copyright 2023-2024 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 2024.2
# Namespace: com.sun.star.frame
from __future__ import annotations
import typing

from ..container.x_container_query import XContainerQuery as XContainerQuery_1cdd0edc
from ..container.x_name_access import XNameAccess as XNameAccess_e2ab0cf6
from ..lang.x_multi_service_factory import XMultiServiceFactory as XMultiServiceFactory_191e0eb6


class XLoaderFactory(XContainerQuery_1cdd0edc, XNameAccess_e2ab0cf6, XMultiServiceFactory_191e0eb6):
    """
    Unified service interface for FrameLoaderFactory and ContentHandlerFactory.
    
    **since**
    
        LibreOffice 4.2

    See Also:
        `API XLoaderFactory <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1frame_1_1XLoaderFactory.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.frame.XLoaderFactory'


