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
# Namespace: com.sun.star.frame
from .x_dispatch_provider import XDispatchProvider as XDispatchProvider_fc690de6
from ..lang.x_initialization import XInitialization as XInitialization_d46c0cca

class ProtocolHandler(XDispatchProvider_fc690de6, XInitialization_d46c0cca):
    """
    Service Class

    special dispatch provider registered for URL protocols
    
    The generic dispatch mechanism on a Frame search for such registered protocol handler and use it if it agrees with the dispatched URL.
    
    Supported URLs must match follow format: protocol scheme:protocol specific part If a handler provides optional arguments (\"?\") or jump marks (\"#\") depends from his definition and implementation. The generic dispatch provider will use registered URL pattern to detect right handler.

    See Also:
        `API ProtocolHandler <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1frame_1_1ProtocolHandler.html>`_
    """


