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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.container
# Libre Office Version: 7.3
from typing_extensions import Literal
from ..lang.event_object import EventObject as EventObject_a3d70b03
from ..uno.x_interface import XInterface as XInterface_8f010a43
import typing


class ContainerEvent(EventObject_a3d70b03):
    """
    Struct Class

    This event is fired when an element is inserted in a container.

    See Also:
        `API ContainerEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1container_1_1ContainerEvent.html>`_
    """
    typeName: Literal['com.sun.star.container.ContainerEvent']

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = ..., Accessor: typing.Optional[object] = ..., Element: typing.Optional[object] = ..., ReplacedElement: typing.Optional[object] = ...) -> None:
        """
        Constructor

        Arguments:
            Source (XInterface, optional): Source value.
            Accessor (object, optional): Accessor value.
            Element (object, optional): Element value.
            ReplacedElement (object, optional): ReplacedElement value.
        """
        ...


    @property
    def Accessor(self) -> object:
        """
        It contains the accessor to the element which is inserted or removed.
        
        The type and the value of the accessor depends on the service.
        """
        ...

    @Accessor.setter
    def Accessor(self, value: object) -> None:
        ...

    @property
    def Element(self) -> object:
        """
        This contains the element that was inserted or removed.
        """
        ...

    @Element.setter
    def Element(self, value: object) -> None:
        ...

    @property
    def ReplacedElement(self) -> object:
        """
        This contains the replaced element.
        """
        ...

    @ReplacedElement.setter
    def ReplacedElement(self, value: object) -> None:
        ...

