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
# Namespace: com.sun.star.accessibility
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

    class AccessibleRelationType(metaclass=UnoConstMeta, type_name="com.sun.star.accessibility.AccessibleRelationType", name_space="com.sun.star.accessibility"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.accessibility.AccessibleRelationType``"""
        pass

    class AccessibleRelationTypeEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.accessibility.AccessibleRelationType", name_space="com.sun.star.accessibility"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.accessibility.AccessibleRelationType`` as Enum values"""
        pass

else:
    if TYPE_CHECKING:
        from com.sun.star.accessibility import AccessibleRelationType as AccessibleRelationType
    else:
        # keep document generators happy
        from ...lo.accessibility.accessible_relation_type import AccessibleRelationType as AccessibleRelationType

    class AccessibleRelationTypeEnum(IntEnum):
        """
        Enum of Const Class AccessibleRelationType

        Collection of relation types.
        
        This list of constants defines the available types of relations that are usable by AccessibleRelation.
        
        We are using constants instead of a more typesafe enum. The reason for this is that IDL enums may not be extended. Therefore, in order to include future extensions to the set of roles we have to use constants here.
        
        **since**
        
            OOo 1.1.2
        """
        INVALID = AccessibleRelationType.INVALID
        """
        Invalid relation type.
        
        Indicates an invalid relation type. This is used to indicate that a retrieval method could not find a requested relation.
        """
        CONTENT_FLOWS_FROM = AccessibleRelationType.CONTENT_FLOWS_FROM
        """
        Content-flows-from relation.
        
        Indicates a content flow between the related objects.
        """
        CONTENT_FLOWS_TO = AccessibleRelationType.CONTENT_FLOWS_TO
        """
        Content-flows-to relation.
        
        Indicates a content flow between the related objects.
        """
        CONTROLLED_BY = AccessibleRelationType.CONTROLLED_BY
        """
        Controlled-by relation type.
        
        Indicates an object is controlled by one or more target objects.
        """
        CONTROLLER_FOR = AccessibleRelationType.CONTROLLER_FOR
        """
        Controller-for relation type.
        
        Indicates an object is a controller for one or more target objects.
        """
        LABEL_FOR = AccessibleRelationType.LABEL_FOR
        """
        Label-for relation type.
        
        Indicates an object is a label for one or more target objects.
        """
        LABELED_BY = AccessibleRelationType.LABELED_BY
        """
        Labeled-by relation type.
        
        Indicates an object is labeled by one or more target objects.
        """
        MEMBER_OF = AccessibleRelationType.MEMBER_OF
        """
        Member-of relation type.
        
        Indicates an object is a member of a group of one or more target objects.
        """
        SUB_WINDOW_OF = AccessibleRelationType.SUB_WINDOW_OF
        """
        Sub-Window-of relation type.
        
        With this relation you can realize an alternative parent-child relationship. The target of the relation contains the parent window. Note that there is no relation that points the other way, from the parent window to the child window.
        """
        NODE_CHILD_OF = AccessibleRelationType.NODE_CHILD_OF
        """
        Node-Child-of relation type.
        
        Indicates an object is a cell in a tree or tree table which is displayed because a cell in the same column is expanded and identifies that cell.
        
        **since**
        
            OOo 3.0
        """
        DESCRIBED_BY = AccessibleRelationType.DESCRIBED_BY
        """
        Described-by relation type.
        
        Indicates an object is described by the target object.
        
        **since**
        
            OOo 3.5
        """

__all__ = ['AccessibleRelationType', 'AccessibleRelationTypeEnum']
