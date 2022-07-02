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
from abc import abstractmethod, ABC

class XExternalUriReferenceTranslator(ABC):
    """
    translates between external and internal URI references.
    
    Some URI schemes leave unspecified important aspects of how to interpret URIs of those schemes. For example, it is unspecified for “file” URLs how to map the byte sequences that constitute the path segments of a “file” URL to filenames on a given platform: The UNO environment always assumes that path segments of “file” URLs represent UTF-8–encoded strings (which have to be mapped to filenames in a platform-specific way), while other applications typically assume that path segments of “file” URLs directly represent a platform's byte-sequence filenames. This interface offers methods to translate between such internal URIs (e.g., UTF-8–encoded “file” URLs used within the UNO environment) and external URIs (e.g., byte-sequence–oriented “file” URLs used by other applications). Typically, only “file” URLs are affected by this translation.
    
    Since the translation process is based on URI schemes, relative URI references (that do not include a scheme) are left unmodified by the translation process.
    
    **since**
    
        OOo 2.0

    See Also:
        `API XExternalUriReferenceTranslator <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1uri_1_1XExternalUriReferenceTranslator.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.uri'
    __ooo_full_ns__: str = 'com.sun.star.uri.XExternalUriReferenceTranslator'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.uri.XExternalUriReferenceTranslator'

    @abstractmethod
    def translateToExternal(self, internalUriReference: str) -> str:
        """
        returns the external counterpart of an internal URI reference.
        """
        ...
    @abstractmethod
    def translateToInternal(self, externalUriReference: str) -> str:
        """
        returns the internal counterpart of an external URI reference.
        """
        ...

__all__ = ['XExternalUriReferenceTranslator']

