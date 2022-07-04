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
# Namespace: com.sun.star.drawing.framework
from typing_extensions import Literal
import typing
from abc import ABC
if typing.TYPE_CHECKING:
    from .anchor_binding_mode import AnchorBindingMode as AnchorBindingMode_c46b128b
    from ...util.url import URL as URL_57ad07b9

class XResourceId(ABC):
    """
    A resource id uses a set of URLs to unambiguously specify a resource of the drawing framework.
    
    Resources of the drawing framework are panes, views, tool bars, and command groups. One URL describes the type of the actual resource. A sequence of URLs (typically one, sometimes two) specifies its anchor, the resource it is bound to. The anchor typically is a pane (for views), or it is empty (for panes).
    
    The resource URL may be empty. In this case the anchor is empty, too. Such an empty resource id does not describe a resource but rather the absence of one. Instead of an empty XResourceId object an empty reference can be used in many places.
    
    The resource URL may have arguments that are passed to the factory method on its creation. Arguments are only available through the getFullResourceURL(). The getResourceURL() method strips them away.

    See Also:
        `API XResourceId <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1drawing_1_1framework_1_1XResourceId.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.drawing.framework.XResourceId']

    def clone(self) -> 'XResourceId':
        """
        Return a copy of the called resource id.
        
        The caller becomes the owner of the new object.
        """
        ...
    def compareTo(self, xId: 'XResourceId') -> int:
        """
        Compare the called XResourceId object with the given one.
        
        The two resource ids A and B are compared so that if A<B (return value is -1) then either A and B are unrelated or A is a direct or indirect anchor of B.
        
        The algorithm for this comparison is quite simple. It uses a double lexicographic ordering. On the lower level individual URLs are compared via the lexicographic order defined on strings. On the higher level two resource ids are compared via a lexicographic order defined on the URLS. So when there are two resource ids A1.A2 (A1 being the anchor of A2) and B1.B2 then A1.A2<B1.B2 when A1<B1 or A1==B1 and A2<B2. Resource ids may have different lengths: A1 < B1.B2 when A1<B1 or A1==B1 (anchors first then resources linked to them.
        """
        ...
    def getAnchor(self) -> 'XResourceId':
        """
        Return a new XResourceId that represents the anchor resource.
        """
        ...
    def getAnchorURLs(self) -> 'typing.Tuple[str, ...]':
        """
        Return the, possibly empty, list of anchor URLs.
        
        The URLs are ordered so that the one in position 0 is the direct anchor of the resource, while the one in position i+1 is the direct anchor of the one in position i.
        """
        ...
    def getFullResourceURL(self) -> 'URL_57ad07b9':
        """
        Return a URL object of the resource URL that may contain arguments.
        """
        ...
    def getResourceTypePrefix(self) -> str:
        """
        Return the type prefix of the resource URL.
        
        This includes all up to and including the second slash.
        """
        ...
    def getResourceURL(self) -> str:
        """
        Return the URL of the resource.
        
        Arguments supplied on creation are stripped away. Use getFullResourceURL() to access them.
        """
        ...
    def hasAnchor(self) -> bool:
        """
        Return whether there is a non-empty anchor URL.
        
        When this method returns FALSE then getAnchorURLs() will return an empty list.
        """
        ...
    def isBoundTo(self, xAnchorId: 'XResourceId', eMode: 'AnchorBindingMode_c46b128b') -> bool:
        """
        Return whether the anchor of the called resource id object represents the same resource as the given object.
        
        Note that not only the anchor of the given object is taken into account. The whole object, including the resource URL, is interpreted as anchor resource.
        
        If eMode is DIRECT then the anchor of the called resource id has to be identical to the given anchor. If eMode is INDIRECT then the given anchor has to be a part of the anchor of the called resource.
        """
        ...
    def isBoundToURL(self, AnchorURL: str, eMode: 'AnchorBindingMode_c46b128b') -> bool:
        """
        Return whether the anchor of the called resource id object represents the same resource as the given anchor URL.
        
        This is a convenience variant of the isBoundTo() function that can also be seen as an optimization for the case that the anchor consists of exactly one URL.
        """
        ...


