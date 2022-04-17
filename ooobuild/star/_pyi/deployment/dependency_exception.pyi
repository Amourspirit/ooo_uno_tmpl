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
# Exception Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.deployment
# Libre Office Version: 7.3
from typing_extensions import Literal
from ooo.oenv.env_const import UNO_NONE
import typing
from ..uno.exception import Exception as Exception_85530a09
from ..uno.x_interface import XInterface as XInterface_8f010a43
from ..xml.dom.x_element import XElement as XElement_a33d0ae9

class DependencyException(Exception_85530a09):
    """
    Exception Class

    describes unsatisfied dependencies a deployment unit has on its target environment.
    
    This exception is intended to be used with an com.sun.star.task.XInteractionHandler.
    
    **since**
    
        OOo 2.0.4

    See Also:
        `API DependencyException <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1deployment_1_1DependencyException.html>`_
    """

    typeName: Literal['com.sun.star.deployment.DependencyException']

    def __init__(self, Message: typing.Optional[str] = ..., Context: typing.Optional[XInterface_8f010a43] = ..., UnsatisfiedDependencies: typing.Optional[typing.Tuple[XElement_a33d0ae9, ...]] = ...) -> None:
        """
        Constructor

        Arguments:
            Message (str, optional): Message value.
            Context (XInterface, optional): Context value.
            UnsatisfiedDependencies (typing.Tuple[XElement, ...], optional): UnsatisfiedDependencies value.
        """
    @property
    def UnsatisfiedDependencies(self) -> typing.Tuple[XElement_a33d0ae9, ...]:
        """
        a sequence of dependencies represented by XML elements.
        
        The exact nature of those XML elements is deliberately left open, so that new kinds of dependencies can be defined in the future. OOo 2.0.4 does not define any kinds of dependencies. Each such XML element should have an attribute whose global name consists of the namespace name http://openoffice.org/extensions/description/2006 and the local part name and whose value is a human-readable (English) description of the dependency. If an instance of OOo does not know more about a specific kind of dependency, it should display the value of that attribute to the user.
        
        The sequence must not be empty, and none of the elements may be NULL.
        """


__all__ = ['DependencyException']

