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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.rdf
from typing_extensions import Literal
import typing
from .x_repository import XRepository as XRepository_995d0adc
if typing.TYPE_CHECKING:
    from ..container.x_enumeration import XEnumeration as XEnumeration_f2180daa
    from .x_metadatable import XMetadatable as XMetadatable_a3000af0
    from .x_node import XNode as XNode_5ee40822
    from .x_resource import XResource as XResource_842709e4
    from .xuri import XURI as XURI_5682078c

class XDocumentRepository(XRepository_995d0adc):
    """
    extends XRepository with document-specific functionality.
    
    This subclass of XRepository provides some methods which only make sense for repositories that are attached to a document. For example, the methods allow for manipulating in-content metadata, which is stored as RDFa.
    
    **since**
    
        OOo 3.2

    See Also:
        `API XDocumentRepository <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1rdf_1_1XDocumentRepository.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.rdf.XDocumentRepository']

    def getStatementRDFa(self, Element: 'XMetadatable_a3000af0') -> object:
        """
        find the RDFa statement(s) associated with an ODF element.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            RepositoryException: ``RepositoryException``
        """
    def getStatementsRDFa(self, Subject: 'XResource_842709e4', Predicate: 'XURI_5682078c', Object: 'XNode_5ee40822') -> 'XEnumeration_f2180daa':
        """
        gets matching RDFa statements from the repository.
        
        This method exists because RDFa statements are not part of any named graph, and thus they cannot be enumerated with XNamedGraph.getStatements().
        
        Any parameter may be NULL, which acts as a wildcard. For example, to get all statements about myURI: getStatementsRDFa(myURI, null, null)

        Raises:
            RepositoryException: ``RepositoryException``
        """
    def removeStatementRDFa(self, Element: 'XMetadatable_a3000af0') -> None:
        """
        remove the RDFa statement(s) that correspond to an ODF element from the repository.
        
        RDFa statements are handled specially because they are not logically part of any graph.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            RepositoryException: ``RepositoryException``
        """
    def setStatementRDFa(self, Subject: 'XResource_842709e4', Predicates: 'typing.Tuple[XURI_5682078c, ...]', Object: 'XMetadatable_a3000af0', RDFaContent: str, RDFaDatatype: 'XURI_5682078c') -> None:
        """
        update the RDFa statement(s) that correspond to an ODF element in the repository.
        
        This method will do the following steps:
        
        RDFa statements are handled specially because they are not logically part of any named graph in the repository. Also, they have rather unusual semantics; just using XNamedGraph.addStatement() would be ambiguous: if the object is a XMetadatable, do we insert the object itself (URI) or its literal content (RDFa)?

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            RepositoryException: ``RepositoryException``
        """

