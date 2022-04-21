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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.security
from typing_extensions import Literal
from ..uno.x_interface import XInterface as XInterface_8f010a43

class XAccessControlContext(XInterface_8f010a43):
    """
    An XAccessControlContext is used to make system resource access decisions based on the context it encapsulates.
    
    More specifically, it encapsulates a context and has methods to check permissions equivalent to XAccessController interface, with one difference: The XAccessControlContext makes access decisions based on the context it encapsulates, rather than that of the current execution thread.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API XAccessControlContext <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1security_1_1XAccessControlContext.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.security.XAccessControlContext']

    def checkPermission(self, perm: object) -> None:
        """
        Determines whether the access request indicated by the specified permission should be allowed or denied, based on this context.
        
        The semantics are equivalent to the security permission classes of the Java platform.
        
        You can also pass a sequence of permissions (sequence< any >) to check a set of permissions, e.g. for performance reasons. This method quietly returns if the access request is permitted, or throws a suitable AccessControlException otherwise.

        Raises:
            AccessControlException: ``AccessControlException``
        """

