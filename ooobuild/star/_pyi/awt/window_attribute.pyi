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
# Const
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.awt
from typing_extensions import Literal


class WindowAttribute(object):
    """
    Const

    These values are used to specify the decorations of a window.
    
    IMPORTANT: These constants have to be disjunct with constants in VclWindowPeerAttribute.

    See Also:
        `API WindowAttribute <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1awt_1_1WindowAttribute.html>`_
    """
    SHOW: Literal[1]
    """
    specifies that the window is initially visible.
    """
    FULLSIZE: Literal[2]
    """
    specifies that the window fills the complete desktop area.
    
    This applies only to top windows.
    """
    OPTIMUMSIZE: Literal[4]
    """
    specifies that the window is optimum size.
    
    This applies only to top windows.
    """
    MINSIZE: Literal[8]
    """
    specifies that the window is minimum size.
    
    This applies only to top windows.
    """
    BORDER: Literal[16]
    """
    specifies that the window has visible borders.
    
    This applies only to top windows.
    """
    SIZEABLE: Literal[32]
    """
    specifies that the size of the window can be changed by the user.
    
    This applies only to top windows.
    """
    MOVEABLE: Literal[64]
    """
    specifies that the window can be moved by the user.
    
    This applies only to top windows.
    """
    CLOSEABLE: Literal[128]
    """
    specifies that the window can be closed by the user.
    
    This applies only to top windows.
    """
    SYSTEMDEPENDENT: Literal[256]
    """
    specifies that the window should support the com.sun.star.awt.XSystemDependentWindowPeer interface.
    
    This flag may be ignored, but in this case no system-dependent extension works.
    """
    NODECORATION: Literal[512]
    """
    specifies that the window should have no decoration.
    """

