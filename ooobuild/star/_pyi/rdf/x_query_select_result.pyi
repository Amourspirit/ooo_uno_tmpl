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
# Libre Office Version: 7.2
# Namespace: com.sun.star.rdf
from typing_extensions import Literal
import typing
from ..container.x_enumeration import XEnumeration as XEnumeration_f2180daa

class XQuerySelectResult(XEnumeration_f2180daa):
    """
    represents the result of a SPARQL \"SELECT\" query.
    
    The result consists of:
    
    Note that each query result retrieved via com.sun.star.container.XEnumeration.nextElement() has the type XNode[], the length of the sequence being the same as the number of query variables.
    
    **since**
    
        OOo 3.0

    See Also:
        `API XQuerySelectResult <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1rdf_1_1XQuerySelectResult.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.rdf.XQuerySelectResult']

    def getBindingNames(self) -> 'typing.Tuple[str, ...]':
        """
        get the names of the query variables.
        """

