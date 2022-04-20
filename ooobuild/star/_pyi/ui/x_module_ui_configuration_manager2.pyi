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
# Namespace: com.sun.star.ui
from typing_extensions import Literal
from .x_module_ui_configuration_manager import XModuleUIConfigurationManager as XModuleUIConfigurationManager_873f1155
from .xui_configuration import XUIConfiguration as XUIConfiguration_c4eb0c34
from .xui_configuration_manager import XUIConfigurationManager as XUIConfigurationManager_24e20eef
from .xui_configuration_persistence import XUIConfigurationPersistence as XUIConfigurationPersistence_661010b9

class XModuleUIConfigurationManager2(XModuleUIConfigurationManager_873f1155, XUIConfiguration_c4eb0c34, XUIConfigurationManager_24e20eef, XUIConfigurationPersistence_661010b9):
    """
    Provides a unified interface for the ModuleUIConfigurationManager service.
    
    **since**
    
        LibreOffice 4.2

    See Also:
        `API XModuleUIConfigurationManager2 <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1ui_1_1XModuleUIConfigurationManager2.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.ui.XModuleUIConfigurationManager2']


