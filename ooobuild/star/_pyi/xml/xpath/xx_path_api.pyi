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
# Namespace: com.sun.star.xml.xpath
from typing_extensions import Literal
import typing
from ...uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..dom.x_node import XNode as XNode_83fb09a5
    from ..dom.x_node_list import XNodeList as XNodeList_ae540b41
    from .xx_path_extension import XXPathExtension as XXPathExtension_194c0ea6
    from .xx_path_object import XXPathObject as XXPathObject_ee270d40

class XXPathAPI(XInterface_8f010a43):
    """

    See Also:
        `API XXPathAPI <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1xml_1_1xpath_1_1XXPathAPI.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.xml.xpath.XXPathAPI']

    def eval(self, contextNode: 'XNode_83fb09a5', expr: str) -> 'XXPathObject_ee270d40':
        """
        Evaluate XPath Expression.

        Raises:
            com.sun.star.xml.xpath.XPathException: ``XPathException``
        """
        ...
    def evalNS(self, contextNode: 'XNode_83fb09a5', expr: str, namespaceNode: 'XNode_83fb09a5') -> 'XXPathObject_ee270d40':
        """
        Evaluate XPath Expression.

        Raises:
            com.sun.star.xml.xpath.XPathException: ``XPathException``
        """
        ...
    def registerExtension(self, serviceName: str) -> None:
        """
        """
        ...
    def registerExtensionInstance(self, aExtension: 'XXPathExtension_194c0ea6') -> None:
        """
        """
        ...
    def registerNS(self, prefix: str, url: str) -> None:
        """
        """
        ...
    def selectNodeList(self, contextNode: 'XNode_83fb09a5', expr: str) -> 'XNodeList_ae540b41':
        """
        Evaluate an XPath expression to select a list of nodes.

        Raises:
            com.sun.star.xml.xpath.XPathException: ``XPathException``
        """
        ...
    def selectNodeListNS(self, contextNode: 'XNode_83fb09a5', expr: str, namespaceNode: 'XNode_83fb09a5') -> 'XNodeList_ae540b41':
        """
        Evaluate an XPath expression to select a list of nodes.

        Raises:
            com.sun.star.xml.xpath.XPathException: ``XPathException``
        """
        ...
    def selectSingleNode(self, contextNode: 'XNode_83fb09a5', expr: str) -> 'XNode_83fb09a5':
        """
        Evaluate an XPath expression to select a single node.

        Raises:
            com.sun.star.xml.xpath.XPathException: ``XPathException``
        """
        ...
    def selectSingleNodeNS(self, contextNode: 'XNode_83fb09a5', expr: str, namespaceNode: 'XNode_83fb09a5') -> 'XNode_83fb09a5':
        """
        Evaluate an XPath expression to select a single node.

        Raises:
            com.sun.star.xml.xpath.XPathException: ``XPathException``
        """
        ...
    def unregisterNS(self, prefix: str, url: str) -> None:
        """
        """
        ...


