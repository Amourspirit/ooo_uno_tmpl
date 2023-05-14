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
# Namespace: com.sun.star.deployment
# Libre Office Version: 7.3
from typing_extensions import Literal
import typing
from ..xml.dom.x_element import XElement as XElement_a33d0ae9


class UpdateInformationEntry(object):
    """
    Struct Class

    Objects of this type are used as elements of the enumeration returned by XUpdateInformationProvider.
    
    **since**
    
        OOo 2.3

    See Also:
        `API UpdateInformationEntry <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1deployment_1_1UpdateInformationEntry.html>`_
    """
    typeName: Literal['com.sun.star.deployment.UpdateInformationEntry']

    def __init__(self, UpdateDocument: typing.Optional[XElement_a33d0ae9] = ..., Description: typing.Optional[str] = ...) -> None:
        """
        Constructor

        Arguments:
            UpdateDocument (XElement, optional): UpdateDocument value.
            Description (str, optional): Description value.
        """
        ...


    @property
    def UpdateDocument(self) -> XElement_a33d0ae9:
        """
        the DOM representation of an update information entry
        """
        ...

    @UpdateDocument.setter
    def UpdateDocument(self, value: XElement_a33d0ae9) -> None:
        ...

    @property
    def Description(self) -> str:
        """
        the (optional) description for an update information entry extracted from the update feed container
        """
        ...

    @Description.setter
    def Description(self, value: str) -> None:
        ...

