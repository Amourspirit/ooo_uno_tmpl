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
# Namespace: com.sun.star.drawing.framework
from typing_extensions import Literal
from abc import ABC

class XModuleController(ABC):
    """
    The module controller is responsible for loading a module (ad-don, plugin, whatever the name) when it is first used.
    
    For this there is a list in the office configuration which associates resource URLs with service names which in turn are associated with modules (or dlls). The path to the office configuration list is MultiPaneGUI/Framework/ResourceFactories in the Impress.xcu file.

    See Also:
        `API XModuleController <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1drawing_1_1framework_1_1XModuleController.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.drawing.framework.XModuleController']

    def requestResource(self, sResourceTypeURL: str) -> None:
        """
        When the specified resource is requested for the first time then create a new instance of the associated factory service.
        """

