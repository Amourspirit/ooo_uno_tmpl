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
# Namespace: com.sun.star.embed


class Aspects(object):
    """
    Const Class

    The constant set contains possible aspects for an embedded object.
    
    This constant set provides a set of values that can be used to specify the kind of object view. It can be used for example by container to request view representation of a certain kind from XEmbeddedObject.
    
    The first 32 bits are reserved for MS OLE aspects.

    See Also:
        `API Aspects <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1embed_1_1Aspects.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.embed'
    __ooo_full_ns__: str = 'com.sun.star.embed.Aspects'
    __ooo_type_name__: str = 'const'

    MSOLE_CONTENT = 1
    """
    specifies view of the object to be displayed as an embedded object inside a container.
    """
    MSOLE_THUMBNAIL = 2
    """
    specifies view of the object to be displayed in a browsing tool.
    """
    MSOLE_ICON = 4
    """
    specifies view of the object when object is represented by Icon.
    """
    MSOLE_DOCPRINT = 8
    """
    specifies view of the object for print preview.
    """

__all__ = ['Aspects']
