# coding: utf-8
#
# Copyright 2023-2024 :Barry-Thomas-Paul: Moss
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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.configuration.backend
import uno
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    # document generators will most likely not see this.
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class NodeAttribute(metaclass=UnoConstMeta, type_name="com.sun.star.configuration.backend.NodeAttribute", name_space="com.sun.star.configuration.backend"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.configuration.backend.NodeAttribute``"""
        pass

    class NodeAttributeEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.configuration.backend.NodeAttribute", name_space="com.sun.star.configuration.backend"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.configuration.backend.NodeAttribute`` as Enum values"""
        pass

else:
    if TYPE_CHECKING:
        from com.sun.star.configuration.backend import NodeAttribute as NodeAttribute
    else:
        # keep document generators happy
        from ....lo.configuration.backend.node_attribute import NodeAttribute as NodeAttribute

    class NodeAttributeEnum(IntEnum):
        """
        Enum of Const Class NodeAttribute

        These values are used to specify the behavior of a node or property in a layer.
        
        The values were chosen so they can be combined with values from SchemaAttribute
        
        **since**
        
            OOo 1.1.2
        """
        FINALIZED = NodeAttribute.FINALIZED
        """
        indicates that a node or property may not be changed or overridden in subsequent layers
        """
        MANDATORY = NodeAttribute.MANDATORY
        """
        indicates that a set item may not be removed or replaced in subsequent layers.
        """
        READONLY = NodeAttribute.READONLY
        """
        indicates that a node or property may not be changed in this or subsequent layer.
        """
        FUSE = NodeAttribute.FUSE
        """
        indicates that contents shall be fused.
        
        Used in XLayerHandler.addOrReplaceNode(), XLayerHandler.addOrReplaceNodeFromTemplate(), XUpdateHandler.addOrReplaceNode(), and XUpdateHandler.addOrReplaceNodeFromTemplate().
        
        **since**
        
            OOo 2.0.3
        """
        MASK = NodeAttribute.MASK
        """
        can be used to mask the node attributes from merged attributes
        """

__all__ = ['NodeAttribute', 'NodeAttributeEnum']
