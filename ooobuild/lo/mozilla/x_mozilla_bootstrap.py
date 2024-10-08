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
# Namespace: com.sun.star.mozilla
from __future__ import annotations
from .x_profile_discover import XProfileDiscover as XProfileDiscover_e060e68
from .x_profile_manager import XProfileManager as XProfileManager_ff500de4
from .x_proxy_runner import XProxyRunner as XProxyRunner_d84b0cf4

class XMozillaBootstrap(XProfileDiscover_e060e68, XProfileManager_ff500de4, XProxyRunner_d84b0cf4):
    """

    See Also:
        `API XMozillaBootstrap <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1mozilla_1_1XMozillaBootstrap.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.mozilla'
    __ooo_full_ns__: str = 'com.sun.star.mozilla.XMozillaBootstrap'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.mozilla.XMozillaBootstrap'


__all__ = ['XMozillaBootstrap']

