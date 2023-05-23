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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.beans
import typing

from ..uno.x_interface import XInterface as XInterface_8f010a43


class XMaterialHolder(XInterface_8f010a43):
    """
    gives access to the material a (tool-) object is working on.
    
    Example: The introspection service allows the inspection of an object's properties and methods. The result is represented as XIntrospectionAccess interface. The inspected object then is the material attached to the introspection tool and an implementation of XIntrospectionAccess should also support XMaterialHolder to give access to this material.

    See Also:
        `API XMaterialHolder <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1beans_1_1XMaterialHolder.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.beans.XMaterialHolder'

    def getMaterial(self) -> typing.Any:
        """
        returns the material that is connected to this (tool-) object
        """
        ...

