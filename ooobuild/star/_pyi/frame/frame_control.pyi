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
# Libre Office Version: 7.4
# Namespace: com.sun.star.frame
from ..awt.uno_control import UnoControl as UnoControl_8f2c0a67

class FrameControl(UnoControl_8f2c0a67):
    """
    Service Class

    contains a frame with a desktop component
    
    If the control is visible and has a valid (loadable) component URL, then the FrameControl.Frame property is set. Normally this control can be used for preview functionality inside any UI.

    See Also:
        `API FrameControl <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1frame_1_1FrameControl.html>`_
    """
    @property
    def ComponentUrl(self) -> str:
        """
        contains the type of the component which is loaded into the frame, or the document which implicitly specifies the type
        """
        ...
    @property
    def Frame(self) -> str:
        """
        the frame held by this control
        
        The Frame is created if the control is shown and the ComponentUrl is set.
        """
        ...

