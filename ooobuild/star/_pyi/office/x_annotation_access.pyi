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
# Namespace: com.sun.star.office
from typing_extensions import Literal
import typing
from abc import ABC
if typing.TYPE_CHECKING:
    from .x_annotation import XAnnotation as XAnnotation_bb8f0be7
    from .x_annotation_enumeration import XAnnotationEnumeration as XAnnotationEnumeration_58fe106e

class XAnnotationAccess(ABC):
    """
    This interface gives access to the annotation for a document content.

    See Also:
        `API XAnnotationAccess <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1office_1_1XAnnotationAccess.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.office.XAnnotationAccess']

    def createAndInsertAnnotation(self) -> 'XAnnotation_bb8f0be7':
        """
        creates a new annotation and inserts it into the document content.
        """
    def createAnnotationEnumeration(self) -> 'XAnnotationEnumeration_58fe106e':
        """
        """
    def removeAnnotation(self, annotation: 'XAnnotation_bb8f0be7') -> None:
        """
        removes the annotation from this document content.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """

