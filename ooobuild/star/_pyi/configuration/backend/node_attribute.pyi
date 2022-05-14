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
# Namespace: com.sun.star.configuration.backend
from typing_extensions import Literal


class NodeAttribute(object):
    """
    Const

    These values are used to specify the behavior of a node or property in a layer.
    
    The values were chosen so they can be combined with values from SchemaAttribute
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API NodeAttribute <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1configuration_1_1backend_1_1NodeAttribute.html>`_
    """
    FINALIZED: Literal[256]
    """
    indicates that a node or property may not be changed or overridden in subsequent layers
    """
    MANDATORY: Literal[512]
    """
    indicates that a set item may not be removed or replaced in subsequent layers.
    """
    READONLY: Literal[1024]
    """
    indicates that a node or property may not be changed in this or subsequent layer.
    """
    FUSE: Literal[2048]
    """
    indicates that contents shall be fused.
    
    Used in XLayerHandler.addOrReplaceNode(), XLayerHandler.addOrReplaceNodeFromTemplate(), XUpdateHandler.addOrReplaceNode(), and XUpdateHandler.addOrReplaceNodeFromTemplate().
    
    **since**
    
        OOo 2.0.3
    """
    MASK: Literal[32512]
    """
    can be used to mask the node attributes from merged attributes
    """

