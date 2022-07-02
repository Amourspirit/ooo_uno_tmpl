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
# Namespace: com.sun.star.frame
from typing_extensions import Literal
from ..uno.x_interface import XInterface as XInterface_8f010a43

class XModuleManager(XInterface_8f010a43):
    """
    can be used to identify office modules.
    
    **since**
    
        OOo 2.0

    See Also:
        `API XModuleManager <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1frame_1_1XModuleManager.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.frame.XModuleManager']

    def identify(self, Module: 'XInterface_8f010a43') -> str:
        """
        identifies the given module.
        
        This identifier can then be used at the service ModuleManager to get more information about this module.
        
        For identification the interface com.sun.star.lang.XServiceInfo is requested on the given module. Because all module service registrations must be unique this value can be queried and checked against the configuration.
        
        Since OOo 2.3.0 also the optional interface XModule will be used. If its exists it will be preferred.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            UnknownModuleException: ``UnknownModuleException``
        """
        ...


