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
# Const
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.rdf
from typing_extensions import Literal


class FileFormat(object):
    """
    Const

    Constants to specify RDF file formats.
    
    These constants are mainly for use with XRepository.importGraph() and XRepository.exportGraph().
    
    Note that these are integers because UNO IDL does not permit string constants.
    
    **since**
    
        OOo 3.0

    See Also:
        `API FileFormat <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1rdf_1_1FileFormat.html>`_
    """
    RDF_XML: Literal[0]
    """
    RDF/XML
    """
    N3: Literal[1]
    """
    N3 (Notation-3)
    """
    NTRIPLES: Literal[2]
    """
    N-Triples
    """
    TRIG: Literal[3]
    """
    TriG
    """
    TRIX: Literal[4]
    """
    TriX
    """
    TURTLE: Literal[5]
    """
    Turtle
    """

