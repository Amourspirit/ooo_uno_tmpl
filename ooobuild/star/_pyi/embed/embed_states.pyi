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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.embed
from typing_extensions import Literal


class EmbedStates:
    """
    Const Class

    This constant set contains possible states for EmbeddedObject.

    See Also:
        `API EmbedStates <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1embed_1_1EmbedStates.html>`_
    """
    LOADED: Literal[0]
    """
    \"Loaded\" - the persistent representation of the object is loaded in memory.
    
    The object is created and assigned with a persistent entry, and a view representation ( metafile and etc. ) can be retrieved ( if there is any ).
    """
    RUNNING: Literal[1]
    """
    \"Running\" - the object is connected and loaded.
    
    The object has a connection to the container client and a component loaded from persistent entry. In case of internal document it also means existing of document model that implements com.sun.star.frame.XModel interface.
    """
    ACTIVE: Literal[2]
    """
    \"Active\" - the object is activated in separate window ( outplace activation ).
    """
    INPLACE_ACTIVE: Literal[3]
    """
    \"Inplace active\" - the object has own window in the container's window.
    
    The object is activated and has its own window in the container's window that allows object to process mouse events and control own rendering.
    """
    UI_ACTIVE: Literal[4]
    """
    \"UI active\" - the inplace active object that has user interface.
    
    The object is inplace active, allowed to have menus, toolbars, keyboard accelerators, and has the focus.
    """

