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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.ui
# Libre Office Version: 2024.2
from ooo.oenv.env_const import UNO_NONE
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
    __ooo_ns__: str = 'com.sun.star.ui'
    __ooo_full_ns__: str = 'com.sun.star.ui.ConfigurationEvent'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.ui.ConfigurationEvent'
    """Literal Constant ``com.sun.star.ui.ConfigurationEvent``"""

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = None, Accessor: typing.Optional[object] = None, Element: typing.Optional[object] = None, ReplacedElement: typing.Optional[object] = None, ResourceURL: typing.Optional[str] = '', aInfo: typing.Optional[object] = None) -> None:
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

        if isinstance(Source, ConfigurationEvent):
            oth: ConfigurationEvent = Source
            self.Source = oth.Source
            self.Accessor = oth.Accessor
            self.Element = oth.Element
            self.ReplacedElement = oth.ReplacedElement
            self.ResourceURL = oth.ResourceURL
            self.aInfo = oth.aInfo
            return

        kargs = {
            "Source": Source,
            "Accessor": Accessor,
            "Element": Element,
            "ReplacedElement": ReplacedElement,
            "ResourceURL": ResourceURL,
            "aInfo": aInfo,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._resource_url = kwargs["ResourceURL"]
        self._a_info = kwargs["aInfo"]
        inst_keys = ('ResourceURL', 'aInfo')
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)


    @property
    def ResourceURL(self) -> str:
        """
        contains the resource URL of the user interface element or a configuration manager, which has been changed, inserted or replaced.
        """
        return self._resource_url

    @ResourceURL.setter
    def ResourceURL(self, value: str) -> None:
        self._resource_url = value

    @property
    def aInfo(self) -> object:
        """
        contains additional information about this configuration event.
        
        The type depends on the specific implementation.
        """
        return self._a_info

    @aInfo.setter
    def aInfo(self, value: object) -> None:
        self._a_info = value


__all__ = ['ConfigurationEvent']
