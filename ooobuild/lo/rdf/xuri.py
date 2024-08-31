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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.rdf
from __future__ import annotations
from abc import abstractmethod
from .x_resource import XResource as XResource_842709e4

class XURI(XResource_842709e4):
    """
    represents a URI node that may occur in a RDF graph.
    
    Note that this is actually an IRI, but the RDF literature speaks of URIs only, so we chose to use established terminology.
    
    The URI is split into a Namespace and a LocalName, using the first applicable of the following criteria:
    
    A URI without a \":\" is invalid. This implies that the Namespace part of a URI must not be empty, while the LocalName part may be empty.
    
    **since**
    
        OOo 3.0

    See Also:
        `API XURI <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1rdf_1_1XURI.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.rdf'
    __ooo_full_ns__: str = 'com.sun.star.rdf.XURI'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.rdf.XURI'

    @property
    @abstractmethod
    def LocalName(self) -> str:
        """
        suffix
        """
        ...

    @property
    @abstractmethod
    def Namespace(self) -> str:
        """
        prefix
        """
        ...


__all__ = ['XURI']

