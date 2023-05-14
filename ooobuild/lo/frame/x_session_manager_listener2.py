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
from abc import abstractmethod
from .x_session_manager_listener import XSessionManagerListener as XSessionManagerListener_582d1050

class XSessionManagerListener2(XSessionManagerListener_582d1050):
    """

    See Also:
        `API XSessionManagerListener2 <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1frame_1_1XSessionManagerListener2.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.frame'
    __ooo_full_ns__: str = 'com.sun.star.frame.XSessionManagerListener2'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.frame.XSessionManagerListener2'

    @abstractmethod
    def doQuit(self) -> None:
        """
        doQuit gets called when the session manager has decided the application should quit.
        
        Under these circumstances bringing up further UI will usually be impossible and must be avoided.
        """
        ...

__all__ = ['XSessionManagerListener2']

