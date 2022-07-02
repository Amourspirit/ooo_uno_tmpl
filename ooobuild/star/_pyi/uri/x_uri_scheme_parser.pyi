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
# Namespace: com.sun.star.uri
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_uri_reference import XUriReference as XUriReference_afc30b6f

class XUriSchemeParser(XInterface_8f010a43):
    """
    parses textual representations of absolute URIs.
    
    See RFC 3986 for a description of URIs and related terms.
    
    **since**
    
        OOo 2.0

    See Also:
        `API XUriSchemeParser <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1uri_1_1XUriSchemeParser.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.uri.XUriSchemeParser']

    def parse(self, scheme: str, schemeSpecificPart: str) -> 'XUriReference_afc30b6f':
        """
        parses the textual representation of an absolute URI.
        
        This method is used to parse URIs (with no fragment part), not URI references (with an optional fragment part).
        
        If an object is returned, the behaviour of its com.sun.star.uri.XUriReference methods must reflect the fact that the object represents an absolute URI reference with the given scheme and scheme-specific part, and without a fragment part.
        """
        ...


