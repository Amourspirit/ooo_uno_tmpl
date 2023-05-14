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
# Namespace: com.sun.star.bridge
from ..uno.x_interface import XInterface as XInterface_8f010a43

class OleApplicationRegistration(XInterface_8f010a43):
    """
    Service Class

    registers UNO objects as COM objects.
    
    That is, COM class factories are registered with COM at runtime. The required EXE server is the application which deploys this service. In order to access the factories by COM API functions, there need to be proper registry entries. This service does not provide for writing those entries.
    
    The instantiation of the registered objects can be carried out by any ordinary mechanism which is used in a certain language to create COM components. For example, CreateObject in Visual Basic, CoCreateInstance in C++.
    
    Currently only a factory for the service com.sun.star.long.MultiServiceFactory is registered by this service. The CLSID is {82154420-0FBF-11d4-8313-005004526AB4} and the ProgId is com.sun.star.ServiceManager.
    
    OleApplicationRegistration does not provide any particular interface because the UNO objects are registered while instantiating this service and deregistered if the implementation, which makes use of this service, is being released.
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API OleApplicationRegistration <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1bridge_1_1OleApplicationRegistration.html>`_
    """
    ...

