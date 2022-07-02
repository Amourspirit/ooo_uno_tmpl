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
# Namespace: com.sun.star.xml.csax
# Libre Office Version: 7.2
from typing_extensions import Literal
import typing


class XMLAttribute(object):
    """
    Struct Class

    A struct to keep information of an element's attribute.

    See Also:
        `API XMLAttribute <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1xml_1_1csax_1_1XMLAttribute.html>`_
    """
    typeName: Literal['com.sun.star.xml.csax.XMLAttribute']

    def __init__(self, sName: typing.Optional[str] = ..., sValue: typing.Optional[str] = ...) -> None:
        """
        Constructor

        Arguments:
            sName (str, optional): sName value.
            sValue (str, optional): sValue value.
        """
        ...


    @property
    def sName(self) -> str:
        """
        the attribute name
        """
        ...


    @property
    def sValue(self) -> str:
        """
        the attribute value
        """
        ...


