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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.rdf
# Libre Office Version: 7.4
from typing_extensions import Literal
import typing
from .x_node import XNode as XNode_5ee40822
from .x_resource import XResource as XResource_842709e4
from .xuri import XURI as XURI_5682078c


class Statement(object):
    """
    Struct Class

    represents a RDF statement, or triple.
    
    **since**
    
        OOo 3.2

    See Also:
        `API Statement <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1rdf_1_1Statement.html>`_
    """
    typeName: Literal['com.sun.star.rdf.Statement']

    def __init__(self, Subject: typing.Optional[XResource_842709e4] = ..., Predicate: typing.Optional[XURI_5682078c] = ..., Object: typing.Optional[XNode_5ee40822] = ..., Graph: typing.Optional[XURI_5682078c] = ...) -> None:
        """
        Constructor

        Arguments:
            Subject (XResource, optional): Subject value.
            Predicate (XURI, optional): Predicate value.
            Object (XNode, optional): Object value.
            Graph (XURI, optional): Graph value.
        """
        ...


    @property
    def Subject(self) -> XResource_842709e4:
        """
        the subject of the RDF statement.
        """
        ...


    @property
    def Predicate(self) -> XURI_5682078c:
        """
        the predicate of the RDF statement.
        """
        ...


    @property
    def Object(self) -> XNode_5ee40822:
        """
        the object of the RDF statement.
        """
        ...


    @property
    def Graph(self) -> XURI_5682078c:
        """
        the named graph that contains this statement, or NULL.
        """
        ...


