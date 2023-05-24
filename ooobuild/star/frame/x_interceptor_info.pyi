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
# Namespace: com.sun.star.frame
from __future__ import annotations
import typing

from ..uno.x_interface import XInterface as XInterface_8f010a43


class XInterceptorInfo(XInterface_8f010a43):
    """
    makes it possible to get information about a registered interceptor and is used by frame interceptor mechanism to perform interception.
    
    Frame can call right interceptor directly without calling all of registered ones. Use it as an additional interface to XDispatchProviderInterceptor. If any interceptor in list doesn't support this interface - these mechanism will be broken and normal list of master-slave interceptor objects will be used from top to the bottom.

    See Also:
        `API XInterceptorInfo <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1frame_1_1XInterceptorInfo.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.frame.XInterceptorInfo'

    def getInterceptedURLs(self) -> typing.Tuple[str, ...]:
        """
        returns the URL list for interception.
        
        Wildcards inside the URLs are allowed to register the interceptor for URLs too, which can have optional arguments (e.g. \"..#..\" or \"..?..\").
        """
        ...


