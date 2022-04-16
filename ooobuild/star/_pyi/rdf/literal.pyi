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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.rdf
import typing
from .x_literal import XLiteral as XLiteral_79ec0969
from .x_node import XNode as XNode_5ee40822
if typing.TYPE_CHECKING:
    from .xuri import XURI as XURI_5682078c

class Literal(XLiteral_79ec0969, XNode_5ee40822):
    """
    Service Class

    represents a literal that may occur in a RDF graph.
    
    **since**
    
        OOo 3.0

    See Also:
        `API Literal <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1rdf_1_1Literal.html>`_
    """
    def create(self, Value: str) -> None:
        """
        creates a plain literal RDF node.
        """
    def createWithLanguage(self, Value: str, Language: str) -> None:
        """
        creates a literal RDF node with a language.
        """
    def createWithType(self, Value: str, Type: 'XURI_5682078c') -> None:
        """
        creates a typed literal RDF node.
        """


