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
from ..container.x_named import XNamed as XNamed_a6520b08
from .x_frame_loader import XFrameLoader as XFrameLoader_ba3a0bad
from ..lang.x_initialization import XInitialization as XInitialization_d46c0cca

class FrameLoader(XNamed_a6520b08, XFrameLoader_ba3a0bad, XInitialization_d46c0cca):
    """
    Service Class

    derivations of this abstract service are used to load components into Frames of the environment
    
    Concrete implementations of this service register, for example, for file name extensions or MIME types to load appropriate components. The components loaded are at least Controller. Instead of SynchronousFrameLoader this one use asynchronous processes to load the component.

    See Also:
        `API FrameLoader <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1frame_1_1FrameLoader.html>`_
    """
    ...


