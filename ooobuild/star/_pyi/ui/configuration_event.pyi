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
# Namespace: com.sun.star.ui
# Libre Office Version: 7.2
from typing_extensions import Literal
from ..container.container_event import ContainerEvent as ContainerEvent_ea50e70
from ..uno.x_interface import XInterface as XInterface_8f010a43
import typing


class ConfigurationEvent(ContainerEvent_ea50e70):
    """
    Struct Class

    this event is broadcasted by a configuration manager whenever the state of user interface element has changed.
    
    **since**
    
        OOo 2.0

    See Also:
        `API ConfigurationEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1ui_1_1ConfigurationEvent.html>`_
    """
    typeName: Literal['com.sun.star.ui.ConfigurationEvent']

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = ..., Accessor: typing.Optional[object] = ..., Element: typing.Optional[object] = ..., ReplacedElement: typing.Optional[object] = ..., ResourceURL: typing.Optional[str] = ..., aInfo: typing.Optional[object] = ...) -> None:
        """
        Constructor

        Arguments:
            Source (XInterface, optional): Source value.
            Accessor (object, optional): Accessor value.
            Element (object, optional): Element value.
            ReplacedElement (object, optional): ReplacedElement value.
            ResourceURL (str, optional): ResourceURL value.
            aInfo (object, optional): aInfo value.
        """


    @property
    def ResourceURL(self) -> str:
        """
        contains the resource URL of the user interface element or a configuration manager, which has been changed, inserted or replaced.
        """


    @property
    def aInfo(self) -> object:
        """
        contains additional information about this configuration event.
        
        The type depends on the specific implementation.
        """


