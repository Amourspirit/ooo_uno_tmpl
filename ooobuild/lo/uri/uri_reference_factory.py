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
# Namespace: com.sun.star.uri
from .x_uri_reference_factory import XUriReferenceFactory as XUriReferenceFactory_a740e47

class UriReferenceFactory(XUriReferenceFactory_a740e47):
    """
    Service Class

    creates URI references.
    
    See RFC 3986 for a description of URI references and related terms.
    
    For parsing absolute URI references, this service tries to use a scheme-specific parser. Such a scheme-specific parser will typically enforce additional restrictions during parsing, and will typically return objects that support extra, scheme-specific interfaces in addition to com.sun.star.uri.XUriReference. If no such parser is found, and for relative URI references, a generic parser is used, which returns objects that only support com.sun.star.uri.XUriReference.
    
    Locating a scheme-specific parser works as follows: A scheme consists of Latin capital letters “A”–“Z”, Latin small letters “a”–“z”, digits “0”–“9”, “+”, “-”, and “.”. A scheme s is transformed into a string s′ character-by-character, by translating Latin capital letters to their small counterparts, translating “+” to “PLUS”, “-” to “HYPHEN”, “.” to “DOT”, and copying Latin small letters and digits unchanged. If the component context used while creating this UriReferenceFactory instance offers a service manager, and there is a service available at that service manager whose name is the concatenation of “com.sun.star.uri.UriSchemeParser_” and s′, then that service is used. It is an error if that service does not support com.sun.star.uri.XUriSchemeParser.
    
    **since**
    
        OOo 2.0

    See Also:
        `API UriReferenceFactory <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1uri_1_1UriReferenceFactory.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.uri'
    __ooo_full_ns__: str = 'com.sun.star.uri.UriReferenceFactory'
    __ooo_type_name__: str = 'service'



__all__ = ['UriReferenceFactory']

