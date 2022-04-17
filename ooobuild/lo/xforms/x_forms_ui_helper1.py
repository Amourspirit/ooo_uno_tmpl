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
# Namespace: com.sun.star.xforms
import typing
from abc import abstractmethod, ABC
if typing.TYPE_CHECKING:
    from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
    from ..frame.x_model import XModel as XModel_7a6e095c
    from .x_model import XModel as XModel_865909f0
    from ..xml.dom.x_document import XDocument as XDocument_aebc0b5e
    from ..xml.dom.x_node import XNode as XNode_83fb09a5

class XFormsUIHelper1(ABC):
    """
    provide several helper methods for the UI
    
    This interfaces is for UI use only, and will likely be unsupported in future versions.

    See Also:
        `API XFormsUIHelper1 <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1xforms_1_1XFormsUIHelper1.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.xforms'
    __ooo_full_ns__: str = 'com.sun.star.xforms.XFormsUIHelper1'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.xforms.XFormsUIHelper1'

    @abstractmethod
    def cloneBindingAsGhost(self, binding: 'XPropertySet_bc180bfa') -> 'XPropertySet_bc180bfa':
        """
        """
    @abstractmethod
    def createAttribute(self, xParent: 'XNode_83fb09a5', sName: str) -> 'XNode_83fb09a5':
        """
        """
    @abstractmethod
    def createElement(self, xParent: 'XNode_83fb09a5', sName: str) -> 'XNode_83fb09a5':
        """
        """
    @abstractmethod
    def getBindingForNode(self, xNode: 'XNode_83fb09a5', bCreate: bool) -> 'XPropertySet_bc180bfa':
        """
        """
    @abstractmethod
    def getBindingName(self, xBinding: 'XPropertySet_bc180bfa', bDetail: bool) -> str:
        """
        """
    @abstractmethod
    def getDefaultBindingExpressionForNode(self, xNode: 'XNode_83fb09a5') -> str:
        """
        """
    @abstractmethod
    def getDefaultServiceNameForNode(self, xNode: 'XNode_83fb09a5') -> str:
        """
        """
    @abstractmethod
    def getNodeDisplayName(self, xNode: 'XNode_83fb09a5', bDetail: bool) -> str:
        """
        """
    @abstractmethod
    def getNodeName(self, xNode: 'XNode_83fb09a5') -> str:
        """
        """
    @abstractmethod
    def getResultForExpression(self, xBinding: 'XPropertySet_bc180bfa', bIsBindingExpression: bool, sExpression: str) -> str:
        """
        """
    @abstractmethod
    def getSubmissionName(self, xSubm: 'XPropertySet_bc180bfa', bDetail: bool) -> str:
        """
        """
    @abstractmethod
    def isValidPrefixName(self, sName: str) -> bool:
        """
        """
    @abstractmethod
    def isValidXMLName(self, sName: str) -> bool:
        """
        """
    @abstractmethod
    def newInstance(self, sName: str, sURL: str, bURLOnce: bool) -> 'XDocument_aebc0b5e':
        """
        """
    @abstractmethod
    def newModel(self, xModel: 'XModel_7a6e095c', sName: str) -> 'XModel_865909f0':
        """
        """
    @abstractmethod
    def removeBindingForNode(self, xNode: 'XNode_83fb09a5') -> None:
        """
        """
    @abstractmethod
    def removeBindingIfUseless(self, xBinding: 'XPropertySet_bc180bfa') -> None:
        """
        """
    @abstractmethod
    def removeInstance(self, sName: str) -> None:
        """
        """
    @abstractmethod
    def removeModel(self, xModel: 'XModel_7a6e095c', sName: str) -> None:
        """
        """
    @abstractmethod
    def renameInstance(self, sFrom: str, sTo: str, sURL: str, bURLOnce: bool) -> None:
        """
        """
    @abstractmethod
    def renameModel(self, xModel: 'XModel_7a6e095c', sFrom: str, sTo: str) -> None:
        """
        """
    @abstractmethod
    def renameNode(self, xNode: 'XNode_83fb09a5', sName: str) -> 'XNode_83fb09a5':
        """
        """
    @abstractmethod
    def setNodeValue(self, xNode: 'XNode_83fb09a5', sValue: str) -> None:
        """
        """

__all__ = ['XFormsUIHelper1']

