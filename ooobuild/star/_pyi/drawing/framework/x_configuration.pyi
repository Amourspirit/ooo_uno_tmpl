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
import typing
from ...util.x_cloneable import XCloneable as XCloneable_99d00aa3
if typing.TYPE_CHECKING:
    from .anchor_binding_mode import AnchorBindingMode as AnchorBindingMode_c46b128b
    from .x_resource_id import XResourceId as XResourceId_5be3103d

class XConfiguration(XCloneable_99d00aa3):
    """
    A configuration describes the resources of an application like panes, views, and tool bars and their relationships that are currently active or are requested to be activated.
    
    Resources are specified by ResourceId structures rather than references so that not only the current configuration but also a requested configuration can be represented.
    
    Direct manipulation of a configuration object is not advised with the exception of the ConfigurationController and objects that implement the XConfigurationChangeRequest interface.

    See Also:
        `API XConfiguration <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1drawing_1_1framework_1_1XConfiguration.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.drawing.framework.XConfiguration']

    def addResource(self, xResourceId: 'XResourceId_5be3103d') -> None:
        """
        Add a resource to the configuration.
        
        This method should be used only by objects that implement the XConfigurationRequest interface or by the configuration controller.
        """
        ...
    def getResources(self, xAnchorId: 'XResourceId_5be3103d', sTargetURLPrefix: str, eSearchMode: 'AnchorBindingMode_c46b128b') -> 'typing.Tuple[XResourceId_5be3103d, ...]':
        """
        Returns the list of resources that are bound directly and/or indirectly to the given anchor.
        
        A URL filter can reduce the set of returned resource ids.
        
        Use an empty string to prevent filtering out resource ids.
        """
        ...
    def hasResource(self, xResourceId: 'XResourceId_5be3103d') -> bool:
        """
        Returns whether the specified resource is part of the configuration.
        
        This is independent of whether the resource does really exist and is active, i.e. has a visible representation in the GUI.
        """
        ...
    def removeResource(self, xResourceId: 'XResourceId_5be3103d') -> None:
        """
        Remove a resource from the configuration.
        
        This method should be used only by objects that implement the XConfigurationRequest interface or by the configuration controller.
        """
        ...


