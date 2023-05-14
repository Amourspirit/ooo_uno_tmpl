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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.accessibility


class AccessibleRelationType(object):
    """
    Const Class

    Collection of relation types.
    
    This list of constants defines the available types of relations that are usable by AccessibleRelation.
    
    We are using constants instead of a more typesafe enum. The reason for this is that IDL enums may not be extended. Therefore, in order to include future extensions to the set of roles we have to use constants here.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API AccessibleRelationType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1accessibility_1_1AccessibleRelationType.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.accessibility'
    __ooo_full_ns__: str = 'com.sun.star.accessibility.AccessibleRelationType'
    __ooo_type_name__: str = 'const'

    INVALID = 0
    """
    Invalid relation type.
    
    Indicates an invalid relation type. This is used to indicate that a retrieval method could not find a requested relation.
    """
    CONTENT_FLOWS_FROM = 1
    """
    Content-flows-from relation.
    
    Indicates a content flow between the related objects.
    """
    CONTENT_FLOWS_TO = 2
    """
    Content-flows-to relation.
    
    Indicates a content flow between the related objects.
    """
    CONTROLLED_BY = 3
    """
    Controlled-by relation type.
    
    Indicates an object is controlled by one or more target objects.
    """
    CONTROLLER_FOR = 4
    """
    Controller-for relation type.
    
    Indicates an object is a controller for one or more target objects.
    """
    LABEL_FOR = 5
    """
    Label-for relation type.
    
    Indicates an object is a label for one or more target objects.
    """
    LABELED_BY = 6
    """
    Labeled-by relation type.
    
    Indicates an object is labeled by one or more target objects.
    """
    MEMBER_OF = 7
    """
    Member-of relation type.
    
    Indicates an object is a member of a group of one or more target objects.
    """
    SUB_WINDOW_OF = 8
    """
    Sub-Window-of relation type.
    
    With this relation you can realize an alternative parent-child relationship. The target of the relation contains the parent window. Note that there is no relation that points the other way, from the parent window to the child window.
    """
    NODE_CHILD_OF = 9
    """
    Node-Child-of relation type.
    
    Indicates an object is a cell in a tree or tree table which is displayed because a cell in the same column is expanded and identifies that cell.
    
    **since**
    
        OOo 3.0
    """
    DESCRIBED_BY = 10
    """
    Described-by relation type.
    
    Indicates an object is described by the target object.
    
    **since**
    
        OOo 3.5
    """

__all__ = ['AccessibleRelationType']
